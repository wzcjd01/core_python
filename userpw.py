#!/usr/bin/env python
#__author__ = 'Wang Zhicheng'
# todo: ex 7-5 (c)-(g) p324

from __future__ import print_function
import time

db = {}


def newuser():
    prompt = 'login desired: >> '

    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try another: >> '
            continue
        else:
            break

    pwd = raw_input('password: >> ')
    val = [pwd, time.time()]
    db.setdefault(name, val)


def olduser():
    name = raw_input('name: ')
    pwd = raw_input('password: ')

    if pwd == db.get(name)[0]:
        last = db.get(name)[1]
        now = time.time()
        four_hour = 4 * 60 * 60

        if now - last <= four_hour:
            print('You already logged in at: %s'
                  % time.ctime(last))
        print('welcom back %s' % name)
    else:
        print('login incorrect')


def remove_user():
    remv = raw_input('Enter user name:>> ').strip()
    reslt = db.pop(remv, None)
    if reslt is None:
        print('No User named as: ', repr(remv))
    else:
        print(remv, 'removed')


def list_user():
    print('name\t\tpassword\t\tlast logged at')
    print ('-' * 52)
    for k, v in db.iteritems():
        print('%-8s\t%-12s\t%s' % (k, v[0], time.ctime(v[1])))


def administration():
    admin_prompt = """
    (R)emove a user
    (L)ist all users and their passwords
    Re(T)urn

    Enter choice:>> """

    admin_done = False
    while not admin_done:

        admin_chosen = False
        while not admin_chosen:
            try:
                admin_choice = raw_input(admin_prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                admin_choice = 't'

            if admin_choice not in 'rlt':
                print('Invalid option, try again')
            else:
                admin_chosen = True

        if admin_choice == 'r': remove_user()
        if admin_choice == 'l': list_user()
        if admin_choice == 't': admin_done = True


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (A)dministration
    (Q)uit

    Enter choice: """

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'

            if choice not in 'neqa':
                print('Invalid option, try again')
            else:
                chosen = True

        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'a': administration()
        if choice == 'q': done = True

if __name__ == '__main__':
    showmenu()

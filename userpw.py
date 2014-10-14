#!/usr/bin/env python
#__author__ = 'Wang Zhicheng'

from __future__ import print_function

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
    db[name] = pwd


def olduser():
    name = raw_input('name: ')
    pwd = raw_input('password: ')

    if pwd == db.get(name):
        print('welcom back %s' % name)
    else:
        print('login incorrect')


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
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

            if choice not in 'neq':
                print('Invalid option, try again')
            else:
                chosen = True

        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'q': done = True

if __name__ == '__main__':
    showmenu()

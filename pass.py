
# todo:
# bind the name getpass to the appropriate function

def win_getpass(maskchar='*'):
    password = ''
    while True:
        ch = getch()
        if ch == '\r' or ch == '\n':
            print
            return password
        elif ch == '\b' or ord(ch) == 127:
            if len(password) > 0:
                sys.stdout.write('\b \b')
                password = password[:-1]
        else:
            if maskchar is not None:
                sys.stdout.write(maskchar)
            password += ch


if __name__ == '__main__':
    print 'Enter passord: >>',
    password = win_getpass("*")
    print password
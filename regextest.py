import re


if __name__ == '__main__':
    p = re.compile('[a-zA-Z0-9_\t\f\v\s]+')
    m = p.match()
    print(m)
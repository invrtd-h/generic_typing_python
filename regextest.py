import re


if __name__ == '__main__':
    p = re.compile('[^\(\)\[\]\{\}]+')

    f = open('input.txt')

    m = p.findall(f.read())
    print(m)

    f.close()
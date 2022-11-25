import ply
import ply.lex as lex
import ply.yacc as yacc


tokens = ('LINE', 'INDENT', 'VPARENS', 'STR', 'VPARENS2')


def t_STR(t: ply.lex.LexToken):
    r'[^ \[\]\(\)\{\}\r\n]'
    return t


if __name__ == '__main__':
    pass
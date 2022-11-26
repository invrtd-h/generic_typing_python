import ply
import ply.lex as lex
import ply.yacc as yacc

tokens = ('INT', 'ADD', 'SUB', 'MUL', 'DIV', 'LP', 'RP')

t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'/'
t_LP = r'\('
t_RP = r'\)'


def t_INT(t: ply.lex.LexToken):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.prep.skip(1)


lex.lex()


def p_e_plus(p):
    'E : E ADD F'
    p[0] = p[1] + p[3]


def p_e_minus(p):
    'E : E SUB F'
    p[0] = p[1] - p[3]


def p_e_r(p):
    'E : F'
    p[0] = p[1]


def p_f_mul(p):
    'F : F MUL G'
    p[0] = p[1] * p[3]


def p_f_div(p):
    'F : F DIV G'
    p[0] = p[1] / p[3]


def p_f_r(p):
    'F : G'
    p[0] = p[1]


def p_g_paren(p):
    'G : LP E RP'
    p[0] = p[2]


def p_g_num(p):
    'G : INT'
    p[0] = p[1]


def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc()


if __name__ == '__main__':
    print(parser.parse(input()))
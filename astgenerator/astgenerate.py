import ply.lex as lex
import ply.yacc as yacc


def is_all_uppercase(s):
    return s == s.upper()


tokens = [
    'TERMINAL', 'NON_TERMINAL', 'WS', 'COLON', 'OR', 'S_COLON'
]

t_COLON = r':'
t_OR = r'\|'
t_S_COLON = r';'


def t_WS(t) -> None:
    r'[\s]+'
    pass


def t_NON_TERMINAL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if is_all_uppercase(t.value):
        t.type = 'TERMINAL'
    return t


def t_TERMINAL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


if __name__ == '__main__':
    from debug02.debug import p_t

    lexer.input(p_t.__doc__.replace('\n', ';'))

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
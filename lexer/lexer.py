import ply.lex as lex

tokens = [
    'STRING',
    'NUMBER',
    "WHITESPACE",
    "S_COLON",
    "COLON",
    "COMMA",
    "R_ARROW",

    "LP1", "LP2", "LP3",
    "RP1", "RP2", "RP3",

    "PLUS", "MINUS", "TIMES", "F_DIV", "I_DIV", "MODULO",
    "EQ", "NEQ", "LT", "GT", "LTE", "GTE",
    "SUBSTITUTION",
    "BIT_AND", "BIT_OR", "BIT_XOR", "BIT_NOT",
    "L_SHIFT", "R_SHIFT",

    "REV_PIPE",

    "ID",
]

reserved = {
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',

    'def': 'DEF',
    'class': 'CLASS',
    'return': 'RETURN',
    'type' : 'TYPE',

    'trait': 'TRAIT',
    'declare': 'DECLARE',
    'declare_fn': 'DECLARE_FN',
    'extends' : 'EXTENDS',
    'typetrace' : 'TYPETRACE',
    'policy' : 'POLICY',
    'applies' : 'APPLIES',
    'generate' : 'GENERATE',
    'printinfo' : 'PRINTINFO',
}

tokens += reserved.values()

t_STRING = r"\"([^\\\"]|\\.)*\" | \'([^\\\']|\\.)*\'"
t_NUMBER = r'\d+'
t_WHITESPACE = r'[\s]+'
t_S_COLON = r';'
t_COLON = r':'
t_COMMA = r','
t_R_ARROW = r'->'

t_LP1 = r'\('
t_LP2 = r'\{'
t_LP3 = r'\['
t_RP1 = r'\)'
t_RP2 = r'\}'
t_RP3 = r'\]'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_F_DIV = r'/'
t_I_DIV = r'//'
t_MODULO = r'%'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_SUBSTITUTION = r'='

t_BIT_AND = r'&'
t_BIT_OR = r'\|'
t_BIT_XOR = r'\^'
t_BIT_NOT = r'~'

t_L_SHIFT = r'<<'
t_R_SHIFT = r'>>'

t_REV_PIPE = r'<\|'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


if __name__ == '__main__':
    f = open('testdata.txt', 'r')
    s = f.read()
    f.close()
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    x = 1
    if type(x) == int:
        print('int')



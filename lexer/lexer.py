import ply.lex as lex

tokens = [
    "WS",
    "S_COLON",
    "COLON",
    "COMMA",
    "R_ARROW",

    "LP1", "LP2", "LP3",
    "RP1", "RP2", "RP3",

    "EQ", "NEQ",
    "ASSIGN", "DOT", "STAR",

    "ID",
]

reserved = {
    'and': 'AND',
    'xor': 'XOR',
    'or': 'OR',
    'not': 'NOT',

    'True': 'TRUE',
    'False': 'FALSE',
    'None': 'NONE',

    'pass': 'PASS',

    'trait': 'TRAIT',
    'var': 'VAR',
    'fn': 'FN',
    'cls_var': 'CLS_VAR',
    'cls_fn': 'CLS_FN',
    'static_fn': 'STATIC_FN',

    'extends': 'EXTENDS',
    'implies': 'IMPLIES',
    'generate': 'GENERATE',
    'trait_of': 'TRAIT_OF',
    'printinfo': 'PRINTINFO',

    'PROGRAM_BEGIN': 'PROGRAM_BEGIN',
    'PROGRAM_END': 'PROGRAM_END',
}

tokens += reserved.values()

# t_STRING = r"\"([^\\\"]|\\.)*\" | \'([^\\\']|\\.)*\'"
# t_NUMBER = r'\d+'
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

t_EQ = r'=='
t_NEQ = r'!='

t_ASSIGN = r'='
t_DOT = r'\.'
t_STAR = r'\*'


def t_WS(t) -> None:
    r'[\s]+'
    pass


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t) -> None:
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


s1: str = """class PtNode:
    __slots__ = ()

    name: str = None

    def ast_print(self, indent: int = 0) -> None:
        print('-' * indent, end='')
        print(self.name)
        for slot in self.__slots__:
            val: PtNode = getattr(self, slot)
            if val is not None:
                val.ast_print(indent + 2)
"""


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

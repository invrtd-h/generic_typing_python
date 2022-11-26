import ply.lex as lex


class PrepLex(object):
    tokens = (
        'STR',
        'NEWLINE', 'TAB', 'SPACE',
        'LP1', 'LP2', 'LP3',
        'RP1', 'RP2', 'RP3'
    )

    t_NEWLINE = r'\n'
    t_STR = r'[^\(\)\[\]\{\}\n\t\s]+'
    t_TAB = r'\t'
    t_SPACE = r'\s'
    t_LP1 = r'\('
    t_LP2 = r'\['
    t_LP3 = r'\('
    t_RP1 = r'\)'
    t_RP2 = r'\]'
    t_RP3 = r'\}'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.prep.skip(1)

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)


if __name__ == '__main__':
    prep = PrepLex()

    td1 = """
    a, b = input(), input()
    memo = [[-1 for _ in range(100)] for _ in range(100)]
    
    def dp(i: int, j: int):
        if i < 0 or j < 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        """

    prep.lexer.input(td1)
    while True:
        tok = prep.lexer.token()
        if not tok:
            break
        print(tok)
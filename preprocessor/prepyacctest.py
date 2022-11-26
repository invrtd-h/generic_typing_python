import ply.yacc as yacc

from preplex import PrepLex
tokens = PrepLex.tokens

from preplex import prep
lexer = prep.lexer

def p_t(p):
    """
    TOT : TOT NEWLINES LINE
        | LINE
    NEWLINES : NEWLINE NEWLINES
             | NEWLINE
    LINE : INDENT CONTENTS
         | CONTENTS
    INDENT : WHITE
           | WHITE INDENT
    WHITE : TAB
          | SPACE
    CONTENTS : SENTENCE LEADING_LPAR
             | LEADING_LPAR
             | SENTENCE
    SENTENCE : STR INDENT SENTENCE
             | STR INDENT
             | STR
    LEADING_LPAR : LP1 LP1RIGHT
                 | LP1 HOLES LP1RIGHT
                 | LP2 LP2RIGHT
                 | LP2 HOLES LP2RIGHT
                 | LP3 LP3RIGHT
                 | LP3 HOLES LP3RIGHT
    LP1RIGHT : CONTENTS2 LEADING_RPAR1
             | LEADING_RPAR1
    LP2RIGHT : CONTENTS2 LEADING_RPAR2
             | LEADING_RPAR2
    LP3RIGHT : CONTENTS2 LEADING_RPAR3
             | LEADING_RPAR3
    CONTENTS2 : SENTENCE2 LEADING_LPAR_INNER
              | LEADING_LPAR_INNER
              | SENTENCE2
    SENTENCE2 : STR HOLES SENTENCE2
              | STR HOLES
              | STR
    HOLES : HOLES HOLE
          | HOLE
    HOLE : WHITE
         | NEWLINE
    LEADING_LPAR_INNER : LP1 LP1RIGHT_INNER
                       | LP1 HOLES LP1RIGHT_INNER
                       | LP2 LP2RIGHT_INNER
                       | LP2 HOLES LP2RIGHT_INNER
                       | LP3 LP3RIGHT_INNER
                       | LP3 HOLES LP3RIGHT_INNER
    LP1RIGHT_INNER : CONTENTS2 LEADING_RPAR1_INNER
                   | LEADING_RPAR1_INNER
    LP2RIGHT_INNER : CONTENTS2 LEADING_RPAR2_INNER
                   | LEADING_RPAR2_INNER
    LP3RIGHT_INNER : CONTENTS2 LEADING_RPAR3_INNER
                   | LEADING_RPAR3_INNER
    LEADING_RPAR1 : RP1__ CONTENTS
                  | RP1__
    RP1__ : RP1 INDENT
          | RP1
    LEADING_RPAR2 : RP2__ CONTENTS
                  | RP2__
    RP2__ : RP2 INDENT
          | RP2
    LEADING_RPAR3 : RP3__ CONTENTS
                  | RP3__
    RP3__ : RP3 INDENT
          | RP3
    LEADING_RPAR1_INNER : RP1____ CONTENTS2
                        | RP1____
    RP1____ : RP1 HOLES
            | RP1
    LEADING_RPAR2_INNER : RP2____ CONTENTS2
                        | RP2____
    RP2____ : RP2 HOLES
            | RP2
    LEADING_RPAR3_INNER : RP3____ CONTENTS2
                        | RP3____
    RP3____ : RP3 HOLES
            | RP3
    """

def p_error(p):
    if type(p) == type(None):
        return
    print("Syntax error at '%s'" % p.value)


parser_test = yacc.yacc()


if __name__ == '__main__':
    f = open("../input.txt", 'r')
    s = f.read()
    f.close()

    s += '\n'

    print(parser_test.parse(s))
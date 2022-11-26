import ply
import ply.yacc as yacc

from preplex import PrepLex
tokens = PrepLex.tokens

from preplex import prep
lexer = prep.lexer

from preptree import *


# Here is our total rule of preprocessor
#
# LINE : INDENT LINE2
#      | LINE2
# LINE2 : BPARENS \NEWLINE\
#       | \NEWLINE\
# INDENT : WHITE
#        | INDENT WHITE
# WHITE : \TAB\
#       | \SPACE\
# BPARENS : BPARENS SENTENCE
#         | BPARENS BPARENS2
#         | SENTENCE
#         | BPARENS2
# SENTENCE : SENTENCE INDENTORSTR
#          | INDENTORSTR
# INDENTORSTR : INDENT
#             | \STR\
# BPARENS2 : \LP1\ \RP1\
#          | \LP2\ \RP2\
#          | \LP3\ \RP3\
#          | \LP1\ BPARENS3 \RP1\
#          | \LP2\ BPARENS3 \RP2\
#          | \LP3\ BPARENS3 \RP3\
# BPARENS3 : BPARENS3 SENTENCE2
#          | BPARENS3 BPARENS2
#          | BPARENS2
# SENTENCE2 : SENTENCE2 INDENTORSTR
#           | SENTENCE2 \NEWLINE\
#           | INDENTORSTR
#           | \NEWLINE\

def p_line_r0(p):
    'LINE : INDENT LINE2'
    return LineToken(p[0], p[1])


def p_line_r1(p):
    'LINE : LINE2'
    return LineToken(None, p[0])


def p_line2_r0(p):
    'LINE2 : BPARENS NEWLINE'
    return Line2Token(p[0])


def p_line2_r1(p):
    'LINE2 : NEWLINE'
    return Line2Token(None)


def p_indent_r0(p):
    'INDENT : WHITE'
    return IndentToken(None, p[0])


def p_indent_r1(p):
    'INDENT : INDENT WHITE'
    return IndentToken(p[0], p[1])


def p_white_r0(p):
    'WHITE : TAB'
    return WhiteToken(True)


def p_white_r1(p):
    'WHITE : SPACE'
    return WhiteToken(False)


def p_bparens_r0(p):
    'BPARENS : BPARENS SENTENCE'
    return BParensToken(p[0], p[1], None)


def p_bparens_r1(p):
    'BPARENS : BPARENS BPARENS2'
    return BParensToken(p[0], None, p[1])


def p_bparens_r2(p):
    'BPARENS : SENTENCE'
    return BParensToken(None, p[0], None)


def p_bparens_r3(p):
    'BPARENS : BPARENS2'
    return BParensToken(None, None, p[0])


def p_sentence_r0(p):
    'SENTENCE : SENTENCE INDENTORSTR'
    return SentenceToken(p[0], p[1])


def p_sentence_r1(p):
    'SENTENCE : INDENTORSTR'
    return SentenceToken(None, p[0])


def p_indentorstr_r0(p):
    'INDENTORSTR : INDENT'
    return IndentOrStrToken(p[0])


def p_indentorstr_r1(p):
    'INDENTORSTR : STR'
    return IndentOrStrToken(p[0])


def p_bparens2_r0(p):
    'BPARENS2 : LP1 RP1'
    return BParens2Token(None, 1)


def p_bparens2_r1(p):
    'BPARENS2 : LP2 RP2'
    return BParens2Token(None, 2)


def p_bparens2_r2(p):
    'BPARENS2 : LP3 RP3'
    return BParens2Token(None, 3)


def p_bparens2_r3(p):
    'BPARENS2 : LP1 BPARENS3 RP1'
    return BParens2Token(p[1], 1)


def p_bparens2_r4(p):
    'BPARENS2 : LP2 BPARENS3 RP2'
    return BParens2Token(p[1], 2)


def p_bparens2_r5(p):
    'BPARENS2 : LP3 BPARENS3 RP3'
    return BParens2Token(p[1], 3)


def p_bparens3_r0(p):
    'BPARENS3 : BPARENS3 SENTENCE2'
    return BParens3Token(p[0], p[1], None)


def p_bparens3_r1(p):
    'BPARENS3 : BPARENS3 BPARENS2'
    return BParens3Token(p[0], None, p[1])


def p_bparens3_r2(p):
    'BPARENS3 : BPARENS2'
    return BParens3Token(None, None, p[0])


def p_sentence2_r0(p):
    'SENTENCE2 : SENTENCE2 INDENTORSTR'
    return Sentence2Token(p[0], p[1], False)


def p_sentence2_r1(p):
    'SENTENCE2 : SENTENCE2 NEWLINE'
    return Sentence2Token(p[0], None, True)


def p_sentence2_r2(p):
    'SENTENCE2 : INDENTORSTR'
    return Sentence2Token(None, p[0], False)


def p_sentence2_r3(p):
    'SENTENCE2 : NEWLINE'
    return Sentence2Token(None, None, True)


def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc()


if __name__ == '__main__':
    f = open("../input.txt", 'r')
    s = f.read()
    f.close()

    s += '\n'

    print(parser.parse(s))

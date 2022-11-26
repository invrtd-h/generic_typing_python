import ply
import ply.yacc as yacc

from preplex import PrepLex

tokens = PrepLex.tokens

from preptree import *


# Here is our total rule of preprocessor
#
# LINE : INDENT VPARENS \NEWLINE\
#      | INDENT \NEWLINE\
#      | VPARENS \NEWLINE\
#      | \NEWLINE\
#      | INDENT VPARENS
#      | INDENT
#      | VPARENS
# INDENT : WHITE
#        | INDENT WHITE
# WHITE : \TAB\
#       | \SPACE\
# VPARENS : VPARENS SENTENCE
#         | VPARENS VPARENS2
#         | VPARENS2
# SENTENCE : SENTENCE INDENTORSTR
#          | INDENTORSTR
# INDENTORSTR : INDENT
#             | \STR\
# VPARENS2 : \LP1\ \RP1\
#          | \LP2\ \RP2\
#          | \LP3\ \RP3\
#          | \LP1\ VPARENS3 \RP1\
#          | \LP2\ VPARENS3 \RP2\
#          | \LP3\ VPARENS3 \RP3\
# VPARENS3 : VPARENS3 SENTENCE2
#          | VPARENS3 VPARENS2
#          | VPARENS2
# SENTENCE2 : SENTENCE2 INDENTORSTR
#           | SENTENCE2 \NEWLINE\
#           | INDENTORSTR
#           | \NEWLINE\

def p_line_r0(p):
    'LINE : INDENT VPARENS NEWLINE'
    return LineToken(p[0], p[1], True)


def p_line_r1(p):
    'LINE : INDENT NEWLINE'
    return LineToken(p[0], None, True)


if __name__ == '__main__':
    pass

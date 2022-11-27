import ply
import ply.yacc as yacc

from preplex import PrepLex
tokens = PrepLex.tokens

from preplex import prep
lexer = prep.lexer

from preptree import *


'''
Here is our total rule of preprocessor.

Rule 0     S' -> S
Rule 1     S -> TOT
Rule 2     S -> TOT NEWLINES
Rule 3     TOT -> TOT NEWLINES LINE
Rule 4     TOT -> LINE
Rule 5     NEWLINES -> NEWLINE NEWLINES
Rule 6     NEWLINES -> NEWLINE
Rule 7     LINE -> INDENT CONTENTS
Rule 8     LINE -> CONTENTS
Rule 9     INDENT -> WHITE
Rule 10    INDENT -> WHITE INDENT
Rule 11    WHITE -> TAB
Rule 12    WHITE -> SPACE
Rule 13    CONTENTS -> SENTENCE LEADING_LPAR
Rule 14    CONTENTS -> LEADING_LPAR
Rule 15    CONTENTS -> SENTENCE
Rule 16    SENTENCE -> STR INDENT SENTENCE
Rule 17    SENTENCE -> STR INDENT
Rule 18    SENTENCE -> STR
Rule 19    LEADING_LPAR -> LP1 LP1RIGHT
Rule 20    LEADING_LPAR -> LP1 HOLES LP1RIGHT
Rule 21    LEADING_LPAR -> LP2 LP2RIGHT
Rule 22    LEADING_LPAR -> LP2 HOLES LP2RIGHT
Rule 23    LEADING_LPAR -> LP3 LP3RIGHT
Rule 24    LEADING_LPAR -> LP3 HOLES LP3RIGHT
Rule 25    LP1RIGHT -> CONTENTS2 LEADING_RPAR1
Rule 26    LP1RIGHT -> LEADING_RPAR1
Rule 27    LP2RIGHT -> CONTENTS2 LEADING_RPAR2
Rule 28    LP2RIGHT -> LEADING_RPAR2
Rule 29    LP3RIGHT -> CONTENTS2 LEADING_RPAR3
Rule 30    LP3RIGHT -> LEADING_RPAR3
Rule 31    CONTENTS2 -> SENTENCE2 LEADING_LPAR_INNER
Rule 32    CONTENTS2 -> LEADING_LPAR_INNER
Rule 33    CONTENTS2 -> SENTENCE2
Rule 34    SENTENCE2 -> STR HOLES SENTENCE2
Rule 35    SENTENCE2 -> STR HOLES
Rule 36    SENTENCE2 -> STR
Rule 37    HOLES -> HOLES HOLE
Rule 38    HOLES -> HOLE
Rule 39    HOLE -> WHITE
Rule 40    HOLE -> NEWLINE
Rule 41    LEADING_LPAR_INNER -> LP1 LP1RIGHT_INNER
Rule 42    LEADING_LPAR_INNER -> LP1 HOLES LP1RIGHT_INNER
Rule 43    LEADING_LPAR_INNER -> LP2 LP2RIGHT_INNER
Rule 44    LEADING_LPAR_INNER -> LP2 HOLES LP2RIGHT_INNER
Rule 45    LEADING_LPAR_INNER -> LP3 LP3RIGHT_INNER
Rule 46    LEADING_LPAR_INNER -> LP3 HOLES LP3RIGHT_INNER
Rule 47    LP1RIGHT_INNER -> CONTENTS2 LEADING_RPAR1_INNER
Rule 48    LP1RIGHT_INNER -> LEADING_RPAR1_INNER
Rule 49    LP2RIGHT_INNER -> CONTENTS2 LEADING_RPAR2_INNER
Rule 50    LP2RIGHT_INNER -> LEADING_RPAR2_INNER
Rule 51    LP3RIGHT_INNER -> CONTENTS2 LEADING_RPAR3_INNER
Rule 52    LP3RIGHT_INNER -> LEADING_RPAR3_INNER
Rule 53    LEADING_RPAR1 -> RP1R CONTENTS
Rule 54    LEADING_RPAR1 -> RP1R
Rule 55    RP1R -> RP1 INDENT
Rule 56    RP1R -> RP1
Rule 57    LEADING_RPAR2 -> RP2R CONTENTS
Rule 58    LEADING_RPAR2 -> RP2R
Rule 59    RP2R -> RP2 INDENT
Rule 60    RP2R -> RP2
Rule 61    LEADING_RPAR3 -> RP3R CONTENTS
Rule 62    LEADING_RPAR3 -> RP3R
Rule 63    RP3R -> RP3 INDENT
Rule 64    RP3R -> RP3
Rule 65    LEADING_RPAR1_INNER -> RP1RR CONTENTS2
Rule 66    LEADING_RPAR1_INNER -> RP1RR
Rule 67    RP1RR -> RP1 HOLES
Rule 68    RP1RR -> RP1
Rule 69    LEADING_RPAR2_INNER -> RP2RR CONTENTS2
Rule 70    LEADING_RPAR2_INNER -> RP2RR
Rule 71    RP2RR -> RP2 HOLES
Rule 72    RP2RR -> RP2
Rule 73    LEADING_RPAR3_INNER -> RP3RR CONTENTS2
Rule 74    LEADING_RPAR3_INNER -> RP3RR
Rule 75    RP3RR -> RP3 HOLES
Rule 76    RP3RR -> RP3
'''


def p_s0(p):
    'S : TOT'
    p[0] = SToken(p[1], null_token)


def p_s1(p):
    'S : TOT NEWLINES'
    p[0] = SToken(p[1], p[2])


def p_tot0(p):
    'TOT : TOT NEWLINES LINE'
    p[0] = TotToken(p[1], p[2], p[3])


def p_tot1(p):
    'TOT : LINE'
    p[0] = TotToken(null_token, null_token, p[1])


def p_newlines0(p):
    'NEWLINES : NEWLINE NEWLINES'
    p[0] = NewlinesToken() + p[2]


def p_newlines1(p):
    'NEWLINES : NEWLINE'
    p[0] = NewlinesToken()


def p_line0(p):
    'LINE : INDENT CONTENTS'
    p[0] = LineToken(p[1], p[2])


def p_line1(p):
    'LINE : CONTENTS'
    p[0] = LineToken(null_token, p[1])


def p_indent0(p):
    'INDENT : WHITE'
    p[0] = IndentToken(p[1], null_token)


def p_indent1(p):
    'INDENT : WHITE INDENT'
    p[0] = IndentToken(p[1], p[2])


def p_white0(p):
    'WHITE : TAB'
    p[0] = '\t'


def p_white1(p):
    'WHITE : SPACE'
    p[0] = ' '


def p_contents0(p):
    'CONTENTS : SENTENCE LEADING_LPAR'
    p[0] = ContentsToken(p[1], p[2])


def p_contents1(p):
    'CONTENTS : SENTENCE'
    p[0] = ContentsToken(p[1], null_token)


def p_contents2(p):
    'CONTENTS : LEADING_LPAR'
    p[0] = ContentsToken(null_token, p[1])


def p_sentence0(p):
    'SENTENCE : STR HOLES SENTENCE'
    p[0] = SentenceToken(p[1], p[2], p[3])


def p_sentence1(p):
    'SENTENCE : STR HOLES'
    p[0] = SentenceToken(p[1], p[2], null_token)


def p_sentence2(p):
    'SENTENCE : STR'
    p[0] = SentenceToken(p[1], null_token, null_token)


def p_leading_lpar0(p):
    'LEADING_LPAR : LP1 LP1RIGHT'
    p[0] = LeadingLParToken(1, null_token, p[2])


def p_leading_lpar1(p):
    'LEADING_LPAR : LP1 HOLES LP1RIGHT'
    p[0] = LeadingLParToken(1, p[2], p[3])


def p_leading_lpar2(p):
    'LEADING_LPAR : LP2 LP2RIGHT'
    p[0] = LeadingLParToken(2, null_token, p[2])


def p_leading_lpar3(p):
    'LEADING_LPAR : LP2 HOLES LP2RIGHT'
    p[0] = LeadingLParToken(2, p[2], p[3])


def p_leading_lpar4(p):
    'LEADING_LPAR : LP3 LP3RIGHT'
    p[0] = LeadingLParToken(3, null_token, p[2])


def p_leading_lpar5(p):
    'LEADING_LPAR : LP3 HOLES LP3RIGHT'
    p[0] = LeadingLParToken(3, p[2], p[3])


def p_lp1right0(p):
    'LP1RIGHT : CONTENTS2 LEADING_RPAR1'
    p[0] = LpRightToken(1, p[1], p[2])


def p_lp1right1(p):
    'LP1RIGHT : LEADING_RPAR1'
    p[0] = LpRightToken(1, null_token, p[1])


def p_lp2right0(p):
    'LP2RIGHT : CONTENTS2 LEADING_RPAR2'
    p[0] = LpRightToken(2, p[1], p[2])


def p_lp2right1(p):
    'LP2RIGHT : LEADING_RPAR2'
    p[0] = LpRightToken(2, null_token, p[1])


def p_lp3right0(p):
    'LP3RIGHT : CONTENTS2 LEADING_RPAR3'
    p[0] = LpRightToken(3, p[1], p[2])


def p_lp3right1(p):
    'LP3RIGHT : LEADING_RPAR3'
    p[0] = LpRightToken(3, null_token, p[1])


def p_contents2_0(p):
    'CONTENTS2 : SENTENCE2 LEADING_LPAR2_INNER'
    p[0] = Contents2Token(p[1], p[2])


def p_contents2_1(p):
    'CONTENTS2 : LEADING_LPAR2_INNER'
    p[0] = Contents2Token(null_token, p[1])


def p_contents2_2(p):
    'CONTENTS2 : SENTENCE2'
    p[0] = Contents2Token(p[1], null_token)


def p_sentence2_0(p):
    'SENTENCE2 : STR HOLES SENTENCE2'
    p[0] = Sentence2Token(p[1], p[2], p[3])


def p_sentence2_1(p):
    'SENTENCE2 : STR HOLES'
    p[0] = Sentence2Token(p[1], p[2], null_token)


def p_sentence2_2(p):
    'SENTENCE2 : STR'
    p[0] = Sentence2Token(p[1], null_token, null_token)


def p_holes0(p):
    'HOLES : HOLES HOLE'
    p[0] = HolesToken(p[1], p[2])


def p_holes1(p):
    'HOLES : HOLE'
    p[0] = HolesToken(null_token, p[1])


def p_hole0(p):
    'HOLE : WHITE'
    p[0] = p[1]


def p_hole1(p):
    'HOLE : NEWLINE'
    p[0] = p[1]


def p_leading_lpar_inner0(p):
    'LEADING_LPAR_INNER : LP1 LP1RIGHT_INNER'
    p[0] = LeadingLParInnerToken(1, null_token, p[2])


def p_leading_lpar_inner1(p):
    'LEADING_LPAR_INNER : LP1 HOLES LP1RIGHT_INNER'
    p[0] = LeadingLParInnerToken(1, p[2], p[3])



def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc()


if __name__ == '__main__':
    f = open("../input.txt", 'r')
    s = f.read()
    f.close()

    s += '\n'

    print(parser.parse(s))



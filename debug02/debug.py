import sys

import ply.yacc as yacc
import lexer.lexer as l
from lexer.lexer import lexer

tokens = l.tokens


def p_t(p):
    """
    Program : PROGRAM_BEGIN S_COLON Stmts S_COLON PROGRAM_END S_COLON
    Stmts : Stmts S_COLON Stmt
          | Stmt
    Stmt : TraitDecl
         | PrintStmt
         | S_COLON
    TraitDecl : TRAIT ID LP1 ClassArgs RP1 COLON LP2 TraitDeclStmts S_COLON RP2
              | TRAIT ID LP1 ClassArgs RP1 EXTENDS UnaryPred COLON LP2 TraitDeclStmts S_COLON RP2
    ClassArgs : MainArg COMMA SubArgs
              | MainArg
    MainArg : ID
    SubArgs : SubArgs COMMA ID
            | ID
    TraitDeclStmts : TraitDeclStmts S_COLON TraitDeclStmt
                   | TraitDeclStmt
    TraitDeclStmt : DECLARE_FN COLON LP2 DeclFnStmts S_COLON RP2
                  | DECLARE COLON LP2 DeclStmts S_COLON RP2
    DeclFnStmts : DeclFnStmts S_COLON DeclFnStmt
                | DeclFnStmt
    DeclFnStmt : ID LP1 PredLists RP1
               | ID LP1 PredLists RP1 R_ARROW UnaryPred
    PredLists : MainPred COMMA SubPreds
              | MainPred
    MainPred : ID
    SubPreds : SubPreds COMMA ID
             | ID
    UnaryPred : PredName
              | PredName LP3 Args RP3
              | LP3 PredExpr RP3
    PredName : ID
    PredExpr : NOT PredExprA
             | PredExprA
    PredExprA : PredExprB
              | PredExprA AND PredExprB
              | PredExprA OR PredExprB
    PredExprB : PredName
              | LP1 PredExpr RP1
    DeclStmts : DeclStmts S_COLON DeclStmt
              | DeclStmt
    DeclStmt : ID
             | ID COLON PredName
    PrintStmt : PRINTINFO ToPrints
    ToPrints : ToPrints COMMA ToPrint
             | ToPrint
    ToPrint : ID
            | BooleanExpr
    BooleanExpr : BooleanExprA
                | NOT BooleanExprA
    BooleanExprA : BooleanExprB
                 | BooleanExprA AND BooleanExprB
                 | BooleanExprA OR BooleanExprB
    BooleanExprB : AtomicBooleanExpr
                 | LP1 BooleanExpr RP1
    AtomicBooleanExpr : Constants
                      | UnaryPred LP1 Args RP1
    Constants : TRUE
              | FALSE
    Args : Args COMMA ID
         | ID
    """
    return


def p_error(p):
    # Panic mode recovery.
    # This code is copied from the official PLY documentation.
    if p:
        print("Syntax error at {}".format(p.value))
    # Read ahead looking for a terminating ";"
    while True:
        tok = parser.token()  # Get the next token
        if not tok:
            return None
        if not tok or tok.type == 'S_COLON':
            break
    parser.errok()

    # Return S_COLON to the parser as the next lookahead token
    return tok


parser = yacc.yacc()

if __name__ == '__main__':
    f = open("../lexer/testdata.txt", 'r')
    s = f.read()
    f.close()

    print(parser.parse(s))

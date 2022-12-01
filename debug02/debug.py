import ply.yacc
import ply.yacc as yacc

import lexer.lexer as ll

tokens = ll.tokens


def p_t(p: ply.yacc.YaccProduction):
    """
    Program : PROGRAM_BEGIN S_COLON Stmts S_COLON PROGRAM_END S_COLON
    Stmts : Stmts S_COLON Stmt
          | Stmt
    Stmt : TraitDecl
         | PolicyDecl
         | PrintStmt
         | GenerateStmt
         | AssignStmt
         | S_COLON
    TraitDecl : TRAIT TraitID LP1 ClassArgs RP1 COLON LP2 TraitDeclStmts S_COLON RP2
              | TRAIT TraitID LP1 ClassArgs RP1 EXTENDS UnaryPred COLON LP2 TraitDeclStmts S_COLON RP2
    TraitID : ID
    ClassArgs : MainArg COMMA SubArgs
              | MainArg
    MainArg : ID
    SubArgs : SubArgs COMMA ID
            | ID
    TraitDeclStmts : TraitDeclStmts S_COLON TraitDeclStmt
                   | TraitDeclStmt
                   | PASS
    TraitDeclStmt : FN COLON LP2 DeclFnStmts S_COLON RP2
                  | VAR COLON LP2 DeclStmts S_COLON RP2
                  | CLS_FN COLON LP2 DeclFnStmts S_COLON RP2
                  | CLS_VAR COLON LP2 DeclStmts S_COLON RP2
                  | STATIC_FN COLON LP2 DeclStaticFnStmts S_COLON RP2
    DeclFnStmts : DeclFnStmts S_COLON DeclFnStmt
                | DeclFnStmt
    DeclFnStmt : FnID LP1 PredLists RP1
               | FnID LP1 PredLists RP1 R_ARROW UnaryPred
               | FnID LP1 PredLists RP1 OBEYS PolicyExpr
    FnID : ID
    PredLists : MainPred COMMA NextPreds
              | MainPred
    MainPred : ID
    NextPreds : NextPreds COMMA NextPred
              | NextPred
    NextPred : ID
    UnaryPred : PredName
              | PredName LP3 Args RP3
              | LP3 PredExpr RP3
              | TYPETRACE LP1 PolicyExpr REV_PIPE Args RP1
              | TRAIT_OF LP1 VarExpr RP1
              | NONE
    PredName : ID
    PredExpr : NOT PredExprA
             | PredExprA
    PredExprA : PredExprB
              | PredExprA AND PredExprB
              | PredExprA OR PredExprB
    PredExprB : UnaryPred
              | LP1 PredExpr RP1
    DeclStmts : DeclStmts S_COLON DeclStmt
              | DeclStmt
    DeclStmt : ID
             | ID COLON UnaryPred
             | LP3 DeclStmtInLP3 RP3
             | LP3 DeclStmtInLP3 RP3 COLON UnaryPred
    DeclStmtInLP3 : DeclStmtInLP3 COMMA ID
                  | ID
    DeclStaticFnStmts : DeclStaticFnStmts S_COLON DeclStaticFnStmt
                      | DeclStaticFnStmt
    DeclStaticFnStmt : StaticFnID LP1 NextPreds RP1
                     | StaticFnID LP1 NextPreds RP1 R_ARROW UnaryPred
                     | StaticFnID LP1 NextPreds RP1 OBEYS PolicyExpr
                     | StaticFnID LP1 RP1
                     | StaticFnID LP1 RP1 R_ARROW UnaryPred
                     | StaticFnID LP1 RP1 OBEYS PolicyExpr
    StaticFnID : ID
    PrintStmt : PRINTINFO ToPrint
    ToPrint : BooleanExpr
            | PredName LP3 Args RP3
            | LP3 PredExpr RP3
            | TYPETRACE LP1 PolicyExpr REV_PIPE Args RP1
            | TRAIT_OF LP1 VarExpr RP1
            | ID
            | UnaryPred DOT PolicyExpr
    BooleanExpr : BooleanExprA
                | NOT BooleanExprA
    BooleanExprA : BooleanExprB
                 | BooleanExprA AND BooleanExprB
                 | BooleanExprA OR BooleanExprB
    BooleanExprB : AtomicBooleanExpr
                 | LP1 BooleanExpr RP1
    AtomicBooleanExpr : Constants
                      | UnaryPred LP1 Args RP1
                      | UnaryPred IMPLIES UnaryPred
    Constants : TRUE
              | FALSE
    Args : Args COMMA ID
         | ID
    PolicyDecl : POLICY PolicyID COLON LP2 PolicyDeclStmts S_COLON RP2
    PolicyID : ID
    PolicyExpr : PolicyName
               | UnaryPred DOT PolicyName
    PolicyName : ID
    PolicyDeclStmts : NonDefaultPolicyDeclStmts S_COLON DefaultPolicyDeclStmt
                    | NonDefaultPolicyDeclStmts
    NonDefaultPolicyDeclStmts : NonDefaultPolicyDeclStmts S_COLON PolicyDeclStmt
                              | PolicyDeclStmt
    PolicyDeclStmt : PredName R_ARROW UnaryPred
                   | TYPENAME TypeID COLON UnaryPred R_ARROW UnaryPred
                   | TYPENAME TypeID R_ARROW UnaryPred
    DefaultPolicyDeclStmt : DEFAULT R_ARROW UnaryPred
    TypeID : ID
    GenerateStmt : GENERATE ToGenerates
    ToGenerates : ToGenerates COMMA ToPrint
                | ToPrint
    AssignStmt : Names ASSIGN AssignExpr
    AssignExpr : Names ASSIGN AssignExpr
               | Names
    Names : Names COMMA ID
          | ID
    VarExpr : PredName DOT VarName
            | LP1 UnaryPred RP1 DOT VarName
    VarName : ID
    """
    try:
        print(p.lexpos(1))
    except:
        pass
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
    f = open("../input.txt", 'r')
    s = f.read()
    f.close()

    from preprocessor.preprocessor import preprocess
    s = preprocess(s)

    print(s[800:900])

    print(parser.parse(s))

# Here are our total rules

"""
program : PROGRAM_BEGIN S_COLON stmts PROGRAM_END S_COLON
        | WS
stmts : stmts stmt
      | stmt
stmt : trait_decl
     | print_stmt
     | generate_stmt
     | assign_stmt
     | S_COLON
trait_decl : TRAIT trait_id LP1 class_args RP1 COLON LP2 trait_decl_stmts RP2 S_COLON
           | TRAIT trait_id LP1 class_args RP1 EXTENDS unary_pred COLON LP2 trait_decl_stmts RP2 S_COLON
trait_id : ID
class_args : main_arg COMMA sub_args
           | main_arg
main_arg : ID
sub_args : necessary_args COMMA optional_args
         | necessary_args
         | optional_args
necessary_args : necessary_args COMMA necessary_arg
               | necessary_arg
necessary_arg : ID
optional_args : optional_args COMMA optional_arg
              | optional_arg
optional_arg : ID ASSIGN unary_pred
trait_decl_stmts : trait_decl_stmts trait_decl_stmt
                 | trait_decl_stmt
                 | PASS S_COLON
trait_decl_stmt : FN COLON LP2 decl_fn_stmts RP2 S_COLON
                | VAR COLON LP2 decl_stmts RP2 S_COLON
                | CLS_FN COLON LP2 decl_cls_fn_stmts RP2 S_COLON
                | CLS_VAR COLON LP2 decl_stmts RP2 S_COLON
                | STATIC_FN COLON LP2 decl_static_fn_stmts RP2 S_COLON
decl_fn_stmts : decl_fn_stmts decl_fn_stmt
              | decl_fn_stmt
decl_fn_stmt : fn_id LP1 pred_args RP1 S_COLON
             | fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON
             | fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON
             | fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON
decl_cls_fn_stmts : decl_cls_fn_stmts decl_cls_fn_stmt
                  | decl_cls_fn_stmt
decl_cls_fn_stmt : fn_id LP1 pred_args RP1 S_COLON
                 | fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON
                 | fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON
                 | fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON
fn_id : ID
pred_args : main_pred COMMA next_preds
          | main_pred
main_pred : ID
next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR COMMA next_named_preds
           | next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR
           | next_anonymous_necessary_preds COMMA next_anonymous_opt_preds
           | next_anonymous_necessary_preds COMMA STAR COMMA next_named_preds
           | next_anonymous_necessary_preds COMMA STAR
           | next_anonymous_necessary_preds
           | next_anonymous_opt_preds COMMA STAR COMMA next_named_preds
           | next_anonymous_opt_preds COMMA STAR
           | next_anonymous_opt_preds
           | STAR next_named_preds
           | STAR
next_anonymous_necessary_preds : next_anonymous_necessary_preds COMMA next_anonymous_necessary_pred
                               | next_anonymous_necessary_pred
next_anonymous_necessary_pred : unary_pred
next_anonymous_opt_preds : next_anonymous_opt_preds COMMA next_anonymous_opt_pred
                         | next_anonymous_opt_pred
next_anonymous_opt_pred : ASSIGN unary_pred
next_named_preds : next_named_preds COMMA next_named_pred
                 | next_named_pred
next_named_pred : next_named_necessary_pred
                | next_named_opt_pred
next_named_necessary_pred : arg_name COLON unary_pred
next_named_opt_pred : arg_name COLON ASSIGN unary_pred
arg_name : ID
type_var_args : type_var_args COMMA type_var_arg
              | type_var_arg
type_var_arg : type_var_id
             | type_var_id COLON unary_pred
type_var_id : ID
unary_pred : pred_name
           | unnamed_pred
unnamed_pred : pred_name LP3 args RP3
             | LP3 pred_expr RP3
             | TRAIT_OF LP1 var_expr RP1
             | NONE
pred_name : ID
pred_expr : pred_expr OR pred_expr_a
          | pred_expr_a
pred_expr_a : pred_expr_a AND pred_expr_b
            | pred_expr_b
pred_expr_b : NOT pred_expr_c
            | pred_expr_c
pred_expr_c : unary_pred
            | LP1 pred_expr RP1
var_expr : unary_pred DOT member_var_name
member_var_name : ID
decl_stmts : decl_stmts decl_stmt
           | decl_stmt
decl_stmt : var_id S_COLON
          | var_id COLON unary_pred S_COLON
          | LP3 vars_id RP3 S_COLON
          | LP3 vars_id RP3 COLON unary_pred S_COLON
vars_id : vars_id COMMA var_id
        | var_id
var_id : ID
decl_static_fn_stmts : decl_static_fn_stmts decl_static_fn_stmt
                     | decl_static_fn_stmt
decl_static_fn_stmt : static_fn_id LP1 next_preds RP1 S_COLON
                    | static_fn_id LP1 next_preds RP1 R_ARROW unary_pred S_COLON
                    | static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 S_COLON
                    | static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 R_ARROW unary_pred S_COLON
                    | static_fn_id LP1 RP1 S_COLON
                    | static_fn_id LP1 RP1 R_ARROW unary_pred S_COLON
                    | static_fn_id LP3 type_var_args RP3 LP1 RP1 S_COLON
                    | static_fn_id LP3 type_var_args RP3 LP1 RP1 R_ARROW unary_pred S_COLON
static_fn_id : ID
print_stmt : PRINTINFO to_print S_COLON
generate_stmt : GENERATE to_print S_COLON
to_print : ID
         | boolean_expr
         | unnamed_pred
boolean_expr : boolean_expr OR boolean_expr_a
             | boolean_expr_a
boolean_expr_a : boolean_expr_a XOR boolean_expr_b
               | boolean_expr_b
boolean_expr_b : boolean_expr_b AND boolean_expr_c
               | boolean_expr_c
boolean_expr_c : boolean_expr_c EQ boolean_expr_d
               | boolean_expr_c NEQ boolean_expr_d
               | boolean_expr_d
boolean_expr_d : NOT boolean_expr_e
               | boolean_expr_e
boolean_expr_e : atomic_boolean_expr
               | LP1 boolean_expr RP1
atomic_boolean_expr : constants
                    | unary_pred LP1 args RP1
                    | unary_pred IMPLIES unary_pred
                    | LP1 unary_pred EQ unary_pred RP1
                    | LP1 unary_pred NEQ unary_pred RP1
constants : TRUE
          | FALSE
args : args COMMA arg
     | arg
arg : ID
assign_stmt : names ASSIGN assign_expr S_COLON
names : names COMMA name
      | name
name : ID
assign_expr : names ASSIGN assign_expr
            | names
"""
import bisect

import ply.yacc
import ply.yacc as yacc

import lexical.lexer as ll

from syntax.ptnodes import *

tokens = ll.tokens


def p_program_r0(p: yacc.YaccProduction) -> None:
    """ program : PROGRAM_BEGIN S_COLON stmts PROGRAM_END S_COLON """
    p[0] = Program(p[3])


def p_program_r1(p: yacc.YaccProduction) -> None:
    """ program : WS """
    p[0] = Program(None)


def p_stmts_r0(p: yacc.YaccProduction) -> None:
    """ stmts : stmts stmt """
    p[0] = Stmts(stmts=p[1], stmt=p[2])


def p_stmts_r1(p: yacc.YaccProduction) -> None:
    """ stmts : stmt """
    p[0] = Stmts(stmt=p[1])


def p_stmt_r0(p: yacc.YaccProduction) -> None:
    """ stmt : trait_decl """
    p[0] = Stmt(next=p[1])


def p_stmt_r1(p: yacc.YaccProduction) -> None:
    """ stmt : print_stmt """
    p[0] = Stmt(next=p[1])


def p_stmt_r2(p: yacc.YaccProduction) -> None:
    """ stmt : generate_stmt """
    p[0] = Stmt(next=p[1])


def p_stmt_r3(p: yacc.YaccProduction) -> None:
    """ stmt : assign_stmt """
    p[0] = Stmt(next=p[1])


def p_stmt_r4(p: yacc.YaccProduction) -> None:
    """ stmt : S_COLON """
    p[0] = Stmt(next=fw.s_colon)


def p_trait_decl_r0(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id LP1 class_args RP1 COLON LP2 trait_decl_stmts RP2 S_COLON """
    p[0] = TraitDecl(trait_id=p[2], class_args=p[4], trait_decl_stmts=p[8])


def p_trait_decl_r1(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id LP1 class_args RP1 EXTENDS unary_pred COLON LP2 trait_decl_stmts RP2 S_COLON """
    p[0] = TraitDecl(trait_id=p[2], class_args=p[4], trait_decl_stmts=p[10], unary_pred=p[7])


def p_trait_id_r0(p: yacc.YaccProduction) -> None:
    """ trait_id : ID """
    p[0] = TraitID(id=p[1])


def p_class_args_r0(p: yacc.YaccProduction) -> None:
    """ class_args : main_arg COMMA sub_args """
    p[0] = ClassArgs(main_arg=p[1], sub_args=p[3])


def p_class_args_r1(p: yacc.YaccProduction) -> None:
    """ class_args : main_arg """
    p[0] = ClassArgs(main_arg=p[1])


def p_main_arg_r0(p: yacc.YaccProduction) -> None:
    """ main_arg : ID """
    p[0] = MainArg(id=p[1])


def p_sub_args_r0(p: yacc.YaccProduction) -> None:
    """ sub_args : necessary_args COMMA optional_args"""
    p[0] = SubArgs(necessary_args=p[1], optional_args=p[3])


def p_sub_args_r1(p: yacc.YaccProduction) -> None:
    """ sub_args : necessary_args """
    p[0] = SubArgs(necessary_args=p[1])


def p_sub_args_r2(p: yacc.YaccProduction) -> None:
    """ sub_args : optional_args """
    p[0] = SubArgs(optional_args=p[1])


def p_necessary_args_r0(p: yacc.YaccProduction) -> None:
    """ necessary_args : necessary_args COMMA necessary_arg """
    p[0] = NecessaryArgs(necessary_args=p[1], necessary_arg=p[3])


def p_necessary_args_r1(p: yacc.YaccProduction) -> None:
    """ necessary_args : necessary_arg """
    p[0] = NecessaryArgs(necessary_arg=p[1])


def p_necessary_arg_r0(p: yacc.YaccProduction) -> None:
    """ necessary_arg : ID """
    p[0] = NecessaryArg(id=p[1])


def p_optional_args_r0(p: yacc.YaccProduction) -> None:
    """ optional_args : optional_args COMMA optional_arg """
    p[0] = OptionalArgs(optional_args=p[1], optional_arg=p[3])


def p_optional_args_r1(p: yacc.YaccProduction) -> None:
    """ optional_args : optional_arg """
    p[0] = OptionalArgs(optional_arg=p[1])


def p_optional_arg_r0(p: yacc.YaccProduction) -> None:
    """ optional_arg : ID ASSIGN unary_pred"""
    p[0] = OptionalArg(id=p[1], unary_pred=p[3])


def p_trait_decl_stmts_r0(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmts : trait_decl_stmts trait_decl_stmt """
    p[0] = TraitDeclStmts(trait_decl_stmts=p[1], trait_decl_stmt=p[2])


def p_trait_decl_stmts_r1(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmts : trait_decl_stmt """
    p[0] = TraitDeclStmts(trait_decl_stmt=p[1])


def p_trait_decl_stmts_r2(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmts : PASS S_COLON """
    p[0] = TraitDeclStmts(pass_=True)


def p_trait_decl_stmt_r0(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : FN COLON LP2 decl_fn_stmts RP2 S_COLON """
    p[0] = TraitDeclStmtFn(decl_fn_stmts=p[4])


def p_trait_decl_stmt_r1(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : VAR COLON LP2 decl_stmts RP2 S_COLON """
    p[0] = TraitDeclStmtVar(decl_var_stmts=p[4])


def p_trait_decl_stmt_r2(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : CLS_FN COLON LP2 decl_cls_fn_stmts RP2 S_COLON """
    p[0] = TraitDeclStmtClsFn(decl_cls_fn_stmts=p[4])


def p_trait_decl_stmt_r3(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : CLS_VAR COLON LP2 decl_stmts RP2 S_COLON """
    p[0] = TraitDeclStmtClsVar(decl_cls_var_stmts=p[4])


def p_trait_decl_stmt_r4(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : STATIC_FN COLON LP2 decl_static_fn_stmts RP2 S_COLON """
    p[0] = TraitDeclStmtStaticFn(decl_static_fn_stmts=p[4])


def p_decl_fn_stmts_r0(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmts : decl_fn_stmts decl_fn_stmt """
    p[0] = DeclFnStmts(decl_fn_stmts=p[1], decl_fn_stmt=p[2])


def p_decl_fn_stmts_r1(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmts : decl_fn_stmt """
    p[0] = DeclFnStmts(decl_fn_stmt=p[1])


def p_decl_fn_stmt_r0(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP1 pred_args RP1 S_COLON """
    p[0] = DeclFnStmt(fn_id=p[1], pred_args=p[3])


def p_decl_fn_stmt_r1(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclFnStmt(fn_id=p[1], pred_args=p[3], unary_pred=p[6])


def p_decl_fn_stmt_r2(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON """
    p[0] = DeclFnStmt(fn_id=p[1], type_var_args=p[3], pred_args=p[6])


def p_decl_fn_stmt_r3(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclFnStmt(fn_id=p[1], type_var_args=p[3], pred_args=p[6], unary_pred=p[9])


def p_decl_cls_fn_stmts_r0(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmts : decl_cls_fn_stmts decl_cls_fn_stmt """
    p[0] = DeclClsFnStmts(decl_cls_fn_stmts=p[1], decl_cls_fn_stmt=p[2])


def p_decl_cls_fn_stmts_r1(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmts : decl_cls_fn_stmt """
    p[0] = DeclClsFnStmts(decl_cls_fn_stmt=p[1])


def p_decl_cls_fn_stmt_r0(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP1 pred_args RP1 S_COLON """
    p[0] = DeclClsFnStmt(fn_id=p[1], pred_args=p[3])


def p_decl_cls_fn_stmt_r1(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclClsFnStmt(fn_id=p[1], pred_args=p[3], unary_pred=p[6])


def p_decl_cls_fn_stmt_r2(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON """
    p[0] = DeclClsFnStmt(fn_id=p[1], type_var_args=p[3], pred_args=p[6])


def p_decl_cls_fn_stmt_r3(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclClsFnStmt(fn_id=p[1], type_var_args=p[3], pred_args=p[6], unary_pred=p[9])


def p_fn_id_r0(p: yacc.YaccProduction) -> None:
    """ fn_id : ID """
    p[0] = FnID(id=p[1])


def p_pred_args_r0(p: yacc.YaccProduction) -> None:
    """ pred_args : main_pred COMMA next_preds """
    p[0] = PredArgs(main_pred=p[1], next_preds=p[3])


def p_pred_args_r1(p: yacc.YaccProduction) -> None:
    """ pred_args : main_pred """
    p[0] = PredArgs(main_pred=p[1])


def p_main_pred_r0(p: yacc.YaccProduction) -> None:
    """ main_pred : ID """
    p[0] = MainPred(id=p[1])


def p_next_preds_r0(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR COMMA next_named_preds """
    p[0] = NextPreds(next_ano_nec_preds=p[1], next_ano_opt_preds=p[3], starred=True, next_named_preds=p[7])


def p_next_preds_r1(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR """
    p[0] = NextPreds(next_ano_nec_preds=p[1], next_ano_opt_preds=p[3], starred=True)


def p_next_preds_r2(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds"""
    p[0] = NextPreds(next_ano_nec_preds=p[1], next_ano_opt_preds=p[3], starred=False)


def p_next_preds_r3(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_necessary_preds COMMA STAR COMMA next_named_preds """
    p[0] = NextPreds(next_ano_nec_preds=p[1], starred=True, next_named_preds=p[5])


def p_next_preds_r4(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_necessary_preds COMMA STAR """
    p[0] = NextPreds(next_ano_nec_preds=p[1], starred=True)


def p_next_preds_r5(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_necessary_preds """
    p[0] = NextPreds(next_ano_nec_preds=p[1], starred=False)


def p_next_preds_r6(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_opt_preds COMMA STAR COMMA next_named_preds """
    p[0] = NextPreds(next_ano_opt_preds=p[1], starred=True, next_named_preds=p[5])


def p_next_preds_r7(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_opt_preds COMMA STAR """
    p[0] = NextPreds(next_ano_opt_preds=p[1], starred=True)


def p_next_preds_r8(p: yacc.YaccProduction) -> None:
    """ next_preds : next_anonymous_opt_preds """
    p[0] = NextPreds(next_ano_opt_preds=p[1], starred=False)


def p_next_preds_r9(p: yacc.YaccProduction) -> None:
    """ next_preds : STAR COMMA next_named_preds """
    p[0] = NextPreds(starred=True, next_named_preds=p[3])


def p_next_preds_r10(p: yacc.YaccProduction) -> None:
    """ next_preds : STAR """
    p[0] = NextPreds(starred=True)


def p_next_anonymous_necessary_preds_r0(p: yacc.YaccProduction) -> None:
    """ next_anonymous_necessary_preds : next_anonymous_necessary_preds COMMA next_anonymous_necessary_pred """
    p[0] = NextAnoNecPreds(next_ano_nec_preds=p[1], next_ano_nec_pred=p[3])


def p_next_anonymous_necessary_preds_r1(p: yacc.YaccProduction) -> None:
    """ next_anonymous_necessary_preds : next_anonymous_necessary_pred """
    p[0] = NextAnoNecPreds(next_ano_nec_pred=p[1])


def p_next_anonymous_necessary_pred_r0(p: yacc.YaccProduction) -> None:
    """ next_anonymous_necessary_pred : unary_pred """
    p[0] = NextAnoNecPred(unary_pred=p[1])


def p_next_anonymous_opt_preds_r0(p: yacc.YaccProduction) -> None:
    """ next_anonymous_opt_preds : next_anonymous_opt_preds COMMA next_anonymous_opt_pred """
    p[0] = NextAnoOptPreds(next_ano_opt_preds=p[1], next_ano_opt_pred=p[3])


def p_next_anonymous_opt_preds_r1(p: yacc.YaccProduction) -> None:
    """ next_anonymous_opt_preds : next_anonymous_opt_pred """
    p[0] = NextAnoOptPreds(next_ano_opt_pred=p[1])


def p_next_anonymous_opt_pred_r0(p: yacc.YaccProduction) -> None:
    """ next_anonymous_opt_pred : ASSIGN unary_pred """
    p[0] = NextAnoOptPred(unary_pred=p[2])


def p_next_named_preds_r0(p: yacc.YaccProduction) -> None:
    """ next_named_preds : next_named_preds COMMA next_named_pred """
    p[0] = NextNamedPreds(next_named_preds=p[1], next_named_pred=p[3])


def p_next_named_preds_r1(p: yacc.YaccProduction) -> None:
    """ next_named_preds : next_named_pred """
    p[0] = NextNamedPreds(next_named_pred=p[1])


def p_next_named_pred_r0(p: yacc.YaccProduction) -> None:
    """ next_named_pred : next_named_necessary_pred """
    p[0] = NextNamedPred(next_named_nec_pred=p[1])


def p_next_named_pred_r1(p: yacc.YaccProduction) -> None:
    """ next_named_pred : next_named_opt_pred """
    p[0] = NextNamedPred(next_named_opt_pred=p[1])


def p_next_named_necessary_pred_r0(p: yacc.YaccProduction) -> None:
    """ next_named_necessary_pred : arg_name COLON unary_pred """
    p[0] = NextNamedNecPred(arg_name=p[1], unary_pred=p[3])


def p_next_named_opt_pred_r0(p: yacc.YaccProduction) -> None:
    """ next_named_opt_pred : arg_name COLON ASSIGN unary_pred """
    p[0] = NextNamedOptPred(arg_name=p[1], unary_pred=p[4])


def p_arg_name_r0(p: yacc.YaccProduction) -> None:
    """ arg_name : ID """
    p[0] = ArgName(id=p[1])


def p_type_var_args_r0(p: yacc.YaccProduction) -> None:
    """ type_var_args : type_var_args COMMA type_var_arg """
    p[0] = TypeVarArgs(type_var_args=p[1], type_var_arg=p[3])


def p_type_var_args_r1(p: yacc.YaccProduction) -> None:
    """ type_var_args : type_var_arg """
    p[0] = TypeVarArgs(type_var_arg=p[1])


def p_type_var_arg_r0(p: yacc.YaccProduction) -> None:
    """ type_var_arg : type_var_id """
    p[0] = TypeVarArg(type_var_id=p[1])


def p_type_var_arg_r1(p: yacc.YaccProduction) -> None:
    """ type_var_arg : type_var_id COLON unary_pred """
    p[0] = TypeVarArg(type_var_id=p[1], unary_pred=p[3])


def p_type_var_id_r0(p: yacc.YaccProduction) -> None:
    """ type_var_id : ID """
    p[0] = TypeVarId(id=p[1])


def p_unary_pred_r0(p: yacc.YaccProduction) -> None:
    """ unary_pred : pred_name """
    p[0] = UnaryPred(pred_name=p[1])


def p_unary_pred_r1(p: yacc.YaccProduction) -> None:
    """ unary_pred : unnamed_pred """
    p[0] = UnaryPred(unnamed_pred=p[1])


def p_unnamed_pred_r0(p: yacc.YaccProduction) -> None:
    """ unnamed_pred : pred_name LP3 args RP3 """
    p[0] = UnnamedPred(pred_name=p[1], args=p[3])


def p_unnamed_pred_r1(p: yacc.YaccProduction) -> None:
    """ unnamed_pred : LP3 pred_expr RP3 """
    p[0] = UnnamedPred(pred_expr=p[2])


def p_unnamed_pred_r2(p: yacc.YaccProduction) -> None:
    """ unnamed_pred : TRAIT_OF LP1 var_expr RP1 """
    p[0] = UnnamedPred(var_expr=p[3])


def p_unnamed_pred_r3(p: yacc.YaccProduction) -> None:
    """ unnamed_pred : NONE """
    p[0] = UnnamedPred(none_=True)


def p_pred_name_r0(p: yacc.YaccProduction) -> None:
    """ pred_name : ID """
    p[0] = PredName(id=p[1])


def p_pred_expr_r0(p: yacc.YaccProduction) -> None:
    """ pred_expr : pred_expr OR pred_expr_a """
    p[0] = PredExpr(pred_expr=p[1], pred_expr_a=p[3])


def p_pred_expr_r1(p: yacc.YaccProduction) -> None:
    """ pred_expr : pred_expr_a """
    p[0] = PredExpr(pred_expr_a=p[1])


def p_pred_expr_a_r0(p: yacc.YaccProduction) -> None:
    """ pred_expr_a : pred_expr_a AND pred_expr_b """
    p[0] = PredExprA(pred_expr_a=p[1], pred_expr_b=p[3])


def p_pred_expr_a_r1(p: yacc.YaccProduction) -> None:
    """ pred_expr_a : pred_expr_b """
    p[0] = PredExprA(pred_expr_b=p[1])


def p_pred_expr_b_r0(p: yacc.YaccProduction) -> None:
    """ pred_expr_b : NOT pred_expr_c """
    p[0] = PredExprB(not_policy=True, pred_expr_c=p[2])


def p_pred_expr_b_r1(p: yacc.YaccProduction) -> None:
    """ pred_expr_b : pred_expr_c """
    p[0] = PredExprB(not_policy=False, pred_expr_c=p[1])


def p_pred_expr_c_r0(p: yacc.YaccProduction) -> None:
    """ pred_expr_c : unary_pred """
    p[0] = PredExprC(unary_pred=p[1])


def p_pred_expr_c_r1(p: yacc.YaccProduction) -> None:
    """ pred_expr_c : LP1 pred_expr RP1 """
    p[0] = PredExprC(pred_expr=p[2])


def p_var_expr_r0(p: yacc.YaccProduction) -> None:
    """ var_expr : unary_pred DOT member_var_name """
    p[0] = VarExpr(unary_pred=p[1], member_var_name=p[3])


def p_member_var_name_r0(p: yacc.YaccProduction) -> None:
    """ member_var_name : ID """
    p[0] = MemberVarName(id=p[1])


def p_decl_stmts_r0(p: yacc.YaccProduction) -> None:
    """ decl_stmts : decl_stmts decl_stmt """
    p[0] = DeclStmts(decl_stmts=p[1], decl_stmt=p[2])


def p_decl_stmts_r1(p: yacc.YaccProduction) -> None:
    """ decl_stmts : decl_stmt """
    p[0] = DeclStmts(decl_stmt=p[1])


def p_decl_stmt_r0(p: yacc.YaccProduction) -> None:
    """ decl_stmt : var_id S_COLON """
    p[0] = DeclStmt(var_id=p[1])


def p_decl_stmt_r1(p: yacc.YaccProduction) -> None:
    """ decl_stmt : var_id COLON unary_pred S_COLON """
    p[0] = DeclStmt(var_id=p[1], unary_pred=p[3])


def p_decl_stmt_r2(p: yacc.YaccProduction) -> None:
    """ decl_stmt : LP3 vars_id RP3 S_COLON """
    p[0] = DeclStmt(vars_id=p[2])


def p_decl_stmt_r3(p: yacc.YaccProduction) -> None:
    """ decl_stmt : LP3 vars_id RP3 COLON unary_pred S_COLON """
    p[0] = DeclStmt(vars_id=p[2], unary_pred=p[5])


def p_vars_id_r0(p: yacc.YaccProduction) -> None:
    """ vars_id : vars_id COMMA var_id """
    p[0] = VarsId(vars_id=p[1], var_id=p[3])


def p_vars_id_r1(p: yacc.YaccProduction) -> None:
    """ vars_id : var_id """
    p[0] = VarsId(var_id=p[1])


def p_var_id_r0(p: yacc.YaccProduction) -> None:
    """ var_id : ID """
    p[0] = VarId(id=p[1])


def p_decl_static_fn_stmts_r0(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmts : decl_static_fn_stmts decl_static_fn_stmt """
    p[0] = DeclStaticFnStmts(decl_static_fn_stmts=p[1], decl_static_fn_stmt=p[2])


def p_decl_static_fn_stmts_r1(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmts : decl_static_fn_stmt """
    p[0] = DeclStaticFnStmts(decl_static_fn_stmt=p[1])


def p_decl_static_fn_stmt_r0(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP1 next_preds RP1 S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1], next_preds=p[3])


def p_decl_static_fn_stmt_r1(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP1 next_preds RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1], next_preds=p[3], unary_pred=p[6])


def p_decl_static_fn_stmt_r2(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1], type_var_args=p[3], next_preds=p[6])


def p_decl_static_fn_stmt_r3(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1], type_var_args=p[3], next_preds=p[6], unary_pred=p[9])


def p_decl_static_fn_stmt_r4(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP1 RP1 S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1])


def p_decl_static_fn_stmt_r5(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP1 RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1], unary_pred=p[5])


def p_decl_static_fn_stmt_r6(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 RP1 S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1], type_var_args=p[3])


def p_decl_static_fn_stmt_r7(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 RP1 R_ARROW unary_pred S_COLON """
    p[0] = DeclStaticFnStmt(static_fn_id=p[1], type_var_args=p[3], unary_pred=p[7])


def p_static_fn_id_r0(p: yacc.YaccProduction) -> None:
    """ static_fn_id : ID """
    p[0] = StaticFnId(id=p[1])


def p_print_stmt_r0(p: yacc.YaccProduction) -> None:
    """ print_stmt : PRINTINFO to_print S_COLON """
    p[0] = PrintStmt(to_print=p[2])


def p_generate_stmt_r0(p: yacc.YaccProduction) -> None:
    """ generate_stmt : GENERATE to_print S_COLON """
    p[0] = GenerateStmt(to_generate=p[2])


def p_to_print_r0(p: yacc.YaccProduction) -> None:
    """ to_print : ID """
    p[0] = ToPrint(id_=p[1])


def p_to_print_r1(p: yacc.YaccProduction) -> None:
    """ to_print : boolean_expr """
    p[0] = ToPrint(boolean_expr=p[1])


def p_to_print_r2(p: yacc.YaccProduction) -> None:
    """ to_print : unnamed_pred """
    p[0] = ToPrint(unnamed_pred=p[1])


def p_boolean_expr_r0(p: yacc.YaccProduction) -> None:
    """ boolean_expr : boolean_expr OR boolean_expr_a """
    p[0] = BooleanExpr(boolean_expr=p[1], boolean_expr_a=p[3])


def p_boolean_expr_r1(p: yacc.YaccProduction) -> None:
    """ boolean_expr : boolean_expr_a """
    p[0] = BooleanExpr(boolean_expr_a=p[1])


def p_boolean_expr_a_r0(p: yacc.YaccProduction) -> None:
    """ boolean_expr_a : boolean_expr_a XOR boolean_expr_b """
    p[0] = BooleanExprA(boolean_expr_a=p[1], boolean_expr_b=p[3])


def p_boolean_expr_a_r1(p: yacc.YaccProduction) -> None:
    """ boolean_expr_a : boolean_expr_b """
    p[0] = BooleanExprA(boolean_expr_b=p[1])


def p_boolean_expr_b_r0(p: yacc.YaccProduction) -> None:
    """ boolean_expr_b : boolean_expr_b AND boolean_expr_c """
    p[0] = BooleanExprB(boolean_expr_b=p[1], boolean_expr_c=p[3])


def p_boolean_expr_b_r1(p: yacc.YaccProduction) -> None:
    """ boolean_expr_b : boolean_expr_c """
    p[0] = BooleanExprB(boolean_expr_c=p[1])


def p_boolean_expr_c_r0(p: yacc.YaccProduction) -> None:
    """ boolean_expr_c : boolean_expr_c EQ boolean_expr_d """
    p[0] = BooleanExprC(boolean_expr_c=p[1], is_eq=True, boolean_expr_d=p[3])


def p_boolean_expr_c_r1(p: yacc.YaccProduction) -> None:
    """ boolean_expr_c : boolean_expr_c NEQ boolean_expr_d """
    p[0] = BooleanExprC(boolean_expr_c=p[1], is_eq=False, boolean_expr_d=p[3])


def p_boolean_expr_c_r2(p: yacc.YaccProduction) -> None:
    """ boolean_expr_c : boolean_expr_d """
    p[0] = BooleanExprC(boolean_expr_d=p[1])


def p_boolean_expr_d_r0(p: yacc.YaccProduction) -> None:
    """ boolean_expr_d : NOT boolean_expr_e """
    p[0] = BooleanExprD(not_policy=True, boolean_expr_e=p[2])


def p_boolean_expr_d_r1(p: yacc.YaccProduction) -> None:
    """ boolean_expr_d : boolean_expr_e """
    p[0] = BooleanExprD(not_policy=False, boolean_expr_e=p[1])


def p_boolean_expr_e_r0(p: yacc.YaccProduction) -> None:
    """ boolean_expr_e : atomic_boolean_expr """
    p[0] = BooleanExprE(atomic_boolean_expr=p[1])


def p_boolean_expr_e_r1(p: yacc.YaccProduction) -> None:
    """ boolean_expr_e : LP1 boolean_expr RP1 """
    p[0] = BooleanExprE(boolean_expr=p[2])


def p_atomic_boolean_expr_r0(p: yacc.YaccProduction) -> None:
    """ atomic_boolean_expr : constants """
    p[0] = AtomicBooleanExprType1(constants=p[1])


def p_atomic_boolean_expr_r1(p: yacc.YaccProduction) -> None:
    """ atomic_boolean_expr : unary_pred LP1 args RP1 """
    p[0] = AtomicBooleanExprType2(unary_pred=p[1], args=p[3])


def p_atomic_boolean_expr_r2(p: yacc.YaccProduction) -> None:
    """ atomic_boolean_expr : unary_pred IMPLIES unary_pred """
    p[0] = AtomicBooleanExprType3(unary_pred=p[1], unary_pred2=p[3])


def p_atomic_boolean_expr_r3(p: yacc.YaccProduction) -> None:
    """ atomic_boolean_expr : LP1 unary_pred EQ unary_pred RP1 """
    p[0] = AtomicBooleanExprType4(unary_pred=p[2], eq_policy=True, unary_pred2=p[4])


def p_atomic_boolean_expr_r4(p: yacc.YaccProduction) -> None:
    """ atomic_boolean_expr : LP1 unary_pred NEQ unary_pred RP1 """
    p[0] = AtomicBooleanExprType4(unary_pred=p[2], eq_policy=False, unary_pred2=p[4])


def p_constants_r0(p: yacc.YaccProduction) -> None:
    """ constants : TRUE """
    p[0] = Constants(is_true=True)


def p_constants_r1(p: yacc.YaccProduction) -> None:
    """ constants : FALSE """
    p[0] = Constants(is_true=False)


def p_args_r0(p: yacc.YaccProduction) -> None:
    """ args : args COMMA arg """
    p[0] = Args(args=p[1], arg=p[3])


def p_args_r1(p: yacc.YaccProduction) -> None:
    """ args : arg """
    p[0] = Args(arg=p[1])


def p_arg_r0(p: yacc.YaccProduction) -> None:
    """ arg : ID """
    p[0] = Arg(id=p[1])


def p_assign_stmt_r0(p: yacc.YaccProduction) -> None:
    """ assign_stmt : names ASSIGN assign_expr S_COLON """
    p[0] = AssignStmt(names=p[1], assign_expr=p[3])


def p_names_r0(p: yacc.YaccProduction) -> None:
    """ names : names COMMA name """
    p[0] = Names(names=p[1], mono_name=p[3])


def p_names_r1(p: yacc.YaccProduction) -> None:
    """ names : name """
    p[0] = Names(mono_name=p[1])


def p_name_r0(p: yacc.YaccProduction) -> None:
    """ name : ID """
    p[0] = Name(id=p[1])


def p_assign_expr_r0(p: yacc.YaccProduction) -> None:
    """ assign_expr : names ASSIGN assign_expr """
    p[0] = AssignExpr(names=p[1], assign_expr=p[3])


def p_assign_expr_r1(p: yacc.YaccProduction) -> None:
    """ assign_expr : names """
    p[0] = AssignExpr(names=p[1])


# Error Recoveries.


def p_trait_decl_stmt_err0(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : error S_COLON """
    print('error detected : {0}'.format(p[1]))


def p_trait_decl_stmt_err1(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : error LP2 error RP2 S_COLON"""
    print('error detected : {0}'.format(p[1]))


def p_assign_expr_err0(p: yacc.YaccProduction) -> None:
    """
    assign_stmt : names ASSIGN error S_COLON
    """
    print('no RHS expression after the assign operator')


def p_trait_decl_err0(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id error COLON LP2 trait_decl_stmts RP2 S_COLON """
    print('the parenthesis is not opened but closed')


def p_trait_decl_err1(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id LP1 class_args error LP2 trait_decl_stmts RP2 S_COLON """
    print('the parenthesis is not closed')


def p_trait_decl_err2(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id LP1 class_args RP1 error RP2 S_COLON """
    print('the curly bracket is not opened but closed')


def p_trait_decl_err3(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id LP1 class_args RP1 LP2 error S_COLON """
    print('the curly bracket is not closed')


def p_trait_decl_err4(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id error EXTENDS unary_pred COLON LP2 trait_decl_stmts RP2 S_COLON """
    print('the parenthesis is not opened but closed')


def p_trait_decl_err5(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id LP1 class_args error EXTENDS unary_pred COLON LP2 trait_decl_stmts RP2 S_COLON """
    print('the parenthesis is not closed')


def p_trait_decl_err6(p: yacc.YaccProduction) -> None:
    """ trait_decl : TRAIT trait_id LP1 class_args RP1 COLON error S_COLON """
    print('the curly bracket is not opened but closed')


# Error recovery : handling the brace error in trait_decl_stmts
def p_trait_decl_stmt_err2(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : FN COLON error RP2 S_COLON """
    print('the curly bracket is not opened but closed')


def p_trait_decl_stmt_err3(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : FN COLON LP2 error S_COLON """
    print('the curly bracket is not closed')


def p_trait_decl_stmt_err4(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : VAR COLON error RP2 S_COLON """
    print('the curly bracket is not opened but closed')


def p_trait_decl_stmt_err5(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : VAR COLON LP2 error S_COLON """
    print('the curly bracket is not closed')


def p_trait_decl_stmt_err6(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : CLS_FN COLON error RP2 S_COLON """
    print('the curly bracket is not opened but closed')


def p_trait_decl_stmt_err7(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : CLS_FN COLON LP2 error S_COLON """
    print('the curly bracket is not closed')


def p_trait_decl_stmt_err8(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : CLS_VAR COLON error RP2 S_COLON """
    print('the curly bracket is not opened but closed')


def p_trait_decl_stmt_err9(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : CLS_VAR COLON LP2 error S_COLON """
    print('the curly bracket is not closed')


def p_trait_decl_stmt_err10(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : STATIC_FN COLON error RP2 S_COLON """
    print('the curly bracket is not opened but closed')


def p_trait_decl_stmt_err11(p: yacc.YaccProduction) -> None:
    """ trait_decl_stmt : STATIC_FN COLON LP2 error S_COLON """
    print('the curly bracket is not closed')


# Error recovery : handling the brace error in trait_decl_stmt
def p_decl_fn_stmt_err0(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id error RP1 S_COLON """
    print('the parenthesis is not opened but closed')


def p_decl_fn_stmt_err1(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP1 error S_COLON """
    print('the parenthesis is not closed')


def p_decl_fn_stmt_err2(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP3 type_var_args RP3 error RP1 S_COLON """
    print('the parenthesis is opened but closed')


def p_decl_fn_stmt_err3(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP3 type_var_args RP3 LP1 error S_COLON """
    print('the parenthesis is not closed')


def p_decl_fn_stmt_err4(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id error RP3 LP1 pred_args RP1 S_COLON """
    print('the square brace is opened but closed')


def p_decl_fn_stmt_err5(p: yacc.YaccProduction) -> None:
    """ decl_fn_stmt : fn_id LP3 error LP1 pred_args RP1 S_COLON """
    print('the square parenthesis is not closed')


# Error recovery : handling the brace error in trait_decl_stmt
def decl_cls_fn_stmt_err0(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id error RP1 S_COLON """
    print('the parenthesis is not opened but closed')


def decl_cls_fn_stmt_err1(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP1 error S_COLON """
    print('the parenthesis is not closed')


def decl_cls_fn_stmt_err2(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 error RP1 S_COLON """
    print('the parenthesis is opened but closed')


def decl_cls_fn_stmt_err3(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 LP1 error S_COLON """
    print('the parenthesis is not closed')


def decl_cls_fn_stmt_err4(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id error RP3 LP1 pred_args RP1 S_COLON """
    print('the square brace is opened but closed')


def decl_cls_fn_stmt_err5(p: yacc.YaccProduction) -> None:
    """ decl_cls_fn_stmt : fn_id LP3 error LP1 pred_args RP1 S_COLON """
    print('the square parenthesis is not closed')


# Error recovery : handling the brace error in decl_stmt
def p_decl_stmt_err0(p: yacc.YaccProduction) -> None:
    """ decl_stmt :  error RP3 S_COLON """
    print('the square bracket is not opened but closed')


def p_decl_stmt_err1(p: yacc.YaccProduction) -> None:
    """ decl_stmt :  error RP3 COLON unary_pred S_COLON """
    print('the square bracket is not closed')


def p_decl_stmt_err2(p: yacc.YaccProduction) -> None:
    """ decl_stmt :  LP3 error S_COLON """
    print('the square bracket is not closed')


# Error recovery : handling the brace error in decl_static_fn_stmt
def p_decl_static_fn_stmt_err0(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id error RP1 S_COLON """
    print('the parenthesis is not opened but closed')


def p_decl_static_fn_stmt_err1(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP1 error S_COLON """
    print('the parenthesis is not closed')


def p_decl_static_fn_stmt_err2(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 error RP1 S_COLON """
    print('the parenthesis is opened but closed')


def p_decl_static_fn_stmt_err3(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 error S_COLON """
    print('the parenthesis is not closed')


def p_decl_static_fn_stmt_err4(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id error RP3 LP1 next_preds RP1 S_COLON """
    print('the square brace is opened but closed')


def p_decl_static_fn_stmt_err5(p: yacc.YaccProduction) -> None:
    """ decl_static_fn_stmt : static_fn_id LP3 error LP1 next_preds RP1 S_COLON """
    print('the square parenthesis is not closed')


def p_error(p) -> None:

    from preprocessor.preprocessor import line_lengths
    x = line_lengths.data

    no = p.lineno - 1

    print('=' * 50)
    print("Syntax error at line %d, column %d" % (no, p.lexpos - x[0][no]))
    print(x[1][p.lineno])
    print(' ' * (p.lexpos - x[0][no]) + '^')


parser: ply.yacc.LRParser = yacc.yacc()


def get_parse_tree(s: str) -> Program:
    from preprocessor.preprocessor import preprocess
    return parser.parse(preprocess(s))


if __name__ == '__main__':
    f = open("../input.txt", 'r')
    s = f.read()
    f.close()

    from preprocessor.preprocessor import preprocess

    s = preprocess(s)

    from utils import logger

    x = parser.parse(s)

    print('=' * 50)
    if x is not None:
        x.parse_tree_print(logger=logger)
        logger.write_on_file(filename='output.txt')
        print("Parsing completed successfully")
    else:
        print("Compiler shut down due to syntax error")

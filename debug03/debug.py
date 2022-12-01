import ply.yacc
import ply.yacc as yacc

import lexer.lexer as ll

tokens = ll.tokens


def p_t(p: ply.yacc.YaccProduction):
    """
    Program : PROGRAM_BEGIN S_COLON stmts PROGRAM_END S_COLON
    stmts : stmts stmt
          | stmt
    stmt : trait_decl
         | policy_decl
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
                    | CLS_FN COLON LP2 decl_fn_stmts RP2 S_COLON
                    | CLS_VAR COLON LP2 decl_stmts RP2 S_COLON
                    | STATIC_FN COLON LP2 decl_static_fn_stmts RP2 S_COLON
    decl_fn_stmts : decl_fn_stmts decl_fn_stmt
                  | decl_fn_stmt
    decl_fn_stmt : fn_id LP1 pred_args RP1 S_COLON
                 | fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON
                 | fn_id LP1 pred_args RP1 OBEYS policy_expr S_COLON
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
    unary_pred : pred_name
               | unnamed_pred
    unnamed_pred : pred_name LP3 args RP3
                 | LP3 pred_expr RP3
                 | TYPETRACE LP1 policy_expr REV_PIPE args RP1
                 | TRAIT_OF LP1 var_expr RP1
                 | NONE
    pred_name : ID
    pred_expr : NOT pred_expr_a
              | pred_expr_a
    pred_expr_a : pred_expr_a AND pred_expr_b
                | pred_expr_a OR pred_expr_b
                | pred_expr_b
    pred_expr_b : unary_pred
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
                        | static_fn_id LP1 next_preds RP1 OBEYS policy_expr S_COLON
                        | static_fn_id LP1 RP1 S_COLON
                        | static_fn_id LP1 RP1 R_ARROW unary_pred S_COLON
                        | static_fn_id LP1 RP1 OBEYS policy_expr S_COLON
    static_fn_id : ID
    print_stmt : PRINTINFO to_print S_COLON
    generate_stmt : GENERATE to_print S_COLON
    to_print : ID
             | boolean_expr
             | unnamed_pred
             | unary_pred DOT member_fn_name
    boolean_expr : NOT boolean_expr_a
                 | boolean_expr_a
    boolean_expr_a : boolean_expr_a AND boolean_expr_b
                   | boolean_expr_a OR boolean_expr_b
                   | boolean_expr_b
    boolean_expr_b : atomic_boolean_expr
                   | LP1 boolean_expr RP1
    atomic_boolean_expr : constants
                        | unary_pred LP1 args RP1
                        | unary_pred IMPLIES unary_pred
    constants : TRUE
              | FALSE
    args : args COMMA arg
         | arg
    arg : ID
    policy_decl : POLICY policy_id COLON LP2 policy_decl_stmts RP2 S_COLON
    policy_id : ID
    policy_decl_stmts : policy_non_default_stmts policy_default_stmt
    policy_non_default_stmts : policy_non_default_stmts policy_non_default_stmt
                             | policy_non_default_stmt
    policy_non_default_stmt : unary_pred R_ARROW unary_pred S_COLON
                            | TYPENAME pred_id COLON unary_pred R_ARROW unary_pred S_COLON
                            | TYPENAME pred_id R_ARROW unary_pred S_COLON
    policy_default_stmt : DEFAULT R_ARROW unary_pred S_COLON
    policy_expr : policy_name
                | unary_pred DOT member_fn_name
    policy_name : ID
    member_fn_name : ID
    pred_id : ID
    assign_stmt : names ASSIGN assign_expr S_COLON
    names : names COMMA name
          | name
    name : ID
    assign_expr : names ASSIGN assign_expr
                | names

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

    print(parser.parse(s))
import syntax.ptnodes as pt
from utils import override


class ASTNode:
    __slots__ = ('data', 'name_order', 'node_name')

    def __init__(self, node_name: str):
        self.data: dict[str, list] = {}
        self.name_order: list[str] = []
        self.node_name = node_name

    def __bool__(self):
        return bool(self.data)

    def insert(self, key: str, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]
            self.name_order.append(key)
        return self

    def __getitem__(self, item):
        return self.data[item][-1]

    def traverse(self, indent: int = 0, *, callback=print):
        if self:
            callback('=' * indent, end=' ')
            callback(self.node_name)
        for name in self.name_order:
            for item in self.data[name]:
                if isinstance(item, ASTNode):
                    item.traverse(indent + 2, callback=callback)
                else:
                    callback('-' * (indent + 2), end=' ')
                    callback(item)
        return self


class ASTLeaf(ASTNode):
    """
    A leaf node in the AST.
    """
    __slots__ = ('data', 'name_order', 'node_name')

    @override
    def __init__(self, node_name: str):
        super().__init__(node_name)

    @override
    def insert(self, key: str, value):
        if isinstance(value, ASTNode):
            raise TypeError("ASTLeaf cannot contain ASTNode")
        return super().insert(key, value)


class Visitor:
    __slots__ = ('node',)

    def __init__(self):
        self.node = ASTNode('init')

    def visit(self, node: pt.PtNode, my_node: ASTNode = None) -> any:
        # Set the default argument.
        if my_node is None:
            my_node = self.node

        # Do nothing if the node is None.
        # You need not to check whether the node to visit is None
        # before calling this function, because this function will
        # do nothing if the node is None.

        if type(node) == type(None):
            return self

        # Overloadings.
        # Ignore the type-check warning message,
        # since types are checked in the
        # following if-else statements.

        if type(node) == pt.Program:
            return self.visit_program(node, my_node)
        elif type(node) == pt.Stmts:
            return self.visit_stmts(node, my_node)
        elif type(node) == pt.Stmt:
            return self.visit_stmt(node, my_node)
        elif type(node) == pt.TraitDecl:
            return self.visit_trait_decl(node, my_node)
        elif type(node) == pt.ClassArgs:
            return self.visit_class_args(node, my_node)
        elif type(node) == pt.SubArgs:
            return self.visit_sub_args(node, my_node)
        elif type(node) == pt.NecessaryArgs:
            return self.visit_necessary_args(node, my_node)
        elif type(node) == pt.NecessaryArg:
            return self.visit_necessary_arg(node, my_node)
        elif type(node) == pt.OptionalArgs:
            return self.visit_optional_args(node, my_node)
        elif type(node) == pt.OptionalArg:
            return self.visit_optional_arg(node, my_node)
        elif type(node) == pt.TraitDeclStmts:
            return self.visit_trait_decl_stmts(node, my_node)
        elif type(node) == pt.TraitDeclStmtFn:
            return self.visit_trait_decl_stmt_fn(node, my_node)
        elif type(node) == pt.TraitDeclStmtVar:
            return self.visit_trait_decl_stmt_var(node, my_node)
        elif type(node) == pt.TraitDeclStmtClsFn:
            return self.visit_trait_decl_stmt_cls_fn(node, my_node)
        elif type(node) == pt.TraitDeclStmtClsVar:
            return self.visit_trait_decl_stmt_cls_var(node, my_node)
        elif type(node) == pt.TraitDeclStmtStaticFn:
            return self.visit_trait_decl_stmt_static_fn(node, my_node)
        elif type(node) == pt.DeclFnStmts:
            return self.visit_decl_fn_stmts(node, my_node)
        elif type(node) == pt.DeclFnStmt:
            return self.visit_decl_fn_stmt(node, my_node)
        elif type(node) == pt.DeclClsFnStmts:
            return self.visit_decl_cls_fn_stmts(node, my_node)
        elif type(node) == pt.DeclClsFnStmt:
            return self.visit_decl_cls_fn_stmt(node, my_node)
        elif type(node) == pt.DeclStaticFnStmts:
            return self.visit_decl_static_fn_stmts(node, my_node)
        elif type(node) == pt.PredArgs:
            return self.visit_pred_args(node, my_node)
        elif type(node) == pt.NextPreds:
            return self.visit_next_preds(node, my_node)
        elif type(node) == pt.NextAnoNecPreds:
            return self.visit_next_ano_nec_preds(node, my_node)
        elif type(node) == pt.NextAnoOptPreds:
            return self.visit_next_ano_opt_preds(node, my_node)
        elif type(node) == pt.NextAnoNecPred:
            return self.visit_next_ano_nec_pred(node, my_node)
        elif type(node) == pt.NextAnoOptPred:
            return self.visit_next_ano_opt_pred(node, my_node)
        elif type(node) == pt.NextNamedPreds:
            return self.visit_next_named_preds(node, my_node)
        elif type(node) == pt.NextNamedPred:
            return self.visit_next_named_pred(node, my_node)
        elif type(node) == pt.NextNamedNecPred:
            return self.visit_next_named_nec_pred(node, my_node)
        elif type(node) == pt.NextNamedOptPred:
            return self.visit_next_named_opt_pred(node, my_node)
        elif type(node) == pt.TypeVarArgs:
            return self.visit_type_var_args(node, my_node)
        elif type(node) == pt.TypeVarArg:
            return self.visit_type_var_arg(node, my_node)
        elif type(node) == pt.UnaryPred:
            return self.visit_unary_pred(node, my_node)
        elif type(node) == pt.UnnamedPred:
            return self.visit_unnamed_pred(node, my_node)
        elif type(node) == pt.PredExpr:
            return self.visit_pred_expr(node, my_node)
        elif type(node) == pt.PredExprA:
            return self.visit_pred_expr_a(node, my_node)
        elif type(node) == pt.PredExprB:
            return self.visit_pred_expr_b(node, my_node)
        elif type(node) == pt.PredExprC:
            return self.visit_pred_expr_c(node, my_node)
        elif type(node) == pt.VarExpr:
            return self.visit_var_expr(node, my_node)
        elif type(node) == pt.DeclStmts:
            return self.visit_decl_stmts(node, my_node)
        elif type(node) == pt.DeclStmt:
            return self.visit_decl_var_stmt(node, my_node)
        elif type(node) == pt.VarsId:
            return self.visit_vars_id(node, my_node)
        elif type(node) == pt.VarId:
            return self.visit_var_id(node, my_node)
        elif type(node) == pt.DeclStaticFnStmts:
            return self.visit_decl_static_fn_stmts(node, my_node)
        elif type(node) == pt.DeclStaticFnStmt:
            return self.visit_decl_static_fn_stmt(node, my_node)
        elif type(node) == pt.PrintStmt:
            return self.visit_print_stmt(node, my_node)
        elif type(node) == pt.GenerateStmt:
            return self.visit_generate_stmt(node, my_node)
        elif type(node) == pt.ToPrint:
            return self.visit_to_print(node, my_node)
        elif type(node) == pt.BooleanExpr:
            return self.visit_boolean_expr(node, my_node)
        elif type(node) == pt.BooleanExprA:
            return self.visit_boolean_expr_a(node, my_node)
        elif type(node) == pt.BooleanExprB:
            return self.visit_boolean_expr_b(node, my_node)
        elif type(node) == pt.BooleanExprC:
            return self.visit_boolean_expr_c(node, my_node)
        elif type(node) == pt.BooleanExprD:
            return self.visit_boolean_expr_d(node, my_node)
        elif type(node) == pt.BooleanExprE:
            return self.visit_boolean_expr_e(node, my_node)
        elif type(node) == pt.AtomicBooleanExprType1:
            return self.visit_atomic_boolean_expr_type1(node, my_node)
        elif type(node) == pt.AtomicBooleanExprType2:
            return self.visit_atomic_boolean_expr_type2(node, my_node)
        elif type(node) == pt.AtomicBooleanExprType3:
            return self.visit_atomic_boolean_expr_type3(node, my_node)
        elif type(node) == pt.AtomicBooleanExprType4:
            return self.visit_atomic_boolean_expr_type4(node, my_node)
        elif type(node) == pt.Args:
            return self.visit_args(node, my_node)
        elif type(node) == pt.AssignStmt:
            return self.visit_assign_stmt(node, my_node)
        elif type(node) == pt.AssignExpr:
            return self.visit_assign_expr(node, my_node)
        elif type(node) == pt.Names:
            return self.visit_names(node, my_node)

        raise NotImplementedError('Visitor.visit() is not implemented yet for type ' + str(type(node)))

    def visit_program(self, node: pt.Program, my_node: ASTNode):
        my_node.insert('Program', ASTNode('Program'))
        self.visit(node.stmts, my_node['Program'])
        return self

    def visit_stmts(self, node: pt.Stmts, my_node: ASTNode):
        self.visit(node.stmts, my_node)
        self.visit(node.stmt, my_node)
        return self

    def visit_stmt(self, node: pt.Stmt, my_node: ASTNode):
        my_node.insert('stmt', ASTNode('statement'))
        self.visit(node.next, my_node['stmt'])
        return self

    def visit_trait_decl(self, node: pt.TraitDecl, my_node: ASTNode):
        my_node.insert('trait_decl', ASTNode('trait declaration'))
        my_node['trait_decl'].insert('id', node.trait_id.id)
        my_node['trait_decl'].insert('class_args', ASTNode('class args'))
        self.visit(node.class_args, my_node['trait_decl']['class_args'])
        my_node['trait_decl'].insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['trait_decl']['unary_pred'])
        my_node['trait_decl'].insert('trait_decl_stmts', ASTNode('declaring statements'))
        self.visit(node.trait_decl_stmts, my_node['trait_decl']['trait_decl_stmts'])
        return self

    def visit_class_args(self, node: pt.ClassArgs, my_node: ASTNode):
        my_node.insert('main_arg', node.main_arg.id)
        my_node.insert('sub_args', ASTNode('sub args'))
        self.visit(node.sub_args, my_node['sub_args'])
        return self

    def visit_sub_args(self, node: pt.SubArgs, my_node: ASTNode):
        self.visit(node.necessary_args, my_node)
        self.visit(node.optional_args, my_node)
        return self

    def visit_necessary_args(self, node: pt.NecessaryArgs, my_node: ASTNode):
        self.visit(node.necessary_args, my_node)
        self.visit(node.necessary_arg, my_node)
        return self

    def visit_necessary_arg(self, node: pt.NecessaryArg, my_node: ASTNode):
        my_node.insert('necessary_arg', node.id)
        return self

    def visit_optional_args(self, node: pt.OptionalArgs, my_node: ASTNode):
        self.visit(node.optional_args, my_node)
        self.visit(node.optional_arg, my_node)
        return self

    def visit_optional_arg(self, node: pt.OptionalArg, my_node: ASTNode):
        my_node.insert('optional_arg', ASTNode('optional'))
        my_node['optional_arg'].insert('id', node.id)
        my_node['optional_arg'].insert('default', ASTNode('default'))
        self.visit(node.unary_pred, my_node['optional_arg']['default'])

        return self

    def visit_trait_decl_stmts(self, node: pt.TraitDeclStmts, my_node: ASTNode):
        self.visit(node.trait_decl_stmts, my_node)
        self.visit(node.trait_decl_stmt, my_node)
        return self

    def visit_trait_decl_stmt_fn(self, node: pt.TraitDeclStmtFn, my_node: ASTNode):
        my_node.insert('fns', ASTNode('member functions'))
        self.visit(node.decl_fn_stmts, my_node['fns'])
        return self

    def visit_trait_decl_stmt_var(self, node: pt.TraitDeclStmtVar, my_node: ASTNode):
        my_node.insert('vars', ASTNode('member variables'))
        self.visit(node.decl_var_stmts, my_node['vars'])
        return self

    def visit_trait_decl_stmt_cls_fn(self, node: pt.TraitDeclStmtClsFn, my_node: ASTNode):
        my_node.insert('cls_fns', ASTNode('class functions'))
        self.visit(node.decl_cls_fn_stmts, my_node['cls_fns'])
        return self

    def visit_trait_decl_stmt_cls_var(self, node: pt.TraitDeclStmtClsVar, my_node: ASTNode):
        my_node.insert('cls_vars', ASTNode('class variables'))
        self.visit(node.decl_cls_var_stmts, my_node['cls_vars'])
        return self

    def visit_trait_decl_stmt_static_fn(self, node: pt.TraitDeclStmtStaticFn, my_node: ASTNode):
        my_node.insert('static_fns', ASTNode('static functions'))
        self.visit(node.decl_static_fn_stmts, my_node['static_fns'])
        return self

    def visit_decl_fn_stmts(self, node: pt.DeclFnStmts, my_node: ASTNode):
        self.visit(node.decl_fn_stmts, my_node)
        self.visit(node.decl_fn_stmt, my_node)
        return self

    def visit_decl_fn_stmt(self, node: pt.DeclFnStmt, my_node: ASTNode):
        my_node.insert('fn', ASTNode('fn'))
        fn_node = my_node['fn']

        fn_node.insert('id', node.fn_id.id)
        fn_node.insert('type_var_args', ASTNode('[args]'))
        self.visit(node.type_var_args, fn_node['type_var_args'])

        fn_node.insert('pred_args', ASTNode('(args)'))
        self.visit(node.pred_args, fn_node['pred_args'])

        fn_node.insert('return_type', ASTNode('return type'))
        self.visit(node.unary_pred, fn_node['return_type'])

        return self

    def visit_decl_cls_fn_stmts(self, node: pt.DeclClsFnStmts, my_node: ASTNode):
        self.visit(node.decl_cls_fn_stmts, my_node)
        self.visit(node.decl_cls_fn_stmt, my_node)
        return self

    def visit_decl_cls_fn_stmt(self, node: pt.DeclClsFnStmt, my_node: ASTNode):
        my_node.insert('fn', ASTNode('fn'))
        fn_node = my_node['fn']

        fn_node.insert('id', node.fn_id.id)
        fn_node.insert('type_var_args', ASTNode('[args]'))
        self.visit(node.type_var_args, fn_node['type_var_args'])

        fn_node.insert('pred_args', ASTNode('(args)'))
        self.visit(node.pred_args, fn_node['pred_args'])

        fn_node.insert('return_type', ASTNode('return type'))
        self.visit(node.unary_pred, fn_node['return_type'])

        return self

    def visit_pred_args(self, node: pt.PredArgs, my_node: ASTNode):
        my_node.insert('main_pred', node.main_pred.id)
        self.visit(node.next_preds, my_node)
        return self

    def visit_next_preds(self, node: pt.NextPreds, my_node: ASTNode):
        my_node.insert('next_anonymous_necessary_preds',
                       ASTNode('anonymous necessary'))
        self.visit(node.next_ano_nec_preds, my_node['next_anonymous_necessary_preds'])

        my_node.insert('next_anonymous_optional_preds',
                       ASTNode('anonymous optional'))
        self.visit(node.next_ano_opt_preds, my_node['next_anonymous_optional_preds'])

        self.visit(node.next_named_preds, my_node)

        return self

    def visit_next_ano_nec_preds(self, node: pt.NextAnoNecPreds, my_node: ASTNode):
        self.visit(node.next_ano_nec_preds, my_node)
        self.visit(node.next_ano_nec_pred, my_node)
        return self

    def visit_next_ano_nec_pred(self, node: pt.NextAnoNecPred, my_node: ASTNode):
        my_node.insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['unary_pred'])
        return self

    def visit_next_ano_opt_preds(self, node: pt.NextAnoOptPreds, my_node: ASTNode):
        self.visit(node.next_ano_opt_preds, my_node)
        self.visit(node.next_ano_opt_pred, my_node)
        return self

    def visit_next_ano_opt_pred(self, node: pt.NextAnoOptPred, my_node: ASTNode):
        my_node.insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['unary_pred'])
        return self

    def visit_next_named_preds(self, node: pt.NextNamedPreds, my_node: ASTNode):
        self.visit(node.next_named_preds, my_node)
        self.visit(node.next_named_pred, my_node)
        return self

    def visit_next_named_pred(self, node: pt.NextNamedPred, my_node: ASTNode):
        self.visit(node.next_named_nec_pred, my_node)
        self.visit(node.next_named_opt_pred, my_node)
        return self

    def visit_next_named_nec_pred(self, node: pt.NextNamedNecPred, my_node: ASTNode):
        my_node.insert('named_argument', ASTNode('named argument'))
        my_node['named_argument'].insert('name', node.arg_name.id)
        my_node['named_argument'].insert('rule', 'rule=necessary')
        my_node['named_argument'].insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['named_argument']['unary_pred'])
        return self

    def visit_next_named_opt_pred(self, node: pt.NextNamedOptPred, my_node: ASTNode):
        my_node.insert('named_argument', ASTNode('named argument'))
        my_node['named_argument'].insert('name', node.arg_name.id)
        my_node['named_argument'].insert('rule', 'rule=optional')
        my_node['named_argument'].insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['named_argument']['unary_pred'])
        return self

    def visit_type_var_args(self, node: pt.TypeVarArgs, my_node: ASTNode):
        self.visit(node.type_var_args, my_node)
        self.visit(node.type_var_arg, my_node)
        return self

    def visit_type_var_arg(self, node: pt.TypeVarArg, my_node: ASTNode):
        my_node.insert('type_var_id', node.type_var_id.id)
        my_node.insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['unary_pred'])
        return self

    def visit_unary_pred(self, node: pt.UnaryPred, my_node: ASTNode):
        if node.pred_name is not None:
            my_node.insert('pred_name', node.pred_name.id)
            my_node.node_name = 'named trait'
        else:
            self.visit(node.unnamed_pred, my_node)
        return self

    def visit_unnamed_pred(self, node: pt.UnnamedPred, my_node: ASTNode):
        if node.pred_name is not None:
            my_node.insert('pred_name', node.pred_name.id)
            my_node.insert('args', ASTNode('args'))
            my_node.node_name = 'unnamed_pred_rule_2'
            self.visit(node.args, my_node['args'])
        elif node.pred_expr is not None:
            my_node.node_name = 'trait AND/OR trait expression'
            self.visit(node.pred_expr, my_node)
        elif node.var_expr is not None:
            my_node.node_name = 'trait of a member variable'
            self.visit(node.var_expr, my_node)
        elif node.NONE is not None:
            my_node.insert('None', 'None')
            my_node.node_name = 'None trait'

        return self

    def visit_pred_expr(self, node: pt.PredExpr, my_node: ASTNode):
        if node.pred_expr is not None and node.pred_expr_a is not None:
            my_node.insert('LHS', ASTNode('predicate expression, LHS'))
            self.visit(node.pred_expr, my_node['LHS'])

            my_node.insert('rule', 'or')

            my_node.insert('RHS', ASTNode('predicate expression, RHS'))
            self.visit(node.pred_expr_a, my_node['RHS'])
        elif node.pred_expr_a is not None:
            self.visit(node.pred_expr_a, my_node)

        return self

    def visit_pred_expr_a(self, node: pt.PredExprA, my_node: ASTNode):
        if node.pred_expr_a is not None and node.pred_expr_b is not None:
            my_node.insert('LHS', ASTNode('predicate expression, LHS'))
            self.visit(node.pred_expr_a, my_node['LHS'])

            my_node.insert('rule', 'and')

            my_node.insert('RHS', ASTNode('predicate expression, RHS'))
            self.visit(node.pred_expr_b, my_node['RHS'])
        elif node.pred_expr_b is not None:
            self.visit(node.pred_expr_b, my_node)

        return self

    def visit_pred_expr_b(self, node: pt.PredExprB, my_node: ASTNode):
        if node.NOT is not None:
            my_node.insert('rule', 'not')
            self.visit(node.pred_expr_c, my_node)
        elif node.pred_expr_c is not None:
            self.visit(node.pred_expr_c, my_node)

        return self

    def visit_pred_expr_c(self, node: pt.PredExprC, my_node: ASTNode):
        if node.unary_pred is not None:
            my_node.insert('unary_pred', ASTNode('unary_pred'))
            self.visit(node.unary_pred, my_node['unary_pred'])
        elif node.LP1 is not None:
            self.visit(node.pred_expr, my_node)

        return self

    def visit_var_expr(self, node: pt.VarExpr, my_node: ASTNode):
        my_node.insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['unary_pred'])

        my_node.insert('rule', '.')

        my_node.insert('member_var_name', node.member_var_name.id)

        return self

    def visit_decl_stmts(self, node: pt.DeclStmts, my_node: ASTNode):
        self.visit(node.decl_stmts, my_node)
        self.visit(node.decl_stmt, my_node)
        return self

    def visit_decl_var_stmt(self, node: pt.DeclStmt, my_node: ASTNode):
        my_node.insert('var', ASTNode('var'))

        if node.var_id is not None:
            my_node['var'].insert('var_id', node.var_id.id)

        elif node.vars_id is not None:
            self.visit(node.vars_id, my_node['var'])

        my_node['var'].insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['var']['unary_pred'])

        return self

    def visit_vars_id(self, node: pt.VarsId, my_node: ASTNode):
        self.visit(node.vars_id, my_node)
        self.visit(node.var_id, my_node)
        return self

    def visit_var_id(self, node: pt.VarId, my_node: ASTNode):
        my_node.insert('var_id', node.id)
        return self

    def visit_decl_static_fn_stmts(self, node: pt.DeclStaticFnStmts, my_node: ASTNode):
        self.visit(node.decl_static_fn_stmts, my_node)
        self.visit(node.decl_static_fn_stmt, my_node)
        return self

    def visit_decl_static_fn_stmt(self, node: pt.DeclStaticFnStmt, my_node: ASTNode):
        my_node.insert('fn', ASTNode('fn'))
        fn_node = my_node['fn']

        fn_node.insert('id', node.static_fn_id.id)
        fn_node.insert('type_var_args', ASTNode('[args]'))
        self.visit(node.type_var_args, fn_node['type_var_args'])

        fn_node.insert('next_preds', ASTNode('(args)'))
        self.visit(node.next_preds, fn_node['next_preds'])

        fn_node.insert('return_type', ASTNode('return type'))
        self.visit(node.unary_pred, fn_node['return_type'])

        return self

    def visit_print_stmt(self, node: pt.PrintStmt, my_node: ASTNode):
        my_node.node_name = 'print:'
        self.visit(node.to_print, my_node)
        return self

    def visit_generate_stmt(self, node: pt.GenerateStmt, my_node: ASTNode):
        my_node.node_name = 'generate:'
        self.visit(node.to_print, my_node)
        return self

    def visit_to_print(self, node: pt.ToPrint, my_node: ASTNode):
        if node.ID is not None:
            my_node.insert('id', node.ID.id)
        elif node.boolean_expr is not None:
            my_node.insert('boolean_expr', ASTNode('boolean expression'))
            self.visit(node.boolean_expr, my_node['boolean_expr'])
        elif node.unnamed_pred is not None:
            my_node.insert('unnamed_pred', ASTNode('unnamed_pred'))
            self.visit(node.unnamed_pred, my_node['unnamed_pred'])

        return self

    def visit_boolean_expr(self, node: pt.BooleanExpr, my_node: ASTNode):
        if node.boolean_expr is not None:
            my_node.insert('LHS', ASTNode('boolean expression, LHS'))
            self.visit(node.boolean_expr, my_node['LHS'])

            my_node.insert('rule', 'or')

            my_node.insert('RHS', ASTNode('boolean expression, RHS'))
            self.visit(node.boolean_expr_a, my_node['RHS'])

        else:
            self.visit(node.boolean_expr_a, my_node)

        return self

    def visit_boolean_expr_a(self, node: pt.BooleanExprA, my_node: ASTNode):
        if node.boolean_expr_a is not None:
            my_node.insert('LHS', ASTNode('boolean expression, LHS'))
            self.visit(node.boolean_expr_a, my_node['LHS'])

            my_node.insert('rule', 'xor')

            my_node.insert('RHS', ASTNode('boolean expression, RHS'))
            self.visit(node.boolean_expr_b, my_node['RHS'])

        else:
            self.visit(node.boolean_expr_b, my_node)

        return self

    def visit_boolean_expr_b(self, node: pt.BooleanExprB, my_node: ASTNode):
        if node.boolean_expr_b is not None:
            my_node.insert('LHS', ASTNode('boolean expression, LHS'))
            self.visit(node.boolean_expr_b, my_node['LHS'])

            my_node.insert('rule', 'and')

            my_node.insert('RHS', ASTNode('boolean expression, RHS'))
            self.visit(node.boolean_expr_c, my_node['RHS'])

        else:
            self.visit(node.boolean_expr_c, my_node)

        return self

    def visit_boolean_expr_c(self, node: pt.BooleanExprC, my_node: ASTNode):
        if node.boolean_expr_c is not None:
            my_node.insert('LHS', ASTNode('boolean expression, LHS'))
            self.visit(node.boolean_expr_c, my_node['LHS'])

            if node.EQ is not None:
                my_node.insert('rule', 'eq')
            elif node.NEQ is not None:
                my_node.insert('rule', 'neq')

            my_node.insert('RHS', ASTNode('boolean expression, RHS'))
            self.visit(node.boolean_expr_d, my_node['RHS'])

        else:
            self.visit(node.boolean_expr_d, my_node)

        return self

    def visit_boolean_expr_d(self, node: pt.BooleanExprD, my_node: ASTNode):
        if node.NOT is not None:
            my_node.insert('rule', 'not')

            self.visit(node.boolean_expr_e, my_node)

        else:
            self.visit(node.boolean_expr_e, my_node)

        return self

    def visit_boolean_expr_e(self, node: pt.BooleanExprE, my_node: ASTNode):
        if node.boolean_expr is not None:
            my_node.insert('inside_parens', ASTNode('boolean expression'))
            self.visit(node.boolean_expr, my_node['inside_parens'])

        else:
            self.visit(node.atomic_boolean_expr, my_node)

        return self

    def visit_atomic_boolean_expr_type1(self, node: pt.AtomicBooleanExprType1, my_node: ASTNode):
        my_node.node_name = 'constant, boolean'

        if node.value():
            my_node.insert('value', True)
        else:
            my_node.insert('value', False)

        return self

    def visit_atomic_boolean_expr_type2(self, node: pt.AtomicBooleanExprType2, my_node: ASTNode):
        my_node.node_name = 'predicate call, boolean'

        my_node.insert('unary_pred', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['unary_pred'])

        my_node.insert('rule', 'fn_call')

        my_node.insert('args', ASTNode('args'))
        self.visit(node.args, my_node['args'])

        return self

    def visit_atomic_boolean_expr_type3(self, node: pt.AtomicBooleanExprType3, my_node: ASTNode):
        my_node.node_name = 'implies expression, boolean'

        my_node.insert('LHS', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['LHS'])

        my_node.insert('rule', 'implies')

        my_node.insert('RHS', ASTNode('unary_pred'))
        self.visit(node.unary_pred2, my_node['RHS'])

        return self

    def visit_atomic_boolean_expr_type4(self, node: pt.AtomicBooleanExprType4, my_node: ASTNode):
        my_node.node_name = 'trait ==/!= trait expression, boolean'

        my_node.insert('LHS', ASTNode('unary_pred'))
        self.visit(node.unary_pred, my_node['LHS'])

        if node.EQ is not None:
            my_node.insert('rule', 'eq')
        elif node.NEQ is not None:
            my_node.insert('rule', 'neq')

        my_node.insert('RHS', ASTNode('unary_pred'))
        self.visit(node.unary_pred2, my_node['RHS'])

        return self

    def visit_args(self, node: pt.Args, my_node: ASTNode):
        self.visit(node.args, my_node)
        my_node.insert('arg', node.arg.id)

        return self

    def visit_assign_stmt(self, node: pt.AssignStmt, my_node: ASTNode):
        my_node.insert('LHSs', ASTNode('names'))
        self.visit(node.names, my_node['LHSs'])

        my_node.insert('rule', 'assign')

        self.visit(node.assign_expr, my_node)

        return self

    def visit_names(self, node: pt.Names, my_node: ASTNode):
        self.visit(node.names, my_node)
        my_node.insert('name', node.mono_name.id)

        return self

    def visit_assign_expr(self, node: pt.AssignExpr, my_node: ASTNode):
        my_node.insert('LHSs', ASTNode('names'))
        self.visit(node.names, my_node['LHSs'])

        self.visit(node.assign_expr, my_node)

        return self


import parser.ptnodes as pt


class Visitor:
    __slots__ = ('dict',)

    def __init__(self):
        pass

    def visit(self, node: pt.PtNode):
        if type(node) == type(None):
            return None
        if type(node) == pt.Program:
            return self.visit_program(node)
        elif type(node) == pt.Stmts:
            return self.visit_stmts(node)
        elif type(node) == pt.Stmt:
            return self.visit_stmt(node)
        elif type(node) == pt.TraitDecl:
            return self.visit_trait_decl(node)
        elif type(node) == pt.TraitID:
            return self.visit_trait_id(node)
        elif type(node) == pt.ClassArgs:
            return self.visit_class_args(node)
        elif type(node) == pt.MainArg:
            return self.visit_main_arg(node)

        raise NotImplementedError('Visitor.visit() is not implemented yet for type ' + str(type(node)))

    def visit_program(self, node: pt.Program):
        self.visit(node.stmts)
        return

    def visit_stmts(self, node: pt.Stmts):
        self.visit(node.stmts)
        self.visit(node.stmt)
        return

    def visit_stmt(self, node: pt.Stmt):
        self.visit(node.next)
        return

    def visit_trait_decl(self, node: pt.TraitDecl):
        self.visit(node.trait_id)
        self.visit(node.class_args)
        self.visit(node.unary_pred)
        self.visit(node.trait_decl_stmts)
        return

    def visit_trait_id(self, node: pt.TraitID):
        self.visit(node.id)
        return

    def visit_class_args(self, node: pt.ClassArgs):
        self.visit(node.main_arg)
        self.visit(node.sub_args)
        return

    def visit_main_arg(self, node: pt.MainArg) -> str:
        return node.id

    def visit_sub_args(self, node: pt.SubArgs):
        self.visit(node.necessary_args)
        self.visit(node.optional_args)
        return

    def visit_necessary_args(self, node: pt.NecessaryArgs):
        self.visit(node.necessary_args)
        self.visit(node.necessary_arg)
        return

    def visit_necessary_arg(self, node: pt.NecessaryArg) -> str:
        return node.id

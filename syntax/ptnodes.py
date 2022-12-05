from utils import override


class PtNode:
    __slots__ = ()

    name: str = 'None'

    def parse_tree_print(self, indent: int = 0, logger=None) -> None:
        if logger is None:
            print('=' * indent, end=' ')
            print(self.name)
        else:
            logger.log('=' * indent + ' ' + self.name)
        for slot in self.__slots__:
            val: PtNode = getattr(self, slot)
            if val is not None:
                val.parse_tree_print(indent + 2, logger)

    def accept(self, visitor) -> 'PtNode':
        return visitor.visit(self)

    def null_init(self) -> None:
        """
        Initialize all slots to None.
        """
        for slot in self.__slots__:
            setattr(self, slot, None)


class TermNode(PtNode):
    __slots__ = ('terminal_name',)

    def __init__(self, name: str) -> None:
        self.terminal_name: str = name

    def __eq__(self, other):
        if isinstance(other, TermNode):
            return self.terminal_name == other.terminal_name
        return False

    @override
    def parse_tree_print(self, indent: int = 0, logger=None) -> None:
        if logger is None:
            print('-' * indent, end=' ')
            print(self.terminal_name)
        else:
            logger.log('-' * indent + ' ' + self.terminal_name)


class IDNode(PtNode):
    __slots__ = ('id',)

    def __init__(self, id: str):
        self.id = id

    def __repr__(self):
        return self.id

    @override
    def parse_tree_print(self, indent: int = 0, logger=None) -> None:
        if logger is None:
            print('-' * indent, end=' ')
            print(self.id)
        else:
            logger.log('-' * indent + ' ' + self.id)


class Flyweights:
    """
    This is a namespace for storing flyweight objects.
    """
    program_begin = TermNode('PROGRAM_BEGIN')
    program_end = TermNode('PROGRAM_END')

    fn = TermNode('fn')
    or_ = TermNode('or')
    and_ = TermNode('and')
    not_ = TermNode('not')
    var = TermNode('var')
    xor = TermNode('xor')
    none = TermNode('None')
    pass_ = TermNode('pass')
    true = TermNode('True')
    false = TermNode('False')
    trait = TermNode('trait_id')
    cls_fn = TermNode('cls_fn')
    cls_var = TermNode('cls_var')
    extends = TermNode('extends')
    implies = TermNode('implies')
    generate = TermNode('generate')
    trait_of = TermNode('trait_of')
    printinfo = TermNode('printinfo')
    static_fn = TermNode('static_fn')

    s_colon = TermNode(';')
    colon = TermNode(':')
    comma = TermNode(',')
    dot = TermNode('.')
    r_arrow = TermNode('->')

    lp1 = TermNode('(')
    rp1 = TermNode(')')
    lp2 = TermNode('{')
    rp2 = TermNode('}')
    lp3 = TermNode('[')
    rp3 = TermNode(']')
    star = TermNode('*')
    assign = TermNode('=')
    eq = TermNode('==')
    neq = TermNode('!=')


fw = Flyweights  # alias


class Program(PtNode):
    __slots__ = ('PROGRAM_BEGIN', 'S_COLON', 'stmts',
                 'PROGRAM_END', 'S_COLON2')

    name: str = 'program'

    def __init__(self, stmts) -> None:
        self.PROGRAM_BEGIN = fw.program_begin
        self.S_COLON = fw.s_colon
        self.stmts = stmts
        self.PROGRAM_END = fw.program_end
        self.S_COLON2 = fw.s_colon


class Stmts(PtNode):
    __slots__ = ('stmts', 'stmt')

    name: str = 'stmts'

    def __init__(self, stmts=None, stmt=None) -> None:
        self.stmts = stmts
        self.stmt = stmt

        if stmt is None:
            raise ValueError("stmt cannot be None")


class Stmt(PtNode):
    __slots__ = ('next',)

    name: str = 'stmt'

    def __init__(self, next) -> None:
        self.next = next


class TraitDecl(PtNode):
    __slots__ = ('TRAIT', 'trait_id', 'LP1', 'class_args', 'RP1',
                 'EXTENDS', 'unary_pred', 'COLON',
                 'LP2', 'trait_decl_stmts', 'RP2', 'S_COLON')

    name: str = 'trait_decl'

    def __init__(self, trait_id, class_args, trait_decl_stmts,
                 *, unary_pred=None) -> None:
        self.TRAIT = fw.trait
        self.trait_id = trait_id
        self.LP1 = fw.lp1
        self.class_args = class_args
        self.RP1 = fw.rp1
        self.unary_pred = unary_pred
        self.COLON = fw.colon
        self.LP2 = fw.lp2
        self.trait_decl_stmts = trait_decl_stmts
        self.RP2 = fw.rp2
        self.S_COLON = fw.s_colon

        if unary_pred is not None:
            self.EXTENDS = fw.extends
        else:
            self.EXTENDS = None


class TraitID(PtNode):
    __slots__ = ('id',)

    name: str = 'trait_id'

    def __init__(self, id: str) -> None:
        self.id: IDNode = IDNode(id)


class ClassArgs(PtNode):
    __slots__ = ('main_arg', 'COMMA', 'sub_args')

    name: str = 'class_args'

    def __init__(self, main_arg, sub_args=None) -> None:
        self.main_arg = main_arg
        self.sub_args = sub_args
        if sub_args is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None


class MainArg(PtNode):
    __slots__ = ('id',)

    name: str = 'main_arg'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class SubArgs(PtNode):
    __slots__ = ('necessary_args', 'COMMA', 'optional_args')

    name: str = 'sub_args'

    def __init__(self, necessary_args=None, optional_args=None) -> None:
        self.necessary_args = necessary_args
        self.optional_args = optional_args

        if necessary_args is not None and optional_args is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if necessary_args is None and optional_args is None:
            raise ValueError('At least one of necessary_args and optional_args must be not None')


class NecessaryArgs(PtNode):
    __slots__ = ('necessary_args', 'COMMA', 'necessary_arg')

    name: str = 'necessary_args'

    def __init__(self, necessary_args=None, necessary_arg=None) -> None:
        self.necessary_args = necessary_args
        self.necessary_arg = necessary_arg

        if necessary_args is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if necessary_arg is None:
            raise ValueError('necessary_arg must be not None')


class NecessaryArg(PtNode):
    __slots__ = ('id',)

    name: str = 'necessary_arg'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class OptionalArgs(PtNode):
    __slots__ = ('optional_args', 'COMMA', 'optional_arg')

    name: str = 'optional_args'

    def __init__(self, optional_args=None, optional_arg=None) -> None:
        self.optional_args = optional_args
        self.optional_arg = optional_arg
        if optional_args is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if optional_arg is None:
            raise ValueError('optional_arg must be not None')


class OptionalArg(PtNode):
    __slots__ = ('id', 'ASSIGN', 'unary_pred')

    name: str = 'optional_arg'

    def __init__(self, id: str, unary_pred) -> None:
        self.id = IDNode(id)
        self.ASSIGN = fw.assign
        self.unary_pred = unary_pred


class TraitDeclStmts(PtNode):
    __slots__ = ('trait_decl_stmts', 'trait_decl_stmt',
                 'PASS', 'S_COLON')

    name: str = 'trait_decl_stmts'

    def __init__(self, trait_decl_stmts=None, trait_decl_stmt=None,
                 pass_=False) -> None:
        if pass_:
            self.trait_decl_stmts = None
            self.trait_decl_stmt = None
            self.PASS = fw.pass_
            self.S_COLON = fw.s_colon
            return

        self.trait_decl_stmts = trait_decl_stmts
        self.trait_decl_stmt = trait_decl_stmt
        self.PASS = None
        self.S_COLON = None


class TraitDeclStmt(PtNode):
    __slots__ = ('decl_type', 'COLON', 'LP2',
                 'decl_stmts', 'RP2', 'S_COLON')

    name: str = 'trait_decl_stmt'


class TraitDeclStmtFn(TraitDeclStmt):
    __slots__ = ('FN', 'COLON', 'LP2', 'decl_fn_stmts', 'RP2', 'S_COLON')

    def __init__(self, decl_fn_stmts) -> None:
        self.FN = fw.fn
        self.COLON = fw.colon
        self.LP2 = fw.lp2
        self.decl_fn_stmts = decl_fn_stmts
        self.RP2 = fw.rp2
        self.S_COLON = fw.s_colon


class TraitDeclStmtVar(TraitDeclStmt):
    __slots__ = ('VAR', 'COLON', 'LP2', 'decl_var_stmts', 'RP2', 'S_COLON')

    def __init__(self, decl_var_stmts) -> None:
        self.VAR = fw.var
        self.COLON = fw.colon
        self.LP2 = fw.lp2
        self.decl_var_stmts = decl_var_stmts
        self.RP2 = fw.rp2
        self.S_COLON = fw.s_colon


class TraitDeclStmtClsFn(TraitDeclStmt):
    __slots__ = ('CLS_FN', 'COLON', 'LP2', 'decl_cls_fn_stmts', 'RP2', 'S_COLON')

    def __init__(self, decl_cls_fn_stmts) -> None:
        self.CLS_FN = fw.cls_fn
        self.COLON = fw.colon
        self.LP2 = fw.lp2
        self.decl_cls_fn_stmts = decl_cls_fn_stmts
        self.RP2 = fw.rp2
        self.S_COLON = fw.s_colon


class TraitDeclStmtClsVar(TraitDeclStmt):
    __slots__ = ('CLS_VAR', 'COLON', 'LP2', 'decl_cls_var_stmts', 'RP2', 'S_COLON')

    def __init__(self, decl_cls_var_stmts) -> None:
        self.CLS_VAR = fw.cls_var
        self.COLON = fw.colon
        self.LP2 = fw.lp2
        self.decl_cls_var_stmts = decl_cls_var_stmts
        self.RP2 = fw.rp2
        self.S_COLON = fw.s_colon


class TraitDeclStmtStaticFn(TraitDeclStmt):
    __slots__ = ('STATIC_FN', 'COLON', 'LP2', 'decl_static_fn_stmts', 'RP2', 'S_COLON')

    def __init__(self, decl_static_fn_stmts) -> None:
        self.STATIC_FN = fw.static_fn
        self.COLON = fw.colon
        self.LP2 = fw.lp2
        self.decl_static_fn_stmts = decl_static_fn_stmts
        self.RP2 = fw.rp2
        self.S_COLON = fw.s_colon


class DeclFnStmts(PtNode):
    __slots__ = ('decl_fn_stmts', 'decl_fn_stmt')

    name: str = 'decl_fn_stmts'

    def __init__(self, decl_fn_stmts=None, decl_fn_stmt=None) -> None:
        self.decl_fn_stmts = decl_fn_stmts
        self.decl_fn_stmt = decl_fn_stmt


class DeclFnStmt(PtNode):
    __slots__ = ('fn_id', 'LP3', 'type_var_args', 'RP3',
                 'LP1', 'pred_args', 'RP1',
                 'R_ARROW', 'unary_pred', 'S_COLON')

    name: str = 'decl_fn_stmt'

    def __init__(self, fn_id, type_var_args=None,
                 pred_args=None, unary_pred=None) -> None:
        self.null_init()

        self.fn_id = fn_id

        if type_var_args is not None:
            self.LP3 = fw.lp3
            self.type_var_args = type_var_args
            self.RP3 = fw.rp3

        self.LP1 = fw.lp1
        self.pred_args = pred_args
        self.RP1 = fw.rp1

        if unary_pred is not None:
            self.R_ARROW = fw.r_arrow
            self.unary_pred = unary_pred

        self.S_COLON = fw.s_colon


class DeclClsFnStmts(PtNode):
    __slots__ = ('decl_cls_fn_stmts', 'decl_cls_fn_stmt')

    name: str = 'decl_cls_fn_stmts'

    def __init__(self, decl_cls_fn_stmts=None,
                 decl_cls_fn_stmt=None) -> None:
        self.decl_cls_fn_stmts = decl_cls_fn_stmts
        self.decl_cls_fn_stmt = decl_cls_fn_stmt


class DeclClsFnStmt(PtNode):
    __slots__ = ('fn_id', 'LP3', 'type_var_args', 'RP3',
                 'LP1', 'pred_args', 'RP1',
                 'R_ARROW', 'unary_pred', 'S_COLON')

    name: str = 'decl_cls_fn_stmt'

    def __init__(self, fn_id, type_var_args=None,
                 pred_args=None, unary_pred=None) -> None:
        self.null_init()

        self.fn_id = fn_id

        if type_var_args is not None:
            self.LP3 = fw.lp3
            self.type_var_args = type_var_args
            self.RP3 = fw.rp3

        self.LP1 = fw.lp1
        self.pred_args = pred_args
        self.RP1 = fw.rp1

        if unary_pred is not None:
            self.R_ARROW = fw.r_arrow
            self.unary_pred = unary_pred

        self.S_COLON = fw.s_colon


class FnID(PtNode):
    __slots__ = ('id',)

    name: str = 'fn_id'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class PredArgs(PtNode):
    __slots__ = ('main_pred', 'COMMA', 'next_preds')

    name: str = 'pred_args'

    def __init__(self, main_pred, next_preds=None) -> None:
        self.main_pred = main_pred
        self.next_preds = next_preds

        if next_preds is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None


class MainPred(PtNode):
    __slots__ = ('id',)

    name: str = 'main_pred'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class NextPreds(PtNode):
    __slots__ = ('next_ano_nec_preds', 'COMMA1',
                 'next_ano_opt_preds', 'COMMA2',
                 'STAR', 'COMMA3',
                 'next_named_preds')

    name: str = 'next_preds'

    def __init__(self, next_ano_nec_preds=None,
                 next_ano_opt_preds=None,
                 starred=False,
                 next_named_preds=None) -> None:
        if next_named_preds is not None:
            self.next_named_preds = next_named_preds
            self.COMMA3 = fw.comma
        else:
            self.next_named_preds = None
            self.COMMA3 = None
        if starred:
            self.STAR = fw.star
            self.COMMA2 = fw.comma
        else:
            self.STAR = None
            self.COMMA2 = None
        if next_ano_opt_preds is not None:
            self.next_ano_opt_preds = next_ano_opt_preds
            self.COMMA1 = fw.comma
        else:
            self.next_ano_opt_preds = None
            self.COMMA1 = None
        if next_ano_nec_preds is not None:
            self.next_ano_nec_preds = next_ano_nec_preds
        else:
            self.next_ano_nec_preds = None
        return


class NextAnoNecPreds(PtNode):
    __slots__ = ('next_ano_nec_preds', 'COMMA', 'next_ano_nec_pred')

    name: str = 'next_anonymous_necessary_preds'

    def __init__(self, next_ano_nec_preds=None,
                 next_ano_nec_pred=None) -> None:
        self.next_ano_nec_preds = next_ano_nec_preds
        self.next_ano_nec_pred = next_ano_nec_pred
        if next_ano_nec_preds is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if next_ano_nec_pred is None:
            raise ValueError('next_ano_nec_pred cannot be None')


class NextAnoNecPred(PtNode):
    __slots__ = ('unary_pred',)

    name: str = 'next_anonymous_necessary_pred'

    def __init__(self, unary_pred) -> None:
        self.unary_pred = unary_pred


class NextAnoOptPreds(PtNode):
    __slots__ = ('next_ano_opt_preds', 'COMMA', 'next_ano_opt_pred')

    name: str = 'next_anonymous_optional_preds'

    def __init__(self, next_ano_opt_preds=None,
                 next_ano_opt_pred=None) -> None:
        self.next_ano_opt_preds = next_ano_opt_preds
        self.next_ano_opt_pred = next_ano_opt_pred
        if next_ano_opt_preds is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if next_ano_opt_pred is None:
            raise ValueError('next_ano_opt_pred cannot be None')


class NextAnoOptPred(PtNode):
    __slots__ = ('ASSIGN', 'unary_pred')

    name: str = 'next_anonymous_optional_pred'

    def __init__(self, unary_pred) -> None:
        self.ASSIGN = fw.assign
        self.unary_pred = unary_pred


class NextNamedPreds(PtNode):
    __slots__ = ('next_named_preds', 'COMMA', 'next_named_pred')

    name: str = 'next_named_preds'

    def __init__(self, next_named_preds=None,
                 next_named_pred=None) -> None:
        self.next_named_preds = next_named_preds
        self.next_named_pred = next_named_pred
        if next_named_preds is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if next_named_pred is None:
            raise ValueError('next_named_pred must not be None')


class NextNamedPred(PtNode):
    __slots__ = ('next_named_nec_pred',
                 'next_named_opt_pred')

    name: str = 'next_named_pred'

    def __init__(self, *, next_named_nec_pred=None,
                 next_named_opt_pred=None) -> None:
        self.next_named_nec_pred = next_named_nec_pred
        self.next_named_opt_pred = next_named_opt_pred

        # check that only one of the two is not None
        a = next_named_nec_pred is None
        b = next_named_opt_pred is None
        if a ^ b:
            pass
        else:
            raise ValueError('next_named_pred must have exactly one child')


class NextNamedNecPred(PtNode):
    __slots__ = ('arg_name', 'COLON', 'unary_pred')

    name: str = 'next_named_necessary_pred'

    def __init__(self, arg_name, unary_pred) -> None:
        self.arg_name = arg_name
        self.COLON = fw.colon
        self.unary_pred = unary_pred


class NextNamedOptPred(PtNode):
    __slots__ = ('arg_name', 'COLON', 'ASSIGN', 'unary_pred')

    name: str = 'next_named_optional_pred'

    def __init__(self, arg_name, unary_pred) -> None:
        self.arg_name = arg_name
        self.COLON = fw.colon
        self.ASSIGN = fw.assign
        self.unary_pred = unary_pred


class ArgName(PtNode):
    __slots__ = ('id',)

    name: str = 'arg_name'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class TypeVarArgs(PtNode):
    __slots__ = ('type_var_args', 'COMMA', 'type_var_arg')

    name: str = 'type_var_args'

    def __init__(self, type_var_args=None, type_var_arg=None) -> None:
        self.type_var_args = type_var_args
        self.type_var_arg = type_var_arg
        if type_var_args is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if type_var_arg is None:
            raise ValueError('type_var_arg must not be None')


class TypeVarArg(PtNode):
    __slots__ = ('type_var_id', 'COLON', 'unary_pred')

    name: str = 'type_var_arg'

    def __init__(self, type_var_id, unary_pred=None) -> None:
        self.type_var_id = type_var_id
        self.unary_pred = unary_pred

        if unary_pred is not None:
            self.COLON = fw.colon
        else:
            self.COLON = None


class TypeVarId(PtNode):
    __slots__ = ('id',)

    name: str = 'type_var_id'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class UnaryPred(PtNode):
    __slots__ = ('pred_name', 'unnamed_pred')

    name: str = 'unary_pred'

    def __init__(self, *, pred_name=None, unnamed_pred=None) -> None:
        self.pred_name = pred_name
        self.unnamed_pred = unnamed_pred

        # check that only one of the two is not None
        a = pred_name is None
        b = unnamed_pred is None
        if a ^ b:
            pass
        else:
            raise ValueError('unary_pred must have exactly one child')


class PredName(PtNode):
    __slots__ = ('id',)

    name: str = 'pred_name'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class UnnamedPred(PtNode):
    __slots__ = ('pred_name', 'LP3', 'args', 'RP3',
                 'LP32', 'pred_expr', 'RP32',
                 'TRAIT_OF', 'LP1', 'var_expr', 'RP1',
                 'NONE')

    name: str = 'unnamed_pred'

    def __init__(self, *, pred_name=None, args=None, pred_expr=None,
                 var_expr=None, none_=None) -> None:
        self.null_init()

        if pred_name is not None:
            self.pred_name = pred_name
            self.LP3 = fw.lp3
            self.args = args
            self.RP3 = fw.rp3
        elif pred_expr is not None:
            self.LP32 = fw.lp3
            self.pred_expr = pred_expr
            self.RP32 = fw.rp3
        elif var_expr is not None:
            self.TRAIT_OF = fw.trait_of
            self.LP1 = fw.lp1
            self.var_expr = var_expr
            self.RP1 = fw.rp1
        elif none_ is not None:
            self.NONE = fw.none


class PredExpr(PtNode):
    __slots__ = ('pred_expr', 'OR', 'pred_expr_a')

    name: str = 'pred_expr'

    def __init__(self, pred_expr=None, pred_expr_a=None) -> None:
        self.pred_expr = pred_expr
        self.pred_expr_a = pred_expr_a
        if pred_expr is not None:
            self.OR = fw.or_
        else:
            self.OR = None
        if pred_expr_a is None:
            raise ValueError('pred_expr_a must not be None')


class PredExprA(PtNode):
    __slots__ = ('pred_expr_a', 'AND', 'pred_expr_b')

    name: str = 'pred_expr_a'

    def __init__(self, pred_expr_a=None, pred_expr_b=None) -> None:
        self.pred_expr_a = pred_expr_a
        self.pred_expr_b = pred_expr_b
        if pred_expr_a is not None:
            self.AND = fw.and_
        else:
            self.AND = None
        if pred_expr_b is None:
            raise ValueError('pred_expr_b must not be None')


class PredExprB(PtNode):
    __slots__ = ('NOT', 'pred_expr_c')

    name: str = 'pred_expr_b'

    def __init__(self, not_policy=False, pred_expr_c=None) -> None:
        self.pred_expr_c = pred_expr_c
        if not_policy:
            self.NOT = fw.not_
        else:
            self.NOT = None
        if pred_expr_c is None:
            raise ValueError('pred_expr_c must not be None')


class PredExprC(PtNode):
    __slots__ = ('unary_pred', 'LP1', 'pred_expr', 'RP1')

    name: str = 'pred_expr_c'

    def __init__(self, unary_pred=None, pred_expr=None) -> None:
        self.unary_pred = unary_pred
        self.pred_expr = pred_expr

        err = ValueError('pred_expr_c must have exactly one child')

        if unary_pred is not None:
            self.LP1 = None
            self.RP1 = None
            if pred_expr is not None:
                raise err
        elif pred_expr is not None:
            self.LP1 = fw.lp1
            self.RP1 = fw.rp1
        else:
            raise err


class VarExpr(PtNode):
    __slots__ = ('unary_pred', 'DOT', 'member_var_name')

    name: str = 'var_expr'

    def __init__(self, unary_pred=None, member_var_name=None) -> None:
        self.unary_pred = unary_pred
        self.DOT = fw.dot
        self.member_var_name = member_var_name


class MemberVarName(PtNode):
    __slots__ = ('id',)

    name: str = 'member_var_name'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class DeclStmts(PtNode):
    __slots__ = ('decl_stmts', 'decl_stmt')

    name: str = 'decl_stmts'

    def __init__(self, decl_stmts=None, decl_stmt=None) -> None:
        self.decl_stmts = decl_stmts
        self.decl_stmt = decl_stmt

        if decl_stmt is None:
            raise ValueError('decl_stmt must not be None')


class DeclStmt(PtNode):
    __slots__ = ('var_id', 'LP3', 'vars_id', 'RP3',
                 'COLON', 'unary_pred', 'S_COLON')

    name: str = 'decl_stmt'

    def __init__(self, var_id=None, vars_id=None, unary_pred=None) -> None:
        err = ValueError('only one of var_id or vars_id can be set')

        self.null_init()

        if var_id is not None:
            self.var_id = var_id
            if vars_id is not None:
                raise err
        elif vars_id is not None:
            self.LP3 = fw.lp3
            self.vars_id = vars_id
            self.RP3 = fw.rp3
        else:
            raise err

        if unary_pred is not None:
            self.COLON = fw.colon
            self.unary_pred = unary_pred
        else:
            pass

        self.S_COLON = fw.s_colon


class VarsId(PtNode):
    __slots__ = ('vars_id', 'COMMA', 'var_id')

    name: str = 'vars_id'

    def __init__(self, vars_id=None, var_id=None) -> None:
        self.vars_id = vars_id
        self.var_id = var_id

        if vars_id is not None:
            self.COMMA = fw.comma
        else:
            self.COMMA = None

        if var_id is None:
            raise ValueError('var_id must not be None')


class VarId(PtNode):
    __slots__ = ('id',)

    name: str = 'var_id'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class DeclStaticFnStmts(PtNode):
    __slots__ = ('decl_static_fn_stmts', 'decl_static_fn_stmt')

    name: str = 'decl_static_fn_stmts'

    def __init__(self, decl_static_fn_stmts=None, decl_static_fn_stmt=None) -> None:
        self.decl_static_fn_stmts = decl_static_fn_stmts
        self.decl_static_fn_stmt = decl_static_fn_stmt


class DeclStaticFnStmt(PtNode):
    __slots__ = ('static_fn_id',
                 'LP3', 'type_var_args', 'RP3',
                 'LP1', 'next_preds', 'RP1',
                 'R_ARROW', 'unary_pred',
                 'S_COLON')

    name: str = 'decl_static_fn_stmt'

    def __init__(self, static_fn_id=None,
                 type_var_args=None,
                 next_preds=None,
                 unary_pred=None) -> None:
        self.null_init()

        self.static_fn_id = static_fn_id

        if type_var_args is not None:
            self.LP3 = fw.lp3
            self.type_var_args = type_var_args
            self.RP3 = fw.rp3

        self.LP1 = fw.lp1
        self.next_preds = next_preds
        self.RP1 = fw.rp1

        if unary_pred is not None:
            self.R_ARROW = fw.r_arrow
            self.unary_pred = unary_pred

        self.S_COLON = fw.s_colon


class StaticFnId(PtNode):
    __slots__ = ('id',)

    name: str = 'static_fn_id'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class PrintStmt(PtNode):
    __slots__ = ('PRINTINFO', 'to_print', 'S_COLON')

    name: str = 'print_stmt'

    def __init__(self, to_print) -> None:
        self.PRINTINFO = fw.printinfo
        self.to_print = to_print
        self.S_COLON = fw.s_colon


class GenerateStmt(PtNode):
    __slots__ = ('GENERATE', 'to_print', 'S_COLON')

    name: str = 'generate_stmt'

    def __init__(self, to_generate) -> None:
        self.GENERATE = fw.generate
        self.to_print = to_generate
        self.S_COLON = fw.s_colon


class ToPrint(PtNode):
    __slots__ = ('ID', 'boolean_expr', 'unnamed_pred')

    name: str = 'to_print'

    def __init__(self, id_=None, boolean_expr=None, unnamed_pred=None):
        err = ValueError('only one of id_, boolean_expr or unnamed_pred can be set')

        self.null_init()

        if id_ is not None:
            self.ID = IDNode(id_)
            if boolean_expr is not None or unnamed_pred is not None:
                raise err
        elif boolean_expr is not None:
            self.boolean_expr = boolean_expr
            if unnamed_pred is not None:
                raise err
        elif unnamed_pred is not None:
            self.unnamed_pred = unnamed_pred
        else:
            raise err


class BooleanExpr(PtNode):
    __slots__ = ('boolean_expr', 'OR', 'boolean_expr_a')

    name: str = 'boolean_expr'

    def __init__(self, boolean_expr=None, boolean_expr_a=None) -> None:
        self.boolean_expr = boolean_expr
        self.boolean_expr_a = boolean_expr_a

        if boolean_expr is not None:
            self.OR = fw.or_
        else:
            self.OR = None


class BooleanExprA(PtNode):
    __slots__ = ('boolean_expr_a', 'XOR', 'boolean_expr_b')

    name: str = 'boolean_expr_a'

    def __init__(self, boolean_expr_a=None, boolean_expr_b=None) -> None:
        self.boolean_expr_a = boolean_expr_a
        self.boolean_expr_b = boolean_expr_b

        if boolean_expr_a is not None:
            self.XOR = fw.xor
        else:
            self.XOR = None


class BooleanExprB(PtNode):
    __slots__ = ('boolean_expr_b', 'AND', 'boolean_expr_c')

    name: str = 'boolean_expr_b'

    def __init__(self, boolean_expr_b=None, boolean_expr_c=None) -> None:
        self.boolean_expr_b = boolean_expr_b
        self.boolean_expr_c = boolean_expr_c

        if boolean_expr_b is not None:
            self.AND = fw.and_
        else:
            self.AND = None

        if boolean_expr_c is None:
            raise ValueError('boolean_expr_c must not be None')


class BooleanExprC(PtNode):
    __slots__ = ('boolean_expr_c', 'EQ', 'NEQ', 'boolean_expr_d')

    name: str = 'boolean_expr_c'

    def __init__(self, boolean_expr_c=None, is_eq: bool = True, boolean_expr_d=None) -> None:
        self.boolean_expr_c = boolean_expr_c
        if boolean_expr_c is None:
            self.EQ = None
            self.NEQ = None
        elif is_eq:
            self.EQ = fw.eq
            self.NEQ = None
        else:
            self.EQ = None
            self.NEQ = fw.neq
        self.boolean_expr_d = boolean_expr_d

        if boolean_expr_d is None:
            raise ValueError('boolean_expr_d must not be None')


class BooleanExprD(PtNode):
    __slots__ = ('NOT', 'boolean_expr_e')

    name: str = 'boolean_expr_d'

    def __init__(self, not_policy: bool = False, boolean_expr_e=None) -> None:
        if not_policy:
            self.NOT = fw.not_
        else:
            self.NOT = None
        self.boolean_expr_e = boolean_expr_e


class BooleanExprE(PtNode):
    __slots__ = ('atomic_boolean_expr',
                 'LP1', 'boolean_expr', 'RP1')

    name: str = 'boolean_expr_e'

    def __init__(self, atomic_boolean_expr=None, boolean_expr=None) -> None:
        self.null_init()

        err = ValueError('only one of atomic_boolean_expr or boolean_expr can be set')

        if atomic_boolean_expr is not None:
            self.atomic_boolean_expr = atomic_boolean_expr
            if boolean_expr is not None:
                raise err
        elif boolean_expr is not None:
            self.LP1 = fw.lp1
            self.boolean_expr = boolean_expr
            self.RP1 = fw.rp1


class AtomicBooleanExpr(PtNode):
    name: str = 'atomic_boolean_expr'

    pass


class AtomicBooleanExprType1(AtomicBooleanExpr):
    __slots__ = ('constants',)

    def __init__(self, constants) -> None:
        self.constants = constants

    def value(self) -> bool:
        if self.constants == fw.true:
            return True
        return False


class AtomicBooleanExprType2(AtomicBooleanExpr):
    __slots__ = ('unary_pred', 'LP1', 'args', 'RP1')

    def __init__(self, unary_pred, args) -> None:
        self.unary_pred = unary_pred
        self.LP1 = fw.lp1
        self.args = args
        self.RP1 = fw.rp1


class AtomicBooleanExprType3(AtomicBooleanExpr):
    __slots__ = ('unary_pred', 'IMPLIES', 'unary_pred2')

    def __init__(self, unary_pred, unary_pred2) -> None:
        self.unary_pred = unary_pred
        self.IMPLIES = fw.implies
        self.unary_pred2 = unary_pred2


class AtomicBooleanExprType4(AtomicBooleanExpr):
    __slots__ = ('LP1', 'unary_pred', 'EQ', 'NEQ', 'unary_pred2', 'RP1')

    def __init__(self, unary_pred, unary_pred2, eq_policy: bool = True) -> None:
        self.LP1 = fw.lp1
        self.unary_pred = unary_pred
        if eq_policy:
            self.EQ = fw.eq
        else:
            self.NEQ = fw.neq
        self.unary_pred2 = unary_pred2
        self.RP1 = fw.rp1


class Constants(PtNode):
    __slots__ = ('VALUE',)

    name: str = 'constants'

    def __init__(self, is_true: bool = True) -> None:
        if is_true:
            self.VALUE = fw.true
        else:
            self.VALUE = fw.false


class Args(PtNode):
    __slots__ = ('args', 'COMMA', 'arg')

    name: str = 'args'

    def __init__(self, args=None, arg=None) -> None:
        if args is not None:
            self.args = args
            self.COMMA = fw.comma
        else:
            self.args = None
            self.COMMA = None

        self.arg = arg

        if arg is None:
            raise ValueError('arg must not be None')


class Arg(PtNode):
    __slots__ = ('id',)

    name: str = 'arg'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class AssignStmt(PtNode):
    __slots__ = ('names', 'ASSIGN', 'assign_expr', 'S_COLON')

    name: str = 'assign_stmt'

    def __init__(self, names, assign_expr) -> None:
        self.names = names
        self.assign_expr = assign_expr
        self.ASSIGN = fw.assign

        self.S_COLON = fw.s_colon


class Names(PtNode):
    __slots__ = ('names', 'COMMA', 'mono_name')

    name: str = 'names'

    def __init__(self, names=None, mono_name=None) -> None:
        if names is not None:
            self.names = names
            self.COMMA = fw.comma
        else:
            self.names = None
            self.COMMA = None

        self.mono_name = mono_name

        if mono_name is None:
            raise ValueError('name must not be None')


class Name(PtNode):
    __slots__ = ('id',)

    name: str = 'name'

    def __init__(self, id: str) -> None:
        self.id = IDNode(id)


class AssignExpr(PtNode):
    __slots__ = ('names', 'ASSIGN', 'assign_expr')

    name: str = 'assign_expr'

    def __init__(self, names=None, assign_expr=None) -> None:
        if assign_expr is not None:
            self.names = names
            self.ASSIGN = fw.assign
        else:
            self.names = names
            self.ASSIGN = None

        self.assign_expr = assign_expr


if __name__ == '__main__':
    p = Program(Program(Program(None)))
    p.parse_tree_print()

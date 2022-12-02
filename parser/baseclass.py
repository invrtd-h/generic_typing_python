from utils import override


class AstNode:
    __slots__ = ()

    name: str = 'None'

    def parse_tree_print(self, indent: int = 0, logger=None) -> None:
        if logger is None:
            print('=' * indent, end=' ')
            print('=' * indent, end=' ')
            print(self.name)
        else:
            logger.log('=' * indent + ' ' + self.name)
        for slot in self.__slots__:
            val: AstNode = getattr(self, slot)
            if val is not None:
                val.parse_tree_print(indent + 2, logger)

    def null_init(self) -> None:
        """
        Initialize all slots to None.
        """
        for slot in self.__slots__:
            setattr(self, slot, None)


class TermNode(AstNode):
    __slots__ = ('terminal_name',)

    def __init__(self, name: str) -> None:
        self.terminal_name: str = name

    @override
    def parse_tree_print(self, indent: int = 0, logger=None) -> None:
        if logger is None:
            print('-' * indent, end=' ')
            print(self.terminal_name)
        else:
            logger.log('-' * indent + ' ' + self.terminal_name)


class IDNode(AstNode):
    __slots__ = ('id',)

    def __init__(self, id: str):
        self.id = id

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
    trait = TermNode('trait')
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

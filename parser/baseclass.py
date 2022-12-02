from utils import override


class AstNode:
    __slots__ = ()

    name: str = 'None'

    def ast_print(self, indent: int = 0) -> None:
        print('-' * indent, end='')
        print(self.name)
        for slot in self.__slots__:
            val: AstNode = getattr(self, slot)
            if val is not None:
                val.ast_print(indent + 2)

    def null_init(self) -> None:
        """
        Initialize all slots to None.
        :return:
        """
        for slot in self.__slots__:
            setattr(self, slot, None)


class TermNode(AstNode):
    __slots__ = ('terminal_name',)

    def __init__(self, name: str) -> None:
        self.terminal_name: str = name

    @override
    def ast_print(self, indent: int = 0) -> None:
        print('-' * indent, end='')
        print(self.terminal_name)


class IDNode(AstNode):
    __slots__ = ('id',)

    def __init__(self, id: str):
        self.id = id

    @override
    def ast_print(self, indent: int = 0) -> None:
        print('-' * indent, end='')
        print("ID :", self.id)


class Flyweights:
    """
    This is a namespace for storing flyweight objects.
    """
    program_begin = TermNode('PROGRAM_BEGIN')
    program_end = TermNode('PROGRAM_END')

    or_ = TermNode('or')
    and_ = TermNode('and')
    not_ = TermNode('not')
    xor = TermNode('xor')
    none = TermNode('None')
    pass_ = TermNode('pass')
    true = TermNode('True')
    false = TermNode('False')
    trait = TermNode('trait')
    extends = TermNode('extends')
    implies = TermNode('implies')
    generate = TermNode('generate')
    trait_of = TermNode('trait_of')
    printinfo = TermNode('printinfo')

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
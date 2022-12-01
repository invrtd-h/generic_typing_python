class AstNode:
    __slots__ = ()

    name: str = None

    def ast_print(self, indent: int = 0) -> None:
        print('-' * indent, end='')
        print(self.name)
        for slot in self.__slots__:
            val: AstNode = getattr(self, slot)
            if val is not None:
                val.ast_print(indent + 2)


class Program(AstNode):
    __slots__ = ('program_begin', 's_colon', 'stmts', 's_colon2', 'program_end', 's_colon3')

    name: str = 'Program'

    def __init__(self, program_begin, s_colon, stmts, s_colon2, program_end, s_colon3):
        self.program_begin = program_begin
        self.s_colon = s_colon
        self.stmts = stmts
        self.s_colon2 = s_colon2
        self.program_end = program_end
        self.s_colon3 = s_colon3


if __name__ == '__main__':
    pass

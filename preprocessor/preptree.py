from typing import Optional
from typing import Union


class NullToken:
    __slots__ = ()

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return ''

    def __bool__(self) -> bool:
        return False


null_token = NullToken()


class SToken:
    __slots__ = ('tot', 'newlines')

    def __init__(self,
                 tot: 'TotToken',
                 newlines: Union['NewlinesToken', NullToken]) -> None:
        self.tot: 'TotToken' = tot
        self.newlines: Union['NewlinesToken', NullToken] = newlines


class TotToken:
    __slots__ = ('next', 'newlines', 'line')

    def __init__(self,
                 next: Union['TotToken', NullToken],
                 newlines: Union['NewlinesToken', NullToken],
                 line: Union['LineToken', NullToken]) -> None:
        self.next: Union['TotToken', NullToken] = next
        self.newlines: Union['NewlinesToken', NullToken] = newlines
        self.line: Union['LineToken', NullToken] = line


class NewlinesToken:
    __slots__ = 'x'

    def __init__(self):
        self.x: int = 1

    def __add__(self, other: 'NewlinesToken') -> 'NewlinesToken':
        self.x += other.x
        return self


class LineToken:
    __slots__ = ('indent', 'contents')

    def __init__(self,
                 indent: Union['IndentToken', NullToken],
                 contents: 'ContentsToken') -> None:
        self.indent: Union['IndentToken', NullToken] = indent
        self.contents: 'ContentsToken' = contents


class IndentToken:
    __slots__ = ('c', 'next')

    def __init__(self,
                 c: str,
                 next: Union['IndentToken', NullToken]) -> None:
        self.c: str = c
        self.next: Union['IndentToken', NullToken] = next


class ContentsToken:
    __slots__ = ('sentence', 'leading_lpar')

    def __init__(self,
                 sentence: Union['SentenceToken', NullToken],
                 leading_lpar: Union['LeadingLParToken', NullToken]) -> None:
        self.sentence: Union['SentenceToken', NullToken] = sentence
        self.leading_lpar: Union['LeadingLParToken', NullToken] = leading_lpar


class SentenceToken:
    __slots__ = ('strs', 'indent', 'sentence')

    def __init__(self,
                 strs: str,
                 indent: Union['IndentToken', NullToken],
                 sentence: Union['SentenceToken', NullToken]) -> None:
        self.strs: str = strs
        self.indent: Union['IndentToken', NullToken] = indent
        self.sentence: Union['SentenceToken', NullToken] = sentence


class LeadingLParToken:
    __slots__ = ('par_type', 'holes', 'lpright')

    def __init__(self,
                 lpar: int,
                 holes: Union['HolesToken', NullToken],
                 lpright: 'LpRightToken') -> None:
        self.par_type: int = lpar
        self.holes: Union['HolesToken', NullToken] = holes
        self.lpright: 'LpRightToken' = lpright


class LpRightToken:
    __slots__ = ('par_type', 'contents2', 'leading_rpar')

    def __init__(self,
                 par_type: int,
                 contents2: Union['Contents2Token', NullToken],
                 leading_rpar: 'LeadingRParToken') -> None:
        self.par_type: int = par_type
        self.contents2: Union['Contents2Token', NullToken] = contents2
        self.leading_rpar: 'LeadingRParToken' = leading_rpar


class Contents2Token:
    __slots__ = ('sentence2', 'lli')

    def __init__(self,
                 sentence2: Union['Sentence2Token', NullToken],
                 lli: Union['LeadingLParInnerToken', NullToken]) -> None:
        self.sentence2: Union['Sentence2Token', NullToken] = sentence2
        self.lli: Union['LeadingLParInnerToken', NullToken] = lli


class Sentence2Token:
    __slots__ = ('strs', 'holes', 'sentence2')

    def __init__(self,
                 strs: str,
                 holes: Union['HolesToken', NullToken],
                 sentence2: Union['Sentence2Token', NullToken]) -> None:
        self.strs: str = strs
        self.holes: Union['HolesToken', NullToken] = holes
        self.sentence2: Union['HolesToken', NullToken] = sentence2


class HolesToken:
    __slots__ = ('next', 'hole')

    def __init__(self,
                 next: Union['HolesToken', NullToken],
                 hole: str) -> None:
        self.next: Union['HolesToken', NullToken] = next
        self.hole: str = hole


class LeadingLParInnerToken:
    __slots__ = ('par_type', 'holes', 'lpright_inner')

    def __init__(self,
                 par_type: int,
                 holes: Union['HolesToken', NullToken],
                 lpright_inner: 'LpRightInnerToken') -> None:
        self.par_type: int = par_type
        self.holes: Union['HolesToken', NullToken] = holes
        self.lpright_inner: 'LpRightInnerToken' = lpright_inner


class LpRightInnerToken:
    __slots__ = ('par_type', 'contents2', 'lri')

    def __init__(self,
                 par_type: int,
                 contents2: Union['Contents2Token', NullToken],
                 lri: 'LeadingRParInnerToken') -> None:
        self.par_type: int = par_type
        self.contents2: Union['Contents2Token', NullToken] = contents2
        self.lri: 'LeadingRParInnerToken' = lri


class LeadingRParToken:
    __slots__ = ('par_type', 'rpr', 'contents')

    def __init__(self,
                 par_type: int,
                 rpr: 'RPRToken',
                 contents: Union[ContentsToken, NullToken]) -> None:
        self.par_type: int = par_type
        self.rpr: 'RPRToken' = rpr
        self.contents: Union[ContentsToken, NullToken] = contents


class RPRToken:
    __slots__ = ('par_type', 'indent')

    def __init__(self,
                 par_type: int,
                 indent: Union[IndentToken, NullToken]) -> None:
        self.par_type: int = par_type
        self.indent: Union[IndentToken, NullToken] = indent


class LeadingRParInnerToken:
    __slots__ = ('par_type', 'rprr', 'contents2')

    def __init__(self,
                 par_type: int,
                 rprr: 'RPRRToken',
                 contents2: Union[Contents2Token, NullToken]) -> None:
        self.par_type: int = par_type
        self.rprr: 'RPRRToken' = rprr
        self.contents2: Union[Contents2Token, NullToken] = contents2


class RPRRToken:
    __slots__ = ('par_type', 'holes')

    def __init__(self,
                 par_type: int,
                 holes: Union[HolesToken, NullToken]) -> None:
        self.par_type: int = par_type
        self.holes: Union[HolesToken, NullToken] = holes
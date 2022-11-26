from typing import Optional
from typing import Union


class LineToken:
    __slots__ = ("indent", "bparens", "newline")

    def __init__(self, indent, bparens: Optional["BParensToken"], newline: bool):
        self.indent = indent
        self.bparens = bparens
        self.newline: bool = newline


class IndentToken:
    __slots__ = ("next", "white")

    def __init__(self, next: Optional["IndentToken"], white: "WhiteToken"):
        self.next: Optional["IndentToken"] = next
        self.white: "WhiteToken" = white


class WhiteToken:
    __slots__ = "is_tab"

    tab_indent: int = 4

    def __init__(self, is_tab: bool):
        self.is_tab: bool = is_tab


class BParensToken:
    __slots__ = ("bparens", "sentence", "bparens2")

    def __init__(self,
                 bparens: Optional["BParensToken"],
                 sentence: Optional["SentenceToken"],
                 bparens2: Optional["BParens2Token"]):
        self.bparens: Optional["BParensToken"] = bparens
        self.sentence: Optional["SentenceToken"] = sentence
        self.bparens2: Optional["BParens2Token"] = bparens2


class SentenceToken:
    __slots__ = ("next", "indent_or_str")

    def __init__(self, next: Optional["SentenceToken"], indent_or_str: "IndentOrStrToken"):
        self.next: Optional["SentenceToken"] = next
        self.indent_or_str = indent_or_str


class IndentOrStrToken:
    __slots__ = "data"

    def __init__(self, data: Union["IndentToken", str]):
        self.data = data


class BParens2Token:
    __slots__ = ("bparens3", "outerparen")

    def __init__(self, bparens3, outerparen: int):
        self.bparens3 = bparens3
        self.outerparen: int = outerparen

        # {1 : (), 2 : [], 3 : {}}


class BParens3Token:
    __slots__ = ("next", "sentence", "bparens2")

    def __init__(self,
                 next: Optional["BParens3Token"],
                 sentence: Optional[SentenceToken],
                 bparens2: Optional[BParens2Token]):
        self.next: Optional["BParens3Token"] = next
        self.sentence: Optional[SentenceToken] = sentence
        self.bparens2: Optional[BParens2Token] = bparens2


class Sentence2Token:
    __slots__ = ("next", "indent_or_str", "newline")

    def __init__(self,
                 next: Optional["Sentence2Token"],
                 indent_or_str: Optional[IndentOrStrToken],
                 newline: bool):
        self.next: Optional["Sentence2Token"] = next
        self.indent_or_str: Optional[IndentOrStrToken] = indent_or_str
        self.newline: bool = newline
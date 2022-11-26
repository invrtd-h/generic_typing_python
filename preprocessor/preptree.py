from typing import Optional
from typing import Union


class LineToken:
    __slots__ = ("indent", "vparens", "newline")

    def __init__(self, indent, vparens: Optional["VParensToken"], newline: bool):
        self.indent = indent
        self.vparens = vparens
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


class VParensToken:
    __slots__ = ("vparens", "sentence", "vparens2")

    def __init__(self,
                 vparens: Optional["VParensToken"],
                 sentence: Optional["SentenceToken"],
                 vparens2: Optional["VParens2Token"]):
        self.vparens: Optional["VParensToken"] = vparens
        self.sentence: Optional["SentenceToken"] = sentence
        self.vparens2: Optional["VParens2Token"] = vparens2


class SentenceToken:
    __slots__ = ("next", "indent_or_str")

    def __init__(self, next: Optional["SentenceToken"], indent_or_str: "IndentOrStrToken"):
        self.next: Optional["SentenceToken"] = next
        self.indent_or_str = indent_or_str


class IndentOrStrToken:
    __slots__ = "data"

    def __init__(self, data: Union["IndentToken", str]):
        self.data = data


class VParens2Token:
    __slots__ = ("vparens3", "outerparen")

    def __init__(self, vparens3, outerparen: str):
        self.vparens3 = vparens3
        self.outerparen: str = outerparen


class VParens3Token:
    __slots__ = ("next", "sentence", "vparens2")

    def __init__(self,
                 next: Optional["VParens3Token"],
                 sentence: Optional[SentenceToken],
                 vparens2: Optional[VParens2Token]):
        self.next: Optional["VParens3Token"] = next
        self.sentence: Optional[SentenceToken] = sentence
        self.vparens2: Optional[VParens2Token] = vparens2


class Sentence2Token:
    __slots__ = ("next", "indent_or_str", "newline")

    def __init__(self,
                 next: Optional["Sentence2Token"],
                 indent_or_str: Optional[IndentOrStrToken],
                 newline: bool):
        self.next: Optional["Sentence2Token"] = next
        self.indent_or_str: Optional[IndentOrStrToken] = indent_or_str
        self.newline: bool = newline
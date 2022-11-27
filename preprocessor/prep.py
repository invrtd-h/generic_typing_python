from typing import Optional
from functools import reduce


class ProgramLine:
    __slots__ = ("data", "initial_indents", "indent_policy")

    def __init__(self, raw_line: str) -> None:
        i: int = 0
        while i < len(raw_line) and (raw_line[i] == " " or raw_line[i] == '\t'):
            i += 1

        if raw_line[:i].count(' ') != i and raw_line[:i].count('\t') != i:
            raise ValueError("Indentation must be either all spaces or all tabs")

        self.initial_indents: int = i
        self.data: str = raw_line[i:]

        self.indent_policy: Optional[str] = None
        if not raw_line:
            pass
        elif raw_line[0] == ' ':
            self.indent_policy = ' '
        elif raw_line[0] == '\t':
            self.indent_policy = '\t'

    def __bool__(self) -> bool:
        return bool(self.data)


class Program:
    __slots__ = ("lines", "indent_type")

    def __init__(self, raw_program: str) -> None:
        splitted_data: list[str] = Program._nlparse(raw_program)
        self.lines: list[ProgramLine] = [ProgramLine(line) for line in splitted_data]

        # determine indent type of program
        self.indent_type: Optional[str] = None

        for p_line in self.lines:
            if p_line.indent_policy is not None:
                if self.indent_type is None:
                    self.indent_type = p_line.indent_policy
                elif self.indent_type != p_line.indent_policy:
                    raise ValueError("Indentation must be either all spaces or all tabs")

        self._add_semicolon()
        self._add_parentheses()

    def __repr__(self) -> str:
        """Returns the program as a string"""
        temp = map(self.line_to_str, self.lines)
        return reduce(lambda x, y: x + "\n" + y, temp)

    def line_to_str(self, line: ProgramLine) -> str:
        """Returns a ProgramLine as a string"""
        if self.indent_type is None:
            return line.data
        return self.indent_type * line.initial_indents + line.data

    @staticmethod
    def _nlparse(s: str) -> list[str]:
        ret = ["PROGRAM BEGIN", ""]
        stack = []

        for c in s:
            if not stack and c == '\n':
                ret.append("")
            if c != '\n':
                ret[-1] += c

            if stack:
                if stack[-1] == '"' and c != '"':
                    continue
                if stack[-1] == "'" and c != "'":
                    continue

            if c in {'(', '[', '{'}:
                stack.append(c)
            elif c in {'"', "'"} and (not stack or stack[-1] not in {'"', "'"}):
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    raise Exception('Unbalanced parentheses')
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    raise Exception('Unbalanced parentheses')
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    raise Exception('Unbalanced parentheses')
            elif c == '"':
                if stack and stack[-1] == '"':
                    stack.pop()
                else:
                    raise Exception('Unbalanced parentheses')
            elif c == '\'':
                if stack and stack[-1] == '\'':
                    stack.pop()
                else:
                    raise Exception('Unbalanced parentheses')

        ret.append("PROGRAM END")
        return ret

    def _add_semicolon(self) -> None:
        for line in self.lines:
            if line and line.data[-1] not in ';:':
                line.data += ';'
        return None

    def _add_parentheses(self) -> None:
        stack: list[ProgramLine] = []

        for line in self.lines:
            if not line:
                continue

            while stack and line.initial_indents <= stack[-1].initial_indents:
                line.data = '}' + line.data
                stack.pop()

            if line.data[-1] == ';':
                continue
            if line.data[-1] == ':':
                if stack and line.initial_indents < stack[-1].initial_indents:
                    raise ValueError("Unexpected Indentation")
                line.data += '{'
                stack.append(line)


if __name__ == '__main__':
    f = open("../input.txt", 'r')
    s = f.read()
    f.close()

    result = Program(s)
    print(result)
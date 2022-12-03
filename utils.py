from typing import Sequence


def no_effect_decorator(func):
    return func


override = no_effect_decorator
noexcept = no_effect_decorator


class Implicit_type_conversion:
    __slots__ = ('func', 'types')

    def __init__(self, func, *types):
        self.func = func
        self.types = types

    def __call__(self, *args, **kwargs):
        lis = []
        for i in range(len(args)):
            lis.append(self.types[i](args[i]))
        return self.func(*lis, **kwargs)


def implicit_type_conversion(*types):
    def decorator(func):
        return Implicit_type_conversion(func, *types)
    return decorator


def idtt(x):
    return x


class Logger:
    __slots__ = ('_log',)

    _end_char: str = '\n'

    def __init__(self):
        self._log: str = ""

    def get_log(self) -> str:
        return self._log

    def pop_log(self) -> str:
        log = self._log
        self._log = ""
        return log

    def write_on_file(self, *, filename: str) -> None:
        f = open(filename, 'w')
        f.write(self._log)
        f.close()

    @classmethod
    def set_end_char(cls, end_char: str) -> None:
        cls._end_char = end_char

    def log(self, msg: str) -> None:
        self._log += msg + self._end_char


logger = Logger()


def merge(arr1: Sequence, arr2: Sequence) -> list:
    """
    Merge two sorted sequences into a sorted sequence.
    """
    p1, p2 = 0, 0
    ret = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            ret.append(arr1[p1])
            p1 += 1
        else:
            ret.append(arr2[p2])
            p2 += 1
    if p1 < len(arr1):
        ret.extend(arr1[p1:])
    if p2 < len(arr2):
        ret.extend(arr2[p2:])
    return ret


def is_duplicated(sorted_: Sequence) -> bool:
    """
    Check if there are duplicated elements in a sorted sequence.
    :param sorted_: a sorted sequence
    :return: True if there is a duplicated element, False otherwise
    """
    for i in range(len(sorted_) - 1):
        if sorted_[i] == sorted_[i + 1]:
            return True
    return False


class DuplicatedError(Exception):
    pass


class FnConflictError(Exception):
    pass


class VarConflictError(Exception):
    pass


class GPErrors:
    __slots__ = ()

    @staticmethod
    def duplicated_error(msg: str) -> DuplicatedError:
        return DuplicatedError(msg)

    @staticmethod
    def fn_conflict_error(msg: str) -> FnConflictError:
        return FnConflictError(msg)

    @staticmethod
    def var_conflict_error(msg: str) -> VarConflictError:
        return VarConflictError(msg)


errs = GPErrors()


@implicit_type_conversion(int, int)
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add('1', '2'))

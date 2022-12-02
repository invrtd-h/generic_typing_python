def no_effect_decorator(func):
    return func


override = no_effect_decorator


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

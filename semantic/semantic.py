from enum import Enum
from typing import Optional as opt
from utils import merge, is_duplicated, errs


class FnPolicy(Enum):
    fn = 0
    cls_fn = 1
    static_fn = 2


class VarPolicy(Enum):
    var = 0
    cls_var = 1


class ArgPolicy(Enum):
    anonymous_necessary = 0
    anonymous_optional = 1
    named_necessary = 2
    named_optional = 3


# aliases
ap = ArgPolicy
vp = VarPolicy
fp = FnPolicy


class FnInfo:
    __slots__ = ('name', 'ano_nec', 'ano_opt', 'named_nec', 'named_opt', 'ret', 'policy')

    def __init__(self,
                 name: str,
                 ano_nec: tuple['Trait'],
                 ano_opt: tuple['Trait'],
                 named_nec: tuple[tuple[str, 'Trait']],
                 named_opt: tuple[tuple[str, 'Trait']],
                 ret: 'Trait',
                 policy: FnPolicy) -> None:
        """
        :param name: the name of the function
        :param ano_nec: the anonymous necessary arguments of the function
        :param ano_opt: the anonymous optional arguments of the function
        :param named_nec: the named necessary arguments of the function
        :param named_opt: the named optional arguments of the function
        :param ret: the trait of the return value of the function
        :param policy: determine whether it is a method, a class method or a static method
        """
        self.name = name
        self.ano_nec = ano_nec
        self.ano_opt = ano_opt
        self.named_nec: tuple[tuple[str, 'Trait']] = tuple(sorted(named_nec, key=lambda x: x[0]))
        self.named_opt: tuple[tuple[str, 'Trait']] = tuple(sorted(named_opt, key=lambda x: x[0]))
        self.ret = ret
        self.policy = policy

        merged = merge([x[0] for x in self.named_nec], [x[0] for x in self.named_opt])

        if is_duplicated(merged):
            raise errs.duplicated_error('Duplicated name was found in the named arguments of the function')


class VarInfo:
    __slots__ = ('name', 'trait', 'policy')

    def __init__(self, name: str, trait, policy: VarPolicy):
        self.name: str = name
        self.trait = trait
        self.policy: VarPolicy = policy


class Trait:
    __slots__ = ('fns_dict', 'vars_dict')

    def __init__(self, fns: list[FnInfo], vars: list[VarInfo]):
        fns_dict: dict[str, FnInfo] = {x.name: x for x in fns}
        vars_dict: dict[str, VarInfo] = {x.name: x for x in vars}


if __name__ == '__main__':
    pass
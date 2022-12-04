from enum import Enum
from typing import Union
from typing import Optional as opt
from utils import merge, is_duplicated, errs, noexcept


class FnPolicy(Enum):
    fn = 0
    cls_fn = 1
    static_fn = 2


class VarPolicy(Enum):
    var = 0
    cls_var = 1


# aliases
vp = VarPolicy
fp = FnPolicy

var_id = str
trait_id = str


class FnInfo:
    __slots__ = ('name', 'ano_nec', 'ano_opt', 'named_nec', 'named_opt', 'ret', 'policy')

    def __init__(self,
                 name: str,
                 ano_nec: tuple[trait_id],
                 ano_opt: tuple[trait_id],
                 named_nec: tuple[tuple[var_id, trait_id]],
                 named_opt: tuple[tuple[var_id, trait_id]],
                 ret: trait_id,
                 policy: FnPolicy) -> None:
        """
        :param name: the name of the function
        :param ano_nec: the anonymous necessary arguments of the function
        :param ano_opt: the anonymous optional arguments of the function
        :param named_nec: the named necessary arguments of the function
        :param named_opt: the named optional arguments of the function
        :param ret: the trait_id of the return value of the function
        :param policy: determine whether it is a method, a class method or a static method
        """
        self.name = name
        self.ano_nec = ano_nec
        self.ano_opt = ano_opt
        self.named_nec: tuple[tuple[str, str]] = tuple(sorted(named_nec, key=lambda x: x[0]))
        self.named_opt: tuple[tuple[str, str]] = tuple(sorted(named_opt, key=lambda x: x[0]))
        self.ret = ret
        self.policy = policy

        merged = merge([x[0] for x in self.named_nec], [x[0] for x in self.named_opt])

        if is_duplicated(merged):
            raise errs.duplicated_error('Duplicated name was found in the named arguments of the function')

    @classmethod
    def conflicts(cls, a: 'FnInfo', b: 'FnInfo'):
        if isinstance(a, cls) and isinstance(b, cls):
            raise TypeError('The two arguments must be FnInfo')
        if a.name != b.name:
            return False
        if a.policy != b.policy:
            return True
        if a.ano_nec != b.ano_nec or a.ano_opt != b.ano_opt or a.named_nec != b.named_nec or b.named_opt != b.named_opt:
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, FnInfo):
            return False
        return self.name == other.name and self.ano_nec == other.ano_nec and self.ano_opt == other.ano_opt and \
               self.named_nec == other.named_nec and self.named_opt == other.named_opt and self.ret == other.ret and \
               self.policy == other.policy

    def __repr__(self):
        ret: str = "fn: "
        if self.policy == fp.fn:
            ret += 'member_fn, '
        elif self.policy == fp.cls_fn:
            ret += 'class_fn, '
        elif self.policy == fp.static_fn:
            ret += 'static_fn, '

        ret += 'name = ' + self.name + ', '

        for ids in self.ano_nec:
            ret += ids
            ret += ', '
        for ids in self.ano_opt:
            ret += '='
            ret += ids
            ret += ', '
        for name, ids in self.named_nec:
            ret += name + ': ' + ids + ', '
        for name, ids in self.named_opt:
            ret += name + ':= ' + ids + ', '

        return ret[:-2]


class VarInfo:
    __slots__ = ('name', 'trait_id', 'policy')

    def __init__(self, name: str, trait_id_: trait_id, policy: VarPolicy):
        self.name: str = name
        self.trait_id: trait_id = trait_id_
        self.policy: VarPolicy = policy

    @classmethod
    def conflicts(cls, a: 'VarInfo', b: 'VarInfo') -> bool:
        if not isinstance(a, cls) or not isinstance(b, cls):
            raise TypeError('The two arguments must be VarInfo')
        return a.name == b.name and (a.policy != b.policy or a.trait_id != b.trait_id)

    def __eq__(self, other: 'VarInfo') -> bool:
        if not isinstance(other, VarInfo):
            return False
        return self.name == other.name and self.trait_id == other.trait_id and self.policy == other.policy

    def __repr__(self) -> str:
        ret = 'var: '
        if self.policy == vp.var:
            ret += 'member variable, '
        else:
            ret += 'class variable, '
        ret += 'name = ' + self.name + ', trait = ' + self.trait_id

        return ret


class TraitInfo:
    __slots__ = ('fns_dict', 'vars_dict', 'maybe_fns_dict', 'maybe_vars_dict')

    def __init__(self, fns: list[FnInfo] = [], vars: list[VarInfo] = []):

        # the dictionary for holding the functions that the trait must have
        fns_dict: dict[str, FnInfo] = {x.name: x for x in fns}

        # the dictionary for holding the variables that the trait must have
        vars_dict: dict[str, VarInfo] = {x.name: x for x in vars}

        # the dictionary for holding the functions that the trait may have
        maybe_fns_dict: dict[str, FnInfo] = {}

        # the dictionary for holding the variables that the trait may have
        maybe_vars_dict: dict[str, VarInfo] = {}

    def __eq__(self, other: 'TraitInfo') -> bool:
        if not isinstance(other, TraitInfo):
            return False
        return self.fns_dict == other.fns_dict and self.vars_dict == other.vars_dict and \
               self.maybe_fns_dict == other.maybe_fns_dict and self.maybe_vars_dict == other.maybe_vars_dict

    def __le__(self, other: 'TraitInfo') -> bool:
        if not isinstance(other, TraitInfo):
            raise TypeError('The RHS must be a trait')
        for fn in self.fns_dict.values():
            if fn.name not in other.fns_dict:
                return False
            if FnInfo.conflicts(fn, other.fns_dict[fn.name]):
                return False
        for var in self.vars_dict.values():
            if var.name not in other.vars_dict:
                return False
            if VarInfo.conflicts(var, other.vars_dict[var.name]):
                return False
        for fn in self.maybe_fns_dict.values():
            if fn.name not in other.fns_dict:
                return False
            if FnInfo.conflicts(fn, other.fns_dict[fn.name]):
                return False
            if fn.name not in other.maybe_fns_dict:
                return False
            if FnInfo.conflicts(fn, other.maybe_fns_dict[fn.name]):
                return False
        for var in self.maybe_vars_dict.values():
            if var.name not in other.vars_dict:
                return False
            if VarInfo.conflicts(var, other.vars_dict[var.name]):
                return False
            if var.name not in other.maybe_vars_dict:
                return False
            if VarInfo.conflicts(var, other.maybe_vars_dict[var.name]):
                return False
        return True

    def __ge__(self, other: 'TraitInfo') -> bool:
        if not isinstance(other, TraitInfo):
            raise TypeError('The RHS must be a trait')
        return other.__le__(self)

    def __lt__(self, other: 'TraitInfo') -> bool:
        return self.__le__(other) and self != other

    def __gt__(self, other: 'TraitInfo') -> bool:
        return self.__ge__(other) and self != other

    def __or__(self, other: 'TraitInfo') -> 'TraitInfo':
        if not isinstance(other, TraitInfo):
            raise TypeError('The RHS must be a trait')
        if TraitInfo.conflicts(self, other):
            raise errs.conflict_error('The two traits conflict with each other')
        
        ret = TraitInfo()

        for fn in self.fns_dict:
            check = other.contains(fn)
            if check == 'always':
                ret.add_fn(fn, rule='always')
            else:
                ret.add_fn(fn, rule='maybe')
        for var in self.vars_dict:
            check = other.contains(var)
            if check == 'always':
                ret.add_var(var, rule='always')
            else:
                ret.add_var(var, rule='maybe')
        for fn in self.maybe_fns_dict:
            ret.add_fn(fn, rule='maybe')
        for var in self.maybe_vars_dict:
            ret.add_var(var, rule='maybe')

        for fn in other.fns_dict:
            check = self.contains(fn)
            if check == 'no':
                ret.add_fn(fn, rule='maybe')
        for var in other.vars_dict:
            check = self.contains(var)
            if check == 'no':
                ret.add_var(var, rule='maybe')
        for fn in other.maybe_fns_dict:
            check = self.contains(fn)
            if check == 'no':
                ret.add_fn(fn, rule='maybe')
        for var in other.maybe_vars_dict:
            check = self.contains(var)
            if check == 'no':
                ret.add_var(var, rule='maybe')
        
        return ret

    def negate(self) -> 'TraitInfo':
        return TraitInfo()

    def __and__(self, other: 'TraitInfo') -> 'TraitInfo':
        if not isinstance(other, TraitInfo):
            raise TypeError('The two arguments must be TraitInfo')
        if TraitInfo.conflicts(self, other):
            raise errs.conflict_error('The two traits conflict with each other')
        
        ret = TraitInfo()
        
        for fn in self.fns_dict:
            ret.add_fn(fn, rule='always')
        for var in self.vars_dict:
            ret.add_var(var, rule='always')
        for fn in self.maybe_fns_dict:
            check = other.contains(fn)
            if check == 'always':
                ret.add_fn(fn, rule='always')
            else:
                ret.add_fn(fn, rule='maybe')
        for var in self.maybe_vars_dict:
            check = other.contains(var)
            if check == 'always':
                ret.add_var(var, rule='always')
            else:
                ret.add_var(var, rule='maybe')

        for fn in other.fns_dict:
            check = self.contains(fn)
            if check == 'no':
                ret.add_fn(fn, rule='always')
        for var in other.vars_dict:
            check = self.contains(var)
            if check == 'no':
                ret.add_var(var, rule='always')
        for fn in other.maybe_fns_dict:
            check = self.contains(fn)
            if check == 'no':
                ret.add_fn(fn, rule='maybe')
        for var in other.maybe_vars_dict:
            check = self.contains(var)
            if check == 'no':
                ret.add_var(var, rule='maybe')

        return ret

    def add_fn(self, fn: FnInfo, *, rule: str):
        """Note that this function does NOT check whether the conflict exists.
        It is the caller's responsibility to check"""
        if rule == 'always':
            self.fns_dict[fn.name] = fn
        elif rule == 'maybe':
            self.maybe_fns_dict[fn.name] = fn
        else:
            msg = f'Conflicting function {fn.name} was found'
            raise errs.fn_conflict_error(msg)
        return

    def add_var(self, var: VarInfo, *, rule: str):
        """Note that this function does NOT check whether the conflict exists.
        It is the caller's responsibility to check"""
        if rule == 'always':
            self.fns_dict[var.name] = var
        elif rule == 'maybe':
            self.maybe_fns_dict[var.name] = var
        else:
            msg = f'Conflicting variable {var.name} was found'
            raise errs.var_conflict_error(msg)
        return

    def safely_add_fn(self, fn: FnInfo, *, rule: str) -> None:
        if not self.trait_fn_conflicts(fn):
            self.add_fn(fn, rule=rule)
        else:
            msg = f'Conflicting variable {fn.name} was found'
            raise errs.fn_conflict_error(msg)
        return

    def safely_add_var(self, var: VarInfo, *, rule: str) -> None:
        if not self.trait_var_conflicts(var):
            self.add_var(var, rule=rule)
        else:
            msg = f'Conflicting variable {var.name} was found'
            raise errs.var_conflict_error(msg)
        return

    @noexcept
    def contains(self, item: Union[FnInfo, VarInfo]) -> str:
        if isinstance(item, FnInfo):
            if item.name in self.fns_dict:
                if item == self.fns_dict[item.name]:
                    return 'always'
                return 'conflict'
            if item.name in self.maybe_fns_dict:
                if item == self.maybe_fns_dict[item.name]:
                    return 'maybe'
                return 'conflict'
            return 'no'
        elif isinstance(item, VarInfo):
            if item.name in self.vars_dict:
                if item == self.vars_dict[item.name]:
                    return 'always'
                return 'conflict'
            if item.name in self.maybe_vars_dict:
                if item == self.maybe_vars_dict[item.name]:
                    return 'maybe'
                return 'conflict'
            return 'no'
        else:
            raise TypeError('The argument must be either FnInfo or VarInfo')

    @classmethod
    def conflicts(cls, a: 'TraitInfo', b: 'TraitInfo') -> bool:
        if not isinstance(a, cls) or not isinstance(b, cls):
            raise TypeError('The two arguments must be TraitInfo')
        for fn in a.fns_dict.values():
            if fn.name in b.fns_dict and FnInfo.conflicts(fn, b.fns_dict[fn.name]):
                return True
        for var in a.vars_dict.values():
            if var.name in b.vars_dict and VarInfo.conflicts(var, b.vars_dict[var.name]):
                return True
        return False

    @noexcept
    def trait_fn_conflicts(self, fn: FnInfo) -> bool:
        if fn.name in self.fns_dict:
            if FnInfo.conflicts(fn, self.fns_dict[fn.name]):
                return True
        if fn.name in self.maybe_fns_dict:
            if FnInfo.conflicts(fn, self.maybe_fns_dict[fn.name]):
                return True
        return False

    @noexcept
    def trait_var_conflicts(self, var: VarInfo) -> bool:
        if var.name in self.vars_dict:
            if VarInfo.conflicts(var, self.vars_dict[var.name]):
                return True
        if var.name in self.maybe_vars_dict:
            if VarInfo.conflicts(var, self.maybe_vars_dict[var.name]):
                return True
        return False

    def __repr__(self) -> str:
        ret = 'The trait must have these functions : \n'
        for x, fn in self.fns_dict:
            ret += str(fn) + '\n'
        ret += 'The trait may have these functions : \n'
        for x, fn in self.maybe_fns_dict:
            ret += str(fn) + '\n'
        ret += 'The trait must have these variables : \n'
        for x, var in self.vars_dict:
            ret += str(var) + '\n'
        for x, var in self.maybe_vars_dict:
            ret += str(var) + '\n'

        return ret


if __name__ == '__main__':
    pass

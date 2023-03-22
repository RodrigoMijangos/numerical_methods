import math

from sympy.core import Function
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr as parser, T


def truncate(number: float, digits: int) -> float:
    return round(number, digits)


def parse_expression(expression: str) -> Function:
    return parser(expression, transformations=T[:])


def eval_expression(expression: Function, value: float) -> float:
    return expression.evalf(subs={x: value})


def assign_values(polarity: tuple[bool, bool], values: tuple[float, float],
                  replace: float, evaluation: float) -> tuple[float, float]:
    positive_a = polarity[0]
    a, b = values
    positive_c = is_positive(evaluation)

    if positive_c:
        if positive_a:
            return replace, b
        else:
            return a, replace
    else:
        if positive_a:
            return a, replace

    return replace, b


def is_positive(value: float) -> bool:
    return value > 0


def root_founded(evaluation: float) -> bool:
    return evaluation == 0


def check_truncate_values(a: float, b: float, decimals) -> bool:
    return round(a, decimals) == round(b, decimals)

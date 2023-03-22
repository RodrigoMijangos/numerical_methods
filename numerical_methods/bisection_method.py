from utility.util import *
from numerical_methods.responses.responses import BisectionResponse

from sympy.core import Function


def bisection(parameters: tuple[float, float], function: Function,
              index: int = None, error: float | int = None, decimals: int = None,
              show_decimals: int = None) -> list[BisectionResponse]:
    if index is None:
        index = 50
    if error is None:
        error = 0.001
    if decimals is None:
        decimals = 4
    if show_decimals is None:
        show_decimals = 4

    a, b = parameters

    a_evaluated, b_evaluated = eval_expression(function, a), eval_expression(function, b)

    polarity = is_positive(a_evaluated), is_positive(b_evaluated)

    return generate_i(polarity, function, parameters, index, error, decimals, show_decimals)


def generate_i(polarity: tuple[bool, bool], function: Function, parameters: tuple[float, float],
               index: int, error: float | int, accuracy_decimals: int, show_decimals: int,
               results: list[BisectionResponse] = None, last: BisectionResponse = None) -> list[BisectionResponse]:
    if results is None:
        results = list()

    a, b = parameters

    k = results.__len__() + 1

    k_i = generate_range(a, b)

    fk_i = eval_expression(function, k_i)

    parameters = assign_values(polarity, parameters, k_i, fk_i)

    n_row = BisectionResponse(k, a, b, k_i, fk_i)

    if last is not None:
        ep = abs(k_i - last.ik)
        n_row.ep = ep

    simplified = simplify_data(n_row, show_decimals)

    results.append(simplified)

    if n_row.k == index:
        return results
    if n_row.ep is not None:
        if n_row.ep <= error:
            return results
    if check_truncate_values(n_row.ik, n_row.a, accuracy_decimals) \
            or check_truncate_values(n_row.ik, n_row.b, accuracy_decimals):
        return results
    if root_founded(fk_i):
        return results

    return generate_i(polarity, function, parameters, index, error, accuracy_decimals, show_decimals, results, n_row)


def simplify_data(row: BisectionResponse, accuracy: int) -> BisectionResponse:
    a = truncate(row.a, accuracy)
    b = truncate(row.b, accuracy)
    ki = truncate(row.ik, accuracy)
    f_eval = truncate(row.f_eval, accuracy)
    simplified = BisectionResponse(row.k, a, b, ki, f_eval)
    if row.ep is not None:
        ep = truncate(row.ep, accuracy)
        simplified.ep = ep
    return simplified


def generate_range(a: float, b: float) -> float:
    return (a + b) / 2

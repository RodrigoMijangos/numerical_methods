from sympy.core import Function, Float
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr as parser, T
from numerical_methods.responses.newton_rapshon_response import NewtonRaphsonResponse, Response
from numerical_methods.responses.multifunction_response import MultifunctionResponse, BisectionResponse


def truncate(number: float, digits: int) -> float:
    return Float(number, digits)


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
    return Float(a, decimals) == Float(b, decimals)


def simplify_data(row: Response, accuracy: int) -> Response:
    ik = truncate(row.ik, accuracy)
    f_eval = truncate(row.f_eval, accuracy)

    if isinstance(row, BisectionResponse):
        a = truncate(row.a, accuracy)
        b = truncate(row.b, accuracy)
        if isinstance(row, MultifunctionResponse):
            fa_eval = truncate(row.fa_eval, accuracy)
            fb_eval = truncate(row.fb_eval, accuracy)
            simplified = MultifunctionResponse(row.k, a, b, fa_eval, fb_eval, ik, f_eval)
        else:
            simplified = BisectionResponse(row.k, a, b, ik, f_eval)
    else:
        if isinstance(row, NewtonRaphsonResponse):
            df_eval = truncate(row.df_eval, accuracy)
            simplified = NewtonRaphsonResponse(row.k, ik, f_eval, df_eval)
        else:
            simplified = Response(row.k, ik, f_eval)

    if row.ep is not None:
        simplified.ep = truncate(row.ep, accuracy)

    return simplified


def is_done(index: int, accuracy: int, error: int | float, row: Response) -> bool:
    a = row.k == index
    if row.ep is not None:
        d = row.ep <= error
    else:
        d = False
    e = root_founded(row.f_eval)
    if isinstance(row, BisectionResponse):
        b = check_truncate_values(row.a, row.ik, accuracy)
        c = check_truncate_values(row.b, row.ik, accuracy)
        return a or b or c or d or e

    return a or d or e


def to_print(obj: Response) -> str:
    if isinstance(obj, NewtonRaphsonResponse):
        return f"{obj.k} \t {obj.ik} \t {obj.f_eval} \t {obj.df_eval} \t {obj.ep}"
    if isinstance(obj, BisectionResponse):
        return f"{obj.k} \t {obj.a} \t {obj.b} \t {obj.ik} \t {obj.f_eval} \t {obj.ep}"
    if isinstance(obj, MultifunctionResponse):
        return f"{obj.k} \t {obj.a} \t {obj.b} \t {obj.fa_eval} \t {obj.fb_eval} \t {obj.ik} \t {obj.f_eval} \t {obj.ep}"

from utility.util import Response, NewtonRaphsonResponse, Function, x, eval_expression, simplify_data, root_founded, \
    check_truncate_values


def newton_raphson(initial: int | float, function: Function, index: int = None,
                   accuracy_decimals: int = None, show_decimals: int = None, error: int | float = None) -> list[Response]:
    if index is None:
        index = 50
    if accuracy_decimals is None:
        accuracy_decimals = 4
    if show_decimals is None:
        show_decimals = 2
    if error is None:
        error = 0.001

    return generate_i(function, index, accuracy_decimals, show_decimals, error, initial=initial)


def generate_i(function: Function, index: int, accuracy_decimals: int, show_decimals: int, error: int | float,
               initial: float = None, results: list[Response] = None,
               d_function: Function = None, last: NewtonRaphsonResponse = None) -> list[Response]:

    if results is None:
        results = list()

    if d_function is None:
        d_function = function.diff(x)

    if last is None:
        k = 0
        ik = initial
        f_eval = eval_expression(function, ik)
        df_eval = eval_expression(d_function, ik)
        row = NewtonRaphsonResponse(k, ik, f_eval, df_eval)
    else:
        k = last.k + 1
        ik = generate_k(last.ik, last.f_eval, last.df_eval)
        f_eval = eval_expression(function, ik)
        df_eval = eval_expression(d_function, ik)
        ep = abs(last.ik - ik)
        row = NewtonRaphsonResponse(k, ik, f_eval, df_eval, ep)

    simplified = simplify_data(row, show_decimals)

    results.append(simplified)

    if is_done(index, accuracy_decimals, error, simplified, last):
        return results

    return generate_i(function, index, accuracy_decimals, show_decimals, error,
                      results=results, d_function=d_function, last=row)


def generate_k(i: float | int, f_eval: int | float, df_eval: int | float) -> int | float:
    return i - (f_eval / df_eval)


def is_done(index: int, accuracy: int, error: int | float, row: Response, last: NewtonRaphsonResponse = None) -> bool:
    a = index == row.k
    if last is not None:
        b = check_truncate_values(row.ik, last.ik, accuracy)
    else:
        b = False
    if row.ep is not None:
        c = row.ep <= error
    else:
        c = False
    d = root_founded(row.f_eval)

    return a or b or c or d

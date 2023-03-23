from utility.util import Response, MultifunctionResponse, Function, \
    eval_expression, simplify_data, is_done


def secant(parameters: tuple[int | float, int | float], function: Function,
           index: int = None, error: int | float = None, decimals: int = None,
           show_decimals: int = None) -> list[Response]:
    if index is None:
        index = 50
    if error is None:
        error = 0.001
    if decimals is None:
        decimals = 4
    if show_decimals is None:
        show_decimals = 4

    return generate_i(parameters, function, index, error, decimals, show_decimals)


def generate_i(parameters: tuple[int | float, int | float], function: Function,
               index: int, error: int | float, accuracy_decimals: int, show_decimals: int,
               results: list[MultifunctionResponse] = None, last: MultifunctionResponse = None
               ) -> list[MultifunctionResponse]:
    if results is None:
        results = list()

    if last is not None:
        k = last.k + 1

        a, b = last.b, last.ik

        fa_eval, fb_eval = last.fb_eval, last.f_eval
    else:
        k = results.__len__() + 2

        a, b = parameters

        fa_eval, fb_eval = eval_expression(function, a), eval_expression(function, b)

    k_i = generate_ki(a, b, fa_eval, fb_eval)

    fk_i = eval_expression(function, k_i)

    ep = abs(k_i - b)

    row = MultifunctionResponse(k, a, b, fa_eval, fb_eval, k_i, fk_i, ep=ep)

    simplified_row = simplify_data(row, show_decimals)

    results.append(simplified_row)

    if is_done(index, accuracy_decimals, error, simplified_row):
        return results

    return generate_i(parameters, function, index, error, accuracy_decimals, show_decimals, results, row)


def generate_ki(a: int | float, b: int | float, fa_eval: int | float, fb_eval: int | float) -> int | float:
    return b - ((b - a) / (fb_eval - fa_eval)) * fb_eval

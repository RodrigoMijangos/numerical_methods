from utility.util import Response, MultifunctionResponse, Function, eval_expression, \
    assign_values, is_positive, simplify_data, check_truncate_values, root_founded, is_done


def false_position(parameters: tuple[int | float, int | float], function: Function,
                   index: int = None, error: int | float = None,
                   decimals: int = None, show_decimals: int = None) -> list[Response]:
    if index is None:
        index = 50
    if error is None:
        error = 0.001
    if decimals is None:
        decimals = 4
    if show_decimals is None:
        show_decimals = 4

    a, b = parameters

    k = 1

    fa_eval, fb_eval = eval_expression(function, a), eval_expression(function, b)

    ik = generate_ki(a, b, fa_eval, fb_eval)

    f_eval = eval_expression(function, ik)

    row = MultifunctionResponse(k, a, b, fa_eval, fb_eval, ik, f_eval)

    return generate_i(row, function, index, error, decimals, show_decimals)


def generate_i(last: MultifunctionResponse, function: Function,
               index: int, error: float | int, accuracy_decimals: int, show_decimals: int,
               results: list[Response] = None, polarity: tuple[bool, bool] = None) -> list[Response]:
    if polarity is None:
        if results is None:
            results = list()
            results.append(simplify_data(last, show_decimals))
        polarity = is_positive(last.fa_eval), is_positive(last.fb_eval)

    k = last.k + 1

    a, b = assign_values(polarity, (last.a, last.b), last.ik, last.f_eval)

    fa_eval, fb_eval = assign_values(polarity, (last.fa_eval, last.fb_eval), last.f_eval, last.f_eval)

    ki = generate_ki(a, b, fa_eval, fb_eval)

    fk_i = eval_expression(function, ki)

    ep = abs(ki - last.ik)

    row = MultifunctionResponse(k, a, b, fa_eval, fb_eval, ki, fk_i, ep)

    simplified = simplify_data(row, show_decimals)

    results.append(simplified)

    if is_done(index, accuracy_decimals, error, simplified):
        return results

    return generate_i(row, function, index, error, accuracy_decimals, show_decimals, results, polarity)


def generate_ki(a, b, fa_eval, fb_eval) -> int | float:
    return ((a * fb_eval) - (b * fa_eval)) / (fb_eval - fa_eval)

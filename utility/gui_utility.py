from numerical_methods.bisection_method import bisection, Response
from numerical_methods.newton_raphson_method import newton_raphson
from numerical_methods.secant_method import secant
from numerical_methods.false_position_method import false_position
from utility.util import Function


def get_responses(option: int, function: Function, *values, **kwargs) -> list[Response]:

    if option != 1:
        if option == 0:
            return bisection(parameters=(values[0], values[1]), function=function,
                             index=kwargs['index'],
                             error=kwargs['error'],
                             decimals=kwargs['accuracy'],
                             show_decimals=kwargs['show_decimals'])

        if option == 2:
            return secant(parameters=(values[0], values[1]), function=function,
                          index=kwargs['index'],
                          error=kwargs['error'],
                          decimals=kwargs['accuracy'],
                          show_decimals=kwargs['show_decimals'])

        if option == 3:
            return false_position(parameters=(values[0], values[1]), function=function,
                                  index=kwargs['index'],
                                  error=kwargs['error'],
                                  decimals=kwargs['accuracy'],
                                  show_decimals=kwargs['show_decimals'])

    else:
        return newton_raphson(initial=values[0], function=function,
                              index=kwargs['index'],
                              error=kwargs['error'],
                              accuracy_decimals=kwargs['accuracy'],
                              show_decimals=kwargs['show_decimals'])

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import Frame
from sympy.core import Function
from sympy.abc import x
from numpy import arange
from numerical_methods.responses.bisection_response import BisectionResponse
from numerical_methods.responses.response import Response


def graph(option: int, function: Function, frame: Frame, results: list[Response | BisectionResponse]) -> Frame:

    fig = Figure(figsize=(5, 5), dpi=100)

    if option != 1:
        if isinstance(results[0], BisectionResponse):
            a = max(results, key=lambda result: result.a).a
            b = max(results, key=lambda result: result.b).b

            if a > b:
                xmax = a + 1
                xmin = b - 1
            else:
                xmax = b + 1
                xmin = a - 1
        else:
            xmax = 5
            xmin = -5
    else:
        xmin = max(results, key=lambda result: result.ik).ik
        xmax = xmin + 1
        xmin -= 1

    step = abs(xmax - xmin)/25

    y = [[i, function.evalf(subs={x: i})] for i in arange(xmin, xmax, step)]

    f_y = [[result.ik, result.f_eval] for result in results]

    plot1 = fig.add_subplot(111)

    plot1.plot(*zip(*y), label="Función")

    plot1.plot(*zip(*f_y), label="Valores evaluados", color='blue', marker='o', ls='')

    plot1.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    plot1.legend()

    canvas = FigureCanvasTkAgg(fig, master=frame)

    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, frame)

    toolbar.update()

    canvas.get_tk_widget().pack()

    return frame

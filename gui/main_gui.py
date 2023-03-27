from tkinter.ttk import Combobox
from tkinter import *

from gui.graph_gui import graph
from utility.util import parse_expression
from gui.table_gui import show_table
from utility.gui_utility import get_responses


def start():
    root = Tk()

    root.resizable(False, False)

    frame = Frame(root, relief='sunken')
    frame.grid(sticky="we", padx=20, pady=20)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    label = Label(frame, text="Calcular la raíz de una función mediante métodos numéricos")
    label.grid(row=0, column=0, columnspan=4)
    label.grid_rowconfigure(1, weight=1)
    label.grid_columnconfigure(1, weight=1)

    Label(frame, text="Inserte la función").grid(row=1)

    f_input = Entry(frame)
    f_input.grid(row=2, column=0, pady=5, padx=10)

    Label(frame, text="Valores Iniciales").grid(row=1, column=1, columnspan=2, pady=5, padx=10)

    a_in = Entry(frame, width=10)
    a_in.grid(row=2, column=1, pady=5, padx=10)

    b_in = Entry(frame, width=10)
    b_in.grid(row=2, column=2, pady=5, padx=10)

    Label(frame, text="Seleccionar el Método").grid(row=1, column=3, pady=5, padx=10)

    combo = Combobox(frame, state='readonly', values=["Bisección", "Newton-Raphson", "Secante", "Falsa Posición"])
    combo.grid(row=2, column=3, pady=5, padx=10)

    combo.bind('<<ComboboxSelected>>', lambda e: _when_combo_changes(combo, b_in))
    combo.current(0)

    Label(frame, text="Iteraciones").grid(row=3, column=0)
    itr_in = Entry(frame, width=10)
    itr_in.grid(row=4, column=0)
    Label(frame, text="Margen de error").grid(row=3, column=1)
    err_in = Entry(frame, width=10)
    err_in.grid(row=4, column=1)
    Label(frame, text="Decimales parecidos").grid(row=3, column=2)
    acc_in = Entry(frame, width=10)
    acc_in.grid(row=4, column=2)
    Label(frame, text="Mostrar decimales").grid(row=3, column=3)
    show_in = Entry(frame, width=10)
    show_in.grid(row=4, column=3)

    Button(frame, text="Iniciar", command=lambda: _do(
        combo.current(),
        a_in.get(),
        b_in.get(),
        f_input.get(),
        itr_in.get(),
        acc_in.get(),
        show_in.get(),
        err_in.get()
    )).grid(row=5, column=3, pady=10)

    root.mainloop()


def _when_combo_changes(combo, entry):
    if combo.current() == 1:
        entry.config(state=DISABLED)
    else:
        if entry['state'] == DISABLED:
            entry.config(state=NORMAL)


def _do(option: int, a: str, b: str, function: str, *args):

    a = float(a)
    if b != '':
        b = float(b)
    index, accuracy, show = int(args[0]), int(args[1]), int(args[2]) + 1
    error = float(args[3])

    function = parse_expression(function)

    results = get_responses(option, function, a, b,
                            index=index,
                            accuracy=accuracy,
                            show_decimals=show,
                            error=error
                            )

    ws = Tk()
    ws.title('Resultados de la ejecución')
    ws.geometry('800x600')
    ws.resizable(False, False)
    ws['bg'] = '#AC99F2'

    table_frame = Frame(ws)

    table_frame = show_table(option, results, table_frame)

    graph_frame = Frame(ws)

    graph_frame = graph(option, function, graph_frame, results)

    table_frame.pack()

    graph_frame.pack()

    ws.mainloop()

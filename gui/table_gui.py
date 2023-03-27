from tkinter import *
from tkinter.ttk import Treeview
from numerical_methods.responses.bisection_response import BisectionResponse
from numerical_methods.responses.multifunction_response import MultifunctionResponse
from numerical_methods.responses.newton_rapshon_response import NewtonRaphsonResponse
from numerical_methods.responses.response import Response


def show_table(option: int, results: list[Response], frame: Frame) -> Frame:

    treeView = set_columns(option, frame)

    treeView = set_data(treeView, results)

    treeView.pack(fill=BOTH, expand=1)

    return frame


def set_data(view: Treeview, data: list[Response]) -> Treeview:
    for n in data:
        if isinstance(n, NewtonRaphsonResponse):
            view.insert(parent='', index=END, text='',
                        values=(n.k, n.ik, n.f_eval, n.df_eval, n.ep))
        elif isinstance(n, MultifunctionResponse):
            view.insert(parent='', index=END, text='',
                        values=(n.k, n.a, n.b, n.fa_eval, n.fb_eval, n.ik, n.f_eval, n.ep))
        elif isinstance(n, BisectionResponse):
            view.insert(parent='', index=END, text='',
                        values=(n.k, n.a, n.b, n.ik, n.f_eval, n.ep))
    return view


def set_columns(option: int, frame: Frame) -> Treeview:
    view = Treeview(frame)

    if option != 1:
        if option > 1:
            view['columns'] = ('col_k', 'col_a', 'col_b', 'a_eval', 'b_eval', 'ik', 'f_eval', 'ep')
        else:
            view['columns'] = ('col_k', 'col_a', 'col_b', 'ik', 'f_eval', 'ep')
    else:
        view['columns'] = ('col_k', 'ik', 'f_eval', 'df_eval', 'ep')

    view.column('#0', width=0, stretch=NO)
    view.heading('#0', text="", anchor=CENTER)

    view.column("col_k", anchor=CENTER, width=80)
    view.heading("col_k", text='K', anchor=CENTER)

    if option != 1:
        view.column('col_a', anchor=CENTER, width=80)
        view.heading('col_a', text='A', anchor=CENTER)

        view.column('col_b', anchor=CENTER, width=80)
        view.heading('col_b', text='B', anchor=CENTER)

        if option > 1:
            view.column('a_eval', anchor=CENTER, width=80)
            view.heading('a_eval', text='f(A)', anchor=CENTER)

            view.column('b_eval', anchor=CENTER, width=80)
            view.heading('b_eval', text='f(B)', anchor=CENTER)

        view.column('ik', anchor=CENTER, width=80)
        view.heading('ik', text='Xk', anchor=CENTER)

        view.column('f_eval', anchor=CENTER, width=80)
        view.heading('f_eval', text='f(Xk)', anchor=CENTER)

    else:
        view.column('ik', anchor=CENTER, width=80)
        view.heading('ik', text='Xk', anchor=CENTER)

        view.column('f_eval', anchor=CENTER, width=80)
        view.heading('f_eval', text='f(Xk)', anchor=CENTER)

        view.column('df_eval', anchor=CENTER, width=80)
        view.heading('df_eval', text='d/dx f(Xk)', anchor=CENTER)

    view.column('ep', anchor=CENTER, width=80)
    view.heading('ep', text='Porcentual Error', anchor=CENTER)

    return view

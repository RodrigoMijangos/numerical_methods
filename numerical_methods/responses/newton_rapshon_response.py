from numerical_methods.responses.response import Response


class NewtonRaphsonResponse(Response):

    def __init__(self, k: int, ik: int | float, f_eval: int | float, df_eval: int | float, ep: int | float = None):
        super().__init__(k, ik, f_eval, ep)
        self._df_eval = df_eval

    @property
    def df_eval(self):
        return self._df_eval

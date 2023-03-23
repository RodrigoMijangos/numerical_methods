from numerical_methods.responses.bisection_response import BisectionResponse


class MultifunctionResponse(BisectionResponse):

    def __init__(self,
                 k: int,
                 a: int | float,
                 b: int | float,
                 fa_eval: int | float,
                 fb_eval: int | float,
                 ik: int | float,
                 f_eval: int | float,
                 ep: int | float = None
                 ):
        super().__init__(k, a, b, ik, f_eval, ep)
        self._fa_eval = fa_eval
        self._fb_eval = fb_eval

    @property
    def fa_eval(self):
        return self._fa_eval

    @property
    def fb_eval(self):
        return self._fb_eval

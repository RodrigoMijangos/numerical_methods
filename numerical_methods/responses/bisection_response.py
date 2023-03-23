from numerical_methods.responses.response import Response


class BisectionResponse(Response):

    def __init__(self,
                 k: int,
                 a: int | float,
                 b: int | float,
                 ik: int | float,
                 f_eval: int | float,
                 ep: int | float = None
                 ):
        super().__init__(k, ik, f_eval, ep)
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

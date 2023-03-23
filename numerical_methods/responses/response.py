class Response:

    def __init__(self, k: int, ik: float | int, f_eval: float | int, ep: int | float = None):
        self._k = k
        self._ik = ik
        self._f_eval = f_eval
        self._ep = ep

    @property
    def k(self):
        return self._k

    @property
    def ik(self):
        return self._ik

    @property
    def f_eval(self):
        return self._f_eval

    @property
    def ep(self):
        return self._ep

    @ep.setter
    def ep(self, ep: float | int):
        self._ep = ep

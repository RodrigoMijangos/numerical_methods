class BisectionResponse:

    def __init__(self, k: int, a: float, b: float, ik: float, f_eval: float, ep: float = None):
        self._k = k
        self._a = a
        self._b = b
        self._ik = ik
        self._f_eval = f_eval
        self._ep = ep

    @property
    def k(self):
        return self._k

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

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
    def ep(self, ep: float):
        self._ep = ep

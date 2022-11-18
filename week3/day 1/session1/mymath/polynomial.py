class Polynomial:
    def __init__(self, *coeff) -> None:
        self.coeff = coeff

    def __call__(self, x:float) -> float:
        """Evaluate polynomial for the given parameter x"""


        return sum( c*(x**i) for i,c in enumerate(self.coeff) )

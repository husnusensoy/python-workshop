from dataclasses import dataclass
from typing import List


@dataclass
class Polynomial:
    """
    a + bx + cx^2
    """
    coeff: List[float]

    def eval(self, x:float) -> float:
        """
        res = c
        res = res * x + b # cx +b 
        res = res * x + a # cx^2 +bx +a
        
        """

        res: float = 0.

        for i, c in enumerate(self.coeff):
            res += c * x**i

        return res


    def derivate(self) :
        ...
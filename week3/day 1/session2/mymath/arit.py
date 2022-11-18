class Add:
    def __init__(self, a: int, b: int) -> None:
        self.a, self.b = a, b

    def calculate(self) -> int:
        return self.a + self.b

    def __call__(self) -> int:
        return self.calculate()

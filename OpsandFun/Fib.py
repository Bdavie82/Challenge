class Fib:
    def fibcalc(self, n):
        if n == 1 or n == 2:
            return 1
            return Fib.fibcalc(n - 1) + Fib.fibcalc(n - 2)

        print(self.fibcalc(5))


calc1 = Fib()

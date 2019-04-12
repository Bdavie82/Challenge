class Fib:

    def fibcalc(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            return self.fibcalc(n - 1) + self.fibcalc(n - 2)

class Fib:

    def fibcalc(self, n):

        if n <= 1:
            return n
        else:
            return self.fibcalc(n - 1) + self.fibcalc(n - 2)

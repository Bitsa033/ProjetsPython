class Calculatrice:
    plus = '+'
    moins = '-'
    multiplie = '*'
    divise = '/'

    def calcul(self, a, b, comparateur):
        if comparateur == self.plus:
            return a + b
        elif comparateur == self.moins:
            return a - b
        elif comparateur == self.multiplie:
            return a * b
        elif comparateur == self.divise:
            return a / b

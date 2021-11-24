def divizor_comun(a, b):
    while a % b != 0:
        old_a = a
        old_b = b

        a = old_b
        b = old_a % old_b
    return b


class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def set_numarator(self, numarator):
        self.numarator = numarator

    def set_numitor(self, numitor):
        self.numitor = numitor

    def __str__(self):
        return str(self.numarator) + "/" + str(self.numitor)

    def __add__(self, fr):
        numarator_nou = self.numarator * fr.numitor + fr.numarator * self.numitor
        numitor_nou = self.numitor * fr.numitor
        return Fractie(numarator_nou, numitor_nou)
        # dc = divizor_comun(numarator_nou, numitor_nou)    Metoda cu simplificarea fractiei
        # return Fractie(numarator_nou / dc, numitor_nou / dc)

    def __sub__(self, fr):
        numarator_nou = self.numarator * fr.numitor - self.numitor * fr.numarator
        numitor_nou = self.numitor * fr.numitor
        return Fractie(numarator_nou, numitor_nou)
        # dc = divizor_comun(numarator_nou, numitor_nou)
        # return Fractie(numarator_nou / dc, numitor_nou / dc)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)
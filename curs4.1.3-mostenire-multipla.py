class Dreptunghi:
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def aria(self):
        return self.lungime * self.latime

class Patrat(Dreptunghi):
    def __init__(self, latura):
        super().__init__(latura, latura)

class Figura3d:
    def volumul(self):
        return self.aria() * self.inaltime

class Cub(Figura3d, Patrat):
    def __init__(self, lungime):
        super().__init__(lungime)
        self.inaltime = lungime

    def aria_unei_fete(self):
        return super().aria()

    def suprafata_totala(self):
        return super().aria() * 6
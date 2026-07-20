import random


RONDAS = 1000
CAPITAL = 1000


class LaPekillada:

    def __init__(self):
        self.apuestas = {
            "A": 1,
            "B": 1,
            "C": 1
        }

        self.cero = 1

        self.capital = CAPITAL
        self.max_apuesta = 0


    def ronda(self):

        resultado = random.choice(
            ["A", "B", "C", "0"]
        )

        coste = (
            sum(self.apuestas.values())
            +
            self.cero
        )

        self.capital -= coste
        # Resultado columna
        if resultado in ["A","B","C"]:

            # premio docena 3x
            premio = self.apuestas[resultado] * 3

            self.capital += premio

            for col in self.apuestas:

                if col == resultado:
                    self.apuestas[col] = 1
                else:
                    self.apuestas[col] *= 2
            # el 0 no salió
            self.cero += 1
        else:
            # salió cero
            self.capital += self.cero * 36

            self.cero = 1

        self.max_apuesta = max(
            self.max_apuesta,
            max(self.apuestas.values()),
            self.cero
        )
        

    def simular(self):

        for i in range(RONDAS):
            self.ronda()
            

    def informe(self):

        print("\n=== LA PEKILLADA v2 ===")

        print(
            "Capital final:",
            self.capital
        )

        print(
            "Ganancia:",
            self.capital - CAPITAL
        )

        print(
            "Máxima apuesta alcanzada:",
            self.max_apuesta
        )

pk = LaPekillada()

pk.simular()

pk.informe()

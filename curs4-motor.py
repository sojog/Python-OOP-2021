# Definiți clasa Motor conținând informații despre seria motorului, puterea acestuia și numărul de kilometri parcurși. 
# Derivați din această clasă specializările MotorElectric și MotorBenzina, care aduc în plus informații privind bateria (% consumat din baterie la 1 km), respectiv consumul de combustibil în litri la suta de kilometri.
# Implementați MotorHibrid, derivând din cele două tipuri de motoare, asigurându-vă că seria motorului este moștenită într-un singur exemplar. 
# Definiți o metodă de avertizare atunci când au rămas sub 10 l de combustibil în rezervor sau bateria a atins un grad de descărcare de peste 90%.
class Motor:
    def __init__(self,serie_motor,km_parcursi,kp):
        self.serie_motor = serie_motor
        self.km_parcursi = km_parcursi
        self.kp = kp

class MotorEletric(Motor):
    def __init__(self,serie_motor,km_parcursi,kp,consum):
        super().__init__(serie_motor,km_parcursi,kp)
        self.consum = consum


class MotorBenzina(Motor):
    def __init__(self,serie_motor,km_parcursi,kp,consum_b):
        super().__init__(serie_motor,km_parcursi,kp)
        self.consum_b = consum_b


from time import sleep


# class
class pc:
    def __init__(self, marca, ram, led):
        self.marca = marca
        self.ram = ram
        self.led = led

    def ligar(self):
        print('ligando...')
        sleep(2)
        print('computador ligado')

    def desligar(self):
        print('Desligando...')

    def info(self):
        print(self.marca, self.ram, self.led)

# computador
computador = pc('asus', '8gb', 'led = sim')

# ligar, pedir info, desligar
computador.ligar()
computador.info()
computador.desligar()

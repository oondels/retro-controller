from gpiozero import Button
from signal import pause

class Botao:
    def __init__(self, nome, gpio):
        self.nome = nome
        self.button = Button(gpio)
        self.button.when_pressed = self.on_press

    def on_press(self):
        print(f"[{self.nome}] foi pressionado")

class Controle:
    def __init__(self):
        self.botoes = [
            Botao("R1", 17),
            Botao("R2", 27),
            Botao("L1", 22),
            Botao("L2", 10),
            Botao("Up", 9),
            Botao("Left", 11),
            Botao("Right", 5),
            Botao("Down", 13),
            Botao("Triangulo", 14),
            Botao("Bola", 15),
            Botao("Triangulo", 18),
            Botao("Triangulo", 23),
        ]

    def iniciar(self):
        print("Controle iniciado. Aguardando eventos...")
        pause()

if __name__ == "__main__":
    controle = Controle()
    controle.iniciar()

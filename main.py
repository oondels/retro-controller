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
            Botao("Up", 2),
            Botao("Left", 3),
            Botao("Right", 4),
            Botao("Down", 17),
        ]

    def iniciar(self):
        print("Controle iniciado. Aguardando eventos...")
        pause()

if __name__ == "__main__":
    controle = Controle()
    controle.iniciar()

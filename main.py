#!/usr/bin/env python3
import time
import uinput
from gpiozero import Button
from signal import pause

# 1) Liste todos os eventos que seu controle vai usar
events = [
    uinput.KEY_UP,
    uinput.KEY_DOWN,
    uinput.KEY_LEFT,
    uinput.KEY_RIGHT,
    uinput.KEY_LEFTSHIFT,  # exemplo para Select
    uinput.KEY_ENTER,      # exemplo para Start
    uinput.KEY_A,          # Triângulo → A
    uinput.KEY_B,          # Bola       → B
    uinput.KEY_X,          # Quadrado   → X
    uinput.KEY_Y,          # X (“retângulo”) → Y
    uinput.KEY_Q,          # L1
    uinput.KEY_W,          # L2
    uinput.KEY_E,          # R1
    uinput.KEY_R,          # R2
]

# 2) Cria o dispositivo virtual
device = uinput.Device(events)
time.sleep(0.5)  # garante que o /dev/uinput subiu

# 3) Mapeamento GPIO → evento uinput
mapping = {
    2:  uinput.KEY_UP,
    3:  uinput.KEY_LEFT,
    4:  uinput.KEY_RIGHT,
    17: uinput.KEY_DOWN,
    22: uinput.KEY_Q,        # L1
    27: uinput.KEY_W,        # L2
    19: uinput.KEY_E,        # R1
    26: uinput.KEY_R,        # R2
    10: uinput.KEY_LEFTSHIFT,# Select
    9:  uinput.KEY_ENTER,    # Start
    11: uinput.KEY_A,        # Triângulo
    5:  uinput.KEY_B,        # Bola
    6:  uinput.KEY_X,        # Quadrado
    13: uinput.KEY_Y,        # X
}

class Botao:
    def __init__(self, nome, gpio_pin):
        self.nome = nome
        self.pin = gpio_pin
        self.button = Button(gpio_pin)
        # quando apertar, chama on_press
        self.button.when_pressed = self.on_press

    def on_press(self):
        ev = mapping[self.pin]
        # Press + Release
        device.emit(ev, 1)  
        device.emit(ev, 0)
        # (opcional) log no console
        print(f"[{self.nome}] → {ev}")

class Controle:
    def __init__(self):
        # crie um Botao para cada entrada
        self.botoes = [
            Botao("Up", 2),
            Botao("Left", 3),
            Botao("Right", 4),
            Botao("Down", 17),
            Botao("L1", 22),
            Botao("L2", 27),
            Botao("R1", 19),
            Botao("R2", 26),
            Botao("Select", 10),
            Botao("Start", 9),
            Botao("Triangulo", 11),
            Botao("Bola", 5),
            Botao("Quadrado", 6),
            Botao("X", 13),
        ]

    def iniciar(self):
        print("Controle iniciado. Aguardando eventos...")
        pause()

if __name__ == "__main__":
    ctrl = Controle()
    ctrl.iniciar()

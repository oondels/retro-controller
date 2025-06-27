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
    19:  uinput.KEY_UP,
    13:  uinput.KEY_LEFT,
    6:  uinput.KEY_RIGHT,
    5: uinput.KEY_DOWN,
    11: uinput.KEY_Q,        # L1
    9: uinput.KEY_W,        # L2
    7: uinput.KEY_E,        # R1
    8: uinput.KEY_R,        # R2
    10: uinput.KEY_LEFTSHIFT,# Select
    26:  uinput.KEY_ENTER,    # Start
    12: uinput.KEY_A,        # Triângulo
    20: uinput.KEY_B,        # Bola
    16: uinput.KEY_X,        # Quadrado
    21: uinput.KEY_Y,        # X
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
            Botao("Up", 19),
            Botao("Left", 13),
            Botao("Right", 6),
            Botao("Down", 5),
            
            Botao("L1", 11),
            Botao("L2", 9),
            Botao("R1", 7),
            Botao("R2", 8),
            
            Botao("Select", 10),
            Botao("Start", 26),
            
            Botao("Triangulo", 12),
            Botao("Bola", 20),
            Botao("Quadrado", 16),
            Botao("X", 21),
        ]

    def iniciar(self):
        print("Controle iniciado. Aguardando eventos...")
        pause()

if __name__ == "__main__":
    ctrl = Controle()
    ctrl.iniciar()

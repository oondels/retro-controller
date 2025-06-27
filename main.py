#!/usr/bin/env python3
import time
import uinput
from gpiozero import Button
from signal import pause

# 1) Liste todos os eventos que seu controle vai usar
events = [
    uinput.KEY_UP,
    uinput.KEY_LEFT,
    uinput.KEY_RIGHT,
    uinput.KEY_DOWN,
    
    uinput.KEY_Q,          # L1
    uinput.KEY_E,          # R1
    uinput.KEY_Z,          # L2
    uinput.KEY_C,          # R2
    
    uinput.KEY_ENTER,       # Start KEY_RIGHTSHIFT
    uinput.KEY_RIGHTSHIFT,  # Select
    
    uinput.KEY_H,        # X
    uinput.KEY_G,        # Bola
    uinput.KEY_T,        # Triangulo
    uinput.KEY_F,        # Quadrado
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
    
    9: uinput.KEY_Q,        # L1
    8: uinput.KEY_E,        # R1
    11: uinput.KEY_Z,        # L2
    7: uinput.KEY_C,        # R2
    
    26: uinput.KEY_ENTER,    # Start
    10: uinput.KEY_RIGHTSHIFT,# Select
    
    20: uinput.KEY_H,        # X
    21: uinput.KEY_G,        # Bola
    12: uinput.KEY_T,        # Triangulo
    16: uinput.KEY_F,        # Quadrado
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
    
    def on_release(self):
        ev = mapping[self.pin]
        # Press + Release
        device.emit(ev, 0)
        print(f"[{self.nome}] → {ev}")
        

class Controle:
    def __init__(self):
        # crie um Botao para cada entrada
        self.botoes = [
            Botao("Up", 19),
            Botao("Left", 13),
            Botao("Right", 6),
            Botao("Down", 5),
            
            Botao("L1", 9),
            Botao("L2", 11),
            Botao("R1", 8),
            Botao("R2", 7),
            
            Botao("Start", 26),
            Botao("Select", 10),
            
            Botao("X", 20),
            Botao("Bola", 21),
            Botao("Triangulo", 12),
            Botao("Quadrado", 16),
        ]

    def iniciar(self):
        print("Controle iniciado. Aguardando eventos...")
        pause()

if __name__ == "__main__":
    ctrl = Controle()
    ctrl.iniciar()

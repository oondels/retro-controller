#!/usr/bin/env python3
import time
from evdev import UInput, ecodes as e
from gpiozero import Button
from signal import pause

# 1) Eventos suportados pelo controle
eventos = {
    # Direcional
    e.KEY_UP,
    e.KEY_DOWN,
    e.KEY_LEFT,
    e.KEY_RIGHT,

    # Botões frontais
    e.KEY_H,     # X
    e.KEY_G,     # B
    e.KEY_T,     # Y
    e.KEY_F,     # A

    # Ombros
    e.KEY_Q,     # L1
    e.KEY_E,     # R1
    e.KEY_Z,     # L2
    e.KEY_C,     # R2

    # Sistema
    e.KEY_ENTER,         # Start
    e.KEY_RIGHTSHIFT,    # Select
}

# 2) Cria o dispositivo virtual
device = UInput(events={e.EV_KEY: eventos}, name="Controle-GPIO", version=0x3)
time.sleep(0.2)  # aguarda o /dev/input/event ser criado

# 3) Mapeamento dos GPIOs para teclas
mapping = {
    19:  e.KEY_UP,
    13:  e.KEY_LEFT,
    6:   e.KEY_RIGHT,
    5:   e.KEY_DOWN,

    9:   e.KEY_Q,          # L1
    8:   e.KEY_E,          # R1
    11:  e.KEY_Z,          # L2
    7:   e.KEY_C,          # R2

    26:  e.KEY_ENTER,      # Start
    10:  e.KEY_RIGHTSHIFT, # Select

    20:  e.KEY_H,          # X
    21:  e.KEY_G,          # B
    12:  e.KEY_T,          # Y
    16:  e.KEY_F,          # A
}

class Botao:
    def __init__(self, nome, gpio_pin):
        self.nome = nome
        self.pin = gpio_pin
        self.ev = mapping[self.pin]
        self.button = Button(self.pin)
        self.button.when_pressed = self.on_press
        self.button.when_released = self.on_release

    def on_press(self):
        device.write(e.EV_KEY, self.ev, 1)
        device.syn()
        print(f"[{self.nome}] pressionado")

    def on_release(self):
        device.write(e.EV_KEY, self.ev, 0)
        device.syn()
        print(f"[{self.nome}] liberado")

class Controle:
    def __init__(self):
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
            Botao("B", 21),
            Botao("Y", 12),
            Botao("A", 16),
        ]

    def iniciar(self):
        print("Controle GPIO com evdev iniciado.")
        pause()

if __name__ == "__main__":
    ctrl = Controle()
    ctrl.iniciar()

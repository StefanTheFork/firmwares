#ehehfhedudheudheudheudheduheudheduhedh

import board
 
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
print("herlo wold")

_KEY_CFG = [
    board.GP0,  board.GP1,  board.GP2,  board.GP3,
    board.GP4,  board.GP5,  board.GP6,  board.GP7,
    board.GP8,  board.GP9,  board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15,
    board.GP16, board.GP17, board.GP18, board.GP19,
    board.GP20, board.GP21, board.GP22, board.GP26, board.GP27
]

# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        self.matrix = KeysScanner(
            pins=_KEY_CFG,
        )
        
keyboard = MyKeyboard()
 
keyboard.keymap = [
    [
        KC.ESC,    KC.q,    KC.w,    KC.e, KC.r, KC.t,
        KC.TAB,    KC.a,    KC.s,    KC.d, KC.f, KC.g,
        KC.LSHIFT, KC.z,    KC.x,    KC.c, KC.v, KC.b,
        KC.LCTL,   KC.LGUI, KC.LALT, KC.A, KC.B, KC.SPC, KC.BSPACE
    ],
]
 
if __name__ == '__main__':
    keyboard.go()

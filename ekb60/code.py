import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.extensions.international import International

keyboard = KMKKeyboard()

# Config

keyboard.tap_time = 150
keyboard.debug_enabled = False

# Exstentions / Modules

keyboard.modules = [Layers(), HoldTap()]
keyboard.extensions = [International()]

# Hardware configuration, it's messy i know

keyboard.row_pins = (
        board.GP4,
        board.GP5,
        board.GP2,
        board.GP1,
        board.GP0
)

keyboard.col_pins = (
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

XXXXXXX = KC.NO
_______ = KC.TRNS
CAPS = KC.LT(1, KC.CAPS)

keyboard.keymap = [
    [
        # Defualt layer
        KC.ESC,   KC.N1,    KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQUAL, XXXXXXX,   KC.BSPC,
        KC.TAB,   XXXXXXX,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC,  KC.RBRC,   XXXXXXX,
        KC.MO(1), XXXXXXX,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,  KC.BSLASH, KC.ENTER,
        KC.LSFT,  KC.NUBS,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, XXXXXXX,  KC.RSFT,   XXXXXXX,
        KC.LCTRL, KC.LGUI,  XXXXXXX, KC.LALT, XXXXXXX, XXXXXXX, KC.SPC, XXXXXXX,  XXXXXXX, XXXXXXX, KC.RALT, KC.RGUI, XXXXXXX,  KC.RCTRL,  XXXXXXX
    ],
    [
        # Layer 1, regular util buttons
        KC.TILDE, KC.F1,  KC.F2,   KC.F3,   KC.F4,     KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,   KC.F11,  KC.F12,  _______, KC.DEL,
        _______, _______, _______, _______, _______,   _______, _______, _______, KC.PGUP, _______, _______,  _______, _______, _______, _______,
        _______, _______, _______, _______, KC.PGDOWN, _______, _______, KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, _______, _______, _______, _______,
        _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______, _______,  _______, _______, KC.CAPS, _______,
        _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______, _______,  _______, _______, _______, _______
    ]
]

if __name__ == '__main__':
    keyboard.go()

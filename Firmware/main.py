#You import all the IOs of your board
import board

#These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap, Macros

#For the display
from kmk.modules.layers import Layers

#For OLED display
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
import busio

#This is the main instance of your keyboard
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())


#Adding display extensions
i2c_bus = busio.I2C(board.D5, board.D4)
driver = SSD1306(i2c = i2c_bus)
display = Display(display = driver, width = 128, height = 32, brightness = 0.8)
display.entries = [
    TextEntry(text = "MACROPAD!", x = 0, y = 16, x_anchor = "L", y_anchor = "T", layer = 0),
]
keyboard.extensions.append(display)

#Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
cut = KC.MACRO(Press(KC.LCTRL), Tap(KC.X), Release(KC.LCTRL))
copy = KC.MACRO(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL))
paste = KC.MACRO(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL))
right_tab = KC.MACRO(Press(KC.LCTRL), Tap(KC.TAB), Release(KC.LCTRL))
left_tab = KC.MACRO(Press(KC.LCTRL), Press(KC.LSFT), Tap(KC.TAB), Release(KC.LCTRL), Release(KC.LSFT))
save = KC.MACRO(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL))

#Define your pins here!
PINS = [board.D0, board.D10, board.D8, board.D7,board.D9,board.D1]

#Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#Here you define the buttons corresponding to the pins
#Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
#And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [[
    cut,
    copy,
    paste,
    left_tab,
    right_tab,
    save]]

if __name__ == "__main__":
    keyboard.go()




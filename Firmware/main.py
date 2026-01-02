#You import all the IOs of your board
import board

#These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.LED import statusLED

#For the display
from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

#For OLED display
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
import busio

#This is the main instance of your keyboard
keyboard = KMKKeyboard()

#Adding display extensions
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)
driver = SSD1306(i2c = i2c_bus)
display = Display(display = driver, width = 128, height = 32, brightness = 0.8)
display.entries = [
    TextEntry(text = "Cutting", x = 0, y = 16, x_anchor = "L", y_anchor = "T", layer = 0),
    TextEntry(text = "Copying", x = 0, y = 16, x_anchor = "L", y_anchor = "T", layer = 1),
    TextEntry(text = "Pasting", x = 0, y = 16, x_anchor = "L", y_anchor = "T", layer = 2),
    TextEntry(text = "Left Tab", x = 0, y = 16, x_anchor = "L", y_anchor = "T", layer = 3),
    TextEntry(text = "Right Tab", x = 0, y = 16, x_anchor = "L", y_anchor = "T", layer = 4),
    TextEntry(text = "Saving", x = 0, y = 16, x_anchor = "L", y_anchor = "T", layer = 5)
]
keyboard.extensions.append(display)

#Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

#Add the statusLED extension
statusLed = statusLED(led_pin = [board.GP_29], brightness = 30)
keyboard.extensions.append(statusLED)

#Define your pins here!
PINS = [board.GP_27, board.GP_2, board.GP_3, board.GP_26,board.GP_1,board.GP_4]

#Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#Here you define the buttons corresponding to the pins
#Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
#And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [[
    KC.Macro(KC.TO(0), Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD)),  
    KC.Macro(KC.TO(1), Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  
    KC.Macro(KC.TO(2), Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
    KC.Macro(KC.TO(3), Press(KC.LCMD), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(4), Press(KC.LCMD(KC.LSFT)), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(5), Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD))],
    
    #To prevent soft-locking from changes in layers
    [
    KC.Macro(KC.TO(0), Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD)),  
    KC.Macro(KC.TO(1), Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  
    KC.Macro(KC.TO(2), Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
    KC.Macro(KC.TO(3), Press(KC.LCMD), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(4), Press(KC.LCMD(KC.LSFT)), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(5), Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD))
],[
    KC.Macro(KC.TO(0), Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD)),  
    KC.Macro(KC.TO(1), Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  
    KC.Macro(KC.TO(2), Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
    KC.Macro(KC.TO(3), Press(KC.LCMD), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(4), Press(KC.LCMD(KC.LSFT)), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(5), Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD))
],[
    KC.Macro(KC.TO(0), Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD)),  
    KC.Macro(KC.TO(1), Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  
    KC.Macro(KC.TO(2), Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
    KC.Macro(KC.TO(3), Press(KC.LCMD), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(4), Press(KC.LCMD(KC.LSFT)), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(5), Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD))
],[
    KC.Macro(KC.TO(0), Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD)),  
    KC.Macro(KC.TO(1), Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  
    KC.Macro(KC.TO(2), Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
    KC.Macro(KC.TO(3), Press(KC.LCMD), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(4), Press(KC.LCMD(KC.LSFT)), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(5), Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD))
],[
    KC.Macro(KC.TO(0), Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD)),  
    KC.Macro(KC.TO(1), Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  
    KC.Macro(KC.TO(2), Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
    KC.Macro(KC.TO(3), Press(KC.LCMD), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(4), Press(KC.LCMD(KC.LSFT)), Tap(KC.TAB), Release(KC.LCMD)), 
    KC.Macro(KC.TO(5), Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD))
]]

#Start kmk!
if __name__ == 'main':
    keyboard.go()
lightvalue = 0
kitronik_VIEW128x64.control_display_on_off(True)
radio.set_group(52)
def on_forever():
    global lightvalue
    lightvalue = pins.analog_read_pin(AnalogPin.P1)
    kitronik_VIEW128x64.show(lightvalue)
    kitronik_VIEW128x64.refresh()
basic.forever(on_forever)
def on_button_pressed_a():
    radio.send_string("left")
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    radio.send_string("right")
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_ab():
    radio.send_string("both")
input.on_button_pressed(Button.AB, on_button_pressed_ab)
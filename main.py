lightvalue = 0
timel = 1000
timer = 1000
timeb = 1000
hasran = False
kitronik_VIEW128x64.control_display_on_off(True)
radio.set_group(52)
def on_forever():
    global lightvalue
    global hasran
    lightvalue = smarthome.read_light_intensity(AnalogPin.P1)
    if lightvalue >= 80 and not hasran:
        radio.send_string("COFFEE TIME")
        hasran = True
    
    
    kitronik_VIEW128x64.show("value: " + str(lightvalue) + " hasran: " + str(hasran) + "        ")
    kitronik_VIEW128x64.refresh()
basic.forever(on_forever)
def on_button_pressed_a():
    global timel
    global hasran
    radio.send_value("left", timel)
    if hasran == True:
        hasran = False
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global timer
    radio.send_value("right", timer)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_ab():
    global timeb
    radio.send_value("both", timeb)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
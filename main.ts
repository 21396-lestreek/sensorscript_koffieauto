let lightvalue = 0
kitronik_VIEW128x64.controlDisplayOnOff(true)
radio.setGroup(52)
basic.forever(function on_forever() {
    
    lightvalue = pins.analogReadPin(AnalogPin.P1)
    kitronik_VIEW128x64.show(lightvalue)
    kitronik_VIEW128x64.refresh()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("left")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("right")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendString("both")
})

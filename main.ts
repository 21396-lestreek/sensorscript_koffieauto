let lightvalue = 0
let timel = 1000
let timer = 1000
let timeb = 1000
let hasran = false
kitronik_VIEW128x64.controlDisplayOnOff(true)
radio.setGroup(52)
basic.forever(function on_forever() {
    
    
    lightvalue = smarthome.ReadLightIntensity(AnalogPin.P1)
    if (lightvalue >= 80 && !hasran) {
        radio.sendString("COFFEE TIME")
        hasran = true
    }
    
    kitronik_VIEW128x64.show("value: " + ("" + lightvalue) + " hasran: " + ("" + hasran) + "        ")
    kitronik_VIEW128x64.refresh()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    
    radio.sendValue("left", timel)
    if (hasran == true) {
        hasran = false
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    radio.sendValue("right", timer)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    radio.sendValue("both", timeb)
})

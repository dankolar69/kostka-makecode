let x: number;
forever(function on_forever() {
    
})
function on_logo_touched() {
    if (input.logoIsPressed()) {
        basic.showNumber(randint(1, 6))
        basic.showNumber(6)
    } else {
        basic.showNumber(randint(0, 10))
        basic.showNumber(10)
    }
    
}

function tlacitkoA() {
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
    })
}

if (input.buttonIsPressed(Button.A)) {
    x = randint(0, 10)
    if (x == 1) {
        basic.showLeds(`
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (x == 2) {
        basic.showLeds(`
            # # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (x == 3) {
        basic.showLeds(`
            # # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (x == 4) {
        basic.showLeds(`
            # # # # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (x == 5) {
        basic.showLeds(`
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (x == 6) {
        basic.showLeds(`
            # # # # #
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    
}


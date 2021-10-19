function on_logo_touched() {
    if (input.logoIsPressed()) {
        basic.showNumber(randint(1, 6))
    } else {
        basic.showNumber(randint(0, 10))
    }
    
}


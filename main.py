def on_forever():
    pass
forever(on_forever)

def on_logo_touched():
    if input.logo_is_pressed():
        basic.show_number(randint(1,  6))
        basic.show_number(6)
    else:
        basic.show_number(randint(0, 10))
        basic.show_number(10)
def on_gesture_shake():
    input.on_gesture(Gesture.SHAKE, on_gesture_shake)
def tlacitkoA():
    def on_button_pressed_a():
        pass
    input.on_button_pressed(Button.A, on_button_pressed_a) 

if input.button_is_pressed(Button.A):
        x = randint(0, 10)
        if x == 1:
            basic.show_leds("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        elif x == 2:
            basic.show_leds("""
            # # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        elif x == 3:
            basic.show_leds("""
            # # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        elif x == 4:
            basic.show_leds("""
            # # # # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        elif x == 5:
            basic.show_leds("""
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        elif x == 6:
            basic.show_leds("""
            # # # # #
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            """)

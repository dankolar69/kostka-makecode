def on_logo_touched():
    if input.logo_is_pressed():
        basic.show_number(randint(1, 6))
    else:
        basic.show_number(randint(0, 10))
def on_gesture_shake():
    input.on_gesture(Gesture.SHAKE, on_gesture_shake)
def on_button_pressed_a():
    input.on_button_pressed(Button.A, on_button_pressed_a)

    if input.button_is_pressed(Button.A):
             x = randint(0, 10)

    elif x == 1:
                    soundExpression.giggle(1)
                    basic.show_leds("""
                    # . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 2:
                    soundExpression.giggle(2)
                    basic.show_leds("""
                    # # . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 3:
                    soundExpression.giggle(3)
                    basic.show_leds("""
                    # # # . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 4:
                    soundExpression.giggle(4)
                    basic.show_leds("""
                    # # # # .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 5:
                    soundExpression.giggle(5)
                    basic.show_leds("""
                    # # # # #
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 6:
                    soundExpression.giggle(6)
                    basic.show_leds("""
                    # # # # #
                    # . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 7:
                    soundExpression.giggle(7)
                    basic.show_leds("""
                    # # # # #
                    # # . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)    
    elif x == 8:
                    soundExpression.giggle(8)
                    basic.show_leds("""
                    # # # # #
                    # # # . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 9:
                    soundExpression.giggle(9)
                    basic.show_leds("""
                    # # # # #
                    # # # # .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
    elif x == 10:
                    soundExpression.giggle(10)
                    basic.show_leds("""
                    # # # # #
                    # # # # #
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
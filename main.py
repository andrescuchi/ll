while True:
    temp= str(input.temperature())

    if input.temperature() > 30:
        basic.show_icon(IconNames.HAPPY)
        basic.show_string(temp)
    
    elif input.temperature() >= 20 and input.temperature() <= 30:
        basic.show_icon(IconNames.GHOST)
        basic.show_string(temp)

    else:
        basic.show_icon(IconNames.SAD)
        basic.show_string(temp)

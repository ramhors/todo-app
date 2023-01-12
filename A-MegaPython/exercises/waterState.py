zero = 0;
hundered = 100
def water_state(temperature):
    if temperature <= zero:
        return "Solid"
    elif  0 < temperature < hundered:
        return "Liquid"
    else:
        return "Gas"
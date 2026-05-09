def temperature_conversion(temp, threshold, unit='C'):
    unit = unit.upper()

    if unit == 'C':
        converted = (temp * 9 / 5) + 32
    elif unit == 'F':
        converted = (temp - 32) * 5 / 9
    else:
        raise ValueError("Unit must be 'C' or 'F'")

    if converted < threshold:
        return "Cold advisory"
    else:
        return "Heat alert"

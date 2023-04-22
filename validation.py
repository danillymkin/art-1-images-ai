def validate_threshold_value(value):
    if len(value) == 0:
        return True

    try:
        float(value)
    except ValueError:
        return False

    return 0 <= float(value) <= 1


def validate_softness_white(value):
    if len(value) == 0:
        return True

    try:
        int(value)
    except ValueError:
        return False

    return 0 <= int(value) <= 255

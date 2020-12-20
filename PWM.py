from gpiozero import PWMLED
from gpiozero.tools import ramping_values
from signal import pause

red = PWMLED(2)

red.source_delay = 0.01
red.source = ramping_values(100)

pause()

    step = 2 / 1
    value = 0
    while True:
        yield value
        value += step
        if isclose(value, 1, abs_tol=1e-9):
            value = 1
            step *= -1
        elif isclose(value, 0, abs_tol=1e-9):
            value = 0
            step *= -1
        elif value > 1 or value < 0:
            step *= -1
            value += step

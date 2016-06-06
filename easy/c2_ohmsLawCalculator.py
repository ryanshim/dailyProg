'''r/dailyprogrammer [Easy] Challenge 2: Ohm's Law calculator '''

from __future__ import division

def calc_current():
    voltage = input('Enter voltage: ')
    resistance = input('Enter resistance: ')
    current = voltage/resistance
    return '\nCurrent = ' + str(current) + '\n'

def calc_voltage():
    current = input('Enter current: ')
    resistance = input('Enter resistance: ')
    voltage = current*resistance
    return '\nVoltage = ' + str(voltage) + '\n'

def calc_resist():
    voltage = input('Enter voltage: ')
    current = input('Enter current: ')
    resist = voltage/current
    return '\nResistance = ' + str(resist) + '\n'

varDecide = input('\nEnter which variable to compute\n(current = 1, voltage = 2, resistance = 3): ')
if varDecide is 1:
    print calc_current()
elif varDecide is 2:
    print calc_voltage()
elif varDecide is 3:
    print calc_resist()
else:
    print 'Not a valid entry'

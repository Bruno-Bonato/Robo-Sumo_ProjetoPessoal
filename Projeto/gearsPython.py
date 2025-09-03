import time
import math
import func
from ev3dev2.motor import LargeMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

btn = Button()

color_sensor = ColorSensor(INPUT_1)
sensor = UltrasonicSensor(INPUT_2)

modo = 'BUSCANDO'
modo_girar = 'ESQUERDA'

while True:
    if func.detec_borda(color_sensor):
        func.parar_motores(left_motor, right_motor)
        time.sleep(0.1)
        func.recuar(tank_drive)
        func.girar_90(left_motor, right_motor)
        modo = 'BUSCANDO'
    else:
        modo_girar = func.decisao(sensor, tank_drive, left_motor, right_motor, modo, modo_girar, color_sensor)
    time.sleep(0.1)







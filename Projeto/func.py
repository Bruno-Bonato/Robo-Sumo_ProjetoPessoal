import time

def andar_para_frente(left_motor, right_motor):
    left_motor.run_forever(speed_sp=300)
    right_motor.run_forever(speed_sp=300)

def parar_motores(left_motor, right_motor):
    left_motor.stop()
    right_motor.stop()

def girar_esquerda(left_motor, right_motor):
    left_motor.run_forever(speed_sp=300)
    right_motor.run_forever(speed_sp=-300)

def girar_direita(left_motor, right_motor):
    left_motor.run_forever(speed_sp=-300)
    right_motor.run_forever(speed_sp=300)

def girar_90(left_motor, right_motor):
    left_motor.run_forever(speed_sp=300)
    right_motor.run_forever(speed_sp=-300)
    time.sleep(1.2)
    parar_motores(left_motor, right_motor)

def recuar(tank_drive):
    tank_drive.on_for_rotations(-25, -25, 0.7)

def ler_distancia(sensor):
    distancia = sensor.distance_centimeters
    print('Distância:', distancia)
    return distancia

def detec_borda(color_sensor):
    cor_detectada = color_sensor.color
    if cor_detectada == 5:
        print('Borda vermelha detectada!')
        return True
    else:
        return False

def andar_controlado(tank_drive, color_sensor, left_motor, right_motor):
    left_motor.run_forever(speed_sp=300)
    right_motor.run_forever(speed_sp=300)

    tempo_inicio = time.time()
    tempo_andar = 1.0

    while time.time() - tempo_inicio < tempo_andar:
        if detec_borda(color_sensor):
            parar_motores(left_motor, right_motor)
            print('Borda detectada durante caminhada!')
            return
        time.sleep(0.01)

    parar_motores(left_motor, right_motor)

def decisao(sensor, tank_drive, left_motor, right_motor, modo, modo_girar, color_sensor):
    distancia = ler_distancia(sensor)

    if distancia < 30:
        print('EMPURRANDO...')
        andar_para_frente(left_motor, right_motor)
        return modo_girar
    else:
        print('BUSCANDO...')
        if modo_girar == 'ESQUERDA':
            girar_esquerda(left_motor, right_motor)
            novo_modo_girar = 'DIREITA'
        else:
            girar_direita(left_motor, right_motor)
            novo_modo_girar = 'ESQUERDA'

        time.sleep(0.7)
        andar_controlado(tank_drive, color_sensor, left_motor, right_motor)
        return novo_modo_girar

 
       
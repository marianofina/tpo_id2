from config.mysql import mysql
from datetime import time


def get_horario_turno(horario: str):
    try:
        hora, minuto = validator(horario)
        if (hora < 0 or hora > 23) and (minuto != 0 or minuto != 15 or minuto != 30 or minuto != 45):
            return False
        else:
            print(hora, minuto)
            return hora, minuto
    except Exception as e:
        print(e)
        return False


def validator(horario: str):
    try:
        if len(horario) == 5:
            hora, minuto = horario.split(':')
            hora = int(hora)
            minuto = int(minuto)
            return hora, minuto
        else:
            return False
    except Exception as e:
        print(e)
        return False


def get_hora_disp(id_disp: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT horario_disp FROM disponibilidad WHERE id_disp = %s', (id_disp,))
        data = cursor.fetchone()
        cursor.close()
        return data[1], data[2]
    except Exception as e:
        print(e)
        return None


def citas_x_turno(horario: str, id_disp: str):
    try:
        hora_turno, minuto_turno = get_horario_turno(horario)
        hora_inicio, minuto_inicio = validator(get_hora_disp(id_disp)[0])
        hora_fin, minuto_fin = validator(get_hora_disp(id_disp)[1])
        horario_turno = time(hora_turno, minuto_turno)
        horario_inicio = time(hora_inicio, minuto_inicio)
        horario_fin = time(hora_fin, minuto_fin)
        if horario_inicio <= horario_turno <= horario_fin:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def validator_medico(hora_inicio: str, hora_fin: str):
    try:
        hora_inicio = hora_inicio.split(':')
        hora_fin = hora_fin.split(':')
        hora_inicio = int(hora_inicio[0])
        hora_fin = int(hora_fin[0])
        if hora_inicio < hora_fin:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

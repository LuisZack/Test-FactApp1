import os
import platform
import requests
import sys
import time


def enviar_mensaje_telegram(mensaje):
    TOKEN = '7070294206:AAHnrinmuF_VxebhaiCQmq9zT3TfiKEJWlc'
    CHAT_ID = '1154774418'
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': mensaje}

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()  # Lanza un error si la respuesta no es 200
        print('Mensaje enviado a Telegram con éxito.')
    except requests.exceptions.RequestException as e:
        print(f'Error al enviar mensaje a Telegram: {e}')

    #requests.post(url, data=data)


def hacer_ping(sitio):
    param = '-n 1' if platform.system().lower() == 'windows' else '-c 1'
    while True:
        comando = f'ping {param} {sitio}'
        respuesta = os.system(comando)
        
        if respuesta == 0:
            print(f'El sitio {sitio} está accesible.')
            msj_t=f'Acceso ÉXITOSO al sitio {sitio}'
        else:
            print(f'No se pudo acceder al sitio {sitio}.')
            msj_t=f'Alerta: No se pudo acceder al sitio {sitio}'
            
        enviar_mensaje_telegram(msj_t)
        
        time.sleep(10)  # Espera 10 segundos antes de volver a hacer ping

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sitio = sys.argv[1]
    else:
        sitio = 'halzfac.net.pe'
    hacer_ping(sitio)



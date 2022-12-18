# IMPORTANDO BIBLIOTECAS DO PYTHON --> NÃO MEXER AQUI!
# Elas servem para a gente poder usar algumas funções especiais.
import socket
import threading
import time
import sys
# --------------------------------------------------------------



# CONECTANDO COM O DRONE --> NAO MEXER AQUI!
tello_address = ('192.168.10.1', 8889)
local_address = ('', 9000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)
# --------------------------------------------------------------



# CRIANDO A FUNÇÃO QUE ENVIA A MENSAGEM DO CÓDIGO DE VOO PARA O DRONE --> NÃO MEXER AQUI!
def send(message):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Enviando mensagem para Drone: " + message)
  except Exception as e:
    print("ERRO!")
# -------------------------------------------------------------------------------------
    


# CRIANDO A FUNÇÃO QUE RECEBE SE A MENSAGEM DE CÓDIGO DE VOO PARA O DRONE FOI RECEBIDA COM ERRO OU SEM ERRO --> NÃO MEXER AQUI!
def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(128)
      print("Mensagem recebida pelo Drone: " + response.decode(encoding='utf-8'))
    except Exception as e:
      sock.close()
      print("Error receiving: " + str(e))
      break
# ---------------------------------------------------------------------------------------------------------------------------




# CRIANDO A FUNÇÃO COM A LÓGICA DE PROGRAMAÇÃO QUE CODIFICAREMOS!
def rodar():


# INICIANDO A CONEXÃO COM O DRON --> NÃO MEXER AQUI!
  receiveThread = threading.Thread(target=receive)
  receiveThread.daemon = True
  receiveThread.start()
# ----------------------------------------------------------------------

  try:
      command = input('Digite "command" e aperte a tela ENTER para começar ;)\n')
      send(command)

  except KeyboardInterrupt as e:
      sock.close()


# PROGRAMAREMOS AQUI:
  try:
    send('takeoff')
    time.sleep(3)
    contador = 5 #variável contadora do loop!
    #criando o loop
    for repetição in range (contador):
      #if par:
    if repetição % 2 == 0;
    send ('flip f')
    time.sleep(3)

    send('takeoff')
    time.sleep(3)

    #if impar
    send ('land')
    time.sleep(3)
  
  except KeyboardInterrupt as e:
      sock.close()
      breakpoint
# --------------------------------------------------------------




# RODANDO O PROGRAMA
rodar()
# ------------------


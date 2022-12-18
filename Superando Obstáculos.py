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







# PROGRAMAREMOS AQUI:

  try:
      #programaremos aqui nosso primeiro print!
      print("Python + Drone Tello --> João Cota")
      print("\n")
      print("\n")
      command = input('Digite "command" e aperte a tela ENTER para começar ;)\n')

      #programaremos aqui a função sair.
      if command == 'sair':
          #mensagem dizendo que o programa foi finalizado.
          print('Programa finalizado com sucesso\n')
          #comando em python que fecha o programa.
          sys.exit()
      #-----------------------------------------------------

      
      send(command)

  except KeyboardInterrupt as e:
      sock.close()


  while True:
    try:
        print("\n")
        message = input("Digite o comando de voo: ")
        send(message)

    except KeyboardInterrupt as e:
        sock.close()
        breakpoint
# --------------------------------------------------------------




# RODANDO O PROGRAMA
rodar()
# ------------------


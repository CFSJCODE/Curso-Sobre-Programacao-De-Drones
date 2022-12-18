# IMPORTANDO BIBLIOTECAS DO PYTHON --> NÃO MEXER AQUI!
# Elas servem para a gente poder usar algumas funções especiais.
import socket
import threading
import time
import sys
# --------------------------------------------------------------

SAIR = 'sair'

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

# Programaremos aqui nossos prints do loop
  while True:
    try:
        print("\n")
        escolha = input("Você quer fazer um loop no próximo código? --- (sim/nao): ")

        # Programaremos aqui o print 2
        if escolha == 'sim':
          print("\n")
          qtd = input("Quantas vezes quer repetir? ")
        #---------------------------------------------  

        #Senão
        else:
          qtd = 1
        #---------------------------------------------

        #convertendo qtd para número
        qtd = int(qtd)
        #---------------------------------------------
        
        print("\n")
        message = input("Digite o comando de voo: ")

        #caso 1
        if qtd>1 and (message == 'takeoff' or message == 'land'):
          print("Comandos de Voo 'takeoff' e 'land' apenas são executados uma vez!")
          print("\n")
          print("Loop excluído!")
          send(message)

        elif qtd > 1:
          for repetir in range(qtd):
            send(message)
            #Esperando 3 segundos
            time.sleep(3)
            #--------------------
        #----------------------------

        #caso 2
        if qtd == 1:
          send(message)
        #----------------------------
        
    except:
      print("erro")
# --------------------------------------------------------------




# RODANDO O PROGRAMA
rodar()
# ------------------
SAIR = 'sair'

if SAIR == 'sair':
  print('Programa finalizado com sucesso\n')
  sys.exit()


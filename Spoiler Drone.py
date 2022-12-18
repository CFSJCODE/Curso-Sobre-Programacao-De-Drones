import socket
import threading
import time
import sys

tello_address = ('192.168.10.1', 8889)
local_address = ('', 9000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)


def send(message):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("ERRO!")

def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      sock.close()
      print("Error receiving: " + str(e))
      break

      
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

print('****************** VOANDO COM PYTHON ******************\n*\n*\n*\n*\n*')
print('ATENÇÃO: Digite "sair" em qualquer momento para encerrar o programa :) ---\n*\n*\n*\n*\n*')


try:

    if (sys.version_info > (3, 0)):
      
      command = input('Digite "command" e aperte a tela ENTER para começar ;)\n')
      if command == 'sair':
        print('Programa finalizado com sucesso\n')
        sys.exit()
      
    else:
    
     command = raw_input('Digite "command" e aperte a tela ENTER para começar ;)\n')
     if command == 'sair':
        print('Programa finalizado com sucesso\n')
        sys.exit()
    
    send(command)
 
except KeyboardInterrupt as e:
    sock.close()


while True:
  
  try:

    if (sys.version_info > (3, 0)):
      escolha = input('\nVocê quer fazer um loop no próximo código? --- (sim/nao)\n')
      if escolha == 'sair':
        print('Programa finalizado com sucesso\n')
        sys.exit()
      if escolha == 'sim':
        qtd = input('\nQuantas vezes quer repetir?\n')  
        if qtd == 'sair':
          print('Programa finalizado com sucesso\n')
          break
        qtd = int(qtd)
        if qtd>0:
          print('\nDigite o comando de voo e aperte a tecla ENTER:') 
          message = input('')

      else:
        qtd =1 
        print('\nDigite o comando de voo e aperte a tecla ENTER:')
        message = input('')  

    else: 
      escolha = raw_input('\nVocê quer fazer um loop no próximo código? --- (sim/nao)\n')
      if escolha == 'sair':
        print('Programa finalizado com sucesso\n')
        sys.exit()
      if escolha == 'sim':
        qtd = raw_input('\nQuantas vezes quer repetir?\n')
        if qtd == 'sair':
          print('Programa finalizado com sucesso\n')
          break
        qtd = int(qtd)
        if qtd>0:
          print('\nDigite o comando de voo e aperte a tecla ENTER:') 
          message = raw_input('')

      else:
        qtd = 1;
        print('\nDigite o comando de voo e aperte a tecla ENTER:')
        message = raw_input('')  
    

    if message == 'sair':
      print("Programa finalizado com sucesso")
      break

    if escolha == 'nao':
      send(message)
    elif escolha == 'sim' and (message == 'takeoff' or message == 'land'):
      print("\nComandos de pousar e decolar apenas podem ser rodados uma vez. --------> Loop descartado.")
      send(message)
    else:
      for i in range(qtd):
        send(message)

   
 
  except KeyboardInterrupt as e:
    sock.close()
    break

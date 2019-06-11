import requests
import json
import docker

print('==============================================')
print('Escolha uma das seguintes opções: ')
print('1 - Armazenar dados do container.')
print('2 - Receber dados do servidor.')
print('9 - Sair da aplicação.')
print('==============================================')

x = input()

if x == 1:
    cli = docker.from_env()
    print(cli)
    stats = cli.stats('containercliente')
    print(stats)
    url = 'http://192.168.50.2:5000/container'
    for stat in stats:
        # TODO
        payload = {
            'Horario da Requisiçao': stat,
            'Nome do Container': stat,
            'Id do Container': stat,
            'Id da Imagem': stat,
            'Uso de CPU': stat,
            'Uso de Memoria': stat
        }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
if x == 2:
    url = 'http://192.168.50.2:5000/containers'
    r = requests.get(url)
    print(r)
if x == 9:
    exit()

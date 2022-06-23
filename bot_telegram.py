import json
import os
import time

import requests
import schedule


class TelegramBot:
    def __init__(self):
        iTOKEN  = 'LOCAL ONDE ADD O TOKEN'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'

    def Iniciar(self):
        iUPDATE_ID = None
        while True:
            iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = iATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, mensagem, primeira_mensagem):
        print('mensagem do cliente: ' + str(mensagem))
        if primeira_mensagem == True or mensagem.lower() in ('dicas','menu ','oi'):
            return f'''Olá seja bem vindo a Bot_Dicas de Youtube, temos informação e novidades da Bee Solution:{os.linesep}1 - Monitoramento de Olt Datacom {os.linesep}2 - Monitoramento Olt Fiberhome {os.linesep}3 - Monitoramento de Olt Zte '''
        if mensagem == '1':
            return f'''https://www.youtube.com/watch?v=6TwN2fL4qT8{os.linesep}Vai la deixa o seu link   (s/n)
            '''
        elif mensagem == '2':
            return f'''https://www.youtube.com/watch?v=Tjd2w9a4fEw{os.linesep}Vai la deixa o seu link   (s/n)
            '''
        elif mensagem == '3':
            return f'''https://www.youtube.com/watch?v=zHgjWE7mej4{os.linesep}Vai la deixa o seu link  (s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Obrigado,  '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' volte para o menu e escolha outro video.... '''
        else:
            return 'Assim que tivemos Novidade avisaremos  ou digite ( dicas )'

    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))




bot = TelegramBot()
bot.Iniciar()
import random
import PySimpleGUI as sg


class ChuteONumero:

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Ligar(self):

        layout = [[sg.Text('Seu Chute: ', size=(34, 0))],
                  [sg.Input(size=(18, 0), key='ValorChute')],
                  [sg.Button('Chutar!')], [sg.Output(size=(39, 10))]]

        self.janela = sg.Window('Chute!', layout=layout)

        self.GerarNumRand()

        try:
            while True:

                self.LerValor()

                if self.evento == 'Chutar!':
                    self.ValorDoChute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.ValorDoChute) > self.valor_aleatorio:
                            print('\n[Chute um valor mais baixo...]\n')
                            self.LerValor()
                            break
                        elif int(self.ValorDoChute) < self.valor_aleatorio:
                            print('\n[Chute um valor mais alto...]\n')
                            self.LerValor()
                            break
                        if int(self.ValorDoChute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('\nParabéns você acertou o número!\n')
                            break
        except:
            print('Digite apenas números inteiros...')
            self.Ligar()

    def LerValor(self):
        self.evento, self.valores = self.janela.Read()

    def PedirValor(self):
        self.ValorDoChute = input('\nChute um número:\n')

    def GerarNumRand(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,
                                              self.valor_maximo)


chute = ChuteONumero()
chute.Ligar()

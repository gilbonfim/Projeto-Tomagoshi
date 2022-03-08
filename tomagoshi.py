from time import sleep
class Animal:
    nome = ''
    especie = ''
    fome = 0
    
    def __str__(self):
        return f'Nome: {self.nome}; Especie: {self.especie}; Fome: {self.fome}'
    
    def __init__(self, nome, especie, fome=0):
        self.nome = nome
        self.especie = especie
        self.fome = fome
    
    def andar(self, fome_nova=1):
        self.fome += fome_nova
        
    def comer(self, comida=0):
        self.fome -= comida
        sleep(0.5)
        print('Alimentando o Animal')
        sleep(0.5)
        if self.fome < 0:
            self.fome = 0
            print('Animal comeu até ficar satisfeito e deixou comida no prato.')
            
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número interio válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m ')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc
animais = [Animal('Cavalo', 'Equino')]

while True:
    resposta = menu(['Alimentar Animal.', 'Andar com Animal.', 'Mostrar estado do Animal.', 'Sair do Sistema.'])
    if resposta == 1:
        animais[0].comer()
    elif resposta == 2:
        cabecalho('Animal Andando')
        animais[0].andar()

    elif resposta == 3:
        for animal in sorted(animais, key=lambda l : l.especie):
            print(animal)
    elif resposta == 4:
        print('Saindo do programa... See you soon!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
    
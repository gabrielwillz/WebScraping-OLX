from WebScrapingOLX import BuscarDadosOLX

def main():

    print('''\033[1;91m
    █░░░█ █▀▀ █▀▄ ▄▀▀ ▄▀ █▀▀▄ ▄▀▄ █▀▄ ▀ █▄░█ ▄▀▀░     ▄▀▄ █░░ █░█ 
    █░█░█ █▀▀ █▀█ ░▀▄ █░ █▐█▀ █▀█ █░█ █ █░▀█ █░▀▌     █░█ █░▄ ▄▀▄ 
    ░▀░▀░ ▀▀▀ ▀▀░ ▀▀░ ░▀ ▀░▀▀ ▀░▀ █▀░ ▀ ▀░░▀ ▀▀▀░     ░▀░ ▀▀▀ ▀░▀ 
    \033[0;0m''')
    print('\033[1;33m')
    print('------------------------------------------------------------------------------------------------')
    print('Opções de Dados: \n #pages = quantidade de paginas \n #regiao = SP, RJ \n #busca = 1 para IPhone | 2 para Carro | 3 para Notebook | 4 para Computador')
    print('\033[0;0m')


    pag = int(input('Quantas Páginas quer extrair? INSIRA ---> '))
    reg = str(input('Qual região você quer? INSIRA ---> '))
    bus = str(input('Qual número da busca? INSIRA ---> '))

    BuscarDadosOLX(pages=pag, regiao=reg, busca=bus)



main()


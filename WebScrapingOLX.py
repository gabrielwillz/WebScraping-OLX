import selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)
final = []
lista_buscas = []

def BuscarDadosOLX(pages=4, regiao='SP', busca='1'):
    RegiaoBuscar = {'SP': 'sao-paulo-e-regiao', 'RJ': 'rio-de-janeiro-e-regiao'}
    Prefix = {'SP': 'sp', 'RJ': 'rj'}
    ObjetoBusca = {'1': 'iphone', '2': 'carro', '3': 'notebook', '4': 'computador'}
    
    

    for x in range(1, pages):
        #print('Loop NUMERO: ' + str(x))
        url = 'https://' + Prefix[regiao] + '.olx.com.br/' + RegiaoBuscar[regiao] + '?q=' + ObjetoBusca[busca]
        if x == '0':
            print('somente a primeira pagina')
        else:
            url = 'https://' + Prefix[regiao] + '.olx.com.br/' + RegiaoBuscar[regiao] + '?o=' + str(x) + '&q=' + ObjetoBusca[busca]
            print(f'\033[1;32mLINK DA BUSCA ==>>> {url}\033[0;0m')
            lista_buscas.append(url)
        
 
    

    for i in lista_buscas:
        browser.get(i)
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source,'lxml')

        a = soup.find_all('li', class_="sc-1fcmfeb-2 juiJqh")
       
        for i in a:
            data = titulo = preco = ''

            try:
                data = i.find(class_="sc-1iuc9a2-3 kcOvhi sc-ifAKCX fWUyFm").contents[0].split()[0]
            except:
                pass
                    
            try:
                titulo = i.find('h2', class_="sc-1iuc9a2-1 dTvKuJ sc-ifAKCX eKQLlb").contents[0]
            except:
                pass    
            
            try:
                preco = i.find(class_="sc-1iuc9a2-8 bTklot sc-ifAKCX eoKYee").text
            except:
                pass
            
            final.append([data, titulo, preco])


    Data = pd.DataFrame(final, columns=['Data','Titulo', 'Preco'])
    Data.to_excel('Lista_Final.xlsx')
    print('\033[1;91m====>>>>> SEU ARQUIVO ESTÁ PRONTO!!!!!\033[0;0m')


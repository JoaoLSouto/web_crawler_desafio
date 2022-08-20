import requests
from bs4 import BeautifulSoup
from selenium import  webdriver
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.tripadvisor.com.br')
sleep(2)

#localizar a barra de pesquisa
input_place = navegador.find_element('input')
sleep(1)

#digitar as palavras chaves 
input_place.send_keys('Congresso Nacional - Brasília')
sleep(1)    

#encontrar a opção que tenha como botão uma foto e este será o único resultado encontrado com estas palavras chaves.
button_stay = navegador.find_element('button > picture')
sleep(1)
button_stay.click()

#após entrar na pagina do congresso nacional, precisamos localizar o botão que redirecionará para a média e quantidade de avaliações.
Searchsvg= navegador.find_element('svg')
Searchsvg.click()

page.content = navegador. page_source
site = BeautifulSoup(page.content, 'html.parser')

#encontrar o valor da média e quantidade de avaliações atráves da localização especifica dos atributos.
media = site.find('div', attrs={'class': 'f u j'}) 

avaliacoes = site.find('div', attrs={'span': 'class'}) 
print(avaliacoes.prettify())

print('## Resultado da coleta de dados ##')
print('Avaliação do local: ', avaliacoes, 'de ', media)

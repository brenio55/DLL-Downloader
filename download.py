import os.path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def abrirLista():
    lista = []

    with open('lista.txt') as listaArquivo:
        lista = listaArquivo.readlines()

        b = len(lista)
        b = range(b)
        url = []
        urlFalta = []

        chromeOptions = Options()
        chromeOptions.add_extension('./adblock.crx')
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        time.sleep(5)
        
        def ElementCheck(selector):
            try:
                driver.find_element_by_css_selector(selector)
            except:
                return False
            global baixar1
            baixar1 = driver.find_element_by_css_selector(selector)
            return True
            

        for a in b:            
            lista[a] = str(lista[a]).replace('\n', "")

            url.append(a)
            urlFalta.append(a)
            url[a] = 'https://pt.dll-files.com/' + lista[a] + '.html'
            urlFalta[a] = ''

            print(url[a])
            
            driver.get(url[a])

            valorBol = ElementCheck('#grid-container > section:nth-child(1) > div.download-pane > div.download-link > a')
            
            if valorBol == True:
                baixar1.click()
                time.sleep(7)        
                contadorFor = a + 89        
                print('Baixados: ', contadorFor)
                print('Concluído!')

            else:
                contador = contadorFor - 89
                print(url[a], 'não continha link. Pulando e armazenando variável...')

                if os.path.exists('faltas.txt'):
                    with open('faltas.txt', 'a') as arquivoFaltas:                        
                        urlFalta[a] = lista[a]
                        arquivoFaltas.write(str(urlFalta) + '' + str(contador) + '\n')
                else:
                    with open('faltas.txt', 'w') as arquivoFaltas:
                        urlFalta[a] = lista[a]
                        arquivoFaltas.write(str(urlFalta) + '' + str(contador) + '\n')

            

        driver.quit()

if __name__ == "__main__":
    abrirLista()
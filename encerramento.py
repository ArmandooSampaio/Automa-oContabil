from selenium import webdriver
import time
import logging

logging.basicConfig(filename='encerramento_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def auto_encerramento(empresa, login, senha): 
    try:
        navegador = webdriver.Chrome()
        navegador.maximize_window()
        navegador.get('https://iss.fortaleza.ce.gov.br/grpfor/login.seam?cid=1644247')

        fazer_login = navegador.find_element("class name", "btn")
        fazer_login.click()

        navegador.find_element("id", "username").send_keys(login)
        navegador.find_element("id", "password").send_keys(senha)
        navegador.find_element("id", "botao-entrar").click()

        time.sleep(5)

        
    except Exception as e:
        logging.error(f"{empresa}: Erro ao tentar concluir o encerramento")
        return
  
    
    finally:
        if navegador:
            navegador.quit()

from selenium import webdriver
import time

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
        print( empresa, ": Não foi possivel concluir sua solicitação com sucesso")
    
    finally:
        if navegador:
            navegador.quit()

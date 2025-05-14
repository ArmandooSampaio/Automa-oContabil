from selenium import webdriver
import time

def auto_encerramento(login, senha): 
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    navegador.get('https://iss.fortaleza.ce.gov.br/grpfor/login.seam?cid=1644247')

    fazer_login = navegador.find_element("class name", "btn")
    fazer_login.click()

    navegador.find_element("id", "username").send_keys(login)
    navegador.find_element("id", "password").send_keys(senha)
    navegador.find_element("id", "botao-entrar").click()

    navegador.close()

auto_encerramento("02488017329", "Fas201020")

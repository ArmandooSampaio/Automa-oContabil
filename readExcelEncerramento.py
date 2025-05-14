import pandas as pd
from encerramento import auto_encerramento

def data_read():
    df = pd.read_excel(r"C:\Users\USER\OneDrive\Code\Arquivos\Pasta1.xlsx")

    for _ , row in df.iterrows():
        empresa = row['EMPRESA']
        login = row['LOGIN']
        senha = row['SENHA'] 
        auto_encerramento(empresa, login, senha)
        print(empresa)
        
if __name__ == "__main__":
    data_read()


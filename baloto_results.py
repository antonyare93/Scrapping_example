# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd


url = 'https://www.baloto.com/resultados-' #baloto o revancha / num_sorteo
tipos = ['baloto', 'revancha']

datos = ['tipo', 'sorteo', 'num1', 'num2', 'num3', 'num4', 'num5', 'power', 'fecha']
resultados = []
resultados.append(datos)
with webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe") as driver:
    for sorteo in range(2081,2261):
        for tipo in tipos:
            resultado = []
            resultado.append(tipo)
            resultado.append(sorteo)
            driver.get(f'{url}{tipo}/{sorteo}')
            time.sleep(2)
            for balota in driver.find_elements(by=By.CLASS_NAME, value='yellow-ball'):
                resultado.append(balota.text)
            
            power_ball = driver.find_element(by=By.CLASS_NAME, value='red-ball')
            resultado.append(power_ball.text)

            datos_fecha = driver.find_element(by=By.CLASS_NAME, value='gotham-medium.white-color')
            resultado.append(datos_fecha.text)
            resultados.append(resultado)

# %%
df_resultados = pd.DataFrame(np.array(resultados))
df_resultados.columns = df_resultados.iloc[0]
df_resultados = df_resultados[(df_resultados.index != 0)].copy()
# %%
df_resultados.to_csv('./Dataset_baloto/resultados_baloto.csv', sep='|', index=False)

# %%

import time
from faker import Faker
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import string


# Gerador de dados fake
fake = Faker()
usuario = fake.user_name() + str(fake.random_int(1000, 9999))
senha = fake.password(length=10)

# Configurações do Chrome
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 5)

driver.get("https://www.roblox.com")

#--------------------------DATA DE NASCIMENTO----------------------------

select_day = Select(driver.find_element(By.ID, "DayDropdown"))
select_day.select_by_value("01")

select_month = Select(driver.find_element(By.ID, "MonthDropdown"))
select_month.select_by_value("Jan")

select_year = Select(driver.find_element(By.ID, "YearDropdown"))
select_year.select_by_value("2000")

#-------------------------------USUÁRIO----------------------------------

fake = Faker()

nome_base = fake.user_name()  # exemplo: "marcelo.souza"
sufixo_numerico = str(random.randint(1000, 9999))  # 5 dígitos
usuario = nome_base + sufixo_numerico  # exemplo final: "marcelo.souza84291"

campo_usuario = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "signup-username"))
)
campo_usuario.click()
campo_usuario.send_keys(usuario)

#-------------------------------SENHA----------------------------------

fake = Faker()

# Gera uma senha entre 8 e 20 caracteres
while True:
    password = fake.password(length=12)
    if 8 <= len(password) <= 20:
        break

# Localiza e preenche o campo de senha
campo_senha = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "signup-password"))
)
campo_senha.click()
campo_senha.send_keys(password)

#-------------------------SELECIONAR GÊNERO------------------------

botao_male = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "MaleButton"))
)
botao_male.click()

#-------------------------CLICANDO EM CADASTRAR--------------------

botao_cadastrar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "signup-button"))
)
botao_cadastrar.click()


print("Data selecionada: 01/01/2000")
print("Nick:", usuario)
print("Senha:", password)
print("Gênero: Masculino")


time.sleep(12)  # aguarda 12 segundos para garantir que tudo carregue
driver.quit()  # encerra o navegador

with open("contas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{usuario},{password}\n")
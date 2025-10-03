from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# VARIABLES DE ENTRADA 
nombre = "Bruno"
apellido = "Morales"
correo = "brunomorales@gmail.com"
mesNacimiento = "January"
diaNacimiento = "17"
anoNacimiento = "2002"

ciudad = "Mexico City"
codigoPostal = "15200"
pais = "Mexico"

sistemaOperativo = "Windows"
versionSO = "Windows 11" 
idiomaSO = "Spanish"

password = "Pass@word1"



# Iniciar navegador
buscar = webdriver.Chrome()
buscar.get("https://www.utest.com/")
wait = WebDriverWait(buscar, 10)

# Aceptar cookies
try:
    cookie_banner = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    cookie_banner.click()
    print("Banner de cookies cerrado.")
except:
    print("No apareció el banner de cookies.")

# Clic en Join Now

botonInicio = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Join Now")))
time.sleep(2)
botonInicio.click()

### Datos Personales ###
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys(nombre)
buscar.find_element(By.ID, "lastName").send_keys(apellido)
buscar.find_element(By.ID, "email").send_keys(correo)
buscar.find_element(By.ID, "birthMonth").send_keys(mesNacimiento)
buscar.find_element(By.ID, "birthDay").send_keys(diaNacimiento)
buscar.find_element(By.ID, "birthYear").send_keys(anoNacimiento)
time.sleep(1)

# Botón siguiente (Datos personales → Dirección)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[2]/button"))
).click()

### Direccion ###
wait.until(EC.presence_of_element_located((By.ID, "city")))
time.sleep(2)
buscar.execute_script(f"document.getElementById('city').value = '{ciudad}'")
buscar.find_element(By.ID, "zip").send_keys(codigoPostal)
buscar.find_element(By.ID, "countryId").send_keys(pais)
time.sleep(2)
buscar.find_element(By.CLASS_NAME, "btn-blue").click()

### Dispositivos ###
wait.until(EC.element_to_be_clickable((By.NAME, "osId"))).click()
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-select-choices-row")))

opciones = buscar.find_elements(By.CLASS_NAME, "ui-select-choices-row")
for opcion in opciones:
    if sistemaOperativo in opcion.text:
        buscar.execute_script("arguments[0].click();", opcion)
        break

wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "ui-select-choices-row")))
opciones_version = buscar.find_elements(By.CLASS_NAME, "ui-select-choices-row")

for opcion in opciones_version:
    texto = opcion.text.strip()
    if not texto:
        continue
    if versionSO in texto:
        buscar.execute_script("arguments[0].click();", opcion)
        break

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Select OS language']"))).click()
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-select-choices-row")))

opciones_language = buscar.find_elements(By.CLASS_NAME, "ui-select-choices-row")
for opcion in opciones_language:
    if idiomaSO in opcion.text:
        buscar.execute_script("arguments[0].click();", opcion)
        break

time.sleep(2)
buscar.find_element(By.CLASS_NAME, "btn-blue").click()

### Finalizar ###
wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
buscar.find_element(By.ID, "confirmPassword").send_keys(password)
buscar.find_element(By.NAME, "termOfUse").click()
time.sleep(1)
buscar.find_element(By.NAME, "privacySetting").click()

# Botón final
buscar.find_element(By.ID, "laddaBtn").click()
time.sleep(3)

# Redirigir a la página principal
##buscar.get("https://www.utest.com/")

login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.unauthenticated-nav-bar__log-in")))
login_btn.click()

email_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
time.sleep(2)
email_field.clear()
email_field.send_keys(correo)

login_button = wait.until(EC.element_to_be_clickable((By.ID, "kc-login")))
login_button.click()

password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
time.sleep(2)
password_field.clear()
password_field.send_keys(password)

signin_button = wait.until(EC.element_to_be_clickable((By.ID, "kc-login")))
signin_button.click()

time.sleep(5)
buscar.quit()

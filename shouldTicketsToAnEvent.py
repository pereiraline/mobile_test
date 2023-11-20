# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium import webdriver

# For W3C actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:deviceName"] = "Android"
caps["appium:appPackage"] = "com.sympla.tickets"
caps["appium:appActivity"] = "com.sympla.tickets.legacy.ui.splash.view.SplashActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

options = UiAutomator2Options()
options.load_capabilities(caps)
driver = webdriver.Remote("http://127.0.0.1:4723",  options=options)


# Example using WebDriverWait
wait = WebDriverWait(driver, 60)

element = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@resource-id=\"com.sympla.tickets:id/bottom_navigation_item_title\" and @text=\"Perfil\"]")))

btnPerfil = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.sympla.tickets:id/bottom_navigation_item_title\" and @text=\"Perfil\"]")
btnPerfil.click()

btnEntrarPerfil = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/profile_btn_enter")
btnEntrarPerfil.click()

waitInputEmail = wait.until(EC.presence_of_element_located((By.ID, "com.sympla.tickets:id/email")))

inputEmail = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/email")
inputEmail.click()
inputEmail.send_keys("allain.11@hotmail.com")

waitInputPassword = wait.until(EC.presence_of_element_located((By.ID, "com.sympla.tickets:id/password")))

inputPassword = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/password")
inputPassword.click()
inputPassword.send_keys("@Carbono13")

btnEnter = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/enter")
btnEnter.click()


waitBtnMapa = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@resource-id=\"com.sympla.tickets:id/bottom_navigation_item_title\" and @text=\"Mapa\"]")))

btnMapa = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.sympla.tickets:id/bottom_navigation_item_title\" and @text=\"Mapa\"]")
btnMapa.click()

# Depois do mapa

waitBtnEscolherCidadeManual = (EC.presence_of_element_located((By.ID,"com.sympla.tickets:id/button_choose_city")))

btnEscolherCidadeManual = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/button_choose_city")
btnEscolherCidadeManual.click()

# Escolher cidade 
waitEditTxtCitiesSearch = wait.until(EC.element_to_be_clickable((By.ID, "com.sympla.tickets:id/editTxtCitiesSearch")))
inputEditTxtCitiesSearch = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/editTxtCitiesSearch")
inputEditTxtCitiesSearch.click()
inputEditTxtCitiesSearch.send_keys("Recife")
inputEditTxtCitiesSearch.click()

selectCity = driver.find_element(by=AppiumBy.XPATH, value="//androidx.recyclerview.widget.RecyclerView[@resource-id=\"com.sympla.tickets:id/recyclerViewCities\"]/android.view.ViewGroup")
selectCity.click()


# Ver em lista 
waitBtnViewList = wait.until(EC.element_to_be_clickable((By.ID, "com.sympla.tickets:id/button_view_list")))
btnViewList = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/button_view_list")
btnViewList.click()

# Click no evento
waitEvent = wait.until(EC.element_to_be_clickable((By.ID, "com.sympla.tickets:id/rvEvents"))) 

select_event = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.sympla.tickets:id/imgBanner\"])[2]")
select_event.click()


# Click no VER INGRESSO
wait_see_ticket = wait.until(EC.element_to_be_clickable((By.ID, "com.sympla.tickets:id/event_buy_button"))) 
see_ticket = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/event_buy_button")
see_ticket.click()

# Encontre o elemento usando XPath
wait_see_ticket = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text=\"Ingressos\"]"))) 
elemento = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Ingressos\"]")

# Obtenha o texto do elemento
texto_do_elemento = elemento.text

# Valide se o texto é igual a "Ingressos"
assert texto_do_elemento == "Ingressos", f"O texto não é igual a 'Ingressos'. Texto atual: {texto_do_elemento}"

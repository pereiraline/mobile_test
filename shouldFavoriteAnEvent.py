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

# Click no nome do evento
waitSecundEvent = wait.until(EC.element_to_be_clickable((By.ID, "com.sympla.tickets:id/rvEvents"))) 
selectSecundEvent = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageButton[@resource-id=\"com.sympla.tickets:id/btnFavorite\"])[2]")
selectSecundEvent.click()

# Ir para tela de favoritos
favoriteMenu = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.sympla.tickets:id/bottom_navigation_item_title\" and @text=\"Favoritos\"]")
favoriteMenu.click()

# Assertiva 
favorite_button = driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/floating_fav_button_image")

# Deve validar se o botão está visível
assert favorite_button.is_displayed(), "O botão não está visível"
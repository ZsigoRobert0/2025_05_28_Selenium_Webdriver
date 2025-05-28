from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome beállítások
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Webdriver inicializálása
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Oldal megnyitása
    driver.get("https://parking-garage-app.netlify.app/")
    
    # Várunk, amíg az oldal teljesen betölt
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-link"))
    )
    
    # Login linkre kattintás
    login_link = driver.find_element(By.ID, "login-link")
    login_link.click()
    
    # Várunk, amíg a login oldal betölt
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    
    # Bejelentkezési adatok megadása
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    
    email_input.send_keys("juhaszabi123@gmail.com")
    password_input.send_keys("Audi")
    
    # Login gombra kattintás
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Várunk, amíg a bejelentkezés megtörténik
    time.sleep(4)
    
    # Ellenőrizzük, hogy sikeres volt-e a bejelentkezés
    assert "juhaszabi123" in driver.page_source
    
    print("Sikeres bejelentkezés!")

finally:
    # Böngésző bezárása
    driver.quit() 
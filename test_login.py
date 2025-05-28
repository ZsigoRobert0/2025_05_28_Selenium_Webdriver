from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# Firefox beállítások
firefox_options = Options()
firefox_options.add_argument("--start-maximized")
firefox_options.add_argument("--disable-gpu")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Webdriver inicializálása
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

try:
    # Oldal megnyitása
    driver.get("https://parking-garage-app.netlify.app/")  # Itt add meg a megfelelő URL-t
    
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
    
    email_input.send_keys("juhaszabi123@gmail.com")  # Itt megadod a megfelelő email címet
    password_input.send_keys("Audi")  # Itt megadod a megfelelő jelszót
    
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
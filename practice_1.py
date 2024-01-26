
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

op = webdriver.ChromeOptions()
op.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=op)
driver.get('https://web.whatsapp.com/')

wait = WebDriverWait(driver, 3000)
search = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')))
#search = driver.find_element(By.XPATH,value='//*[@id="side"]/div[1]/div/div[2]/div[2]')
search.send_keys("omkar")
search.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 3000)

text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')))

for i in range (25000):
    text = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')))
    text.send_keys("hello omkar")
    text.send_keys(Keys.ENTER)
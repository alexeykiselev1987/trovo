from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard
browser = webdriver.Chrome()
browser.get('https://trovo.live')
#открытие максимального окна
browser.maximize_window()
#browser.set_window_size(1920, 1080)
loginbutton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div[3]/div[4]/button")#Full XPATH
time.sleep(1)
loginbutton.click()
time.sleep(5)
#поиск поля логина
loginfield = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div[1]/div/input")#Full XPATH
time.sleep(5)
loginfield.click()
time.sleep(5)
loginfield.send_keys("aleksey.kiselev49631@gmail.com")
print("Введите пароль")
time.sleep(20)
#поиск поля пароля
passwordfield = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div[3]/div/input")#Full XPATH
time.sleep(5)
passwordfield.click()
#ActionChains(browser).move_by_offset(490, 565).click().perform()
#keyboard.write("longuspenisbasisvita")
passwordfield.send_keys("longuspenisbasisvita")
time.sleep(5)
keyboard.press("enter")
time.sleep(1)
keyboard.release("enter")
time.sleep(5)
print(browser.window_handles)
browser.get('https://trovo.live/s/likethedevil?roomType=1')
time.sleep(5)
print(browser.window_handles)
#поиск конкурсов
konkursi = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div/button/img")#Full XPATH
time.sleep(5)
konkursi.click()
time.sleep(5)
#поиск боксов
boxs = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/button[3]/div/img")#Full XPATH
time.sleep(5)
boxs.click()
time.sleep(5)
#кликаем на бокс
ActionChains(browser).move_by_offset(950, 570).click().perform()
time.sleep(5)
print(browser.window_handles)
print({browser.current_url})
#переключаем вкладку в селениуме
browser.switch_to.window(browser.window_handles[1])
time.sleep(5)
print({browser.current_url})
#Нажимаем "Присоединиться к квесту"
#ActionChains(browser).move_by_offset(960, 535).click().perform()
#time.sleep(5)
#print({browser.current_url})
#кликаем на страницу
#ActionChains(browser).move_by_offset(950, 370).click().perform()
#Нажимаем "Отслеживать"
#ActionChains(browser).move_by_offset(1300, 1005).click().perform()
OtslezhivatButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/section/div[2]/div[1]/button/span[1]")#Full XPATH
time.sleep(5)
OtslezhivatButton.click()
time.sleep(5)
print(browser.window_handles)
TreasureField = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[3]")#Full XPATH
time.sleep(5)
browser.switch_to_frame("iframe_dialog_1677874939428")
time.sleep(5)
#Нажимаем "Присоединиться к квесту"
#ActionChains(browser).move_by_offset(960, 535).click().perform()
#time.sleep(5)
#принимаем правила чата
#ActionChains(browser).move_by_offset(1737, 900).click().perform()
#PravilaChata = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/section/div[2]/section/section/div/button")#Full XPATH
#time.sleep(5)
#PravilaChata.click()
#time.sleep(5)
#Нажимаем "Присоединиться к квесту"
JoinTheQuestButton = browser.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/section[2]/div/button")#Full XPATH
time.sleep(5)
JoinTheQuestButton.click()
time.sleep(5)
#Выполняем условие №1
#ActionChains(browser).move_by_offset(1068, 624).click().perform()
Task1 = browser.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/section[2]/ul/li/div/pre")#Full XPATH
time.sleep(5)
Task1.click()
time.sleep(5)
#Выполняем условие №2
#Task2 = browser.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/section[2]/ul/li/div/pre")#Full XPATH
#time.sleep(5)
#Task2.click()
#time.sleep(5)
#Нажимаем "Отправить"
OtpravitButton = browser.find_element(By.XPATH, "/html/body/div[1]/section/div[1]/section[2]/ul/li/div/pre")#Full XPATH
time.sleep(5)
OtpravitButton.click()
time.sleep(5)
#Закрываем текущую вкладку
keyboard.press("ctrl+w")
time.sleep(1)
keyboard.release("ctrl+w")
print(browser.window_handles)
#поиск элемента по id(устарело)
#user_name = browser.find_element_by_id("user-name")
#правильный поиск по id
#user_name = browser.find_element(By.ID, "user-name")   #ID
#user_name = browser.find_element(By.NAME, "user-name")  #NAME
#user_name = browser.find_element(By.XPATH, "//*[@id='user-name']")#Full XPATH
#user_name = browser.find_element(By.XPATH, "//input[@id='user_name']")#ID XPATH
#user_name = browser.find_element(By.XPATH, "//input[@data-test='username']")#data-test XPATH
#password = browser.find_element(By.CSS_SELECTOR, "#password")#CSS_SELECTOR
#password.send_keys("secret_sauce")
#стирание символов
#user_name.send_keys(Keys.BACKSPACE)
#time.sleep(5)
#user_name.send_keys(Keys.BACKSPACE)
#time.sleep(5)
#добавление букв
#user_name.send_keys("er")
#time.sleep(5)
#выбор кнопки
#button_login = browser.find_element(By.XPATH, "//input[@value='Login']")
#нажатие на кнопку
#button_login.click()
#Нажатие кнопки Enter
#password.send_keys(Keys.RETURN)
#скроллинг страницы
#browser.execute_script("window.scrollTo(x,y)")
#обновление страницы
#browser.refresh()
#пауза
#time.sleep(10)
#закрытие браузера
#browser.close()
#ID
#NAME
#CLASS_NAME
#XPATH
#LINK_TEXT
#TAG_NAME
#CSS_SELECTOR

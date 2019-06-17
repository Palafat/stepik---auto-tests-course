from selenium import webdriver
import time
link = "http://"
browser = webdriver.Chrome(executable_path='/home/user/Документы/Chromedriver/chromedriver')
browser.get(link)
time.sleep(2)
browser.find_element_by_name("login").send_keys()
browser.find_element_by_name("password").send_keys()
browser.find_element_by_xpath("//button[contains(text(),'Войти')]").click()
time.sleep(1)
browser.find_element_by_xpath("//i[@class='fal fa-comments']").click()
time.sleep(1)
browser.find_element_by_xpath("//span[contains(text(),'Тестерович Тестер - Вадим Девелопер')]").click()
browser.find_element_by_xpath("//textarea[@placeholder='Введите Сообщение']").send_keys("Прозноз погоды/Курсы")
browser.find_element_by_xpath("//button[@class='chat-controls-submit btnSaveProfile']").click()

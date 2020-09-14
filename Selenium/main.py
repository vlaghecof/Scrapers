import requests, bs4, re, time, selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:\\Users\\Vlad\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chromedriver.exe')


#driver.get("https://techwithtim.net/")
driver.get("https://orteil.dashnet.org/cookieclicker/")

# this is to navigate and select elemets
# pp=driver.find_element_by_name('s')
#
# pp.clear()
# pp.send_keys("test")
# pp.send_keys(Keys.ENTER)
#
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     articles=main.find_elements_by_tag_name("article")
#     for article in articles:
#        header=article.find_element_by_class_name("entry-summary")
#        print(header.text)
#
# finally:
#      driver.quit()


#navigating links
# link=driver.find_element_by_link_text("Python Programming")
# link.click()
#
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()
#
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     element.click()
#
#
# except:
#    # driver.quit()
#    pass

#cookie clicker build


driver.implicitly_wait(5)


cookie=driver.find_element_by_id("bigCookie")
cookieCount=driver.find_element_by_id("cookies")

items=[ driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]



actions=ActionChains(driver)
actions.click(cookie)

page10 = driver.find_element_by_id("storeBulk10")
page1 = driver.find_element_by_id("storeBulk1")
page10.click()

step=1;
ok=1
while True:
   step=step%2000
   step+=1




   actions.perform()
   count=int (str(cookieCount.text.split(" ")[0]).replace(",",""))

   if count > 1000 and ok==1:
       items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(4, -1, -1)]
       ok=0


   if step%100==0:
       page1.click()
       print(step)
   if step%100==10:
       page10.click()
       print(step)


   if count >= 100 and count%100<70:
       upgrade = driver.find_element_by_id("upgrade0")
       upgrade.click()

   for item in items :
       aux1 = str(item.text.split(" ")[0])
       if str(aux1).__contains__(","):
           aux=aux1.replace(",", "")
           value=int(aux)
       else:
           if str(aux1).__contains__("."):
               aux = aux1.replace(".", "")
               value = int(aux)
           else:
            value=int(aux1)

       if value<=count:
            upgradeActions=ActionChains(driver)
            upgradeActions.move_to_element(item)
            upgradeActions.click()
            upgradeActions.perform()




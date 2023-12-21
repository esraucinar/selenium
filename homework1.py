from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#"https://www.saucedemo.com/"

#-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
class Test_SauceDemo:
      def user(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(5)
       
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        testResult = errorMessage.text =="Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
testClass = Test_SauceDemo()
testClass.user()

#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
class Test_SauceDemo:
        def passPasword(self):
            driver =webdriver.Chrome()
            driver.get("https://www.saucedemo.com")
            driver.maximize_window() 
            sleep(5)
            usernameInput = driver.find_element(By.ID,"user-name")
            usernameInput.send_keys("standard_user") 
            sleep(5)
            passwordInput = driver.find_element(By.ID,"password")
            passwordInput.send_keys("")
            sleep(5)
            loginButton = driver.find_element(By.ID,"login-button")
            loginButton.click()
            sleep(5)
            errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
            testResult = errorMessage.text =="Epic sadface: Password is required"
            print(f"TEST SONUCU: {testResult}")
testClass = Test_SauceDemo()
testClass.passPasword()
#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
class Test_SauceDemo:
        def sorry(self):
            driver =webdriver.Chrome()
            driver.get("https://www.saucedemo.com")
            driver.maximize_window() 
            sleep(5)
            usernameInput = driver.find_element(By.ID,"user-name")
            usernameInput.send_keys("locked_out_user")
            sleep(5)
            passwordInput = driver.find_element(By.ID,"password")
            passwordInput.send_keys("secret_sauce")
            sleep(5)
            loginButton = driver.find_element(By.ID,"login-button")
            loginButton.click()
            errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
            testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
            print(f"TEST SONUCU: {testResult}")
testClass = Test_SauceDemo()
testClass.sorry()

#-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde 
#kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
class Test_SauceDemo:
    def successfull_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        listOfElement = driver.find_elements(By.CLASS_NAME, "inventory_item")
        urunSayisi = len(listOfElement) == 6
        print(len(listOfElement))
        print(f"BEKLENEN SONUC : {urunSayisi}")

testClass = Test_SauceDemo()
testClass.successfull_login()




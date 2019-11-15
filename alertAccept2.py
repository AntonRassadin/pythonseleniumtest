from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x = browser.find_element_by_css_selector('#input_value').text
    inputAnswer = browser.find_element_by_css_selector("#answer")
    inputAnswer.send_keys(calc(x))

    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()

    alert = browser.switch_to.alert
    alertText = alert.text
    answer = alertText.split(': ')[-1]
    alert.accept()

    link2 = 'https://stepik.org/catalog?language=en'
    browser.get(link2)

    time.sleep(3)

    buttonLogIn = browser.find_element_by_css_selector(".navbar__auth_type_login")
    buttonLogIn.click()

    email = browser.find_element_by_css_selector("#id_login_email")
    email.send_keys('@mail') # @mail from account of stepik.org

    login = browser.find_element_by_css_selector("#id_login_password")
    login.send_keys('pass') #pass is password from account of stepik.org

    buttonLogIn = browser.find_element_by_css_selector('.sign-form__btn.button_with-loader')
    buttonLogIn.click()
    time.sleep(2)

    browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    time.sleep(5)

    inputAnswer = browser.find_element_by_css_selector(".string-quiz__textarea")
    inputAnswer.send_keys(answer)

    button = browser.find_element_by_css_selector('button.submit-submission')
    button.click()

finally:
    time.sleep(10)
    browser.quit()


import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
# from webdriver_auto_update import check_driver
import chromedriver_autoinstaller
import requests
from selenium.webdriver.support.select import Select

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

page_url = " https://www.tendable.com/"
driver.get(page_url)
driver.maximize_window()

#home accessible 
r = requests.head(page_url)
print(r.ok)
print("Home page :",driver.title())

#OurStroy
our_stroy_link= driver.find_element(By.XPATH,"//a[normalize-space()='Our Story']")
print(our_stroy_link.text)
print("Link1 clickable:",our_stroy_link.is_enabled)

#OurSolution
Our_solution_link = driver.find_element(By.LINK_TEXT,"Our Solution")
print("Link 2 :",Our_solution_link.is_enabled)

#Why Tendable
Why_tendable_link = driver.find_element(By.LINK_TEXT,"Why Tendable?")
print("Link3 clickable :",Why_tendable_link.is_enabled)

# Request Demo Button

def verify_request_demo_button(driver):
    
    # //div[@class='button-links-panel']/a[3]
    try:
        req_demo_butn= "//div[@class='button-links-panel']//a[@class='button'][normalize-space()='Request a Demo']"

        if req_demo_butn.is_displayed():
            print("Request demo Button is present")

            if req_demo_butn.is_enable():
                print("Request demo button is active")
            else:
                print("button is not active")
        else:
            print("Button is not present")
    except Exception as e:
        print(f'Error while verifying the Req button: {str(e)}')

def contact_us_linkform(driver):

    contact_us_link= driver.find_element(By.LINK_TEXT,"Contact Us")
    contact_us_link.click()

    #marketing contact us form
    contact_us_btn = " (//button[@class='body-button bg-plain-600 toggle-control'][normalize-space()='Contact'])[1]"

    driver.find_element(By.XPATH,contact_us_btn).click()

    #Form completion
    driver.find_element(By.XPATH,"(//input[@id='form-input-fullName'])[1]").send_keys("Sohil Jain")
    driver.find_element(By.XPATH,"(//input[@id='form-input-organisationName'])[1]").send_keys("SA Tech")
    driver.find_element(By.XPATH,"(//input[@name='cellPhone'])[1]").send_keys("9424534524")
    driver.find_element(By.XPATH,"(//input[@name='email'])[1]").send_keys("abc@gmail.com")

    job = Select(driver.find_element(By.XPATH,"(//select[@id='form-input-jobRole'])[1]"))
    job.select_by_value("Management")

    Agree_button =driver.find_element(By.XPATH,"(//input[@id='form-input-consentAgreed-0'])[1]")
    Agree_button.click()

    Submit_btn = driver.find_element(By.XPATH,"//button[contains(@data-loading-text,'Loading...')][normalize-space()='Submit']")
    Submit_btn.click()

def check_error(driver):

    driver.implicitly_wait(5)
    try:
        error_message = driver.find_element(By.XPATH,"//p[contains(text(),'Sorry, there was an error submitting the form.')]")
        if error_message.is_displayed():
            print("PASS : Error message displayed")
        else :
            print("Fail : Error message didnt appeared")

    except:
        print("Test case Failed")

verify_request_demo_button(driver)
contact_us_linkform(driver)
check_error(driver)

driver.quit()
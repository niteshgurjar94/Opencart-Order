import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.tutorialsninja.com/demo/")
driver.maximize_window()

'''
#Phones & Button
phones = driver.find_element(By.XPATH,'//a[text()="Phones & PDAs"]')
phones.click()


#Select 2 iPhones
iPhone = driver.find_element(By.XPATH,'//a[text()="iPhone"]')
iPhone.click()
time.sleep(2)

first_pic = driver.find_element(By.XPATH,'//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

next_click = driver.find_element(By.XPATH,'/html/body/div[2]/div/button[2]')
for i in range(0,5):
    next_click.click()
    time.sleep(2)

#Close
Cross = driver.find_element(By.XPATH,'//button[@title="Close (Esc)"]')
Cross.click()
'''

#Screenshot
driver.save_screenshot('ss.png')
screenshot = Image.open('ss.png')
#screenshot.show()

'''
#Quantity
quantity = driver.find_element(By.ID, 'input-quantity')
quantity.click()
time.sleep(1)
quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

add_to_button=driver.find_element(By.ID,'button-cart')
add_to_button.click()
time.sleep(2)
'''

#Laptop
Laptops = driver.find_element(By.XPATH,'//a[text()="Laptops & Notebooks"]')
action= ActionChains(driver)
action.move_to_element(Laptops).perform()
time.sleep(2)
Laptops_2 =driver.find_element(By.XPATH,'//a[text()="Show AllLaptops & Notebooks"]')
Laptops_2.click()

#Click on HP Laptop
HP = driver.find_element(By.XPATH,'//a[text()="HP LP3065"]')
HP.click()

add_to_button_2 = driver.find_element(By.XPATH,'//button[@id="button-cart"]')

add_to_button_2.location_once_scrolled_into_view
time.sleep(1)

#Calender
calendar = driver.find_element(By.XPATH,'//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar = driver.find_element(By.XPATH,'//th[@class="next"]')
month_year=driver.find_element(By.XPATH,'//th[@class="picker-switch"]')

#Year:2022 month
while month_year.text != 'December 2022':
    next_click_calendar.click()

#day 31
calendar_date = driver.find_element(By.XPATH,'//td[text()="31"]')
calendar_date.click()
time.sleep(2)

add_to_button_2.click()
time.sleep(2)

#Go to cart
go_to_cart = driver.find_element(By.ID,'cart-total')
go_to_cart.click()
time.sleep(2)

#View_cart = driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[2]/div/p/a[2]')
#View_cart.click()
#time.sleep(1)

#Remove item from the Shop cart when it is not available

#remove = driver.find_element(By.XPATH,'//i[@class="fa fa-times-circle"]')
#remove.click()

#Click on Check out for guest
check_out = driver.find_element(By.XPATH,'//i[@class="fa fa-share"]')
check_out.click()
time.sleep(1)

#Now click on guest
guest = driver.find_element(By.XPATH,'//input[@value="guest"]')
guest.click()

#Continue
continue_1 = driver.find_element(By.XPATH,'//input[@value="Continue"]')
continue_1.click()
time.sleep(1)

#SCrolling

step_2=driver.find_element(By.XPATH,'//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

#Fill your all personal all details

first_name = driver.find_element(By.ID,'input-payment-firstname')
first_name.click()
first_name.send_keys("John")
time.sleep(1)

last_name = driver.find_element(By.ID,'input-payment-lastname')
last_name.click()
last_name.send_keys("Cena")
time.sleep(1)

email = driver.find_element(By.ID,'input-payment-email')
email.click()
email.send_keys("john.cena@gmail.com")
time.sleep(1)

telephone = driver.find_element(By.ID,'input-payment-telephone')
telephone.click()
telephone.send_keys("+91-78795141904")
time.sleep(1)

address = driver.find_element(By.ID,'input-payment-address-1')
address.click()
address.send_keys("Airen Hieghts Near AB Road,Indore")
time.sleep(1)

city = driver.find_element(By.ID,'input-payment-city')
city.click()
city.send_keys("Indore")
time.sleep(1)

post_code = driver.find_element(By.ID,'input-payment-postcode')
post_code.click()
post_code.send_keys("451020")
time.sleep(1)

country = Select(driver.find_element(By.ID,'input-payment-country'))
country.select_by_visible_text('India')
time.sleep(1)

#Region
region=driver.find_element(By.ID,'input-payment-zone')
dropdown_1=Select(region)
time.sleep(1)
dropdown_1.select_by_visible_text('Madhya Pradesh')

#To be continue
continue_2 = driver.find_element(By.ID,'button-guest')
continue_2.click()
time.sleep(2)

continue_3 = driver.find_element(By.ID,'button-shipping-method')
continue_3.click()
time.sleep(2)

#Accept Terms & Conditions
T_C = driver.find_element(By.XPATH,'//input[@name="agree"]')
T_C.click()
time.sleep(1)

continue_4 = driver.find_element(By.XPATH,'//*[@id="button-payment-method"]')
continue_4.click()
time.sleep(1)

#Final Price
FP = driver.find_element(By.XPATH,'//*[@id="collapse-checkout-confirm"]/div/div[1]/table/tfoot/tr[3]/td[2]')
print("This is the final :" + FP.text)
time.sleep(2)

#Order confirm
OC = driver.find_element(By.XPATH,'//*[@id="button-confirm"]')
OC.click()
time.sleep(2)

#Success
success_text = driver.find_element(By.XPATH,'//*[@id="content"]/h1')
print(success_text.text)
time.sleep(1)

#Screenshot-2
driver.save_screenshot('order.png')
screenshot = Image.open('order.png')
screenshot.show()

#Close Webdriver
driver.close()
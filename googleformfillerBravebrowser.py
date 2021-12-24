from selenium import webdriver
import time, pandas, random
option = webdriver.ChromeOptions()
option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(executable_path='/Users/kski/Downloads/chromedriver', options=option)
driver.implicitly_wait(1)   # implicit wait 1s to poll for missing elements
# CONTROLS HERE:
reporttype = "end" # or "end" / "start"
shifttype = "wfh"  # or "pm" or "wfh"

driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=sJGeMh_i-0igcUVnF-zCjqeywbPDy5dNrFyUot5TnLxUREhPUUVIUFRMMkJINDY4QjVUNVgyVVVMTy4u&qrcode=true")
# time.sleep(4)
datepick = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/input[1]')
datepick.click()
yy = pandas.to_datetime('today').normalize()
datepick.send_keys(yy.strftime('%d/%m/%Y'))
label = driver.find_element_by_xpath('//*[@id="QuestionId_r6c04e3ad6c5e4fd09c875f6ac870c6c7"]/div/div[1]/span[2]')
label.click()
if reporttype == "start":
    reporttiming1st = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/label/input')
elif reporttype == "end":
    reporttiming1st = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/label/input')
reporttiming1st.click()
if shifttype == "am":
    amshift = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/div[2]/input')
elif shifttype == "pm":
    amshift = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/div[3]/input')
elif shifttype == "wfh":
    amshift = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/div[4]/input')
amshift.click()
department = driver.find_element_by_xpath('//*[@id="SelectId_0"]/div')
department.click()
customerservice = driver.find_element_by_xpath('//*[@id="SelectId_0"]/div[2]/div[6]')
customerservice.click()
nameigg = driver.find_element_by_xpath('//*[@id="SelectId_1"]/div')
nameigg.click()
me = driver.find_element_by_xpath('//*[@id="SelectId_1"]/div[2]/div[14]')
me.click()
tempreading = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div/input')
tempreading.click()
tempreading.send_keys(str(round(random.uniform(36.0, 37.3), 1)))
resp = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[7]/div/div[2]/div/div[2]/div/label/input')
resp.click()
submitbutton = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button/div')
submitbutton.click()
time.sleep(2)
driver.close()
# ActionChains(driver).move_to_element(datepick).click().send_keys("24/05/2021").perform()
# ActionChains(driver).move_to_element(reporttiming1st).click().perform()
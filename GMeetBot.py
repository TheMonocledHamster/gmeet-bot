import webbrowser
import time
import math
import pathlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCons
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


email_id,pass_word,meet_code = (open('login-details.txt').read().split('\n'))[:3]
path = pathlib.Path(__file__).parent.absolute() / "chromedriver.exe"


#Give browser perms and disable notifs
the_chrome_options = Options()
the_chrome_options.add_argument("use-fake-device-for-media-stream")
the_chrome_options.add_argument("use-fake-ui-for-media-stream")
the_chrome_options.add_argument("--disable-notifications")
driver=webdriver.Chrome(path, options=the_chrome_options)

#GMeet Login and Join
identifierID = 'identifierId'
PWxpath = '//*[@id="password"]/div[1]/div/div[1]/input'
MBxpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]'
LExpath = '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input'
CAMxpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div'
AUDxpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div'
JOINxpath1 = '//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span'
JOINxpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span'
NUMxpath = '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]'
ENDxpath = '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div/span'
url = 'https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.159644724.887115149.1602468384-1763864472.1602468384&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

driver.get(url)
enterID = driver.find_element_by_id(identifierID)
enterID.send_keys(email_id)
enterID.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
enterPW = driver.find_element_by_xpath(PWxpath)
enterPW.send_keys(pass_word)
enterPW.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
click2Enter = driver.find_element_by_xpath(MBxpath)
click2Enter.click()
driver.implicitly_wait(10)
enterLink = driver.find_element_by_xpath(LExpath)
enterLink.send_keys(meet_code)
enterLink.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
camButton = driver.find_element_by_xpath(CAMxpath)
camButton.click() #Cam Off
audioButton = driver.find_element_by_xpath(AUDxpath)
audioButton.click() #Mic Off
driver.implicitly_wait(10)
ignore = (NoSuchElementException,StaleElementReferenceException)
joinMeet = WebDriverWait(driver,15,ignored_exceptions=ignore).until(ExpCons.element_to_be_clickable((By.XPATH,JOINxpath)))
joinMeet.click() #Meet Joined
driver.implicitly_wait(10)
studentsHere = WebDriverWait(driver,10,ignored_exceptions=ignore).until(ExpCons.element_to_be_clickable((By.XPATH,NUMxpath)))
attend_count = int(studentsHere.text)
driver.implicitly_wait(10)

while True:
	changed_count = int(studentsHere.text)
	if changed_count > attend_count :
		attend_count = changed_count
	elif changed_count <= round(0.25*attend_count):
		EndCall = driver.find_element_by_xpath(ENDxpath)
		EndCall.click()
		break
driver.quit()
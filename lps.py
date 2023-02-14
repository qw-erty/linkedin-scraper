from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Replace the path with the location where your ChromeDriver is installed
driver = webdriver.Chrome('F:\installations\chromedriver_win32\chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Replace the LinkedIn profile URL with your own LinkedIn profile URL
url = 'https://www.linkedin.com/in/abcd/'

driver.get(url)

# Set the maximum amount of time to wait for the page to load (in seconds)
wait_time = 20

# Wait for the page to load
driver.implicitly_wait(20)

try:     
    wait = WebDriverWait(driver, wait_time)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#public_profile_contextual-sign-in > div > section > button")))
except:
    print("cross not found reload")


# Click the button using its CSS selector
driver.find_element(By.CSS_SELECTOR,'#public_profile_contextual-sign-in > div > section > button').click()


# Click the button using its JavaScript path
# button = driver.execute_script('return document.querySelector("#public_profile_contextual-sign-in > div > section > button")')
# button.click()

# Find and print the name on the profile
name = driver.find_element(By.CSS_SELECTOR,'#main-content > section.core-rail.mx-auto.papabear\:w-core-rail-width.mamabear\:max-w-\[790px\].babybear\:max-w-\[790px\] > div > section > section.top-card-layout.container-lined.overflow-hidden.babybear\:rounded-\[0px\] > div > div.top-card-layout__entity-info-container.flex.flex-wrap.papabear\:flex-nowrap > div:nth-child(1) > h1')
print('Name:', name.text)

# Find and print the headline on the profile
headline = driver.find_element(By.CSS_SELECTOR,'#main-content > section.core-rail.mx-auto.papabear\:w-core-rail-width.mamabear\:max-w-\[790px\].babybear\:max-w-\[790px\] > div > section > section.top-card-layout.container-lined.overflow-hidden.babybear\:rounded-\[0px\] > div > div.top-card-layout__entity-info-container.flex.flex-wrap.papabear\:flex-nowrap > div:nth-child(1) > h2')
print('Headline:', headline.text)

# Find and print the location on the profile
location = driver.find_element(By.CSS_SELECTOR,'#main-content > section.core-rail.mx-auto.papabear\:w-core-rail-width.mamabear\:max-w-\[790px\].babybear\:max-w-\[790px\] > div > section > section.top-card-layout.container-lined.overflow-hidden.babybear\:rounded-\[0px\] > div > div.top-card-layout__entity-info-container.flex.flex-wrap.papabear\:flex-nowrap > div:nth-child(1) > h3 > div')
print('location:', location.text)

# Scroll down to the end of the page
# scroll_pause_time = 1
# screen_height = driver.execute_script("return window.screen.height;")
# i = 1
# while True:
#     # Scroll down to the bottom of the page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
#     # Wait to load the page
#     driver.implicitly_wait(scroll_pause_time)
    
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == screen_height:
#         break
#     else:
#         screen_height = new_height
#         i += 1

# # Print the total number of scrolls performed
# print("Total Scrolls: ", i)

wait = WebDriverWait(driver, wait_time)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main-content > section.core-rail.mx-auto.papabear\:w-core-rail-width.mamabear\:max-w-\[790px\].babybear\:max-w-\[790px\] > div > section > section.core-section-container.my-3.core-section-container--with-border.border-b-1.border-solid.border-color-border-faint.m-0.py-3.pp-section.experience > div > ul")))


# Find and print the experience on the profile
experienceList = driver.find_element(By.CSS_SELECTOR, "#main-content > section.core-rail.mx-auto.papabear\:w-core-rail-width.mamabear\:max-w-\[790px\].babybear\:max-w-\[790px\] > div > section > section.core-section-container.my-3.core-section-container--with-border.border-b-1.border-solid.border-color-border-faint.m-0.py-3.pp-section.experience > div > ul")
experience = experienceList.find_elements(By.TAG_NAME,'li')
# print('experience:', experience)

# properties = dir(experience[0])
# print(properties)

for element in experience:
    
    title = element.find_element(By.CLASS_NAME, "profile-section-card__title")
    print("title: ", title.text)

    subTitle = element.find_element(By.CLASS_NAME, "profile-section-card__subtitle")
    print("subTitle: ", subTitle.text)

    description = element.find_element(By.CLASS_NAME, "show-more-less-text")
    print("description: ", description.text)

    try:
        duration = element.find_element(By.CLASS_NAME, "experience-item__duration")
        print("duration: ", duration.text)

    except: 
        
        duration = element.find_element(By.CLASS_NAME, "experience-group-position__duration")
        print("duration: ", duration.text)

        


    
# Close the browser
driver.quit()

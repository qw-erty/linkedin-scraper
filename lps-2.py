import time
import csv

start = time.time()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service1 = Service(r"F:\installations\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless')

driver = webdriver.Chrome(service=service1 , options=options )

# Assuming your CSV file has a header row
file_path = 'linkedin.csv'

def read_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            yield row

# Read data from CSV file
data_generator = read_csv(file_path)

# Skip header row
header = next(data_generator)

urls = []

count = 0

# authentication
driver.get("https://www.linkedin.com/login")

# enter username
driver.find_element(By.CSS_SELECTOR,'#username').send_keys("gevirok694@semonir.com")

# enter password
driver.find_element(By.CSS_SELECTOR,'#password').send_keys("SuuNaaMii1234$$")


# click on login button
driver.find_element(By.TAG_NAME,'button').click()

# driver.implicitly_wait(20)

#csv data in loop
for row in data_generator:
    count +=1 
    urls.append(row[0])

for url in urls:
    print(url)

    # url = 'https://www.linkedin.com/in/abhinav-aggrawal-aa97b6201/?original_referer=&challengeSource=AgEgtS3I2d_B1AAAAYlYj5G7RoubeStsEP3LUHXe0xRGyC67hj24kx3i_SGd4HU&challegeType=AgEGqMWib90TzAAAAYlYj5G-a30K25l3GjyaeiBNPlkd0ni-i_809Y8&memberId=AgGrNP6bjztR5wAAAYlYj5HBx8MRi0LjNWj5VdcMelt-IMY&recognizeDevice=AgGZRpMtmuYi-QAAAYlYj5HF8vgbqm8k-k7ha9JkIAPLwCLyZwXQ&challengeId=AQEzfuCP_Us96wAAAYlYlC-xId61UgItC51tW0FGsKLkf58FwfGiKCeqDYKZakgXCAcy4qiynSr_ziAMjrD7CcgJG-KX4uyRSQ&submissionId=b897f50d-dbfb-7117-f935-aecdf63e5815&challengeSource=AgFbpWrCAYmMDAAAAYlYlLKAkRmDF05XcNuEibsGY3xbeHJDLht1bsGiWwGqSqU&challegeType=AgFbEi6QGzG1tQAAAYlYlLKEJv-L6mGhmTjq4g_ssTIsa2tytu8hXMQ&memberId=AgGuBvN0oqlaWwAAAYlYlLKHq9HOVvAn7BVjG3-fpE_nUII&recognizeDevice=AgHEOMT-JaKAqQAAAYlYlLKLw-posj2EIY8VqPaJS-gqGIcchG8g'

    driver.get(url)

    # Set the maximum amount of time to wait for the page to load (in seconds)
    # wait_time = 30

    # Wait for the page to load
    driver.implicitly_wait(2)

    # try:     
    #     wait = WebDriverWait(driver, wait_time)
    #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#public_profile_contextual-sign-in > div > section > button")))
    # except:
    #     print("cross not found reload")


    driver.find_element(By.CSS_SELECTOR,'#public_profile_contextual-sign-in > div > section > button').click()

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
    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1
    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait to load the page
        driver.implicitly_wait(scroll_pause_time)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == screen_height:
            break
        else:
            screen_height = new_height
            i += 1

    # Print the total number of scrolls performed
    print("Total Scrolls: ", i)

    wait = WebDriverWait(driver, wait_time)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main-content > section.core-rail.mx-auto.papabear\:w-core-rail-width.mamabear\:max-w-\[790px\].babybear\:max-w-\[790px\] > div > section > section.core-section-container.my-3.core-section-container--with-border.border-b-1.border-solid.border-color-border-faint.m-0.py-3.pp-section.experience > div > ul")))

    # Find and print the experience on the profile
    experienceList = driver.find_element(By.CSS_SELECTOR, "#main-content > section.core-rail.mx-auto.papabear\:w-core-rail-width.mamabear\:max-w-\[790px\].babybear\:max-w-\[790px\] > div > section > section.core-section-container.my-3.core-section-container--with-border.border-b-1.border-solid.border-color-border-faint.m-0.py-3.pp-section.experience > div > ul")
    experience = experienceList.find_elements(By.TAG_NAME,'li')

    for element in experience:
        
        title = element.find_element(By.CLASS_NAME, "profile-section-card__title")
        print("title: ", title.text)

        subTitle = element.find_element(By.CLASS_NAME, "profile-section-card__subtitle")
        print("subTitle: ", subTitle.text)

        try:
            description = element.find_element(By.CLASS_NAME, "show-more-less-text")
            print("description: ", description.text)
        except:
            print("description: NA")

        try:
            duration = element.find_element(By.CLASS_NAME, "experience-item__duration")
            print("duration: ", duration.text)

        except: 
            
            duration = element.find_element(By.CLASS_NAME, "experience-group-position__duration")
            print("duration: ", duration.text)

    end1 = time.time()
    print(end1 - start)        

# Close the browser
driver.quit()

end = time.time()
print(end - start)
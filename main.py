from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Provide link for a linkedin job page
driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=100025096&keywords=juniro%20python%20developer&location=Toronto%2C%20Ontario%2C%20Canada')
driver.maximize_window()
login_button = driver.find_element_by_link_text('Sign in')
login_button.click()

# Provide login credentials
login_id = driver.find_element_by_id("username")
login_id.send_keys("youremail@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("yourpassword")
sign_in_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.send_keys(Keys.ENTER)

# Provide a particular job title
desired_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in desired_jobs:
    print("called")
    job.click()
    time.sleep(2)
    # Searching for Easy Apply
    try:
        apply_button = driver.find_element_by_css_selector('.jobs-s-apply button')
        apply_button.click()
        time.sleep(5)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If there is Next instead of Submit, we are skipping since its a multi-step applicaton.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
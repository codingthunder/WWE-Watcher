from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#wd = None

class url_has_changed(object):
    def __init__(self, correct_url):
        self.correct_url = correct_url
    
    def __call__(self,driver):
        try:
            if self.correct_url not in driver.current_url:
                return driver.current_url
            else:
                return False
        except:
            return True



def open_browser(profilePath : str = None):
    if profilePath is not None:
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=" + profilePath)
        return webdriver.Chrome(chrome_options=options)
    
    return webdriver.Chrome()
   

def go_to_page(driver, newUrl):
    if driver is None:
        return False
    driver.get(newUrl)
    return True

def wait_for_url_to_change(driver):
    wait = WebDriverWait(driver, 20000)
    result = wait.until(url_has_changed(driver.current_url),"What were you watching that you had the video on for so long?")
    return result

# def window_is_open(driver):
#     DISCONNECTED_MSG = 'Unable to evaluate script: disconnected: not connected to DevTools\n'

#     logs = driver.get_log('driver')

#     if len(logs) == 0:
#         return True

#     if driver.get_log('driver')[-1]['message'] == DISCONNECTED_MSG:
#         return False
    
#     return True



#driver = webdriver.Chrome()

#url = dataframe1.

# driver.get("http://www.python.org")

# assert "Python" in driver.title

# elem = driver.find_element(By.NAME, "q")

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

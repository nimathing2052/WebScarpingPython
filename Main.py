from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ExtractText import ExtractText
from FileWriter import FileWriter


class Main:
    def __init__(self, url):
        self.url = url
        
    def run(self):
        # initialize the Chrome driver with WebDriver Manager
        driver = webdriver.Chrome(ChromeDriverManager().install())

        try:
            # go to the URL
            driver.get(self.url)
            driver.maximize_window()
            
            # wait for the consent pop-up to appear
            try:
                pop_up = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Close']")))
                # click the close button to dismiss the pop-up
                pop_up.click()

            except:
                # handle exception if the pop-up does not appear
                print("Consent pop-up did not appear")

            time.sleep(5)
            print('Pop-up successfully cleared')

            driver.execute_script("window.scrollTo(0, 500)") #scroll down
            time.sleep(1)

            # get the list of names and labels
            xpath_getter = ExtractText(driver)
            names = xpath_getter.get_names()
            labels = xpath_getter.get_labels()

            # create a CSV file with Name and Label
            file_writer = FileWriter('data.csv', names, labels)
            file_writer.write_file()

        except Exception as e:
            print("Sorry, something went wrong:", e)

        finally:
            # close the driver
            driver.quit()

if __name__ == '__main__':
    program = Main("https://microdata.worldbank.org/index.php/catalog/4684/data-dictionary/F1?file_name=micro_npl.dta")
    program.run()

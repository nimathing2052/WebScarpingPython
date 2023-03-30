from selenium.webdriver.common.by import By

class ExtractText:
    def __init__(self, driver):
        self.driver = driver
        
    def get_names(self):
        name_elems = self.driver.find_elements(By.XPATH, "//div[@class='container-fluid table-variable-list data-dictionary ']//a[@class='var-id text-break']")
        return [elem.text for elem in name_elems]
        
    def get_labels(self):
        label_elems = self.driver.find_elements(By.XPATH, "//div[@class='container-fluid table-variable-list data-dictionary ']//a[@class='var-id']")
        return [elem.text for elem in label_elems]
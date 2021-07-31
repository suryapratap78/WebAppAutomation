from selenium import webdriver


class BasePage():

    def inputInTextbox(self, locator, value):
        self.locator = locator
        self.value = value
        self.locator.click()
        self.locator.clear()
        self.locator.send_keys(self.value)

    def clickButton(self, locator):
        self.locator = locator
        self.locator.click()


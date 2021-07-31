
from pageObjects.TestBasePage import BasePage

class SASLoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # SAS Login Page locators
    textbox_username_id = 'Logon_UserID_TextBox'
    textbox_password_id = 'Logon_OTP_TextBox'
    button_login_id = 'Logon_Button'
    text_loginerror_id = 'Logon_ErrorMsgPanel_ErrorMsgPanel_ErrorMsg_Label'

    # SAS Page header locators
    sasLogoutButtonId = "Header_Header_Logout_ImageButton"
    sasWelcomeTextID = "Header_Header_Welcome_Label"

    def sasLogin(self, testusername, testpassword):
        self.inputInTextbox(self.driver.find_element_by_id(self.textbox_username_id), testusername)
        self.inputInTextbox(self.driver.find_element_by_id(self.textbox_password_id), testpassword)
        self.clickButton(self.driver.find_element_by_id(self.button_login_id))

    def sasLogout(self):
        self.clickButton(self.driver.find_element_by_id(self.sasLogoutButtonId))

    def getWelcomeText(self):
        self.welcomeText = self.driver.find_element_by_id(self.sasWelcomeTextID)
        print("----- "+self.welcomeText.text+" -----this is the value of welcome text")
        return self.welcomeText.text

    def getLoginErrorText(self):
        self.loginErrorText = self.driver.find_element_by_id(self.text_loginerror_id)
        print("----- "+self.loginErrorText.text+" -----this is the value of Login Error text")
        return self.loginErrorText.text
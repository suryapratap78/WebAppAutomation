import pytest
import json
import time
from selenium import webdriver
from pageObjects.SASLoginPage import SASLoginPage
from utilities.customLogger import LogGen

class Test_001_Login:
    logger = LogGen.loggen()
    testFile = open("./Configurations/testConfig.json")
    jsonData = json.load(testFile)

    @pytest.mark.sanity
    def test_validSasLogin(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started SAS Valid Login test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.jsonData['sasConsoleClassicUrl'])

        self.sasloginpage = SASLoginPage(self.driver)
        self.sasloginpage.sasLogin(self.jsonData['sasChildOperator'], self.jsonData['sasChildOpPass'])

        if self.sasloginpage.getWelcomeText() == self.jsonData['loginSuccessHeader']:
            self.logger.info("\n valid login scenario has been tested successfully *********")
            assert True
        else:
            self.logger.error("****Valid Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sasValidLoginFailure_{}.png".format(time.time()))
            assert False

    @pytest.mark.sanity
    def test_invalidSasLogin(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.jsonData['sasConsoleClassicUrl'])

        self.sasloginpage = SASLoginPage(self.driver)
        self.sasloginpage.sasLogin(self.jsonData['sasInvalidOp'], self.jsonData['sasChildOpPass'])

        if self.sasloginpage.getLoginErrorText() == self.jsonData['loginErrorMessage']:
            print("\n valid login scenario has been tested successfully *********")
            assert True
        else:
            self.logger.error("****SAS Invalid Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sasInvalidLoginFailure_{}.png".format(time.time()))
            assert False
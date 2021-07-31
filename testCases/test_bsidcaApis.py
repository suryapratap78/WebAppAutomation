import sys, os
import json
import unittest
#import HtmlTestRunner
import requests
import string
import random
import pytest

from pageObjects.ApiBodyPage import BsidcaSoapBodies
from utilities.customLogger import LogGen

class BsidcaTests(unittest.TestCase):   #Automation of SOAP APIs

    @classmethod
    def setUpClass(cls):
        frozen = 'not'
        # import testData.json
        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            frozen = 'ever so'
            bundle_dir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

        print('we are', frozen, 'frozen')
        cls.testFile = open("../Configurations/testConfig.json")
        cls.jData = json.load(cls.testFile)
        cls.logger = LogGen.loggen()

        cls.url = "http://{}/bsidca/bsidca.asmx?WSDL".format(cls.jData['sasBaseUrl'])
        cls.headers = {'content-type': 'application/soap+xml'}
        cls.connect_body = BsidcaSoapBodies.connectApi_body.format(cls.jData['sasRootOperatorName'],
                                                                   cls.jData['sasRootOperatorPass'])
        cls.connect_response = requests.post(cls.url, data=cls.connect_body, headers=cls.headers)

        print(cls.connect_response.headers)

        cls.headers.update(cookie=cls.connect_response.headers['Set-Cookie'])
        cls.logger.info("==============All set to execute BSIDCA APIs==============")

    #@pytest.mark.sanity
    def test_addGroupApi(self):
        soap_group = "soapGroup_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        print(soap_group)
        self.addGroup_body = BsidcaSoapBodies.addGroupApi_body.format(soap_group, self.jData['sasSanityaccount'])
        self.logger.info("==============Running add group API test==============")
        self.addGroup_response = requests.post(self.url, data=self.addGroup_body, headers=self.headers)
        print("________add group reponse___________",self.addGroup_response)
        if self.addGroup_response.status_code == 200:
            self.logger.info("==============created soap group==============" + soap_group)
        else:
            self.logger.info("==============Group creation failed==============")
        assert self.addGroup_response.status_code == 200, "Groups weren't created, test failed"

  

    @classmethod
    def tearDownClass(cls):
        cls.testFile.close()


if __name__ == '__main__':
    unittest.main()
    """if getattr(sys, 'frozen', False):
        print("running through installer")
        report_path = "\HtmlReport"
    elif __file__:
        print("running through script")
        report_path = "./Reports"
    print("caculated path for reports folder ")
    print(report_path)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path))"""

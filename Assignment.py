import unittest
from appium import webdriver as mobile_driver


class SiteOpening_tests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['avd'] = "Pixel_XL_API_26"
        desired_caps['avdLaunchTimeout'] = 90000
        #desired_caps['adbExecTimeout'] = 50000
        # options.set_capability("androidPackage", "com.android.chrome")
        # options.setExperimentalOption("androidPackage", "com.android.chrome");
        # desired_caps['appPackage'] = "com.android.chrome"
        # desired_caps['appActivity'] = "com.google.android.apps.chrome.Main"
        desired_caps['browserName'] = "Chrome"
        self.driver = mobile_driver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_clickCrome(self):
        print("Running")
        driver=self.driver
        driver.implicitly_wait(10)
        driver.get("http://qainfotech.com")
        title=driver.title
        self.assertEqual("QA InfoTech | Your Software Testing Partner", title)
        print(title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SiteOpening_tests)
    unittest.TextTestRunner(verbosity=0).run(suite)
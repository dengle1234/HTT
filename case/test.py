import pytest
from selenium import webdriver
from page.login_page import LoginPage
from common.log import Log
from selenium.webdriver.chrome.service import Service


class TestLogin:
    # 登录
    #
    # def setup_class(self):
    #     Log.right_log("-------用例前置工作：打开浏览器--------")
    #     try:
    #         self.driver = webdriver.Chrome(
    #             service=Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'))
    #     except:
    #         raise ValueError('浏览器驱动异常')
    #     else:
    #         self.driver.get('http://39.108.0.214:4042/account/login')
    #         self.driver.maximize_window()
    #         self.page = LoginPage(self.driver)
    #
    # def teardown_class(self):
    #     self.driver.quit()
    #     Log.right_log("-------用例后置工作：关闭浏览器--------")

    @pytest.mark.run(order=2)
    def test_loginUI01(self, ):
        a = 1
        print('-----测试-----1')
        assert a == 1

    @pytest.mark.run(order=1)
    def test_loginUI02(self, ):
        a = 1
        print('-----测试-----2')
        assert a == 1


if __name__ == '__main__':
    pytest.main(['-s', 'test.py'])

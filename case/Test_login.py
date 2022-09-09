import pytest
from selenium import webdriver
from page.login_page import LoginPage
from common.log import Log
from selenium.webdriver.chrome.service import Service


class TestLogin:
    # 登录

    def setup_class(self):
        Log.right_log("-------用例前置工作：打开浏览器--------")
        try:
            self.driver = webdriver.Chrome(
                service=Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'))
        except:
            raise ValueError('浏览器驱动异常')
        else:
            self.driver.get('http://39.108.0.214:4042/account/login')
            self.driver.maximize_window()
            self.page = LoginPage(self.driver)

    def teardown_class(self):
        self.driver.quit()
        Log.right_log("-------用例后置工作：关闭浏览器--------")

    """冒烟测试标记"""
    # @pytest.mark.run(order=2)
    @pytest.mark.parametrize("case_id, name, pwd, assertion_tips",
                             [("UI-0011", "", '', '必填项不能为空'),
                              ("UI-0012", "test01", '', '必填项不能为空'),
                              ("UI-0013", "test01", '123456', '帐号或密码不正确！'),
                              ("UI-0014", "test011", '666666', '帐号或密码不正确！'),
                              ("UI-0015", "test03", '6666666', '帐号或密码不正确！')])
    def test_login_UI_01(self, case_id, name, pwd, assertion_tips):
        """
        海拓通用户登录,异常登录测试
        :param case_id: 用例编号
        :param name: 用户名
        :param pwd: 密码
        :param assertion_tips: 断言内容
        """
        # 模块:登录功能
        text = self.page.page_operation(name, pwd)
        # 断言.....
        assert text == assertion_tips

    @pytest.mark.parametrize("case_id, name, pwd, assertion_tips, userid",
                             [("UI-0016", "test01", '666666', '登录成功！', 'TEST01')])
    # @pytest.mark.run(order=1)
    def test_login_UI_02(self, case_id, name, pwd, assertion_tips, userid):
        """
        海拓通用户登录
        :param case_id: 用例编号
        :param name: 用户名
        :param pwd: 密码
        :param assertion_tips: 断言内容
        :param userid: 用户代码
        """
        # 模块:登录功能
        info = self.page.page_operation(name, pwd)
        # 断言.....
        assert info[0] == assertion_tips
        assert info[1] == userid


if __name__ == '__main__':
    pytest.main(['-s', 'Test_login.py::test_login_UI_02'])

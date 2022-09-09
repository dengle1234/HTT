import pytest
from selenium import webdriver
from page.register_page import RegisterPage
from common.log import Log
from selenium.webdriver.chrome.service import Service
# 随机数生成
import random


class TestRegister:
    # 注册
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
            self.page = RegisterPage(self.driver)
            self.page.page_switch()

    def teardown_class(self):
        self.driver.quit()
        Log.right_log("-------用例后置工作：关闭浏览器--------")

    """冒烟测试标记"""

    @pytest.mark.smoke
    @pytest.mark.parametrize("case_id, phone, pwd, pwd2, company_name, assertion_tips",
                             [('UI-0001', '', '', '', '', '必填项不能为空'),
                              ('UI-0002', '15818889999', '', '', '', '必填项不能为空'),
                              ('UI-0003', '15818889999', '666666', '', '', '必填项不能为空'),
                              ('UI-0004', '15818889999', '666666', '123456', '', '两次密码输入不一致！'),
                              ('UI-0005', '15888888888', '666666', '666666', '', '请勾选协议！'),
                              ('UI-0006', '1581856732', '666666', '666666', '', '请输入正确的手机号'),
                              ('UI-0006', '158abc56851', '666666', '666666', '', '请输入正确的手机号'),
                              ('UI-0006', '158185673221', '666666', '666666', '', '请输入正确的手机号'),
                              ('UI-0006', '1581856965！', '666666', '666666', '', '请输入正确的手机号'),
                              ('UI-0007', '15818567323', '666666', '666666', '', '手机号已被注册，可直接登录！'),
                              ('UI-0008', '15818889999', '666666666666666', '666666666666666', '', '密码必须6到12位，且不能出现空格'),
                              ('UI-0009', '15818889999', '66666', '66666', '', '密码必须6到12位，且不能出现空格'),
                              ('UI-0010', '15818889999', '666 666', '666 666', '', '密码必须6到12位，且不能出现空格'),
                              ('UI-0011', '158' + str(random.randint(10000000, 99999999)), '666666', '666666',
                               '测试公司' + str(random.randint(10000000, 99999999)), '注册成功！')])
    def test_register_UI_01(self, case_id, phone, pwd, pwd2, company_name, assertion_tips):
        """
        海拓通用注册
        :param case_id: 用例编号
        :param phone: 手机号
        :param pwd: 密码
        :param pwd2: 确认密码
        :param company_name pwd: 公司名称
        :param assertion_tips: 断言内容
        """
        # 模块:登录功能
        text = self.page.page_operation(phone, pwd, pwd2, company_name)
        # 断言.....
        assert text == assertion_tips

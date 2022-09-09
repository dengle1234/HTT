import time

import pytest
from selenium import webdriver
from page.Warehousing_prediction_page import PredictionBoxPage
from common.log import Log
from selenium.webdriver.chrome.service import Service
from page.login_page import LoginPage
import os

# 随机数生成
import random


class TestPrediction:
    # 中转入库入库预报

    def setup_class(self):
        # 类级别初始化
        try:
            self.driver = webdriver.Chrome(
                service=Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'))
        except:
            raise ValueError('浏览器驱动异常')
        else:
            self.driver.get('http://39.108.0.214:4042/account/login')
            self.driver.maximize_window()
            self.page = LoginPage(self.driver)
            self.page.page_operation('test01', '666666')
            self.page2 = PredictionBoxPage(self.driver)
            Log.right_log("-------类前置工作：打开浏览器--------")

    def teardown_class(self):
        # 类级别初始化
        self.driver.quit()
        Log.right_log("-------类后置工作：关闭浏览器--------")

    def setup_method(self):
        # 方法级别的初始化
        self.driver.refresh()
        Log.right_log("-------用例前置工作：刷新浏览器--------")

    def teardown_method(self):
        # 方法级别的初始化
        pass

    """冒烟测试标记"""

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("case_id, number_order, re, number_box, zy_box_name, zy_box_patch",
                             [('UI-0024-1', 'ZZRK-1', '入库测试1', '1', 'ZY001', '1'),
                              ('UI-0024-2', 'ZZRK-2', '入库测试2', '10', 'ZY005', '5')])
    def test_prediction_UI_01(self, case_id, number_order, re, number_box, zy_box_name, zy_box_patch):
        print('------test_prediction_UI_01-----')
        """
        创建中转入库单-正常
        :param case_id: 用例编号
        :param number_order: 客户订单号
        :param re: 备注
        :param number_box: 入库预报箱数
        :param zy_box_name: 自有箱号
        :param zy_box_patch: 填写自有箱号位置
        """
        # 模块:入库预报
        info = self.page2.page_operation_right(number_order, re, number_box, zy_box_name, zy_box_patch)
        # # 断言.....
        assert info[0] == info[1]  # 订单号对比
        assert info[2] == '待入库'  # 状态对比
        info[4].reverse()  # 列表倒序
        assert info[3] == info[4]  # 箱号对比

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("case_id, number_box, box_type, country, warehouse, now_time, assert_tips",
                             [('UI-0017', '0', '', '', '', '', '请输入正确的整数！'),
                              ('UI-0018', '1', '', '', '', '', '请选择箱子属性！'),
                              ('UI-0019', '201', '普货', '', '', '', '最多生成200个箱子！'),
                              ('UI-0020', '1', '普货', '', '', '', '请选择国家！'),
                              ('UI-0021', '1', '普货', '美国', '', '', '请选择仓库！'),
                              ('UI-0022', '1', '普货', '美国', '波特兰仓库', '', '请选择预计到货时间！'),
                              ('UI-0023', '1', '普货', '美国', '波特兰仓库', '当前时间', '创建成功')])
    def test_prediction_UI_02(self, case_id, number_box, box_type, country, warehouse, now_time, assert_tips):
        print('------test_prediction_UI_02-----')
        """
        创建中转入库单-异常
        :param case_id: 用例ID
        :param number_box: 箱子数
        :param box_type: 箱子属性
        :param country: 国家
        :param warehouse: 仓库
        :param now_time: 时间
        :param assert_tips: 断言
        """
        # 模块:入库预报
        info = self.page2.page_operation_Required(number_box, box_type, country, warehouse, now_time)
        # # 断言.....
        if case_id != 'UI-0023':
            assert info == assert_tips
        else:
            assert info[0] == info[1]  # 订单号对比
            assert info[2] == '待入库'  # 状态对比
            info[4].reverse()  # 列表倒序
            assert info[3] == info[4]  # 箱号对比


if __name__ == '__main__':
    # pytest.main(["-s","allure-test.py"])
    '''
    -q: 安静模式, 不输出环境信息
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -s: 显示程序中的print/logging输出
    '''
    pytest.main(['-s', '-q', 'Test_Warehousing_prediction.py', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate -c -o allure-report")
    print(os.getcwd())
    os.system("allure serve ./allure-results")

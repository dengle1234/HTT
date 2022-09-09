# basepage.py
import os
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import Log
from common.constant import IMG_DIR
from selenium.webdriver.support.ui import Select  # select 下拉框


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, loc, img_desc, timeout=20, frequency=0.5):
        """等待元素可见"""
        try:
            """判断是否可见返回布尔值"""
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            Log.right_log("等待:{} - 元素{}可见成功。".format(img_desc, loc))
        except:
            Log.exception_log("等待:{} - 元素{}可见失败！".format(img_desc, loc))
            self.save_img(img_desc)
            raise ValueError("元素查找失败,或不可使用")

    def get_element(self, loc, img_desc):
        """查找元素"""
        try:
            ele = self.driver.find_element(*loc)
        except:
            Log.exception_log("查找:{} - 元素{}失败！".format(img_desc, loc))
            self.save_img(img_desc)
            raise
        else:
            Log.right_log("查找:{} - 元素{}成功".format(img_desc, loc))
            return ele

    def get_elements(self, loc, img_desc):
        """查找元素,返回多个"""
        try:
            ele = self.driver.find_elements(*loc)
        except:
            Log.exception_log("查找:{} - 元素{}失败！".format(img_desc, loc))
            self.save_img(img_desc)
            raise
        else:
            Log.right_log("查找:{} - 元素{}成功".format(img_desc, loc))
            return ele

    def get_text(self, loc, img_desc, timeout=20, frequency=0.5):
        """获取元素内容"""
        self.wait_ele_visible(loc, img_desc, timeout, frequency)
        ele = self.get_element(loc, img_desc)
        try:
            text = ele.text
            Log.right_log("获取:{} - 元素{}内容获取成功".format(img_desc, loc))
        except:
            Log.exception_log("获取:{} - 元素{}内容获取失败！".format(img_desc, loc))
            self.save_img(img_desc)
        else:
            return text

    def click_element(self, loc, img_desc, timeout=20, frequency=0.5):
        """点击元素"""
        self.wait_ele_visible(loc, img_desc, timeout, frequency)
        ele = self.get_element(loc, img_desc)
        try:
            ele.click()
            Log.right_log("点击:{} - 元素{}成功".format(img_desc, loc))
        except:
            Log.exception_log("点击:{} - 元素{}失败！".format(img_desc, loc))
            self.save_img(img_desc)
            raise

    def input_text(self, loc, value, img_desc, timeout=20, frequency=0.5):
        """在元素中输入文本"""
        self.wait_ele_visible(loc, img_desc, timeout, frequency)
        ele = self.get_element(loc, img_desc)
        try:
            ele.clear()
            ele.send_keys(value)
            Log.right_log("输入：在{} - 元素{}输入文本值({})成功".format(img_desc, loc, value))
        except:
            Log.exception_log("输入：在{} - 元素{}输入文本值({})失败！".format(img_desc, loc, value))
            self.save_img(img_desc)
            raise

    def select_element(self, loc, mode, text, img_desc, timeout=20, frequency=0.5):
        """选项"""
        self.wait_ele_visible(loc, img_desc, timeout, frequency)
        sel = Select(self.driver.find_element(*loc))
        try:
            if mode == 'text':
                sel.select_by_visible_text(text)
            elif mode == 'value':
                sel.select_by_visible_text(text)
            else:
                sel.select_by_index()
        except:
            Log.exception_log("选择{} - 元素{}中的选项({})失败！".format(img_desc, loc, text))
            self.save_img(img_desc)
            raise

    def save_img(self, img_description):
        """保存异常截图"""
        now = time.strftime("%Y-%m-%d %H-%M-%S ", time.localtime())
        """层级-目录-时间+名称"""
        img_path = os.path.join(IMG_DIR, now + img_description + '.png')
        try:
            self.driver.save_screenshot(img_path)
        except:
            Log.exception_log("异常截图失败！")
        else:
            Log.right_log("异常截图成功，截图存放在{}".format(img_path))

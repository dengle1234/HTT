import time


class Log:

    @staticmethod
    def right_log(text):
        """正常日志"""
        try:
            f = open(r'D:\demo\HTT-Selenium\log\log.txt', 'a', encoding='utf-8')
        except:
            raise ValueError("日志文件路径错误,请检查")
        else:
            now = time.strftime("%Y-%m-%d %H-%M-%S ", time.localtime())
            f.write(now + '   ' + text + "\n")
            f.close()

    @staticmethod
    def exception_log(text):
        """异常日志"""
        try:
            f = open(r'D:\demo\HTT-Selenium\log\log.txt', 'a', encoding='utf-8')
        except:
            raise ValueError("日志文件路径错误,请检查")
        else:
            now = time.strftime("%Y-%m-%d %H-%M-%S ", time.localtime())
            f.write(now + '   ' + text + "\n")
            f.close()

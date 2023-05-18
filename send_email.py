import unittest
#from HTMLTestRunner import HTMLTestRunner
from unittestreport import TestRunner


from unittestreport import TestRunner

if __name__ == "__main__":
    # 测试用例目录
    test_dir = r"D:\auto\AutoTest\Launcher_test"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir,'test_main.py')
    # 测试报告路径
    report_path = r"D:\Program Files\report\report.html"
    with open(report_path, "wb") as report:
        suite = unittest.TestSuite()
        runner = TestRunner(discover,
                            filename="report.html",
                            report_dir=".",
                            title="unittestreport测试报告",
                            tester="王建程",
                            desc="Launcher测试报告")
        runner.run()

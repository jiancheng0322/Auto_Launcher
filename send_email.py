import unittest
from unittestreport import TestRunner
import datetime
from bs4 import BeautifulSoup
import test_main
import sqltest
import sftp
import HTMLTestRunner
import urllib

"""
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(demo.MyTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # 获取测试用例的数量
    print(f"Number of tests: {result.testsRun}")

    # 获取失败和错误的测试用例
    for test, error in result.failures:
        print(f"Failed test: {test}\nError: {error}")
    for test, error in result.errors:
        print(f"Errored test: {test}\nError: {error}")   

    # 获取所有测试用例是否通过
    print(f"All tests passed: {not result.failures and not result.errors}")
"""

if __name__ == "__main__":

    # suite = unittest.TestLoader().loadTestsFromTestCase(test_main.MyTest)
    # 测试用例目录
    test_dir = r"D:\auto\AutoTest\Launcher_test"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, 'test_new.py')
    # 测试报告路径
    report_path = r"D:/Program Files/report/report.html"
    time = datetime.datetime.now()
    file = time.strftime('%Y_%m_%d_%H_%M') + '.html'
    with open(report_path, "wb") as report:
        suite = unittest.TestSuite()
        runner = TestRunner(discover,
                            filename=file,
                            report_dir=".",
                            title="launcher测试报告",
                            tester="wangjiancheng",
                            desc="Launcher测试报告",
                            templates=2)
        result = runner.run()
        local_file = file
        remote_path = '/home/report/AppTest/launcher'
        # 调用函数并传入参数
        upload_success = sftp.sftp_transfer_file(local_file=local_file, remote_path=remote_path)
        if upload_success:
            print("Transfer completed successfully.close")
        else:
            print("Transfer failed.")

    total = result.get('all')
    success = int(result.get('success'))
    pass_rate = result.get('pass_rate')
    total_execution_time = result.get('runtime')
    executor = result.get('tester')
    remote_path = '/home/report/AppTest/launcher'

    connection = sqltest.connect_to_database("10.192.110.211", "AppTest", "db", "DBtest123456!")
    try:
        # 写入数据
        # data = (0, time,"X5U", "2.3.2", total, success, pass_rate, "10","wangjiancheng",file,"null",time,time)
        data = (0, time, 'HQK2', '2.4.2', total, success, pass_rate, total_execution_time, executor, file, 'Success', time, time)
        print(data)
        sqltest.write_data_to_database(connection, data)
    finally:
        connection.close()

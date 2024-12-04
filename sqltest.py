import mysql.connector
from mysql.connector import Error


def connect_to_database(host, database, user, password):
    try:
        conn = mysql.connector.connect(host=host,
                                       database=database,
                                       user=user,
                                       password=password,
                                       charset='utf8mb4')
        if conn.is_connected():
            print("连接成功！")
            return conn
    except Error as e:
        print("连接失败：", e)


def write_data_to_database(conn, data):
    cursor = conn.cursor()
    try:
        """
        insert_query = 'INSERT INTO Launcher(`id`,`start_time`,`devices_name`,`app_version_name`,
        `total_test_cases`,' \ '`successful_test_cases`,`pass_rate`,`total_execution_time`,`executor`,`report_url`,
        `execution_status`,`data_entry_time`,`data_entry_update_time`) VALUES(%s,%s,%s,%s,%s,' \ '%s,%s,%s,%s,%s,%s,
        %s,%s); ' 
        """
        insert_query='INSERT INTO AppTest.Launcher(`id`, `start_time`, `device_name`, `app_version_name`, `total_test_cases`, `successful_test_cases`, `pass_rate`, `total_execution_time`, `executor`, `report_url`, `execution_status`, `data_entry_time`, `data_entry_update_time`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        cursor.execute(insert_query, data)
        conn.commit()
        print("数据插入成功！")
    except Error as e:
        print("数据插入失败：", e)
    finally:
        cursor.close()

"""
# 数据库连接信息
host = "10.192.110.211"
database = "AppTest"
user = "db"
password = "DBtest123456!"

# 要插入的数据
#data = ("2", "2.3.2", "D5XP", "22", "20", "2", "2024-05-06")
data=(0, 'time', 'X5U', '2.3.2', 'total', 'success', 'pass_rate', 'total_execution_time', 'executor', 'file', 'null', 'time', 'time')

# 连接数据库
connection = connect_to_database(host, database, user, password)

# 写入数据
write_data_to_database(connection, data)

# 关闭连接
connection.close()
"""
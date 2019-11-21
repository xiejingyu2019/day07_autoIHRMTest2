from unittest import TestCase
from requests import Response
import json, app, pymysql
import logging

app.init_logging()


# 封装数据库工具类
class DBUtils:
    def __init__(self, host=None, user=None, password=None, database=None, autocommit=None, charset='utf8'):
        # 初始化外部传入的数据库连接参数
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.charset = charset

    def __enter__(self):
        # 如果使用了with语法，就会执行以下语句，自动建立连接，获取游标
        # 如果获取连接失败，那么就不会有conn和cursor属性
        # 获取连接失败原因：域名不正确，用户名密码错误，服务器没有启动，数据库不正确等等
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.conn.cursor()
            return self
        except Exception as e:
            print("建立连接或者获取游标异常！： ", e)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 如果使用了with语法，就会自动执行以下语句，自动关闭游标和连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# 通用断言
def assert_utils(self, response, htttpCode, success, code, message):
    """
    @type self:TestCase
    @type response:Response
    """
    # 断言httpcode
    print("assert_utils的selfid", id(self))
    jsonData = response.json()  # type:dict
    self.assertEqual(htttpCode, response.status_code)
    self.assertEqual(success, jsonData.get("success"))
    self.assertEqual(code, jsonData.get("code"))
    self.assertIn(message, jsonData.get("message"))


# 读取登陆数据
def read_login_data():
    login_data = app.BASEDIR + "/data/login.json"
    with open(login_data, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("read_login_data: {}".format(jsonData))
        result_list = []
        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            result_list.append((mobile, password, http_code, success, code, message))
        logging.info("result_list: {}".format(result_list))
    return result_list


if __name__ == '__main__':
    db = DBUtils(host='182.92.81.159',
                 user='readuser',
                 password="iHRM_user_2019",
                 database="ihrm",
                 charset='utf8',
                 autocommit=False)
    with db as db:
        sql = "select * from bs_user limit 1;"
        db.cursor.execute(sql)
        print(db.cursor.fetchall())

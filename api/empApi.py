import requests

import api
import app


class EmpApi:

    def __init__(self):
        self.add_emp_url = "http://182.92.81.159/api/sys/user"
        self.query_emp_url = "http://182.92.81.159/api/sys/user"
        # self.headers = {"Content-Type":"application/json", "Authorization":"Bearer "}
        pass

    #封装添加员工接口
    def add_emp(self, username, mobile):
        headers = app.HEADERS
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-11-01",
            "formOfEmployment": 1,
            "workNumber": "33333222",
            "departmentName": "测试部",
            "correctionTime": "2019-11-18T16:00:00.000Z"
        }
        print("self.headers", app.HEADERS)
        return requests.post(self.add_emp_url, json=jsonData, headers=app.HEADERS)


    #封装查询员工接口
    def query_emp(self):
        headers=app.HEADERS
        id=app.ID
        url=self.query_emp_url+"/"+id
        return requests.get(url,headers=headers)

    #封装修改员工接口
    def update_emp(self,username):
        headers=app.HEADERS
        id=app.ID
        url=self.query_emp_url+"/"+id
        return requests.get(url,json={"username":username},headers=headers)
    #封装删除员工接口
    def delete_emp(self):
        headers=app.HEADERS
        id=app.ID
        url=self.query_emp_url+"/"+id
        return requests.delete(url,headers=headers)
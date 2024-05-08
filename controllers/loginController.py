import json

from helpers.configar import Configur
import requests


class LoginController(Configur):
    def __init__(self):
        super().__init__()

    def checkValue(self, webPath, companyID):
        set_data = {"company_id": companyID}
        ENDPOINT = f"{webPath}/api/verify-company"
        r = requests.post(url=ENDPOINT, json=set_data)

        # extracting response text
        response = json.loads(r.text)
        token = response['token']
        server = response['server']
        usingSqlDb = response['using_sql_db']
        userTableName = response['user_table_name']
        attendanceTable = response['attendance_table']
        id = response['company_id']
        self.writeFile(webPath, companyID, token, server, usingSqlDb, userTableName, attendanceTable, id)
        # print(response)

# ***
# host/path
# verify
# store-log
# ***
# request parem
# company_id
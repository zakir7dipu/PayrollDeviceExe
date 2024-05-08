import json


class Configur:
    def __init__(self):
        super().__init__()
        self.configurData = None

    def readFile(self):
        f = open('helpers\config.json', 'r')
        configurFile = f.read()
        return json.loads(configurFile)

    def validate(self):
        data = self.readFile()
        if data['web_path'] and data['company_id'] and data['using_sql_db'] and data['user_table_name'] and data['attendance_table'] and data['token'] and data['company_db_id']:
            return True
        else:
            return False

    def writeFile(self, webPath, companyID, token, server, usingSqlDb, userTableName, attendanceTable, id):
        data = self.readFile()
        data['web_path'] = webPath
        data['company_id'] = companyID
        data['token'] = token
        data['server'] = server
        data['using_sql_db'] = usingSqlDb
        data['user_table_name'] = userTableName
        data['attendance_table'] = attendanceTable
        data['company_db_id'] = id
        json_object = json.dumps(data)
        with open("helpers\config.json", "w") as outfile:
            outfile.write(json_object)

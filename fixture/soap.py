from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self,app):
        self.app = app

    def get_project_list(self):
        base_url = self.app.config['web']['baseUrl']
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        wsdl_url = f"{base_url}api/soap/mantisconnect.php?wsdl"
        project_list = []
        client = Client(wsdl_url)
        try:
            _array = client.service.mc_projects_get_user_accessible(username,password)
            for element in range(len(_array)):
                id = _array[element].id
                name = _array[element].name
                project_list.append(Project(id=id, name=name))
            return list(project_list)
        except WebFault as ex:
            print(ex)
            return False
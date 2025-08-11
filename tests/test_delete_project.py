from model.project import Project
import random
import pytest
from data.projects import testdata

@pytest.mark.parametrize("project", testdata, ids = [repr(x) for x in testdata])
def test_delete_project(app, project):
    app.session.login("administrator", "root")
    if app.project.count() == 0:
        app.project.create(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    print(old_projects)
    print(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
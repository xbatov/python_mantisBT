import pytest
from model.project import Project
from data.projects import testdata

@pytest.mark.parametrize("project", testdata, ids = [repr(x) for x in testdata])
def test_add_project(app, project):
    old_projects = app.soap.get_project_list()
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
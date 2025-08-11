from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        project = []
        # Получаем базовый URL из конфигурации вместо хардкода
        base_url = self.app.base_url
        for element in wd.find_elements_by_css_selector('.row-1 td a,.row-2 td a'):
            name = element.text
            href = element.get_attribute("href")
            # Формируем ожидаемый префикс URL динамически из базового URL
            expected_prefix = f"{base_url}manage_proj_edit_page.php?project_id="
            href.startswith(expected_prefix)
            # Получаем ID проекта, отрезая динамически вычисляемую длину префикса
            id = href[len(expected_prefix):]
            project.append(Project(name=name, id=id))
        return project

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        select_status = Select(wd.find_element_by_name('status'))
        select_status.select_by_visible_text("%s" % project.status)
        category = wd.find_element_by_name('inherit_global')
        category.send_keys("%s" % project.categories)
        select_view_status = Select(wd.find_element_by_name('view_state'))
        select_view_status.select_by_visible_text("%s" % project.view_state)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_css_selector('.row-1 td a,.row-2 td a'))

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        # Используем базовый URL из конфига для проверки текущего URL
        if wd.current_url == f'{self.app.base_url}manage_proj_delete.php':
            wd.find_element_by_css_selector("input[value='Delete Project']").click()
        else:
            print("This is no delete page")

    def select_project_by_id(self, id):
        wd = self.app.wd
        # Получаем базовый URL из конфигурации
        base_url = self.app.base_url
        for element in wd.find_elements_by_css_selector('.row-1 td a,.row-2 td a'):
            name = element.text
            href = element.get_attribute("href")
            # Формируем ожидаемый префикс URL динамически
            expected_prefix = f"{base_url}manage_proj_edit_page.php?project_id="
            href.startswith(expected_prefix)
            # Вычисляем ID проекта на основе длины динамического префикса
            id_css = href[len(expected_prefix):]
            if id == int(id_css):
                wd.find_element_by_link_text("%s" % name).click()
                break
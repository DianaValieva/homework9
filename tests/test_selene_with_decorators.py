import allure
from selene.support import by
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity
from selene import browser, be


@allure.step("Открываем github")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем нужный репозиторий")
def find_repo():
    s(".header-search-button").click()
    s("#query-builder-test").type("DianaValieva/homework7")
    s("#query-builder-test").submit()


@allure.step("Переходим в репозиторий")
def go_to_repo():
    s(by.link_text("DianaValieva/homework7")).click()


@allure.step("Проверяем наличие нужного Issue")
def check_issue():
    s(by.partial_text("This is test issue for homework 9")).should(be.visible)


@allure.step("Открываем Issues")
def open_issues():
    s("#issues-tab").click()

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "dianavalieva")
@allure.feature("Задачи в репозитории")
@allure.story(" Есть нужная issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_selene_main(open_browser):
    open_main_page()
    find_repo()
    go_to_repo()
    open_issues()
    check_issue()

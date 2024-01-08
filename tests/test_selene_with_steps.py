import allure
from selene.support import by
from selene.support.shared.jquery_style import s
from selene import browser, be

def test_selene():
    with allure.step("Открываем github"):
        browser.open("https://github.com")

    with allure.step("Ищем нужный репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").type("DianaValieva/homework7")
        s("#query-builder-test").submit()

    with allure.step("Переходим в репозиторий"):
        s(by.link_text("DianaValieva/homework7")).click()

    with allure.step("Открываем Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие нужного Issue"):
        s(by.partial_text("This is test issue for homework 9")).should(be.visible)


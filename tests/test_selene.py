from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_selene():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").type("DianaValieva/homework7")
    s("#query-builder-test").submit()

    s(by.link_text("DianaValieva/homework7")).click()

    s("#issues-tab").click()

    s(by.partial_text("This is test issue for homework 9")).should(be.visible)

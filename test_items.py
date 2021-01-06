import time


def test_check_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket').click()
    time.sleep(3)
    button = browser.find_element_by_css_selector('.basket-mini.pull-right.hidden-xs .btn-group a').click()
    time.sleep(3)
    element = browser.find_element_by_css_selector('.col-sm-4 h3 a')
    time.sleep(3)
    assert element.text in "Coders at Work"


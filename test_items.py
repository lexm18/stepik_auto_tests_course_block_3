link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_availability_button(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert len(button) == 1, "button not found"
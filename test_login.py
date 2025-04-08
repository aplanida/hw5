from selene import browser, have, be
from conftest import baseurl


def test_fill_the_form():
    browser.open(baseurl)
    browser.element('#firstName').click().type('Anastasia')
    browser.element('#lastName').click().type('Anastasia')
    browser.element('#userEmail').click().type('anyemail@any.mail')
    browser.element('[for="gender-radio-2"]').click().should(be.existing)
    browser.element('[placeholder="Mobile Number"]').click().type('8888888889')
    browser.element('#dateOfBirthInput').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').double_click()
    browser.element('.react-datepicker__year-select').double_click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').should(be.visible)
    browser.driver.execute_script("window. scrollBy(0, 800)")
    browser.element('[placeholder="Current Address"]').should(be.visible)
    browser.element('#stateCity-label').hover().matching(have.text('State and City'))
    submit = browser.element('#submit')
    assert submit.should(be.existing)
    browser.element('#submit').click()
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element('tbody').should(be.visible)
    browser.element('tbody').should(have.text('Anastasia Anastasia'))
    browser.element('tbody').should(have.text('anyemail@any.mail'))
    browser.element('tbody').should(have.text('Female'))
    browser.element('tbody').should(have.text('8888888889'))
    browser.element('tbody').should(have.text('08 April,2025'))
    browser.element('tbody').should(have.text('Sports'))

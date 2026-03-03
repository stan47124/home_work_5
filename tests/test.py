import pytest
from selene import browser, have

@pytest.mark

def test_registration_form(browser):

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Ivan')

    browser.element('#lastName').type('Ivanov')

    browser.element('#userEmail').type('ivanov@gmail.com')

    browser.element('label[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('+79245731531')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('option[value="2000"]').click()
    browser.element('.react-datepicker__month-select').element('option[value="4"]').click()
    browser.element('.react-datepicker__day--024').click()

    browser.element('.react-datepicker__day--024').click()

    browser.element('.react-select-2-placeholder').type('E')
    browser.all('.subjects-auto-complete__option').element_by(have.text('English')).click()

    browser.element('label[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').set_value('C:\\Users\\user\\Pictures\\Фоновые изображения рабочего стола')

    browser.element('#currentAddress').type('9A Krasnoprudnaya Street')

    browser.element('#react-select-3-input').click()
    browser.all('.css-yt9ioa-option').element_by(have.text('NCR')).click()

    browser.element('#react-select-4-input').click()
    browser.all('.css-yt9ioa-option').element_by(have.text('Delhi')).click()

    browser.element('#submit').click()
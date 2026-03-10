import os

from selene import browser, have

def test_registration_form():

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Jackie')

    browser.element('#lastName').type('Chan')

    browser.element('#userEmail').type('chan@gmail.com')

    browser.element('label[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('9245731531')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.text('May')).click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.text('2000')).click()
    browser.element('.react-datepicker__day--024').click()

    browser.element('#subjectsInput').click().type('E')
    browser.all('.subjects-auto-complete__option').element_by(have.text('English')).click()

    browser.element('label[for="hobbies-checkbox-2"]').click()

    image_path = os.path.join(os.path.dirname(__file__), 'images.png')
    browser.element('#uploadPicture').send_keys(image_path)

    browser.element('#currentAddress').type('9A Krasnoprudnaya Street')

    browser.element('#state').click()
    browser.all('//div[contains(text(), "NCR")]').should(have.size_greater_than(0)).first.click()

    browser.element('#city').click()
    browser.all('//div[contains(text(), "Delhi")]').should(have.size_greater_than(0)).first.click()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    table = browser.element('.table-responsive')
    table.should(have.text('Jackie Chan'))
    table.should(have.text('chan@gmail.com'))
    table.should(have.text('Male'))
    table.should(have.text('9245731531'))
    table.should(have.text('24 May,2000'))
    table.should(have.text('English'))
    table.should(have.text('Reading'))
    table.should(have.text('images.png'))
    table.should(have.text('9A Krasnoprudnaya Street'))
    table.should(have.text('NCR Delhi'))


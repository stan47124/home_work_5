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

    browser.element('#uploadPicture').set_value('C:\\Users\\kstanila\\Pictures\\Screenshots\\Снимок экрана (1).png')

    browser.element('#currentAddress').type('9A Krasnoprudnaya Street')

    browser.element('#state').click()
    browser.all('//div[contains(text(), "NCR")]').should(have.size_greater_than(0)).first.click()

    browser.element('#city').click()
    browser.all('//div[contains(text(), "Delhi")]').should(have.size_greater_than(0)).first.click()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text('Jackie Chan'))

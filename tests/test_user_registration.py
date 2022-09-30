from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.model.pages import registration_form
from demoqa_tests.model.pages.registration_form import (
    given_opened,
)
from demoqa_tests.utils import path
from tests.test_data.users import elena


def test_fail_to_submit_form():
    given_opened()

    # todo: implement


def test_submit_student_registration_form():

    app.registration_form.given_opened()

    # WHEN

    browser.element('#firstName').type(elena.name)
    browser.element('#lastName').type(elena.last_name)
    browser.element('#userEmail').type(elena.email)

    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()

    browser.all('[for^=gender-radio]').by(
        have.exact_text(elena.gender.value)
    ).first.click()
    '''
    # OR
    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()
    # OR
    browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
    browser.element('[id^=gender-radio][value=Male]').element(
        './following-sibling::*'
    ).click()
    # OR better:
    browser.element('[id^=gender-radio][value=Male]').element('..').click()
    # OR
    browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()
    '''
    browser.element('#userNumber').type(elena.user_number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(elena.birth_month)
    browser.element('.react-datepicker__year-select').send_keys(elena.birth_year)
    browser.element(
        f'.react-datepicker__day--0{elena.birth_day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
    '''
    # OR something like
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
    '''

    registration_form.add_subjects(elena.subjects)

    for hobby in elena.hobbies:
        # browser.element(f'//label[contains(.,"{hobby.value}")]').click()
        # browser.element(by.text(hobby.value, tag='label')).click()
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()

    browser.element('[id="uploadPicture"]').send_keys(
        path.to_resource(elena.picture_file)
    )

    browser.element('#currentAddress').type(elena.current_address)

    registration_form.scroll_to_bottom()

    registration_form.set_state(elena.state)
    registration_form.set_city(elena.city)

    browser.element('#submit').perform(command.js.click)

    # THEN

    registration_form.should_have_submitted(
        [
            ('Student Name', f'{elena.name} {elena.last_name}'),
            ('Student Email', elena.email),
            ('Gender', elena.gender.value),
        ],
    )
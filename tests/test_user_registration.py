from demoqa_tests.model.pages import registration_form
from demoqa_tests.model.pages.registration_form import *
from demoqa_tests.utils import turpl_to_string
from demoqa_tests.utils.path import upload_picture
from tests.test_data.users import elena


def test_submit_student_registration_form():
    given_opened_browser()
    # WHEN
    set_first_name(elena.name)
    set_last_name(elena.last_name)
    set_email(elena.email)
    select_gender(elena.gender.value)
    set_mobile(elena.mobile)
    select_date_of_birth()
    select_subjects(elena.subjects)
    scroll_to_bottom()
    select_hobby(elena.hobbies)
    upload_picture(elena.picture_file)
    set_address(elena.current_address)
    set_state(elena.state)
    set_city(elena.city)
    press_submit()

    # THEN
    registration_form.should_have_submitted(
        [
            ('Student Name', f'{elena.name} {elena.last_name}'),
            ('Student Email', elena.email),
            ('Gender', elena.gender.value),
            ('Mobile', elena.mobile),
            ('Date of Birth', f'{elena.birth_day} {elena.birth_month},{elena.birth_year}'),
            ('Subjects', turpl_to_string.convert(elena.subjects)),
            ('Hobbies', turpl_to_string.convert(elena.hobbies)),
            ('Picture', elena.picture_file),
            ('Address', elena.current_address),
            ('State and City', f'{elena.state} {elena.city}')
        ],
    )
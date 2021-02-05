from Pages import RegistrationPage
import pytest

from Utils.Driver import Driver


class Test_Registration(Driver):

    @pytest.mark.smoke
    def test_registration(self):
        c = Driver.open_Browser()
        # RegistrationPage.Click_on_SignIn(c)
        # RegistrationPage.Enter_email(c, "vhbk@gmail.com")
        # RegistrationPage.click_on_create_an_account(c)
        # RegistrationPage.Gender(c)
        # RegistrationPage.First_name(c, "vibha")
        # RegistrationPage.Last_name(c,  "kumari")
        # RegistrationPage.password(c, "78696")
        # RegistrationPage.Company(c, "Nagarro")
        # RegistrationPage.address(c, "a-46")
        # RegistrationPage.city(c, "Noida")
        # RegistrationPage.Select_state(c, "Alaska")
        # RegistrationPage.postal_code(c, "00000")
        # RegistrationPage.Country(c, "India")
        # RegistrationPage.Mobile_number(c, "9875464676")
        # RegistrationPage.Address_Alias(c, "a2")
        # RegistrationPage.Click_on_register_button(c)

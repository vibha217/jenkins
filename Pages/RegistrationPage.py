from Utils.Base_Class import Base_Class
from Utils.Driver import Driver


class Registration(Base_Class, Driver):
    @staticmethod
    def Click_on_SignIn(self):
        ele = Base_Class.getElement(self, "Sign in", "linktext")
        Base_Class.action_click(ele)

    @staticmethod
    def Enter_email(self):
        ele = Base_Class.getElement(self, "email_create", "name")
        Base_Class.action_sendkeys(ele, "vaibhavi217@gmail.com")

    @staticmethod
    def Click_on_create_an_account(self):
        ele = Base_Class.getElement(self, "SubmitCreate", "name")
        Base_Class.action_click(ele)

    @staticmethod
    def Gender(self):
        ele = Base_Class.getElement(self, "id_gender2", "id")
        Base_Class.action_click(ele)

    @staticmethod
    def First_name(self):
        ele = Base_Class.getElement(self, "customer_firstname", "name")
        Base_Class.action_sendkeys(ele, "vaibhavi")

    @staticmethod
    def Last_name(self):
        ele = Base_Class.getElement(self, "customer_lastname", "name")
        Base_Class.action_sendkeys(ele, "kumari")

    @staticmethod
    def password(self):
        ele = Base_Class.getElement(self, "passwd", "name")
        Base_Class.action_sendkeys(ele, "avk987")

    @staticmethod
    def Company(self):
        ele = Base_Class.getElement(self, "company", "id")
        Base_Class.action_sendkeys(ele, "nagarro")

    @staticmethod
    def address(self):
        ele = Base_Class.getElement(self, "address1", "name")
        Base_Class.action_sendkeys(ele, "H-41,alpha-2,Noida")

    @staticmethod
    def city(self):
        ele = Base_Class.getElement(self, "city", "name")
        Base_Class.action_sendkeys(ele, "Noida")

    @staticmethod
    def Select_state(self):
        ele = Base_Class.getElement(self, "//select[@id = 'id_state']", "xpath")
        Base_Class.action_sendkeys(ele, "Alaska")

    @staticmethod
    def postal_code(self):
        ele = Base_Class.getElement(self, "postcode", "name")
        Base_Class.action_sendkeys(ele, "00000")

    @staticmethod
    def Country(self):
        ele = Base_Class.getElement(self, "id_country", "name")
        Base_Class.action_sendkeys(ele, "India")

    @staticmethod
    def Mobile_number(self):
        ele = Base_Class.getElement(self, "phone_mobile", "name")
        Base_Class.action_sendkeys(ele, "8790668903")

    @staticmethod
    def Address_Alias(self):
        ele = Base_Class.getElement(self, "alias", "name")
        Base_Class.action_sendkeys(ele, "a2")

    @staticmethod
    def Click_on_register_button(self):
        ele = Base_Class.getElement(self, "submitAccount", "id")
        Base_Class.action_click(ele)



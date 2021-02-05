from Class.Base_Class import Base_Class


class Login(Base_Class):

    @staticmethod
    def click_on_Sign_In(self):
        ele = Base_Class.getElement(self, "Sign in", "linktext")
        Base_Class.action_click(ele)

    @staticmethod
    def email(self):
        ele = Base_Class.getElement(self, "email_create", "name")
        Base_Class.action_sendkeys(ele, "vaibhavi217@gmail.com")

    @staticmethod
    def enter_Password(self):
        ele = Base_Class.getElement(self, "passwd", "name")
        Base_Class.action_sendkeys(ele, "76bhn")

    @staticmethod
    def click_on_submit(self):
        ele = Base_Class.getElement(self, "SubmitLogin", "name")
        Base_Class.action_click(ele)




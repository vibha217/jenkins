from Class.Base_Class import Base_Class


class Search(Base_Class):

    @staticmethod
    def Search(self):
        ele = Base_Class.getElement(self, "search_query_top","id")
        Base_Class.action_sendkeys(ele, "Printed Dress")

    def click_on_search(self):
        ele = Base_Class.getElement(self, "submit_search","name")
        Base_Class.action_click(ele)

        mobileList = driver.find_elements_by_css_selector("div[data-component-type='s-search-result']")
        print("The List of Numbers of Mobile in a single Page is :" + str(len(mobileList)))

        for mobile in mobileList:
            print(mobile.text)
            print("\n")
            print("------------------------------------------------------------------------")


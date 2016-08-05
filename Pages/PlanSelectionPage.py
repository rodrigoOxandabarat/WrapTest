from BasePageObject import BasePageObject
from RegisterPage import RegisterPage

class PlanSelectionPage(BasePageObject):
    """ 
        Page Object that handles the Plan Selection Page objects 
        and functions
    """
	
    def sign_up_button(self): #returns sign up button
	    return self.get_element_by_text_name("Sign Up")
		
    def try_for_free_button(self): #returns Try for Free button
        return self.get_element_by_text_name("Try for free")
		
    def contact_sales_button(self): #returns Contact Sales button
        return self.get_element_by_text_name("Contact Sales")
		
    def click_on_sign_up_button(self): #clicks on Sign Up button and returns Register Page
        self.sign_up_button().click()
        return RegisterPage(self.driver)
	
	
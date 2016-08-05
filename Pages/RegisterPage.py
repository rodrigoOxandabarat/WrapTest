import time
from BasePageObject import BasePageObject
from InitialPage import InitialPage

class RegisterPage(BasePageObject):
    """ 
        Page Object that handles the Register Page objects 
        and functions
    """
	
    def sign_up_with_facebook_button(self): 
        #returns button to sign up with Facebook button
        return self.get_element_by_attribute("type", "button")
		
    def sign_up_button(self): 
        #returns Sign up button
        return self.get_element_by_attribute("type", "submit")
		
    def email_field(self): 
        #returns email field
        return self.get_element_by_tag_name("input")
    
    def user_name(self): 
        #returns user name input field
        return self.get_element_by_attribute("ng-model", "vm.username")
		
    def password(self): 
        #returns user name input field
        return self.get_element_by_attribute("ng-model", "vm.password")
		
    def first_name(self): 
        #returns first name input field
        return self.get_element_by_attribute("ng-model", "vm.firstName")
		
    def last_name(self): 
        #returns last name input field
        return self.get_element_by_attribute("ng-model", "vm.lastName")
		
    def company(self): 
        #returns company input field
        return self.get_element_by_attribute("ng-model", "vm.company")
		
    def phone(self): 
        #returns phone number input field
        return self.get_element_by_attribute("ng-model", "vm.phone")
 
    def sign_up_with_email(self, email, username, pwd, firstN, lastN, company, ph_nr=None): 
        #signs up by entering email and clicking on sign up button and entering registration data
        self.email_field().send_keys(email)
        self.sign_up_button().click()
        #enter username and password input fields
        self.user_name().send_keys(username) #username
        self.password().send_keys(pwd) #password
        time.sleep(2)
        #click on button
        self.sign_up_button().click()
        #enter name, last name
        self.first_name().send_keys(firstN) #first name
        self.last_name().send_keys(lastN) #last name
        self.company().send_keys(company) #company
        if ph_nr: # if phone number is entered (optional input field)
            self.phone().send_keys(ph_nr) #phone nr.
        time.sleep(2)
        self.sign_up_button().click()
        self.wait_for_loading_element_to_dissapear()
        # returns InitialPage
        return InitialPage(self.driver)
		
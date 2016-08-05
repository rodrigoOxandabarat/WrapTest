import unittest
from Pages.WrapInitialPage import WrapInitialPage

class RegisterAndCreateWrapTest(unittest.TestCase):
    """ 
        Test Class for the exercise. The setUp method is run before the test function is executed, and creates the driver and sets
        the initial page to start testing.
        Then the test follows the steps to register and create a wrap from the templates, using the page object defined on the Pages folder.
        Finally, the tearDown method closes the driver and browser once the test is finished.
        NOTE: The user data for the registration need to be included on lines 22-28.
    """
	
    def setUp(self):
        self.initial_page = WrapInitialPage() #go to initial page
		
    def test_register_and_create_wrap(self):
        #click on Free Trial Link and go to Plan Selection Page
        plan_selection_page = self.initial_page.click_on_free_trial_link()
        #click on Sign up button for a Personal Plan		
        register_page = plan_selection_page.click_on_sign_up_button() 
        # Select register with email typing in email account, and then all requested input fields
        home_page = register_page.sign_up_with_email("rodrigo.oxandabarat@abstracta.com.uy", #email
                                                     "roxandabarat", #username
                                                     "password", #password
                                                     "Rodrigo", #First name
                                                     "Oxandabarat", #last name
                                                     "Abstracta",#company name
                                                     "114490")#phone number
        #create wrap from template and access wrap design page
        wrap_design_page = home_page.create_wrap_from_template()
        #click on publish
        wrap_design_page.click_on_publish_button()
        # verify if wrap got published
        assert wrap_design_page.is_wrap_published(), "Wrap did not get published"		
		
    def tearDown(self):
        self.initial_page.stop() #close page and driver
	
if __name__ == "__main__":
    unittest.main()
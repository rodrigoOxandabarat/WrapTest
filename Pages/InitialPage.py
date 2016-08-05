from BasePageObject import BasePageObject
from TemplatesTab import TemplatesTab
from WrapsTab import WrapsTab
from WrapDesign import WrapDesign

class InitialPage(BasePageObject):
    """ 
        Page Object that handles the Home Page (after loggin in/ register) Page objects 
        and functions
    """
	
    def __init__(self, driver): #Constructor. Creates the Page Object, and creates the handlers for both tabs (Templates tab and Wraps tab)
        BasePageObject.__init__(self, driver)
        self.templates_tab = TemplatesTab(self)
        self.wraps_tab = WrapsTab(self)
		
    def template_tab(self): #returns the object of the templates tab
        return self.get_element_by_attribute("ui-sref", "main.templates")
		
    def click_on_templates_tab(self): #clicks on templates tab
        self.template_tab().click()
		
    def close_tutorial(self): #closes the tutorial by clicking on the X button
        self.get_element_by_class_name("wrap-icon--alert_close").click() #close tutorial	

    def create_wrap_from_template(self): #this function clicks on templates tab and creates a wrap based in one of the templates.
        #NOTE: this function creates a wrap of the "Tell your brand story" type, for the sake of the test. But should be enhanced to
        #be able to handle different types of templates.
        self.click_on_templates_tab()
        self.templates_tab.create_wrap_tell_your_brand_story()
        self.close_tutorial()
        return WrapDesign(self.driver)

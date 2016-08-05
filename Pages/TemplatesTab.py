import time
from GeneralTab import GeneralTab

class TemplatesTab(GeneralTab):
    """ 
        Page Object that handles the Templates Tab Page objects 
        and functions
    """
	
    def select_wrap_template(self, template_name):#on Templates tab, allows to select a template based on the template name
        self.base_page.get_element_by_text_name(template_name).click()
		
    def create_wrap_tell_your_brand_story(self):#creates a wrap, based on the "Tell Your Brand Story" template
        self.select_wrap_template("Commerce")
        base_element = self.base_page.get_element_by_text_name("Tell Your Brand Story").find_element_by_xpath('..')
        time.sleep(2)
        base_element.find_elements_by_xpath("//*[contains(text(), 'Create Wrap')]")[0].click()
        

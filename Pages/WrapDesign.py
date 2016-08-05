import time
from BasePageObject import BasePageObject

class WrapDesign(BasePageObject):
    """ 
        Page Object that handles the Wrap Design Page objects 
        and functions. This page is accessed once a template has been selected.
    """
	
    def publish_button(self):#returns the web element of the Publish button
        return self.get_element_by_text_name("Publish")
	
    def click_on_publish_button(self):#clicks on Publish button, and waits for the publishing to be completed.
        time.sleep(2)
        self.publish_button().click()#click on Publish button
        self.wait_for_loading_element_to_dissapear()
		
    def is_wrap_published(self): #verifies that the success message is displayed
        return self.get_element_by_attribute("type", "PUBLISH").is_displayed()
        

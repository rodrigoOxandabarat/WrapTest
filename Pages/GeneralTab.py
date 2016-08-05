
class GeneralTab:
    """ 
        Base class for all tabs. Contains a reference to the base page that contains the tab.
    """

    def __init__(self, basePage):
        self.base_page = basePage
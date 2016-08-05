# WrapTest
Test in Python for Wrap, which registers and creates a wrap from the templates.
# NOTE: in order to run this test, Python 2.7 needs to be installed. 
#To run it, execute from command line:"python RegisterAndCreateWrapTest.py"

#The test was created based mainly on the Page Object Pattern, and these files are located on the "Pages" folder.
#These page object, have a base Page Object which all others inherit from, which is "BasePageObject", and which defines the general functions that all page objects may need to get different objects, and to wait for others (like the loading element). This class will create and set up the webdriver on its constructor if nothing is passed as a parameter. Otherwise, the webdriver needs to be passed between PageObjects as a parameter. This page also sets the waiting time for the explicit waits.
#There is also one base/general class for tabs in a page. This is used in this test in the Home Page after login, and their references are created on the page constructor. This way, functions and elements can be accessed once clicked on the tab, but without losing the capability to interact with other elements outside the tab.

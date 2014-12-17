from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import datetime

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        tableToDoList = self.browser.find_element_by_id('tableToDoList')
        self.assertTrue(tableToDoList)
        trs = tableToDoList.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [td.text for tr in trs for td in tr.find_elements_by_tag_name('td')])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # If there's a currently logged on user, go to main view;
        # else, displays the login page: username, password
		# --ok
        self.browser.get('http://localhost:8000')
        form_login = self.browser.find_element_by_id('form_login')
        self.assertTrue(form_login)
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

		# Shows the current date,
		# --ok
        now = datetime.datetime.now()
        divCurrentDate = self.browser.find_element_by_id('divCurrentDate')
        self.assertTrue(divCurrentDate)
        self.assertEqual(now.strftime("%B %d, %Y"), divCurrentDate.text)
		
		# with a list of all the To Do items
		# --ok

        # Allows the user to tick off an item in the list (as Done)
		# --ok

        # Allows the user to tick off an item in the list (as Cancelled)
		# --ok

        # At the end of the current date, all items not ticked off as Done, or Cancelled will be transferred to the next day
		# --ok

        # Has a simple user management system,
        # where for each user the username, full name, password, and e-mail address are the only required data.
        # An administrator account is the only one allowed to access the user management module for adding and deleting users.
		# --ok
        self.browser.get('http://localhost:8000/admin')
        self.assertIn('Django site admin', self.browser.title)
        self.browser.get('http://localhost:8000/accounts/logout')



        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
		# --ok
        self.browser.get('http://localhost:8000')
        form_login = self.browser.find_element_by_id('form_login')
        self.assertTrue(form_login)
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('edith')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('edith')
        password_field.send_keys(Keys.RETURN)

        # She notices the page title and header mention to-do lists
		# --ok
        self.assertIn('To-Do lists', self.browser.title)

        # She is invited to enter a to-do item straight away
		# --ok
        self.browser.get('http://localhost:8000/additem')
        form_additem = self.browser.find_element_by_id('form_additem')
        self.assertTrue(form_additem)

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
		# --ok
        description_field = self.browser.find_element_by_name('description')
        description_field.send_keys('Buy peacock feathers')
        description_field.send_keys(Keys.RETURN)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
		# --ok
        tableToDoList = self.browser.find_element_by_id('tableToDoList')
        self.assertTrue(tableToDoList)
        self.check_for_row_in_list_table('Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
		# --ok
        self.browser.get('http://localhost:8000/additem')
        form_additem = self.browser.find_element_by_id('form_additem')
        self.assertTrue(form_additem)
        description_field = self.browser.find_element_by_name('description')
        description_field.send_keys('Use peacock feathers to make a fly')
        description_field.send_keys(Keys.RETURN)

        # The page updates again, and now shows both items on her list
		# --ok
        self.check_for_row_in_list_table('Buy peacock feathers')
        self.check_for_row_in_list_table('Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
		
		
        self.fail('Finish the test!')
		
if __name__ == '__main__':
    unittest.main(warnings='ignore')

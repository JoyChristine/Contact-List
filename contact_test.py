import unittest 
from contact import Contact

#  Test.Case is a subclass inherits methods and variables from another class.

class TestContact(unittest.TestCase):
    
    # TEST 1 - check if objects r being instantiated correctly
    # setup allows definition of instructions
    def setUp(self):
        self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com")
        
    

    def test_init(self):
        

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")
    # teardown executes a set of instructions after every test
    def tearDown(self):
        Contact.contact_list =[]

    # TEST 2 -Save contact
    def test_save_contact(self):
        
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)
    # TEST 3 - Save multiple contacts
    def test_save_multiple_contact(self):
           
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)
# TEST 4 -Delete contact
    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com")
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)


    # TEST NO 5 - find new contact 
    def test_find_new_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com")
        test_contact.save_contact()

        found_contact = Contact.find_by_email("test@user.com")
        self.assertEqual(found_contact.email,test_contact.email)


# confirming inside the block shld run if its inside the module/file
if __name__ == '__main__':
    # unittest.main() collects all the test methods & executes them
    unittest.main()

import email


class Contact:
   
    contact_list = [] 
   

    def __init__(self,first_name,last_name,phone_number,email):
      self.first_name = first_name
      self.last_name = last_name
      self.phone_number = phone_number
      self.email = email

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)
# use a decorator(@) allowing us to make simple modifications to objects
    @classmethod
    def find_by_email(cls, email):
        # loop through contact object to check if email passed == email
        for contact in cls.contact_list:
            if contact.email == email:
                return contact
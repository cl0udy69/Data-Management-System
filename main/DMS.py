import json
import os
import random
import sys

saved_logins = {}
saved_address = {}
saved_banking_info = {}
saved_ssn = {}
saved_phone_number = {}

DATA_FILE = 'save_data.json'

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        saved_data = json.load(file)
        saved_logins = saved_data.get('logins', {})
        saved_address = saved_data.get('address', {})
        saved_banking_info = saved_data.get('banking_info', {})
        saved_ssn = saved_data.get('ssn', {})
        saved_phone_number = saved_data.get('phone_number', {})

def save_data_to_file():
    data_to_save = {
        'logins': saved_logins,
        'address': saved_address,
        'banking_info': saved_banking_info,
        'ssn': saved_ssn,
        'phone_number': saved_phone_number
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data_to_save, file)


def user_selection():
    save_login = input('Welcome to Dorians Digits! Your friendly, safe, secure password manager. Would you like to save a login, generate a new one, save personal information, or see your saved data and logins')
    if save_login in ['1', 'One', 'one', 'Save Login', 'Save login', 'save login']:
        login_saver()
    elif save_login in ['2', 'two', 'Two', 'Generate Login', 'Generate login', 'generate login', 'Generate a new one', 'generate a new one']:
        generate_passwords()
    elif save_login in ['3', 'Three', 'three', 'Save Personal Information', 'Save personal information', 'save personal information', 'Personal Information', 'Personal information', 'personal information']:
        personal_information_selection()
    elif save_login in ['4', 'four', 'Four', 'See all saved logins', 'see all saved logins', 'See saved logins', 'see saved logins', 'See logins', 'see logins', 'See Login', 'See logins', 'see login']:
        see_saved_logins()
    elif save_login in ['5', 'five', 'Five', 'See saved personal information', 'see saved personal information', 'See saved personal info', 'see saved personal info', 'See Personal Information', 'See personal information', 'see personal information', 'See Information', 'See information', 'see information']:
        personal_information_selection()
    elif save_login in ['6', 'six', 'Six', 'Exit Application', 'Exit application', 'exit application', 'End Application', 'End application', 'end application', 'Exit', 'exit', 'End', 'end']:
        save_option = input('Do you want to save your data before exiting? (yes/no): ')
        if save_option.lower() == 'yes':
            save_data_to_file()
        sys.exit()

def handel_user_options():
    option = input('What would you like to do now? ')
    if option in ['1', 'one', 'One', 'Save Login', 'Save login', 'save login']:
        login_saver()
    elif option in ['2', 'two', 'Two', 'Generate a new one', 'generate a new one', 'Generate Password', 'Generate password', 'generate password', 'Generate Login', 'Generate login', 'generaten login', 'Generate New Password', 'Generate new password', 'generate new password', 'Generate New Login', 'Generate new login', 'generate new login', 'New Password', 'New password', 'new password', 'New Login', 'New login', 'new login']:
        generate_passwords()
    elif option in ['3', 'three', 'Three', 'View Personal Information', 'View personal information', 'view personal information', 'See Personal Information','See personal information', 'see personal information', 'Save Address', 'Save address', 'save address', 'Save Billing Address', 'Save billing address', 'save billing address', 'Save Social Security Number', 'Save social security number', 'save social security number', 'Save Social Security', 'Save social security', 'save social security', 'Save SSN', 'Save ssn', 'save SSN', 'save ssn', 'SSN', 'ssn', 'Social Security Number', 'Social security number', 'Social security', 'social security', 'Save Banking Information', 'Save banking information', 'save banking information', 'Save Banking Info', 'Save banking info', 'save banking info', 'Save Phone Number', 'Save phone number', 'Save Number', 'Save number', 'save number', 'See Saved Address', 'See saved address', 'see saved address', 'See Address', 'See address', 'see address', 'View Saved Address', 'View saved address', 'view saved address', 'View Address', 'View address', 'view address', 'See saved banking information', 'see saved banking information', 'See saved banking info', 'see saved banking info', 'See Banking Information', 'See banking information', 'See Banking Info', 'See banking info', 'see banking info', 'View saved banking information', 'view saved banking information', 'View saved banking info', 'view saved banking info', 'View Banking Information', 'View banking information', 'View Banking Info', 'View banking info', 'view banking info', 'See saved social security number', 'see saved social security number', 'See saved social security', 'see saved social security', 'See saved SSN', 'See saved ssn', 'See saved ssn', 'see saved ssn', 'see saved SSN', 'See social security number', 'see saved security number', 'See social security', 'see social security', 'See SSN', 'see SSN', 'See ssn', 'see ssn', 'View saved social security number', 'view saved social security number', 'View saved social security', 'sview saved social security', 'View saved SSN', 'View saved ssn', 'View saved ssn', 'view saved ssn', 'view saved SSN', 'View social security number', 'view saved security number', 'View social security', 'view social security', 'View SSN', 'view SSN', 'View ssn', 'view ssn', 'See saved phone number', 'see saved phone number', 'See saved number', 'see saved number', 'See Phone Number', 'See phone number', 'see phone number', 'See Number', 'See number', 'see number', 'View saved phone number', 'view saved phone number', 'View Saved Number', 'View saved number', 'view saved number', 'View Phone Number', 'View phone number', 'view phone number', 'View Number', 'View number', 'view number']:
        personal_information_selection()
    elif option in ['Exit Application', 'Exit application', 'exit application', 'End Application', 'End application', 'end application', 'Exit', 'exit', 'End', 'end']:
        save_option = input('Do you want to save your data before exiting? (yes/no): ')
        if save_option.lower() == 'yes':
            save_data_to_file()
        sys.exit()
    else:
        print('Invalid option.')

def generate_passwords():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%^&*()_+-=[]{}|;:,.<>/?~'
    number = int(input('Amount of passwords: '))
    length = int(input('Length of password: '))
    special = input('What special characters would you like to delete: ')
    numbers = input('What numbers would you like to delete: ')
    lowercase = input('What lowercase letters would you like to delete: ')
    capitals = input('What capital letters would you like to delete: ')

    for pwd in range(number):  
        password = ''
        for pwd in range(length):
            char = random.choice(chars)
            if char not in special and char not in numbers and char not in lowercase and char not in capitals:
                password += char
        print(password)
        save_generated_password = input('Would you like to save this password (make sure to copy and paste the password)')
        if save_generated_password in ['Yes', 'yes', 'Y', 'y', 'Save Password', 'Save password', 'save password']:
            login_saver()

def login_saver():
    print('Enter the login you would like to save:')
    domain = input('What domain does the login belong to? (e.g. Google, Facebook, Spotify, Steam): ')
    username = input('Username/Email: ')
    password = input('Password: ')

    saved_logins[domain] = {'Username': username, 'Password': password}

def personal_information_selection():
    personal_information = input ('Would you like to save your address, banking information, or social security number. You can also view saved data.')
    if personal_information in ['1', 'one', 'One', 'Save Address', 'Save address', 'save address', 'Save Billing Address', 'Save billing address', 'save billing address']:
        address_saver()
    elif personal_information in ['2', 'two', 'Two', 'Save Banking Information', 'Save banking information', 'save banking information', 'Save Banking Info', 'Save banking info', 'save banking info']:
        bank_saver()
    elif personal_information in ['3', 'three', 'Three', 'Save Social Security Number', 'Save social security number', 'save social security number', 'Save Social Security', 'Save social security', 'save social security', 'Save SSN', 'Save ssn', 'save SSN', 'save ssn', 'SSN', 'ssn', 'Social Security Number', 'Social security number', 'Social security', 'social security']:
        ssn_saver()
    elif personal_information in ['4', 'four', 'Four', ' Save Phone Number', 'Save phone number', 'Save Number', 'Save number', 'save number', '']:
        phone_number_saver()
    elif personal_information in ['5', 'five', 'Five', 'See Saved Address', 'See saved address', 'see saved address', 'See Address', 'See address', 'see address', 'View Saved Address', 'View saved address', 'view saved address', 'View Address', 'View address', 'view address']:
        see_saved_address()
    elif personal_information in ['6', 'six', 'Six', 'See saved banking information', 'see saved banking information', 'See saved banking info', 'see saved banking info', 'See Banking Information', 'See banking information', 'See Banking Info', 'See banking info', 'see banking info', 'View saved banking information', 'view saved banking information', 'View saved banking info', 'view saved banking info', 'View Banking Information', 'View banking information', 'View Banking Info', 'View banking info', 'view banking info']:
        see_saved_banking_info()
    elif personal_information in ['6', 'six', 'Six', 'See saved social security number', 'see saved social security number', 'See saved social security', 'see saved social security', 'See saved SSN', 'See saved ssn', 'See saved ssn', 'see saved ssn', 'see saved SSN', 'See social security number', 'see saved security number', 'See social security', 'see social security', 'See SSN', 'see SSN', 'See ssn', 'see ssn', 'View saved social security number', 'view saved social security number', 'View saved social security', 'sview saved social security', 'View saved SSN', 'View saved ssn', 'View saved ssn', 'view saved ssn', 'view saved SSN', 'View social security number', 'view saved security number', 'View social security', 'view social security', 'View SSN', 'view SSN', 'View ssn', 'view ssn']:
        see_saved_ssn()
    elif personal_information in ['7', 'seven', 'Seven', 'See saved phone number', 'see saved phone number', 'See saved number', 'see saved number', 'See Phone Number', 'See phone number', 'see phone number', 'See Number', 'See number', 'see number', 'View saved phone number', 'view saved phone number', 'View Saved Number', 'View saved number', 'view saved number', 'View Phone Number', 'View phone number', 'view phone number', 'View Number', 'View number', 'view number']:
        see_saved_phone_number()

def address_saver():
    address = input('Street Adress: ')
    state = input('State/province: ')
    city = input('City: ')
    zipcode = input('Zipcode: ')
    aptnumber = input('Apartment Number: ')

    saved_address[address] = {'state': state, 'city': city, 'zipcode': zipcode, 'aptnumber': aptnumber}

def bank_saver(): 
    issuer = input('Card Issuer: ')
    name = input('Card Name: ')
    networks = input('Card Network: ')
    account_opening = ('Date of account opening: ')
    experiation = input('Experiation Date: ')
    cardholder_name = input ('Cardholder Name: ')
    number = input('Credit Card Number: ')
    cvv = input('CVV (the three digits on the back of the card): ')

    saved_banking_info[issuer] = {'name': name, 'networks': networks, 'account_opening': account_opening, 'experiation': experiation, 'cardholder_name': cardholder_name, 'number': number,  'cvv': cvv}\
        
def ssn_saver():
    social_security_number = input('Enter your social security number: ')
    
    saved_ssn[social_security_number] = {'social_security_number': social_security_number}
    
def phone_number_saver():
    phone_number = input('Enter your phone number: ')
    
    saved_phone_number[phone_number] = {'phone_number': phone_number}

def see_saved_logins():
    if not saved_logins:
        print('No saved logins.')
    else:
        print('Saved Logins:')
        for domain, login_info in saved_logins.items():
            print(f'Domain: {domain}, Username/Email: {login_info["Username"]}, Password: {login_info["Password"]}')

def see_saved_address():
    if not saved_address:
        print('No saved personal information.')
    else: 
        print('Saved address: ')
        for address, address_info in saved_address.items():
            print(f'Street Address: {address}, State: {address_info["State/province"]}, City: {address_info["City"]}, Zipcode: {address_info["Zipcode"]}, Apartment Number: {address_info["Apartment Number"]}')

def see_saved_banking_info():
    if not saved_banking_info:
        print('No saved banking information')
    else:
        print('Save banking information: ')
        for issuer, banking_info in saved_banking_info.items():
            print(f'Card Issuer: {issuer}, Card Name: {banking_info["Name"]}, Card Network: {banking_info["Card Network"]}, Date of Account Opening: {banking_info["Date of Account Opening"]}, Expiration Date: {banking_info["Expiration Date"]}, Cardholder Name: {banking_info["Cardholder Name"]}, Credit Card Number: {banking_info["Credit Card Number"]}, CVV: {banking_info["CVV"]},')

def see_saved_ssn():
    if not saved_ssn:
        print('No social security number saved')
    else:
        print('Save social security number: ')
        for social_security_number in saved_ssn.items():
            print(f'Social Security Number: {social_security_number}')
            
def see_saved_phone_number():
    if not saved_phone_number:
        print('No saved phone number')
    else:
        print('Save phone number: ')
        for phone_number in saved_phone_number.items():
            print(f'Phone Number: {phone_number}')

user_selection()
personal_information_selection()
handel_user_options()


# --- NOTES --- # 
# ~ When users generate a new password give them the option to save it 
# ~ Give users the option to test the strength of their password
# ~ Alert user if data is compromised
# ~ Add donation option 
# ~ Fully update file managing system to equate for all new features added
# ~ Create new user handeling options. So in the personal information selection prompt make it so when the user chooses which form of personal information they want to save it would bring up a new prompt with either saving or viewing
# ~ Organize code
# ~ Impliment hashmap
# ~ Add error handling 
# ~ Add validation for user input
# ~ Add ability to edit and delete saved information
# ~ Add searching feature
# ~ Add encryption
# ~ Add input validation
# ~ Extend password generation
# ~ Add generative API key for user authentification
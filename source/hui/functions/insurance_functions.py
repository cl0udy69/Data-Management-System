from file_operations import save_data_to_file, load_data_from_file

def ethnicity_selection():
    ethnicity_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if ethnicity_choices in user_chocices['save_ethnicity_choices']:
        save_ethnicity()
    elif ethnicity_choices in user_choices['see_ethnicity_choices']:
        see_ethnicity()
    elif ethnicity_choices in user_choices['delete_ethnicity_choices']:
        delete_ethnicity()
    elif ethnicity_choices in user_choices['edit_ethnicity_choices']:
        edit_ethnicity()
    else:
        print('Invalid input.')
        
    save_data_to_file(insurance_data, filename)
    
    load_data = load_data_from_file(filename)
    print("Loaded data ", load_data)
        
def save_ethnicity():
    ethnicity = input('Ethnicity: ')
    racial = input('Racial Background: ')
    cultural = input('Cultural Background: ')

    save_ethnicity[ethnicity] = {'ethnicity': ethnicity, 'racial': racial, 'cultural': cultural}
    
def see_ethnicity():
    if not save_ethnicity:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_ethnicity_choices']:
            save_ethnicity()
        elif selection in error_handling_negative['dont_save_ethnicity_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Ethnicity')
        for ethnicity, ethnicity_info in save_ethnicity.items():
            print(f'Ethnicity: {ethnicity_info["ethnicity"]}, Racial Background: {ethnicity_info["racial"]}, Cultural Background: {ethnicity_info["cultural"]}')

def delete_ethnicity(save_ethnicity):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_ethnicity:
        del save_ethnicity[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes')
        if save_changes in error_handling_positive['dont_delete_ethnicity_choices']:
            save_ethnicity_to_file(save_ethnicity, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_ethnicity_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')

def edit_ethnicity():
    print("Select the field you want to edit:")
    for ethnicity, data in save_ethnicity.items():
        print(ethnicity)
        for field in ethnicity:
            print(f" - {field}")
            
    ethnicity_to_edit = input('Enter the field you want to edit: ').lower()
    for ethnicity, data in save_ethnicity.items():
        if ethnicity_to_edit in data:
            new_value = input(f'Enter the new value for {ethnicity_to_edit}: ')
            save_ethnicity[ethnicity][ethnicity_to_edit] = new_value
            print(f'{ethnicity_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Ethnicity not found')

def gender_selection():
    gender_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if gender_choice in user_choices['save_gender_choices']:
        save_gender()
    elif gender_choices in user_choices['see_gender_choices']:
        see_gender()
    elif gender_choices in user_choices['delete_gender_choices']:
        delete_gender()
    elif gender_choices in user_choices['edit_gender_choices']:
        edit_gender()
    else:
        print('Invalid input.')
        
def save_gender():
    sex = input('Sex: ')
    gender = input('Gender: ')
    pronouns = input('Pronouns:')

    save_gender[sex] = {'sex': sex, 'gender': gender, 'pronouns': pronouns}
    
def see_gender():
    if not save_gender:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_gender_choices']:
            save_gender()
        elif selection in error_handling_negative['dont_save_gender_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Gender')
        for sex, gender_info in save_gender.items():
            print(f'Sex: {gender_info["sex"]}, Gender: {gender_info["gender"]}, Pronouns: {gender_info["pronouns"]}')

def delete_gender_field(save_gender):
    field_to_delete = input('Enter the field you want to edit: ').lower()
    if field_to_delete in save_gender:
        del save_gender[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes')
        if save_changes in error_handling_positive['dont_delete_gender_choices']:
            save_gender_to_file(save_gender, 'address.json')
            print('Changes saved')
        elif save_changes in error_handling_negative['delet_gender_choices']:
            print('Changes discarded')
        else:
            ('Invalid input. Changes discarded')
    else:
        print('Field not found')
        
def edit_gender():
    print("Select the field you want to edit:")
    for gender, data in save_gender.items():
        print(gender)
        for field in gender:
            print(f" - {field}")
    
    gender_to_edit = input('Enter the field you want to edit: ').lower()
    for gender, data in save_gender.items():
        if gender_to_edit in data:
            new_value = input(f'Enter the new value for {gender_to_edit}: ')
            save_gender[gender][gender_to_edit] = new_value
            print(f'{gender_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Gender not found')

def insurance_selection():
    insurance_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if insurance_choices in user_choices['save_insurance_choices']:
        save_insurance()
    elif insurance_choices in user_choices['see_insurance_choices']:
        see_address()
    elif insurance_choices in user_choices['delete_insurance_choices']:
        delete_insurance()
    elif insurance_choices in user_choices['edit_insurance_choices']:
        edit_insurance()
    else:
        print('Invalid input.')
        
def save_insurance():
    name = input('Insurance company name: ')
    policy = input('Insurance policy number: ')
    number = input('Insurance group number: ')
    plan = input('Insurance plan type: ')
    effective_date = input('Insurance plan effective date: ')
    expiration_date = input('Insurance plan expiration date: ')
    detail = input('Insurance plan coverage details: ')
    insured = input('Assets Insured: ')
    deductible = input('Insurance plans deductible amount: ')
    co_payment = input('Insurance plans co-pay amount: ')

    save_insurance[name] = {'policy': policy, 'number': number, 'plan': plan, 'effective date': effective_date, 'expiration date': expiration_date, 'detail': detail, 'insured': insured, 'deductible': deductible, 'co-payment': co_payment}

def see_insurance():
    if not save_insurance:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_insurance_choices']:
            save_insurance()
        elif selection in error_handling_negative['dont_save_insurance_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Insurance')
        for name, insurance_info in save_insurance.items():
            print(f'Insurance company name: {insurance_info["name"]}, Insurance policy number: {insurance_info["policy"]}, Insurance group number: {insurance_info["number"]}, Insurance plan type: {insurance_info["plan"]}, Insurance plan effective date: {insurance_info["effective date"]}, Insurance plan expiration date: {insurance_info["expiration date"]}, Insurance plan coverage details: {insurance_info["detail"]}, Assets Insured: {insurance_info["insured"]}, Insurance plans deductible amount: {insurance_info["deductible"]}, Insurance plans co-pay amount: {insurance_info["co-payment"]}')

def delete_insurance(save_insurance):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_insurance:
        del save_insurance[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_insurance_choices']:
            save_insurance_to_file(save_insurance, 'address.json')
            print('Changes saved')
        elif save_changes in error_handling_negative['delete_insurance_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        
def edit_insurance():
    print("Select the field you want to edit:")
    for insurance, data in save_insurance.items():
        print(insurance)
        for field in insurance:
            print(f" - {field}")
            
    insurance_to_edit = input('Select the field you want to edit: ').lower()
    for insurance, data in save_insurance.items():
        if insurance_to_edit in data:
            new_value = input(f'Enter the new value for {insurance_to_edit}: ')
            save_insurance[insurance][insurance_to_edit] = new_value
            print(f'{insurance_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Insurance not found')

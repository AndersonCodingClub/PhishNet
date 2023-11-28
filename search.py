import os
import string
from typing import Tuple, List, Dict


def _get_data() -> List[Dict]:
    """Get emails and phone numbers for 

    Returns:
        List[Dict]: List with structure [email dictionary, phone number dictionary]
    """
    emails = {}
    phone_numbers = {}
    files = [file for file in os.listdir('data') if file.endswith('.txt')]
    for file in files:
        with open(os.path.join('data', file), 'r') as f: 
            content = f.read()
        _, email_line, phone_line = content.split('\n')[:3]
        
        name = file.split('.txt')[0]
        email_string_list = email_line.split('emails: ')[-1].strip()
        phone_string_list = phone_line.split('numbers: ')[-1].strip()
        
        email_list = []
        phone_number_list = []
        if email_string_list != 'none':
            email_list = email_string_list.split(',')
        if phone_string_list != 'none':
            phone_number_list = phone_string_list.split(',')
        emails[name] = email_list
        phone_numbers[name] = phone_number_list
        
    return [emails, phone_numbers]

def _find_match(input_string: str, search_dict: Dict) -> Tuple:
    """Helper function to search through dictionary for a given string

    Args:
        input_string (str): String to look for
        search_dict (Dict): Dictionary to look for the input within

    Returns:
        Tuple: If match is found, tuple with structure (dictionary key, list index) is returned. Otherwise None.
    """
    for key in search_dict:
        if input_string in search_dict[key]:
            return (key, search_dict[key].index(input_string))

def search_for_information(email: str=None, phone_number: str=None) -> Tuple:
    """Search for whether email or phone number is in list of trusted numbers
    
    Args:
        email (str, optional): User-entered email address to search for. Defaults to None.
        phone_number (str, optional): User-entered phone number to search for. Defaults None.

    Returns:
        Tuple: If match is found, tuple with structure (company, index of email in company email list) returned. Otherwise None.
    """
    emails, phone_numbers = _get_data()
    
    if email:
        email = email.lower()
        return _find_match(input_string=email, search_dict=emails)
    elif phone_number:
        formatted_phone_number = phone_number.translate(str.maketrans('', '', string.punctuation))
        formatted_phone_number = phone_number.replace(' ', '')
        if len(formatted_phone_number) > 10:
            # Catch when number with format 1-###-###-#### is entered by removing the leading 1
            formatted_phone_number = formatted_phone_number[(len(formatted_phone_number) - 10):]
        return _find_match(input_string=formatted_phone_number, search_dict=phone_numbers)
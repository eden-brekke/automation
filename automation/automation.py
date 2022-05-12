import re

with open('./automation/potential-contacts.txt') as file:
  text_content = file.read()
  

def get_phone_numbers():
  phone_pattern = r'\b\d{3}\D?\d{3}\D?\d{4}'
  potential_phone_numbers = re.findall(phone_pattern, text_content)
  output_num_list = []
  for numbers in potential_phone_numbers:
    strip_symbols = re.sub('[-.)(]','', numbers)
    output_num_list.append(strip_symbols)

  hyphened_num_list = []  
  for num in output_num_list:
    final_num = num[:3] + '-' + num[3:6] + '-' + num[6:]
    hyphened_num_list.append(final_num)

  without_duplicates_num = list(dict.fromkeys(hyphened_num_list))
  
  with open('./automation/phone_numbers.txt', 'w') as file:
    for number in without_duplicates_num:
      file.write(number)
      file.write('\n')

def get_emails():
  email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
  potential_emails = re.findall(email_pattern, text_content)
  without_duplicates_email = list(dict.fromkeys(potential_emails))
  output_email = "\n".join(without_duplicates_email)

  print(output_email)
      
  with open('./automation/emails.txt', "w") as file:
    for email in potential_emails:
      file.write(email)
      file.write('\n')

get_phone_numbers()
get_emails()
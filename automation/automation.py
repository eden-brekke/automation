import re

with open('./automation/potential-contacts.txt') as file:
  text_content = file.read()
  
phone_pattern = r'\b\d{3}\D?\d{3}\D?\d{4}'

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'

potential_phone_numbers = re.findall(phone_pattern, text_content)

potential_emails = re.findall(email_pattern, text_content)

output_email = "\n".join(potential_emails)

output_phone = "\n".join(potential_phone_numbers)
print(output_email)
print(output_phone)
# with open('./automation/phone_numbers.txt', 'w') as file:
#   for number in potential_phone_numbers:
#     file.write(number)
#     file.write('\n')
    
# with open('./automation/emails.txt', "w") as file:
#   for email in potential_emails:
#     file.write(email)
#     file.write('\n')
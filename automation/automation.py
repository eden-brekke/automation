import re

with open('./automation/potential-contacts.txt') as file:
  text_content = file.read()
  
phone_pattern = r'\d{3}-\d{3}-\d{4}'

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
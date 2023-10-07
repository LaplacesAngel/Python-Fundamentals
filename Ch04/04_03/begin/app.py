import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'
message = 'hello there friend named "hello" hope you are finding hello a nice word today'

five_digit_expression = r'\d{3}\-\d{3}\-\d{4}'

hello_finder = r'hello\w*'

print(re.search(five_digit_expression,five_digit_zip))
print(re.search(five_digit_expression,nine_digit_zip))
print(re.search(five_digit_expression,phone_number))
print(re.search(hello_finder, message))
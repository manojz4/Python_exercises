import re

emails = [
    "gaurav1234@gmail.com",
    "pratik190900234@gmail.com",
    "2009_rocking_person@yahoo.com",
    "GodFather2022@yahoo.com",
    "Brocklesner_89_WWE@yahoo.com",
    "TheRock_WWE@yahoo.com",
    "JohnCena_WWE@yahoo.com",
    "Undertaker_Roman_reigns@outlook.com",
    "6789764666@rediffmail.com",
    "Kane#6789@gmail.com",
       ]

special_emails = [email for email in emails if re.search(r'[#~`]', email)]
print("1) Emails with special characters of #~`!:")
print(special_emails)

number_emails = [email for email in emails if re.match(r'^\d+\b', email)]
print("2) Emails that start with numbers:")
print(number_emails)

number_underscore_emails = [email for email in emails if re.match(r'^\d+_', email)]
print("3) Emails that start with numbers followed by an underscore:")
print(number_underscore_emails)

number_underscore_or_small_case_emails = [email for email in emails if re.match(r'^(\d+|[a-z])_', email)]
print("4) Emails that start with numbers followed by an underscore or small case characters:")
print(number_underscore_or_small_case_emails)

number_underscore_or_any_case_emails = [email for email in emails if re.match(r'^(\d+|[a-zA-Z])_', email)]
print("5) Emails that start with numbers followed by an underscore or small case characters or large case characters:")
print(number_underscore_or_any_case_emails)

only_number_emails = [email for email in emails if re.match(r'^\d+\b@', email)]
print("6) List of emails with only numbers before the @:")
print(only_number_emails)

any_number_emails = [email for email in emails if re.search(r'\d+\b@', email)]
print("7) List of emails with numbers anywhere before the @:")
print(any_number_emails)
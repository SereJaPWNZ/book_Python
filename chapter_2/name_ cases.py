name_user = 'Erik'
text = f'Hello {name_user}, would you like to learn some Python today?'
print(text)


print(name_user.lower())
print(name_user.upper())
print(name_user.title())


quote = "A person who never made a mistake never tried anything new."
famous_person = "    Albert Einstein    "

message = f'\n\t{famous_person} once said, "{quote}"'
print(message)
message_lstrip = f'\n\t{famous_person.lstrip()} once said, "{quote}"'
print(message_lstrip)
message_rstrip = f'\n\t{famous_person.rstrip()} once said, "{quote}"'
print(message_rstrip)
message_strip = f'\n\t{famous_person.strip()} once said, "{quote}"'
print(message_strip)

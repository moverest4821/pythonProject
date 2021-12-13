def main():
    """
    Create dictionary of emails_names
    """
    emails_name = {}
    email = input("Email: ")
    while email !="":
        name = get_email_name(email)
        confirm = input("Is your name {}? (Y/n) ".format(name))
        if confirm.upper() !="":
            name = input("Name: ")
        emails_name[email] = name
        email = input("Email: ")

        for email, name in emails_name.items():
            print("{} ({})".format(name, email))

def get_email_name(email):
    """
    Extract expected name from email address.
    """
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()
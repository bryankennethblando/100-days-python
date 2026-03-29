# create a project that let the user to create its account and let the system to verify it
import string
top_organization = ['@google.com', '@microsoft.com', '@yahoo.com']

# create_acoount
def create_an_account():
    username = input('Enter your username: ')
    organization = input('Enter your\'r organization: ')
    password = input('Create your password: ')
    user_created_account = [username, organization, password]

    return user_created_account

username_validation = lambda username: True if len(username) < 8 else False
organization_validation = lambda org: True if top_organization in org else False
password_validation = lambda user_password: True if user_password in string.punctuation else False


username, org, password = create_an_account()
print(username_validation(username))
print(organization_validation(org))
print(password_validation(password))



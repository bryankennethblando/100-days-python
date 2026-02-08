# finding and fixing bugs in the code part 3: filtering the spam

def remove_spam(email_list):
    # Iterate through the list and remove bad emails

    """for email in email_list:
        if "spam" in email:
            email_list.remove(email)
    return email_list"""

    """
        you need to copy the original list of the email_list: -- copy_email_list = email_list[:]
        so that you can iterate to other email that has a spam on the
        list of emails then create a new list to append the emails that has not a word "spam" in it:
         --- if "spam" not in email:
            new_list.append(email)
    """
    copy_email_list = email_list[:]
    new_list = []
    for email in copy_email_list:
        if "spam" not in email:
            new_list.append(email)
    return new_list

# 🚨 Test Code
my_inbox = ["work_email", "spam_v1", "spam_v2", "family_email"]

clean_inbox = remove_spam(my_inbox)

# 🚨 This should ONLY print work and family. 
# BUT... it prints: ['work_email', 'spam_v2', 'family_email']
print(clean_inbox)

# 🚨 Test Code
my_inbox = ["work_email", "spam_v1", "spam_v2", "family_email"]

clean_inbox = remove_spam(my_inbox)

# 🚨 This should ONLY print work and family. 
# BUT... it prints: ['work_email', 'spam_v2', 'family_email']
print(clean_inbox)
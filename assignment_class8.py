# # create a text file and add the below content without quotation marsk
# content="""
# Hi *user*!

# We've found the best article for you based on your interest: *title*
# Please click *here* to open the article
# """
# with open("a_textfile.txt", "w") as f:
#     f.write(content)
# # task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# # and store the updated content in user_email.txt
# # run program three times with different name, title and link


# # after running the program three times
# # the file user_email.txt must have all three users content
#Solution

# def fileupdater(user, title, here):
#     with open("a_textfile.txt","r") as rf:
#         content=rf.read()

#         content=content.replace("*user*",user)
#         content=content.replace("*title*",title)
#         content=content.replace("*here*",here)


#         with open("user_email.txt","a") as af:
#             af.write(content +"\n\n")

# fileupdater("huda","jannat ke patte", "httpsss//url")
# fileupdater("zaki","da vinci code", "httpsss//url")
# fileupdater("Ahmed","one piece", "httpsss//url")


# # Create a new text file named "student_records.txt" with the following initial content:
# # Student ID | Student Name | Grade
# # 101       | Alice        | A
# # 102       | Bob          | B
# # 103       | Carol        | C

# # Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line
#  to the console.

# # Create a new text file named "updated_records.txt" in write mode('w').
# # Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# # Close both files.

# # Open "updated_records.txt" in append mode('a') and add a new student record:
# # Close the "updated_records.txt" file.

# # Open "updated_records.txt" in read mode and print its contents to the console to verify that the new student record has been added.

#SOLUTION

# with open("students_records.txt", "r") as f:
#     linez=f.readlines()
#     for line in linez:
#         print(line, end="")


# with open("students_records.txt","r") as rf, open("updated_records.txt","w") as wf:
#     material=rf.readlines()
#     for line in material:
#         if "A" in line or "B" in line:
#             wf.write(line)
         
# with open("updated_records.txt","a") as af:
#     af.write(" 999       | Zaki         | C")

# with open("updated_records.txt", "r") as f:
#     liner=f.readlines()
#     print("\n")
#     for line in liner:
#         print(line, end= "")


# #########################
# #########################
# #########################

# """
# ### Assignment: Password Manager Program
# Demo: https://www.youtube.com/watch?v=O8596GPSJV4

# #### Objective:
# Create a password manager program that allows users to store, retrieve, and manage their passwords. 
# The program will use file handling to save and read data, and it will be run in the terminal.

# #### Requirements:
# 1. **File Handling**: Store the passwords in a file. Each entry should include the website, username, and password.
# 2. **Input Function**: Allow users to add new passwords, retrieve existing passwords, and delete passwords.
# 3. **Basic Operations**:
#     - **Add a new password**: Ask for the website, username, and password. Save this information to the file.
#     - **Retrieve a password**: Ask for the website and return the username and password.
#     - **Delete a password**: Ask for the website and remove the corresponding entry from the file.
# 4. **Basic Error Handling**: Handle cases where the website is not found when retrieving or deleting a password and also when file doesn't exists

# #### Program Flow:
# 1. Display a menu with the following options:
#     - Add a new password
#     - Retrieve a password
#     - Delete a password
#     - Exit
# 2. Based on the user's choice, perform the corresponding operation.
# 3. Repeat the menu until the user chooses to exit.

# #### Detailed Instructions:
# 1. **Menu Display**: Create a function to display the menu and get the user's choice.
# 2. **Add Password**:
#     - Prompt the user for the website, username, and password.
#     - Write this information to a file in a structured format.
# 3. **Retrieve Password**:
#     - Prompt the user for the website.
#     - Read the file and find the entry for the given website.
#     - Display the username and password.
# 4. **Delete Password**:
#     - Prompt the user for the website.
#     - Read the file and find the entry for the given website.
#     - Remove the entry and update the file.
# 5. **File Format**: Store each entry in a new line in the format:
#     ```
#     website,username,password
#     ```

# #### Example:
# 1. **Add Password**:
#     ```
#     Enter website: example.com
#     Enter username: user1
#     Enter password: pass123
#     Password saved successfully!
#     ```
# 2. **Retrieve Password**:
#     ```
#     Enter website: example.com
#     Username: user1
#     Password: pass123
#     ```
# 3. **Delete Password**:
#     ```
#     Enter website: example.com
#     Password deleted successfully!
#     ```

# #### Hints:
# - Use functions to keep your code organized.
# - Use lists and dictionaries to manage the data in memory before writing to or reading from the file.
# - Ensure to handle cases where the file may not exist initially.

# #### Additional Notes:
# - Focus on functionality rather than security for this assignment.
# # """
#SOLUTION




import os

def menu():
    print("WELCOME TO PASSWORD MANAGER")
    print("###########################")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Quit\n\n")
    choice=input("Enter Choice here : ")
    return choice


def add_password(file_path):
    website=input("Enter Website name: ")
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    with open(file_path,"a") as f:
        f.write(f"{website},{username},{password}\n")

    print("Password saved Succesfully!!") 

def retrieve_password(file_path):
    website=input("Enter Website name: ")
    
    if not os.path.exists(file_path):
        print("No passwords stored yet.")
        return
    
    with open(file_path,"r") as f:
        for line in f:
            stored_website,stored_username,stored_password=line.split(",")
            if stored_website==website:
                print(f"Username of the website {stored_website} is : {stored_username}")
                print(f"Password of the websit {stored_website} is : {stored_password}")
            else:
                print("No such website was found in the path you provided")

def delete_password(file_path):
    website=input("Enter Website name to delete: ")
    
    if not os.path.exists(file_path):
        print("No passwords stored yet.")
        return
    
    updated_lines=[]
    found=False
    with open(file_path,"r") as f:
        for line in f:
            stored_website,stored_username,stored_password=line.split(",")
            if stored_website!=website:
                updated_lines.append(line)
            else:
                found=True


        if found:
            with open(file_path,"w") as wf:
                
                for line in updated_lines:
                    wf.write(line)
                print("Password was Successfully Deleted")
        else:
            print("No such website was found in the path you provided")
        
def main():
    file_path="Password.txt"

    while True:
        choice=menu()
        
        if choice=="1":
            add_password(file_path)
        elif choice=="2":
            retrieve_password(file_path)

        elif choice=="3":
            delete_password(file_path)

        elif choice=="4":
            print("Exiting....")

            break
        else:
            print("Invalid Choice Try Again")    


if __name__ == "__main__":
    main()





# """
# create the same program again but this time file data should be stored in json
# """
import os
import json

def menu():
    print("WELCOME TO PASSWORD MANAGER")
    print("###########################")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Quit\n\n")
    choice = input("Enter Choice here : ")
    return choice

def load_passwords(file_path):
    if not os.path.exists(file_path):
        return {}
    
    with open(file_path, "r") as f:
        return json.load(f)

def save_passwords(file_path, passwords):
    with open(file_path, "w") as f:
        json.dump(passwords, f)

def add_password(file_path):
    website = input("Enter Website name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    passwords = load_passwords(file_path)
    passwords[website] = {"username": username, "password": password}

    save_passwords(file_path, passwords)

    print("Password saved successfully!!")

def retrieve_password(file_path):
    website = input("Enter Website name: ")

    passwords = load_passwords(file_path)

    if website in passwords:
        print(f"Username of the website {website} is: {passwords[website]['username']}")
        print(f"Password of the website {website} is: {passwords[website]['password']}")
    else:
        print("No such website was found in the path you provided")

def delete_password(file_path):
    website = input("Enter Website name to delete: ")

    passwords = load_passwords(file_path)

    if website in passwords:
        del passwords[website]
        save_passwords(file_path, passwords)
        print("Password was successfully deleted")
    else:
        print("No such website was found in the path you provided")

def main():
    file_path = "Password.json"

    while True:
        choice = menu()
        
        if choice == "1":
            add_password(file_path)
        elif choice == "2":
            retrieve_password(file_path)
        elif choice == "3":
            delete_password(file_path)
        elif choice == "4":
            print("Exiting....")
            break
        else:
            print("Invalid Choice, Try Again")

if __name__ == "__main__":
    main()


# """
# create the same program again but this time file data should be stored in binary using pickle module
# """



# import os
# import pickle

# def menu():
#     print("WELCOME TO PASSWORD MANAGER")
#     print("###########################")
#     print("1. Add Password")
#     print("2. Retrieve Password")
#     print("3. Delete Password")
#     print("4. Quit\n\n")
#     choice = input("Enter Choice here : ")
#     return choice

# def load_passwords(file_path):
#     if not os.path.exists(file_path):
#         return {}
    
#     with open(file_path, "rb") as f:
#         return pickle.load(f)

# def save_passwords(file_path, passwords):
#     with open(file_path, "wb") as f:
#         pickle.dump(passwords, f)

# def add_password(file_path):
#     website = input("Enter Website name: ")
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")

#     passwords = load_passwords(file_path)
#     passwords[website] = {"username": username, "password": password}

#     save_passwords(file_path, passwords)

#     print("Password saved successfully!!")

# def retrieve_password(file_path):
#     website = input("Enter Website name: ")

#     passwords = load_passwords(file_path)

#     if website in passwords:
#         print(f"Username of the website {website} is: {passwords[website]['username']}")
#         print(f"Password of the website {website} is: {passwords[website]['password']}")
#     else:
#         print("No such website was found in the path you provided")

# def delete_password(file_path):
#     website = input("Enter Website name to delete: ")

#     passwords = load_passwords(file_path)

#     if website in passwords:
#         del passwords[website]
#         save_passwords(file_path, passwords)
#         print("Password was successfully deleted")
#     else:
#         print("No such website was found in the path you provided")

# def main():
#     file_path = "Password.dat"  # Binary file extension

#     while True:
#         choice = menu()
        
#         if choice == "1":
#             add_password(file_path)
#         elif choice == "2":
#             retrieve_password(file_path)
#         elif choice == "3":
#             delete_password(file_path)
#         elif choice == "4":
#             print("Exiting....")
#             break
#         else:
#             print("Invalid Choice, Try Again")

# if __name__ == "__main__":
#     main()





# """
# # An email with placeholders for user details that need to be formatted.
# def placeholder(name,status):
#     content="Email 1: \nHello, {name}! \nYour account has been {status}.\n\n"
#     content=content.format(name=name,status=status)
#     with open("email.txt","w") as f:
#         f.write(content)

# placeholder("Zaki", "Deactivated")



# # An email subject in all lowercase that needs to be converted to uppercase.

# content="Email 2: \nsubject: meeting reminder\nbody: Don't forget about the meeting tomorrow.\n\n"
# content_1=content.upper()

# with open("email.txt","a") as f:
#     f.write(content_1)

# # An email body in all uppercase that needs to be converted to lowercase.

# content="Email 3:\nsubject: IMPORTANT UPDATE \nbody: PLEASE REVIEW THE ATTACHED DOCUMENT.\n\n"
# content_1=content.lower()

# with open("email.txt","a") as f:
#     f.write(content_1)



# # An email with a sentence that needs to have the first letter capitalized.

# content="email 4:\nsubject: follow up\nbody: this email needs to be capitalized.\n\n"
# content_1=content.capitalize()

# with open("email.txt","a") as f:
#     f.write(content_1)


# # An email subject that needs to be converted to title case.

# content="Email 5:\nsubject: weekly update\nbody: Here is your weekly update on the project status.\n\n"
# title="weekly update"
# title=title.title()
# if "weekly update" in content:
#     content=content.replace("weekly update",title)

# with open("email.txt","a") as f:
#     f.write(content)


# # An email body with leading and trailing spaces that need to be removed.

# content="email 6:\nsubject:  Feedback\nbody:    Thank you for your feedback. Please respond at your earliest convenience.\n\n"

# if "  " in content:
#     content=content.replace("  ","")

# if "  " in content:
#     content=content.replace("    ","")
# with open("email.txt","a") as f:
#     f.write(content)


# # An email with a repeated word that needs to be replaced.
# import re

# def remove_repeated_words(content):
#     # Use a regular expression to find repeated words
#     pattern = r'\b(\w+)\b\s+\b\1\b'
    
#     # Substitute repeated words with a single instance
#     result = re.sub(pattern, r'\1', content, flags=re.IGNORECASE)
    
#     return result


# content1="Email 7:\nsubject: error report\nbody: The system encountered an error error that needs to be addressed.\n\n"
# remove_repeated_words(content1)

# with open("email.txt","a") as f:
    
#     f.write(content1)
    
# # An email that needs to find the position of a keyword.
# content="Email 8:\nsubject: keyword search\nbody: Please find the keyword 'search' in this email.\n\n"
# position=content.find("search")
# with open("email.txt","a") as f:
#     f.write(content)
#     f.write(f"The keyword search can be found at position {position}\n\n")

# # An email body that needs to be split into a list of words.
# content="Email 9:\n subject: word split\n body: Split this email into individual words.\n\n"
# words_split=content.split(" ")

# with open("email.txt","a") as f:
#     f.write(content)
#     f.write(f"list of words are {words_split}\n\n")


# # An email with a list of words that need to be joined into a single sentence.

# content="Email 10: \nsubject: words join \nbody: join these words into a single sentence.\n\n"
# joined_words=content.replace(" ","")

# with open("email.txt","a") as f:
#     f.write(content)
#     f.write(joined_words)

# emails.txt
# Email 1:
# Hello, {name}! Your account has been {status}.

# Email 2:
# subject: meeting reminder
# body: Don't forget about the meeting tomorrow.

# Email 3:
# subject: IMPORTANT UPDATE
# body: PLEASE REVIEW THE ATTACHED DOCUMENT.

# Email 4:
# subject: follow up
# body: this email needs to be capitalized.

# Email 5:
# subject: weekly update
# body: Here is your weekly update on the project status.

# Email 6:
# subject:  Feedback
# body:    Thank you for your feedback. Please respond at your earliest convenience.    

# Email 7:
# subject: error report
# body: The system encountered an error error that needs to be addressed.

# Email 8:
# subject: keyword search
# body: Please find the keyword 'search' in this email.

# Email 9:
# subject: word split
# body: Split this email into individual words.

# Email 10:
# subject: words join
# body: join these words into a single sentence
# """

 
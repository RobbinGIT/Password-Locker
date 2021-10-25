# Password-Locker
## Author

[Robbin_Mwangi](https://github.com/RobbinGIT)

## Description

This is an a application build in ptython that helps in managing logins and signup credentials of a user for various accounts in essence username and passwords for each account. It also stores the passwords and generates a unique password for user if they do not want to type new password themselves.

## User Stories

The user would like to:
* Create an account for the application or log into the application.
* Store existing accounts login details for various accounts that they have registered for.
* Generate new password for an account
* Delete stored account login details
* Copy credetials

## Installation and setup information

### The application requires the following installations to operate
* python3.9
* pip

#### cloning

* Open Terminal 

* git clone ```https://github.com/RobbinGIT/Password-Locker.git```

* cd PythonPasswordLocker

* code . if using visual studio code

### Running the Application
* To run the application, open the cloned file in the terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py

* To run test for the application
        $ python3 passwordlock_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hello Welcome to your Accounts Password Store... <br>* na ---  Create New Account * sa ---  To show account |
|Select  na| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select sa  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```save```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```sa```|A list of all credentials that has been stored or ```Oops, Account does not exist``` |
|Find a stored credential based on account name|Enter ```fa```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```da```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```ex```| The application exits|

## Technologies Used

* python3.9

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [robbingithimbo@gmail.com]

## License
* *MIT License:*
* Copyright (c) Robbin Mwangi

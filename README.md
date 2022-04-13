# assignment-ATM

<h2> Requirements </h2>

- At least the following flow should be implemented:
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

- For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.

- A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.

- Based on your work, another engineer should be able to implement the user interface. You don't need to implement any REST API, RPC, network communication etc, but just functions/classes/methods, etc.

- You can simplify some complex real world problems if you think it's not worth illustrating in the project.

<h2>What I did in this assignment</h2>

1. Can add user account

2. Check user account and add account

3. There are 4 steps for InsertCard/Checking name and PIN number/SelectAccount
  - In insertcard processing, input name and PIN number.
  - With the name and PIN number, check the name and PIN number with user information.
  - If the user is verified, can select the account.
  - Can do checking balance/operation of Deposit/opration of Withdraw

<h2>How to do?</h2>

1. Clone the project.

````bash
git clone https://github.com/DrageonLee/assignment-ATM.git
````

2. Start the file.
````bash
python ATM.py
````

3. Process
1) Create account
- During this step type name and PIN number
````python
#create user
user_1 = Account()
````
![](https://velog.velcdn.com/images/yg910524/post/dbe2d40d-d10e-48b8-aab2-2a1c743a1551/image.png)


4. 
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
#create the account for user who use first.
print(user_1.checkAccount())
#Add new account for existed user.
print(user_1.addAccount())
````
![](https://velog.velcdn.com/images/yg910524/post/dbe2d40d-d10e-48b8-aab2-2a1c743a1551/image.png)
![](https://velog.velcdn.com/images/yg910524/post/91d9fbf5-f274-44cc-b153-92f1f111f7b6/image.png)

- With created accounts, operate ATM process
````python
#Check the user whether verified user or not with name and PIN number.
operate = Operate()
print(operate.insertCard())
#If the user is verified, go to select the account.
#And then select the operation.
#If the choice is 1. return 'Balance'
````
![](https://velog.velcdn.com/images/yg910524/post/a74ff98e-a7cf-4fa8-9101-a86c53999458/image.png)

````python
#To compare the amount of balance, add one more instance.
operate1 = Operate()
print(operate1.insertCard())
````
- If the choice is 2.'Deposit', then 'Balance' with deposit money.
![](https://velog.velcdn.com/images/yg910524/post/76e11b07-5cfd-4ae6-9455-03e3934a51ce/image.png)

- If the choice is 3.'Withdraw', then 'Balance' with withdraw money. In case that withdraw money is more than balance, print('check again') and input the money again.
![](https://velog.velcdn.com/images/yg910524/post/78ddc1ff-5c43-41f5-ba9e-72f2d5689387/image.png)

![](https://velog.velcdn.com/images/yg910524/post/ef6703e6-81b7-448e-b759-a60e2153a9b4/image.png)

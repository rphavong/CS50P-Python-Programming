## Global

# ## Creating a balance
# balance = 0

# def main():
#     print("Balance:", balance)

# if __name__ == "__main__":
#     main()



# ## Code outputs a 'UnBoundLocalError'
# balance = 0

# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)

# def deposit(n):
#     balance += n

# def withdraw(n):
#     balance -= n

# if __name__ == "__main__":
#     main()



# ## How to approach error from code above, by making varibale into a global variable
# balance = 0

# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == "__main__":
#     main()



## Integrating Object Oriented Programming
class Account:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

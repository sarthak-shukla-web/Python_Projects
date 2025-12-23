# You are required to build a simple personal finance management tool. The program should allow user to :-
#   Add an expense with details like date, category, description and amount.
#   View all recorded expenses in a clean format.
#   Calculate total spendings so far.
#   Exit the program gracefully when the user chooses to.

# print("********** Welcome to Expense Tracker Software **********")
# dates=[]
# categories=[]
# descriptions=[]
# amounts=[]

# def details(date,category,description,amount):
#     date = input("Enter the date of your payment in the format(dd/mm/yyyy) : ")
#     dates.append(date)
#     category = input("Enter the category of your payment, why the payment was done : ")
#     categories.append(category)
#     description = input("Enter where the payment was done : ")
#     descriptions.append(description)
#     amount = int(input("Enter the amount of the payment : "))
#     amounts.append(amount)

# def total_payments(price,i):
#     price = amounts[i]
#     for i in range(len(amounts)):
#         price += amounts[i]
#     print("The total spendings so far is : ")

# def main():
#     details(date,category,description,amount)
#     choice = input("Do you want to continue entering the payment (Y/N) : ")
#     if choice == "Y":
#         main()
#     else:
#         total_payments()

# main()

print("********** Welcome to Expense Tracker Software **********")
dates=[]
categories=[]
descriptions=[]
amounts=[]

while True:
    date = input("Enter the date of your payment in the format(dd/mm/yyyy) : ")
    dates.append(date)
    category = input("Enter the category of your payment, why the payment was done : ")
    categories.append(category)
    description = input("Enter where the payment was done : ")
    descriptions.append(description)
    amount = int(input("Enter the amount of the payment : "))
    amounts.append(amount)
    choice = input("Do you want to continue entering details(Y/N) : ")
    print("\n")
    if choice == "Y":
        continue
    else:
        False
        break
for i in range(len(dates)):
    print("\nPayment",i+1,":-")
    print("Date of Payment : ",dates[i])
    print("Category of Payment :",categories[i])
    print("Description of Payment :",descriptions[i])
    print("Amount of Payment :",amounts[i],"\n")
    i += 1
spendings = 0
for i in range(len(amounts)):
    spendings += amounts[i]
print("\nThe total spendings so far is : ",spendings,"\n")
print("\n********** THANK YOU FOR USING EXPENSE TRACKER SOFTWARE **********")
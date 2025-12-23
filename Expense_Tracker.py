# You are required to build a simple personal finance management tool. The program should allow user to :-
#   Add an expense with details like date, category, description and amount.
#   View all recorded expenses in a clean format.
#   Calculate total spendings so far.
#   Exit the program gracefully when the user chooses to.

# print("********** Welcome to Expense Tracker Software **********")

# dates = []
# categories = []
# descriptions = []
# amounts = []

# def add_expense():
#     date = input("Enter date (dd/mm/yyyy): ")
#     category = input("Enter category: ")
#     description = input("Enter description: ")
#     amount = float(input("Enter amount: "))

#     dates.append(date)
#     categories.append(category)
#     descriptions.append(description)
#     amounts.append(amount)

#     print("Expense added successfully!\n")

# def view_expenses():
#     if len(amounts) == 0:
#         print("No expenses recorded yet.\n")
#         return

#     print("\nDate\t\tCategory\tDescription\tAmount")
#     print("-" * 50)
#     for i in range(len(amounts)):
#         print(f"{dates[i]}\t{categories[i]}\t{descriptions[i]}\t{amounts[i]}")
#     print()

# def total_spending():
#     total = sum(amounts)
#     print(f"Total spending so far: {total}\n")

# def main():
#     while True:
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Total Spending")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == "1":
#             add_expense()
#         elif choice == "2":
#             view_expenses()
#         elif choice == "3":
#             total_spending()
#         elif choice == "4":
#             print("Thank you for using Expense Tracker. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.\n")

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
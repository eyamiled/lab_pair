expenses = []
def add_expense():
description = input("Description: ")
amount = float(input("Amount: "))
expenses.append({
"description": description,
"amount": amount
})
print("Expense added!")
def show_expenses():
# Student B's task
pass
def show_total():
# Student B's task
pass
def main():
while True:
print("\n===== EXPENSE TRACKER =====")
print("1. Add an expense")
print("2. View expenses")
print("3. Show total")
print("4. Exit")
choice = input("Your choice: ")
if choice == "1":
add_expense()
elif choice == "2":
show_expenses()
elif choice == "3":
show_total()
elif choice == "4":
print("Goodbye!")
break

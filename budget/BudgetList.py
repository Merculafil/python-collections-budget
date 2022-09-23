from . import Expense


class BudgetList:
    def __init__(self, budget):
        self._budget = budget
        self._sum_expenses = 0
        self._expenses = []
        self._sum_overages = 0
        self._overages = []

    def append(self, item):
        if self._sum_expenses + item < self._budget:
            self._expenses.append(item)
            self._sum_expenses += item
        else:
            self._overages.append(item)
            self._sum_overages += item

    def __len__(self):
        return len(self._expenses) + len(self._overages)

def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')

    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print('The count of all expenses:', str(len(myBudgetList)))

if __name__ == "__main__":
    main()
def get_currency_input(message):
    while True:
        currency_input = input(message)
        try:
            currency_input = currency_input.replace(',', '.')  
            return float(currency_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def enter_income(language):
    if language == '1':
        income = float(input("Enter your monthly income (TL): "))
    else:
        income = float(input("Aylık gelirinizi girin (TL): "))
    return income

def enter_expenses(language):
    expenses = {}
    while True:
        if language == '1':
            expense_name = input("Enter the expense name (Press 'q' to quit): ")
        else:
            expense_name = input("Giderin adını girin ('q' çıkmak için): ")

        if expense_name.lower() == 'q':
            break
        
        if language == '1':
            expense_amount = float(input(f"Enter the amount for {expense_name} (TL): "))
        else:
            expense_amount = float(input(f"{expense_name} için miktarı girin (TL): "))
        
        expenses[expense_name] = expense_amount
    return expenses

def calculate_total_expenses(expenses):
    return sum(expenses.values())

def calculate_savings(income, total_expenses):
    return income - total_expenses

def generate_report(income, expenses, total_expenses, savings, usd_rate, euro_rate, language):
    if language == '1':
        report = f"--- Expense Report ---\nMonthly Income (TL): {income}\nExpenses:\n"
        for expense_name, amount in expenses.items():
            report += f"- {expense_name}: {amount} TL\n"
        report += f"Total Expenses (TL): {total_expenses}\nSavings (TL): {savings}\n"
        report += f"Savings (USD): {savings / usd_rate:.2f} (TL: {savings})\n"
        report += f"Savings (EURO): {savings / euro_rate:.2f} (TL: {savings})\n"
    else:
        report = f"--- Gider Raporu ---\nAylık Gelir (TL): {income}\nGiderler:\n"
        for expense_name, amount in expenses.items():
            report += f"- {expense_name}: {amount} TL\n"
        report += f"Toplam Gider (TL): {total_expenses}\nBirikim (TL): {savings}\n"
        report += f"Birikim (USD): {savings / usd_rate:.2f} (TL: {savings})\n"
        report += f"Birikim (EURO): {savings / euro_rate:.2f} (TL: {savings})\n"
    return report

def save_report(report):
    with open('report.txt', 'w') as file:
        file.write(report)
    print("Report saved to 'report.txt' file / Rapor 'report.txt' dosyasına kaydedildi.")

def create_expense_report(language):
    if language == '1':
        print("You selected English. Proceeding in English.")
        usd_rate = get_currency_input("Enter the current USD rate (TL): ")
        euro_rate = get_currency_input("Enter the current EURO rate (TL): ")
    else:
        print("Türkçe seçtiniz. Türkçe olarak devam ediliyor.")
        usd_rate = get_currency_input("Güncel USD kuru (TL): ")
        euro_rate = get_currency_input("Güncel EURO kuru (TL): ")

    income = enter_income(language)
    expenses = enter_expenses(language)
    total_expenses = calculate_total_expenses(expenses)
    savings = calculate_savings(income, total_expenses)
    
    report = generate_report(income, expenses, total_expenses, savings, usd_rate, euro_rate, language)
    save_report(report)

# Dil seçimi yap
language = input("Select your language (1 for English / 2 for Türkçe): ")

# Rapor oluştur
create_expense_report(language)

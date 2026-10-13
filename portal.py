USERS = {"SP24-BSE-056": "demo123"}
FEE_DUE = 50000

def login(roll_no, password):
    if not password:
        return "Password required"
    if USERS.get(roll_no) != password:
        return "Invalid credentials"
    return "Login successful"

def pay_fee(amount, fee_due=FEE_DUE):
    if amount <= 0:
        return "Invalid amount", fee_due
    if amount > fee_due:
        return "Overpayment rejected", fee_due
    balance = fee_due - amount
    if balance == 0:
        return "Paid", 0
    return "Partially paid", balance
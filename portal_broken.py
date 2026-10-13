USERS = {"SP24-BSE-056": "demo123"}
FEE_DUE = 50000

def login(roll_no, password):
    # BUG 1: Missing empty password check
    if USERS.get(roll_no) != password:
        return "Invalid credentials"
    return "Login successful"

def pay_fee(amount, fee_due=FEE_DUE):
    # BUG 2: Wrong validation order - allows overpayment
    if amount > fee_due:
        return "Overpayment rejected", fee_due
    # BUG 3: Missing zero/negative amount check
    balance = fee_due - amount
    if balance == 0:
        return "Paid", 0
    return "Partially paid", balance
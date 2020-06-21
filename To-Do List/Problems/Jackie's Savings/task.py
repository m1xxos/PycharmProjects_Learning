def final_deposit_amount(*interest, amount=1000):
    for inter in interest:
        amount *= (inter / 100 + 1)
    return round(amount, 2)

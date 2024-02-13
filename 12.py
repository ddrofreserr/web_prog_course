def get_balance(name, transactions):
    return sum([rec['amount'] for rec in transactions if rec['name'] == name])


def count_debts(names, amount, transactions):
    ans = dict()
    for pers in names:
        pers_deposit = get_balance(pers, transactions)
        if pers_deposit >= amount:
            ans[pers] = 0
        else:
            ans[pers] = amount - pers_deposit
    return ans

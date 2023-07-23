from bank.models import CreditOffer, Credit, Payment
import math


def generate_payment_list(сredit, creditOffer):
    p = сredit.interest_rate / 12 / 100
    monthly_payment = round(creditOffer.amount_credit *
                            (p * math.pow((1 + p), creditOffer.credit_term) /
                             ((math.pow((1 + p), creditOffer.credit_term) - 1))), 2)
    # interestTotal = 0
    summary = creditOffer.amount_credit
    payment_list = []
    for i in range(1, creditOffer.credit_term + 1):
        interest_amount = p * summary
        principal_amount = monthly_payment - interest_amount
        summary -= principal_amount
        payment_list.append(Payment(i, monthly_payment, principal_amount, interest_amount))

    return payment_list

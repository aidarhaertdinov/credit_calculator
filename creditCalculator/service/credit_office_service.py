from bank.models import CreditOffer, Credit, Payment
import math


def generate_payment_list(сredit, creditOffer):
    p = сredit.interest_rate / 12 / 100
    monthly_payment = round(creditOffer.credit_amount *
                            (p * math.pow((1 + p), creditOffer.credit_term) /
                             ((math.pow((1 + p), creditOffer.credit_term) - 1))), 2)
    # interestTotal = 0
    summary = creditOffer.credit_amount
    payment_list = []
    for i in range(1, creditOffer.credit_term + 1):
        interest_amount = round(p * summary, 2)
        principal_amount = round(monthly_payment - interest_amount, 2)
        summary -= principal_amount
        payment = Payment(i, creditOffer.credit_date, monthly_payment, principal_amount, interest_amount)
        payment.save()
        payment_list.append(payment)

    return payment_list

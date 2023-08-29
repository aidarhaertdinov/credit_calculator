from bank.models import Payment
import math
from dateutil.relativedelta import relativedelta


def generate_payment_list_for_credit_offer(creditOffer):

    p = creditOffer.interest_rate / 12 / 100
    monthly_payment = round(creditOffer.credit_amount *
                            (p * math.pow((1 + p), creditOffer.credit_term) /
                             (math.pow((1 + p), creditOffer.credit_term) - 1)), 2)
    summary = creditOffer.credit_amount
    payment_list = []
    for i in range(1, creditOffer.credit_term + 1):
        interest_amount = math.floor(p * summary)
        principal_amount = monthly_payment - interest_amount
        summary = round(summary - principal_amount, 2)
        payment = Payment(date=creditOffer.credit_date + relativedelta(months=i),
                          payment_amount=monthly_payment,
                          principal_amount=principal_amount,
                          interest_amount=interest_amount,
                          debt_balance=summary)
        payment_list.append(payment)

    return payment_list

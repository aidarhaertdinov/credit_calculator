from bank.models import Payment
import math
from dateutil.relativedelta import relativedelta
import bank


def generate_payment_list_for_credit(сredit, creditOffer):

    bank.views.payment_view.delete_payment(сredit)
    p = creditOffer[0].interest_rate / 12 / 100
    monthly_payment = round(сredit.credit_amount *
                            (p * math.pow((1 + p), сredit.credit_term) /
                             (math.pow((1 + p), сredit.credit_term) - 1)), 2)
    summary = сredit.credit_amount
    payment_list = []
    for i in range(1, сredit.credit_term + 1):
        interest_amount = math.floor(p * summary)
        principal_amount = round(monthly_payment - interest_amount, 2)
        summary = round(summary - principal_amount, 2)
        payment = Payment(date=сredit.credit_date + relativedelta(months=i),
                          payment_amount=monthly_payment,
                          principal_amount=principal_amount,
                          interest_amount=interest_amount,
                          debt_balance=summary,
                          credit=сredit)
        payment_list.append(payment)
    payment_save(payment_list)

    return payment_list


def payment_save(payment_list):

    return Payment.objects.bulk_create(payment_list)

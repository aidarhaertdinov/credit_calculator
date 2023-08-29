from django.core.paginator import Paginator
from django.shortcuts import render

from bank.models import CreditOffer, Credit, Payment
from service.credit_office_service import generate_payment_list_for_credit_offer
from service.credit_service import generate_payment_list_for_credit


class PaymentView:

    def get_payment_for_credit_offer(request, credit_offer_id):
        credit_offer = CreditOffer.objects.get(credit_offer_id=credit_offer_id)
        list_payments = generate_payment_list_for_credit_offer(credit_offer)

        return render(request, 'payment/payments.html', {"list_payments": list_payments})

    def get_payment_for_credit(request, credit_id):
        credit = Credit.objects.get(credit_id=credit_id)
        credit_offer = CreditOffer.objects.filter(credit=credit)
        list_payments = generate_payment_list_for_credit(credit, credit_offer)

        return render(request, 'payment/payments.html', {'list_payments': list_payments})

    def delete_payment(credit):
        return Payment.objects.filter(credit=credit).delete()
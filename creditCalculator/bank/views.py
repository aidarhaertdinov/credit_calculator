import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from bank.models import Bank, CreditOffer, Credit, Client, Payment
from creditCalculator.serializers import CreditSerializer, CreditOfferSerializer, ClientSerializer, BankSerializer, \
    PaymentSerializer
from service.credit_office_service import generate_payment_list
from .forms import BankForm


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class BankViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CreditOfferViewSet(ModelViewSet):
    queryset = CreditOffer.objects.all()
    serializer_class = CreditOfferSerializer


class CreditViewSet(ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create_payment(self):
        credit_offer = CreditOffer.objects.first()
        credit = Credit.objects.first()
        list_payments = generate_payment_list(credit, credit_offer)

        return list_payments


def get_payment(request):
    list_payments = Payment.objects.all()

    return render(request, 'payment/payments.html', {'list_payments': list_payments})


def home(request):
    return render(request, 'base.html')


def create_bank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = Bank()
            bank.name = form.cleaned_data['name']
            bank.save()
            return HttpResponseRedirect('/')
    else:
        form = BankForm()
    return render(request, "bank/bank.html", {"form": form})

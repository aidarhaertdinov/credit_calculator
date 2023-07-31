import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from bank.models import Bank, CreditOffer, Credit, Client, Payment
from creditCalculator.serializers import CreditSerializer, CreditOfferSerializer, \
    ClientSerializer, BankSerializer, PaymentSerializer
from service.credit_office_service import generate_payment_list
from .forms import BankForm, ClientForm, CreditForm, CreditOfferForm


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


def home(request):
    return render(request, 'base.html')


def get_payment(request):
    credit_offer = CreditOffer.objects.first()
    credit = Credit.objects.filter(credit_offer=credit_offer)
    list_payments = generate_payment_list(credit, credit_offer)

    return render(request, 'payment/payments.html', {'list_payments': list_payments})


def delete_payment(credit_offer):
    return Payment.objects.filter(credit_offer=credit_offer).delete()


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


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = Client()
            client.name = form.cleaned_data['last_name']
            client.name = form.cleaned_data['first_name']
            client.name = form.cleaned_data['patronymic']
            client.name = form.cleaned_data['phone_number']
            client.name = form.cleaned_data['email']
            client.name = form.cleaned_data['passport_series_number']
            client.save()
            return HttpResponseRedirect('/')
    else:
        form = ClientForm()
    return render(request, "client/client.html", {"form": form})


def create_credit(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            credit = Credit()
            credit.name = form.cleaned_data['credit_limit']
            credit.name = form.cleaned_data['interest_rate']
            credit.save()
            return HttpResponseRedirect('/')
    else:
        form = CreditForm()
    return render(request, "credit/credit.html", {"form": form})


def create_credit_offer(request):
    if request.method == 'POST':
        form = CreditOfferForm(request.POST)
        if form.is_valid():
            credit = CreditOffer()
            credit.name = form.cleaned_data['credit_term']
            credit.name = form.cleaned_data['credit_amount']
            credit.name = form.cleaned_data['credit_date']
            credit.save()
            return HttpResponseRedirect('/')
    else:
        form = CreditOfferForm()
    return render(request, "credit_offer/credit_offer.html", {"form": form})

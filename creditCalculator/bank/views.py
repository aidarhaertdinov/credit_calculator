import json

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from bank.models import Bank, CreditOffer, Credit, Client, Payment
from creditCalculator.serializers import CreditSerializer, CreditOfferSerializer, \
    ClientSerializer, BankSerializer, PaymentSerializer
from service.credit_office_service import generate_payment_list_for_credit_offer
from service.credit_service import generate_payment_list_for_credit
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


def get_payment_for_credit_offer(request, credit_offer_id):
    credit_offer = CreditOffer.objects.get(credit_offer_id=credit_offer_id)
    list_payments = generate_payment_list_for_credit_offer(credit_offer)

    return render(request, 'payment/payments.html', {'list_payments': list_payments})


def get_payment_for_credit(request, credit_id):
    credit = Credit.objects.get(credit_id=credit_id)
    credit_offer = CreditOffer.objects.filter(credit=credit)
    list_payments = generate_payment_list_for_credit(credit, credit_offer)

    return render(request, 'payment/payments.html', {'list_payments': list_payments})


def delete_payment(credit):
    return Payment.objects.filter(credit=credit).delete()


def get_banks(request):
    banks = Bank.objects.all()
    return render(request, "bank/banks.html", {"banks": banks})


def create_bank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BankForm()
    return render(request, "bank/post_bank.html", {"form": form})


def edit_bank(request, bank_id):
    bank = get_object_or_404(Bank, bank_id=bank_id)
    if request.method == "POST":
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = BankForm(instance=bank)
    return render(request, "bank/post_bank.html", {"form": form})


def delete_bank(request, bank_id):
    try:
        bank = Bank.objects.get(bank_id=bank_id)
        bank.delete()
        return HttpResponseRedirect("/")
    except Bank.DoesNotExist:
        return HttpResponseNotFound("<h2>Bank not found</h2>")


def get_clients(request):
    clients = Client.objects.all()
    return render(request, "client/clients.html", {"clients": clients})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ClientForm()
    return render(request, "client/post_client.html", {"form": form})


def edit_client(request, client_id):
    client = get_object_or_404(Client, client_id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ClientForm(instance=client)
    return render(request, "client/post_client.html", {"form": form})


def delete_client(request, client_id):
    try:
        client = Client.objects.get(client_id=client_id)
        client.delete()
        return HttpResponseRedirect("/")
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def get_credits(request):
    credits = Credit.objects.all()
    return render(request, "credit/credits.html", {"credits": credits})


def create_credit(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreditForm()
    return render(request, "credit/post_credit.html", {"form": form})


def edit_credit(request, credit_id):
    credit = get_object_or_404(Credit, credit_id=credit_id)
    if request.method == "POST":
        form = CreditForm(request.POST, instance=credit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = CreditForm(instance=credit)
    return render(request, "credit/post_credit.html", {"form": form})


def delete_credit(request, credit_id):
    try:
        credit = Credit.objects.get(credit_id=credit_id)
        credit.delete()
        return HttpResponseRedirect("/")
    except Credit.DoesNotExist:
        return HttpResponseNotFound("<h2>Credit not found</h2>")


def get_credit_offer(request):
    credit_offers = CreditOffer.objects.all()
    return render(request, "credit_offer/credit_offers.html",
                  {"credit_offers": credit_offers})


def create_credit_offer(request):
    if request.method == 'POST':
        form = CreditOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = CreditOfferForm()
    return render(request, "credit_offer/post_credit_offer.html", {"form": form})


def edit_credit_offer(request, credit_offer_id):
    credit_offer = get_object_or_404(CreditOffer, credit_offer_id=credit_offer_id)
    if request.method == "POST":
        form = CreditOfferForm(request.POST, instance=credit_offer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = CreditOfferForm(instance=credit_offer)
    return render(request, "credit_offer/post_credit_offer.html", {"form": form})


def delete_credit_offer(request, credit_offer_id):
    try:
        credit_offer = CreditOffer.objects.get(credit_offer_id=credit_offer_id)
        credit_offer.delete()
        return HttpResponseRedirect("/")
    except CreditOffer.DoesNotExist:
        return HttpResponseNotFound("<h2>CreditOffer not found</h2>")

import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from bank.models import Bank, CreditOffer, Credit, Client
from creditCalculator.serializers import CreditSerializer, CreditOfferSerializer, ClientSerializer, BankSerializer
from service.credit_office_service import generate_payment_list

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

    def get_payment(self):
        credit_offer = CreditOffer.objects.first()
        credit = Credit.objects.first()
        list_payment = generate_payment_list(credit, credit_offer)

        return Response({"payment": list_payment})




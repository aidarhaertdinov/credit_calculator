
from rest_framework.viewsets import ModelViewSet
from bank.models import Bank, CreditOffer, Credit, Client, Payment
from creditCalculator.serializers import CreditSerializer, CreditOfferSerializer, \
    ClientSerializer, BankSerializer, PaymentSerializer


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

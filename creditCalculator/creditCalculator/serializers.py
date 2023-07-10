from rest_framework.serializers import ModelSerializer
from bank.models import Bank, CreditOffer, Credit, Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class CreditOfferSerializer(ModelSerializer):
    class Meta:
        model = CreditOffer
        fields = '__all__'


class CreditSerializer(ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'




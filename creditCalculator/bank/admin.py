from django.contrib import admin

from bank.models import Bank, CreditOffer, Credit, Client

admin.site.register(Bank)
admin.site.register(CreditOffer)
admin.site.register(Credit)
admin.site.register(Client)
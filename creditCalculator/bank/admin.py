from django.contrib import admin

from bank.models import Bank, CreditOffer, Credit, Client, Payment

admin.site.register(Bank)
admin.site.register(CreditOffer)
admin.site.register(Credit)
admin.site.register(Client)
admin.site.register(Payment)
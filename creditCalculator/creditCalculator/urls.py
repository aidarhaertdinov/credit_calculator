"""
URL configuration for creditCalculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bank.views.view import home
from bank.views.api_view import ClientViewSet, BankViewSet, CreditOfferViewSet, CreditViewSet, \
    PaymentViewSet
from bank.views.credit_offer_view import CreditOfferView
from bank.views.credit_view import CreditView
from bank.views.bank_view import BankView
from bank.views.client_view import ClientView
from bank.views.payment_view import PaymentView

router = DefaultRouter()
router.register(r'api/v1/clients', ClientViewSet)
router.register(r'api/v1/banks', BankViewSet)
router.register(r'api/v1/credit_offers', CreditOfferViewSet)
router.register(r'api/v1/credits', CreditViewSet)
router.register(r'api/v1/payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls', namespace='users')),

    path('create_bank/', BankView.create_bank, name='create_bank'),
    path('get_banks/', BankView.get_banks, name='get_banks'),
    path("edit_bank/<int:bank_id>/", BankView.edit_bank, name='edit_bank'),
    path("delete_bank/<int:bank_id>/", BankView.delete_bank, name='delete_bank'),

    path('create_client/', ClientView.create_client, name='create_client'),
    path('get_clients/', ClientView.get_clients, name='get_clients'),
    path("edit_client/<int:client_id>/", ClientView.edit_client, name='edit_client'),
    path("delete_client/<int:client_id>/", ClientView.delete_client, name='delete_client'),

    path('get_credits/', CreditView.get_credits, name='get_credits'),
    path('create_credit/', CreditView.create_credit, name='create_credit'),
    path("edit_credit/<int:credit_id>/", CreditView.edit_credit, name='edit_credit'),
    path("delete_credit/<int:credit_id>/", CreditView.delete_credit, name='delete_credit'),

    path('get_credit_offer/', CreditOfferView.get_credit_offers, name='get_credit_offer'),
    path('create_credit_offer/', CreditOfferView.create_credit_offer, name='create_credit_offer'),
    path("edit_credit_offer/<int:credit_offer_id>/", CreditOfferView.edit_credit_offer, name='edit_credit_offer'),
    path("delete_credit_offer/<int:credit_offer_id>/", CreditOfferView.delete_credit_offer, name='delete_credit_offer'),

    path('get_payment_credit/<int:credit_id>/', PaymentView.get_payment_for_credit, name='get_payment_for_credit'),
    path('get_payment_credit_offer/<int:credit_offer_id>/', PaymentView.get_payment_for_credit_offer,
         name='get_payment_for_credit_offer'),

]

urlpatterns += router.urls

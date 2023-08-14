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
from django.urls import path
from rest_framework.routers import DefaultRouter
from bank.views import ClientViewSet, BankViewSet, CreditOfferViewSet, CreditViewSet, \
    PaymentViewSet, get_payment_for_credit_offer, home, create_bank, create_client, create_credit, create_credit_offer, \
    get_clients, \
    edit_client, delete_client, get_banks, edit_bank, delete_bank, get_credits, edit_credit, delete_credit, \
    get_credit_offer, delete_credit_offer, edit_credit_offer, get_payment_for_credit
from bank import views

router = DefaultRouter()
router.register(r'api/v1/clients', ClientViewSet)
router.register(r'api/v1/banks', BankViewSet)
router.register(r'api/v1/credit_offers', CreditOfferViewSet)
router.register(r'api/v1/credits', CreditViewSet)
router.register(r'api/v1/payments', PaymentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('create_bank/', create_bank, name='create_bank'),
    path('get_banks/', get_banks, name='get_banks'),
    path("edit_bank/<int:bank_id>/", edit_bank, name='edit_bank'),
    path("delete_bank/<int:bank_id>/", delete_bank, name='delete_bank'),


    path('create_client/', create_client, name='create_client'),
    path('get_clients/', get_clients, name='get_clients'),
    path("edit_client/<int:client_id>/", edit_client, name='edit_client'),
    path("delete_client/<int:client_id>/", delete_client, name='delete_client'),

    path('get_credits/', get_credits, name='get_credits'),
    path('create_credit/', create_credit, name='create_credit'),
    path("edit_credit/<int:credit_id>/", edit_credit, name='edit_credit'),
    path("delete_credit/<int:credit_id>/", delete_credit, name='delete_credit'),

    path('get_credit_offer/', get_credit_offer, name='get_credit_offer'),
    path('create_credit_offer/', create_credit_offer, name='create_credit_offer'),
    path("edit_credit_offer/<int:credit_offer_id>/", edit_credit_offer, name='edit_credit_offer'),
    path("delete_credit_offer/<int:credit_offer_id>/", delete_credit_offer, name='delete_credit_offer'),

    path('get_payment_credit/<int:credit_id>/', get_payment_for_credit, name='get_payment_for_credit'),
    path('get_payment_credit_offer/<int:credit_offer_id>/', get_payment_for_credit_offer,
         name='get_payment_for_credit_offer'),


]

urlpatterns += router.urls
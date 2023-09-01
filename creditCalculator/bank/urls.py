from django.urls import path

from bank.views.bank_view import create_bank, get_banks, edit_bank, delete_bank, get_all_banks_clients
from bank.views.client_view import create_client, get_clients, edit_client, delete_client
from bank.views.credit_offer_view import get_credit_offers, create_credit_offer, edit_credit_offer, delete_credit_offer
from bank.views.credit_view import get_credits, create_credit, edit_credit, delete_credit
from bank.views.payment_view import get_payment_for_credit, get_payment_for_credit_offer

app_name = 'bank'

urlpatterns = [

    path('create_bank/', create_bank, name='create_bank'),
    path('get_banks/', get_banks, name='get_banks'),
    path("edit_bank/<int:bank_id>/", edit_bank, name='edit_bank'),
    path("delete_bank/<int:bank_id>/", delete_bank, name='delete_bank'),
    path("get_all_banks_clients/<int:bank_id>/", get_all_banks_clients, name='get_all_banks_clients'),

    path('create_client/', create_client, name='create_client'),
    path('get_clients/', get_clients, name='get_clients'),
    path("edit_client/<int:client_id>/", edit_client, name='edit_client'),
    path("delete_client/<int:client_id>/", delete_client, name='delete_client'),

    path('get_credits/', get_credits, name='get_credits'),
    path('create_credit/', create_credit, name='create_credit'),
    path("edit_credit/<int:credit_id>/", edit_credit, name='edit_credit'),
    path("delete_credit/<int:credit_id>/", delete_credit, name='delete_credit'),

    path('get_credit_offer/', get_credit_offers, name='get_credit_offer'),
    path('create_credit_offer/', create_credit_offer, name='create_credit_offer'),
    path("edit_credit_offer/<int:credit_offer_id>/", edit_credit_offer, name='edit_credit_offer'),
    path("delete_credit_offer/<int:credit_offer_id>/", delete_credit_offer, name='delete_credit_offer'),

    path('get_payment_credit/<int:credit_id>/', get_payment_for_credit, name='get_payment_for_credit'),
    path('get_payment_credit_offer/<int:credit_offer_id>/', get_payment_for_credit_offer,
         name='get_payment_for_credit_offer'),

]
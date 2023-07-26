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
    PaymentViewSet, get_payment, home, create_bank
from bank import views

router = DefaultRouter()
router.register(r'api/v1/clients', ClientViewSet)
router.register(r'api/v1/banks', BankViewSet)
router.register(r'api/v1/credit_offers', CreditOfferViewSet)
router.register(r'api/v1/credits', CreditViewSet)
router.register(r'api/v1/payments', PaymentViewSet)
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create_bank/', create_bank),
    path('get_payment/', get_payment),
    path('create_payment/', PaymentViewSet.create_payment),


]

urlpatterns += router.urls
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
from rest_framework.routers import SimpleRouter
from bank.views import ClientViewSet, BankViewSet, CreditOfferViewSet, CreditViewSet, PaymentViewSet
from bank import views

router = SimpleRouter()
router.register(r'api/clients', ClientViewSet)
router.register(r'api/banks', BankViewSet)
router.register(r'api/credit_offers', CreditOfferViewSet)
router.register(r'api/credits', CreditViewSet)
# router.register(r'api/get_payment', PaymentViewSet)
#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get_payment/', views.PaymentViewSet.get_payment),

]

urlpatterns += router.urls
"""djangoPharmShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from djangoPharmShop.views import index, AboutView, CartView, ContactView, ShopView, ShopSingleView, ThankyouView, \
    CheckoutView, ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('cart/', CartView.as_view(), name='cart'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop-single/<int:pk>/', ShopSingleView.as_view(), name='shop-single'),
    path('thankyou/', ThankyouView.as_view(), name='thankyou'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]


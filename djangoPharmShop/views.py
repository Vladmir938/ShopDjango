from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView, DetailView
from products.models import Products

def index(request):
    return HttpResponse(render_to_string('index.html'))

class AboutView(TemplateView):
    template_name = 'about.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class ShopView(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        return context

class ShopSingleView(DetailView):
    template_name = 'shop-single.html'
    model = Products


class ThankyouView(TemplateView):
    template_name = 'thankyou.html'

class ProductView(DetailView):
    model = Products
    template_name = 'shop-single.html'

    def get_context_data(self, **kwargs):
        context = ShopSingleView.get_context_data(self, **kwargs)

        try:
            prod = self.request.GET['prod']
            if int(prod) == 1:
                context['products'] = Products.objects.all()
            else:
                context['products'] = Products.objects.filter(product_id=int(prod))
        except:
            context['products'] = Products.objects.all()

        context['products'] = Products.objects.all()
        return context

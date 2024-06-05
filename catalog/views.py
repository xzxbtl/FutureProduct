from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Products, NotesUser
from .forms import UserFormOrder


def main(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/catalog.html', context)


def product(request, product_slug):
    product_cart = Products.objects.get(slug=product_slug)
    context = {
        'product': product_cart,
        'title': "Cart - About"
    }
    return render(request, 'catalog/product.html', context=context)


def upload_photo(request):
    if request.method == 'POST':
        form = UserFormOrder(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            user_name = form.cleaned_data['username']
            wish = form.cleaned_data['wish']
            phone = form.cleaned_data['phone']
            image = form.cleaned_data['image']
            NotesUser.objects.create(username=user_name,
                                                first_name=first_name,
                                                phone=phone,
                                                wish=wish,
                                                images=image)
            return HttpResponseRedirect(reverse('catalog:main'))
    else:
        form = UserFormOrder()

    context = {
        "title": "Make - Order",
        'form': form
    }
    return render(request, 'catalog/user-order.html', context)

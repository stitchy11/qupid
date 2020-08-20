from django.shortcuts import render


def product(request):
    return render(request, 'shop/all_product.html')


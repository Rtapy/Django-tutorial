from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
products = {
    "Shampoo": "Hair strengthening",
    "Soap": "Infused with natural extracts",
    "Sunscreen lotion": "SPF 50+ protective agent",
    "Cosmetics": "Professional formulation",
    "Paper towels": "High absorption",
    "Disinfectant solution": "Antimicrobial effect",
    "Pistachios": "Highest quality",
    "Chocolate": "Creamy taste",
    "Coffee": "Desirable aroma and flavor",
    "Tea": "Freshness and pleasant scent",
    "Cheese": "Best choice for breakfast",
    "Olives": "Freshness and unique taste",
    "Pasta": "Easy and quick",
    "Olive oil": "Antioxidant properties",
    "Fish": "Finest fresh fish",
    "Jam": "Free from artificial additives",
    "Motor oil": "High performance",
    "Gloves": "High-quality",
    "Bag": "Suitable for everyday use",
    "Shoes": "Comfort and durability"
}


def products_list(request):
    global  products
    pro_list = list(products.keys())
    context = {
        "products": pro_list
    }
    # for product in products:
    #     url_path = reverse('products', args=[product])
    #     pro_list += f'\n<li> <a href="{url_path}"> {product} </a> </li>\n'
    #
    # content = f"<ul style='color:red'> {pro_list} </ul>"
    # return HttpResponse(content)
    return render(request, 'products/index.html', context)


def dynamic_chis_num(request, product):
    products_list = list(products.keys())
    if product > len(products_list):
        responsedata = render_to_string('404.html')
        return HttpResponseNotFound(responsedata)

    pro = products_list[product - 1]
    redirect_pro = reverse('products', args=[pro])
    return HttpResponseRedirect(redirect_pro)


def dynamic_chis(request, product):
    pros = products.get(product)
    if pros is None:
        raise Http404()
        # responsedata = render_to_string('404.html')
        # return HttpResponseNotFound(responsedata)
    context = {
        "product": pros,
        "proo": product
    }
    return render(request, 'products/products.html', context)







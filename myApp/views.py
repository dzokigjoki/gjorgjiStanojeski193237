from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from .models import Article, Category


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def product_detail(request, product_id):
    product = get_object_or_404(Article, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'article_detail.html', context)

def category_page(request, category_id):
    category = get_object_or_404(Category, Q(pk=category_id) | Q(name__iexact=category_id))
    products = category.items.all()  # Access related articles using 'articles' attribute
    context = {'category': category, 'products': products}
    return render(request, 'category.html', context)


def cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})

def add_to_cart(request, product_id):
    product = Article.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    cart[product_id] = {
        'name': product.title,
        'price': product.price,
        'photo': product.thumb.url,
    }
    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart
    return redirect('cart')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')




def contact(request):
    article = Article.objects.first()  # Retrieve the first Article object
    return render(request, 'contact.html', {'article': article})



def success(request):
    return render(request, 'ordersuccess.html')



def category(request):
    return render(request, 'category.html')

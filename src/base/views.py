from django.shortcuts import render
from django.db.models import F, Prefetch, Subquery, OuterRef
from product.models import City, Product, Category, ProductImage
from user.models import User
from base.search import Search


# Create your views here.


def index(request):
    custom_word = request.GET.get('customword', None)
    city = request.GET.get('city', None)
    category = request.GET.get('category', None)

    city = int(city) if city and city.isdigit() else None
    category = int(category) if category and category.isdigit() else None

    cities = City.objects.all()
    categories = Category.objects.all()
    if city and category:
        products = Product.objects.filter(city_id=city).filter(category_id=category).select_related('category', 'user',
                                                                                                    'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    elif city:
        products = Product.objects.filter(city_id=city).select_related('category', 'user',
                                                                       'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    elif city and category and custom_word:
        products = Product.objects.filter(city_id=city).filter(category_id=category).filter(
            title__icontains=custom_word).select_related('category', 'city', 'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    elif city and custom_word:
        products = Product.objects.filter(city_id=city).filter(title__icontains=custom_word).select_related('category',
                                                                                                            'city',
                                                                                                            'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    elif category and custom_word:
        products = Product.objects.filter(category_id=category).filter(title__icontains=custom_word).select_related(
            'category',
            'city',
            'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    elif category:
        products = Product.objects.filter(category_id=category).select_related('category', 'user',
                                                                               'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    elif custom_word:
        products = Product.objects.filter(title__icontains=custom_word).select_related('category',
                                                                                       'city',
                                                                                       'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    else:
        products = Product.objects.select_related('category', 'user', 'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )

    _format_products = []
    for i in products:
        _format_products.append({
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'price': i.price,
            'user': i.user.username,
            'city': i.city.name,
            'category': i.category.name,
            'parent_category': i.parent_category_name,
            'discount': i.discount,
            'image': i.productimage_set.all()[0].image
        })

    context = {
        "cities": cities,
        "categories": categories,
        "products": _format_products,
        "selected_ctg": category,
        "selected_city": city,
        "custom_word": custom_word,

    }
    return render(request, 'index.html', context)


def category(request):
    print(request.GET)
    custom_word = request.GET.get('customword', None)
    city = request.GET.get('city', None)
    category = request.GET.get('category', None)

    city = int(city) if city and city.isdigit() else None
    category = int(category) if category and category.isdigit() else None

    cities = City.objects.all()
    categories = Category.objects.all()
    if city and category:
        products = Product.objects.filter(city_id=city).filter(category_id=category).select_related('category', 'user',
                                                                                                    'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    elif city:
        products = Product.objects.filter(city_id=city).select_related('category', 'user',
                                                                       'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    elif city and category and custom_word:
        products = Product.objects.filter(city_id=city).filter(category_id=category).filter(
            title__icontains=custom_word).select_related('category', 'city', 'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    elif city and custom_word:
        products = Product.objects.filter(city_id=city).filter(title__icontains=custom_word).select_related('category',
                                                                                                            'city',
                                                                                                            'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    elif category and custom_word:
        products = Product.objects.filter(category_id=category).filter(title__icontains=custom_word).select_related(
            'category',
            'city',
            'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    elif category:
        products = Product.objects.filter(category_id=category).select_related('category', 'user',
                                                                               'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    elif custom_word:
        products = Product.objects.filter(title__icontains=custom_word).select_related('category',
                                                                                       'city',
                                                                                       'user').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')))
    else:
        products = Product.objects.select_related('category', 'user', 'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )

    _format_products = []
    for i in products:
        _format_products.append({
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'price': i.price,
            'user': i.user.username,
            'city': i.city.name,
            'category': i.category.name,
            'parent_category': i.parent_category_name,
            'discount': i.discount,
            'image': i.productimage_set.all()[0].image
        })

    context = {
        "cities": cities,
        "categories": categories,
        "products": _format_products,
        "selected_ctg": category,
        "selected_city": city,
        "custom_word": custom_word,

    }
    return render(request, 'category.html', context)


def errors(request):
    return render(request, '404.html', {})


def home_2(request):
    return render(request, 'index-2.html', {})


def home_3(request):
    return render(request, 'index-3.html', {})


def adlistinggrid(request):
    return render(request, 'adlistinggrid.html', {})


def adlistinglist(request):
    return render(request, 'adlistinglist.html', {})


def adsdetails(request, pk):
    one_products = Product.objects.filter(id=pk).select_related('category', 'user', 'city').prefetch_related(
        Prefetch('productimage_set', queryset=ProductImage.objects.all())
    ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
    )

    one_format_product = []
    for i in one_products:
        images = [image.image for image in i.productimage_set.all()]
        condition_choice = dict(Product.CHOICES).get(i.condition)
        for j in images:
            print(j)
        one_format_product.append({
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'price': i.price,
            'user': i.user.username,
            'phone_number': i.user.phone_number,
            'user_image': i.user.photo,
            'status': i.status,
            'created_date': i.created_date,
            'city': i.city.name,
            'category': i.category.name,
            'parent_category': i.parent_category_name,
            'discount': i.discount,
            'image': images,
            'condition': condition_choice
        })

    products = Product.objects.select_related('category', 'user', 'city').prefetch_related(
        Prefetch('productimage_set', queryset=ProductImage.objects.all())
    ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
    )

    _format_products = []
    for i in products:
        _format_products.append({
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'price': i.price,
            'user': i.user.username,
            'city': i.city.name,
            'category': i.category.name,
            'parent_category': i.parent_category_name,
            'discount': i.discount,
            'image': i.productimage_set.all()[0].image
        })

    context = {
        "selected_products": one_format_product,
        "products": _format_products

    }
    print(context['selected_products'])
    return render(request, 'ads-details.html', context)


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def post_ads(request):
    return render(request, 'create.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def testimonial(request):
    return render(request, 'testimonial.html', {})


def faq(request):
    return render(request, 'faq.html', {})


def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def login(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})


def privacy_setting(request):
    return render(request, 'privacy-setting.html', {})


def account_profile_setting(request):
    return render(request, 'account-profile-setting.html', {})


def account_myads(request):
    return render(request, 'account-myads.html', {})


def payments(request):
    return render(request, 'payments.html', {})


def account_favourite_ads(request):
    return render(request, 'account-favourite-ads.html', {})


def privacy_setting(request):
    return render(request, 'privacy-setting.html', {})


def offermessages(request):
    return render(request, 'offermessages.html', {})

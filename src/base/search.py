from django.shortcuts import render
from django.db.models import F, Prefetch, Subquery, OuterRef
from product.models import City, Product, Category, ProductImage
from user.models import User


def Search(request, url=""):
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

    return render(request, url, context)

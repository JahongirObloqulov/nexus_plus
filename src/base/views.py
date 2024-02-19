from django.shortcuts import render
from product.models import City, Category

# Create your views here.


def index(request):
    cities = City.objects.all()
    categories = Category.objects.all()
    context = {
        "cities": cities,
        "categories": categories
    }
    return render(request, "index.html", context)


def category(request):
    cities = City.objects.all()
    categories = Category.objects.all()
    context = {
        "cities": cities,
        "categories": categories
    }
    return render(request, "category.html", context)


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


def adsdetails(request):
    return render(request, 'ads-details.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def post_ads(request):
    return render(request, 'post-ads.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def testimonial(request):
    return render(request, 'testimonial.html', {})


def faq(request):
    return render(request, 'faq.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html', {})


def blog_grid_full_width(request):
    return render(request, 'blog-grid-full-width.html', {})


def single_post(request):
    return render(request, 'single-post.html', {})


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

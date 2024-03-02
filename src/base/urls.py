from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/list/', views.category, name="category"),
    path('errors/', views.errors, name="errors"),
    path('home_2/', views.home_2, name='home_2'),
    path('home_3/', views.home_3, name='home_3'),
    path('adlistinggrid/', views.adlistinggrid, name='adlistinggrid'),
    path('adlistinglist/', views.adlistinglist, name='adlistinglist'),
    path('<int:product_id>/adsdetails/', views.adsdetails, name='adsdetails'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('post_ads/', views.post_ads, name='post-ads'),
    path('pricing/', views.pricing, name='pricing'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('blog_left_sidebar/', views.blog_left_sidebar, name='blog-left-sidebar'),
    path('blog_grid_full_width/', views.blog_grid_full_width, name='blog-grid-full-width'),
    path('single_post/', views.single_post, name='single-post'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('privacy_setting/', views.privacy_setting, name='privacy-setting'),
    path('account_myads/', views.account_myads, name='account-myads'),
    path('payments/', views.payments, name='payments'),
    path('account_favourite_ads/', views.account_favourite_ads, name='account-favourite-ads'),
    path('account_profile_setting/', views.account_profile_setting, name='account-profile-setting'),
    path('offermessages/', views.offermessages, name='offermessages')
]
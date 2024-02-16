from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/', views.category, name="category"),
    path('errors/', views.errors, name="errors"),
    path('home_2/', views.home_2, name='home_2'),
    path('home_3/', views.home_3, name='home_3'),
    path('adlistinggrid/', views.adlistinggrid, name='adlistinggrid'),
    path('adlistinglist/', views.adlistinglist, name='adlistinglist'),
    path('adsdetails/', views.adsdetails, name='adsdetails'),
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
]
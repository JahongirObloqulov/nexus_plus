from django.shortcuts import render
from .forms import ProductForm, ProductImageFormset
from .models import ProductImage
# Create your views here.


def product_create(request):
    form = ProductForm()
    if request.POST:
        form = ProductForm(request.POST or None)
        # formset = ProductImageFormset()
        if form.is_valid():
            product = form.save()
            files = request.POST.getlist('file')
            for file in files:
                ProductImage.objects.create(
                    product=product,
                    image=file
                )
    context = {
        "form": form,
        # "formset": formset
    }
    return render(request, 'create.html', context)

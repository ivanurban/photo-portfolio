from django.shortcuts import render

from .models import Images

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def image_list(request):
    #images = Images.objects.all()
    object_list = Images.objects.all()

    paginator = Paginator(object_list, 12)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)


    return render(request, 'gallery/image/image_list.html', {'page': page, 'images': images})
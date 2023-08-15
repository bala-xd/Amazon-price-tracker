from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Link
from .forms import AddLinkForm
from django.views.generic import DeleteView

def home_view(request):
    discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = 'couldnt get the price..'
        except:
            error = 'Something went wrong...'
    form = AddLinkForm()
    qs = Link.objects.all()
    items = qs.count()

    if items > 0:
        disc_list = []
        for i in qs:
            if i.old > i.cur:
                disc_list.append(i)
            discounted = len(disc_list)

    context = {
        'qs':qs,
        'items_no': items,
        'no_discounted': discounted,
        'form': form,
        'error': error,
    }

    return render(request, 'main.html', context)

class delete_view(DeleteView):
    model = Link
    template_name = 'confirm_del.html'
    success_url = reverse_lazy('home')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')
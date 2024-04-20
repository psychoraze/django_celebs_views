from django.shortcuts import render, redirect
from .models import *
from .forms import CelebrityForm
from django.views.generic import *
import django.urls


def index(request):
    celebrities = Celebrity.objects.order_by("-age")
    return render(request, "index.html", {"celebrities": celebrities})


class CelebrityCreate(CreateView):
    model = Celebrity
    form_class = CelebrityForm
    template_name = "create.html"
    success_url = django.urls.reverse_lazy("index")


class CelebrityDelete(DeleteView):
    model = Celebrity
    template_name = "delete.html"
    success_url = django.urls.reverse_lazy("index")


class CelebrityUpdate(UpdateView):
    model = Celebrity
    form_class = CelebrityForm
    template_name = "update.html"
    success_url = django.urls.reverse_lazy("index")


class CelebrityList(ListView):
    model = Celebrity
    template_name = "index.html"
    context_object_name = "celebrities"


class CelebrityDetail(DetailView):
    model = Celebrity
    template_name = "detail.html"
    context_object_name = "celebrity"

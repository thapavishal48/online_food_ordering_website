from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views import View
from django.views.generic import (          #use ( ) when we to use many import
    TemplateView,
    ListView,
    DetailView,
    CreateView
)
from .models import ResturantLocation

from django.http import HttpResponseRedirect,Http404
from .forms import ResturantLocationModelForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ContactView(TemplateView):
    template_name="contact.html"

    def get_context_data(self,**kwargs):
        context={
            "resturant_name":"109 degrees",
            "items": ["veg momo","chicken momo"],
        }
        return context


def resturant_list(request):
    template_name = "resturants/resturant_list.html"
    query_set = ResturantLocation.objects.all()     # objects: select * from ResturantLocation in sql query
    context = {"resturants": query_set}
    return render(request, template_name, context)



class ResturantListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("userauth:login")
    template_name = "resturants/resturant_list.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = ResturantLocation.objects.filter(owner__username__exact=user)
        else:
            raise Http404
        return queryset



class ResturantDetailView(DetailView):
    template_name = "resturants/resturantlocation_detail.html"
    def get_object(self, queryset=None):    #here slug is used to identify theS particular resturants
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(ResturantLocation, slug=slug)
        return obj

def resturant_createview(request):
    form = ResturantLocationModelForm(request.GET or None)
    errors = ""

    print("request.POST: {}".format(request.POST))
    print("request.GET: {}".format(request.GET))
    print("Form is valid: {}".format(form.is_valid()))

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy("resturants:list"))
    if form.errors:
        errors = form.errors

    template_name = 'resturants/form.html'
    context = {"resturant_form": form, "form_error": errors}
    return render(request, template_name, context)


class ResturantCreateView(LoginRequiredMixin, CreateView):      #LoginRequireMixin
    #login_url = "/login/"
    login_url = reverse_lazy("userauth:login")
    form_class = ResturantLocationModelForm
    template_name = "resturants/form.html"
    #success_url = "/resturants/"
    success_url = reverse_lazy("resturants:list")


    def form_valid(self, form):
        instance = form.save(commit=False)  #commit=False is used to make temporarily save but not hardcoded(permanently save) in database
        instance.owner =self.request.user
        return super().form_valid(form)




class HomeTemplateView(TemplateView):
        template_name = "resturants/resturants_home.html"
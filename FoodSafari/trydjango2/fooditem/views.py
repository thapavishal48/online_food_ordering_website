from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import FoodItem
from .forms import FoodItemForm
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
class FoodItemListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy("userauth:login")
    template_name = "fooditem/list.html"
    def get_queryset(self):
        return FoodItem.objects.filter(user__username__exact=self.request.user)


class FoodItemDetailView(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy("userauth:login")
    template_name = "fooditem/detail.html"
    def get_queryset(self):
        return FoodItem.objects.filter(user__username__exact=self.request.user)

class FoodItemCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy("userauth:login")
    form_class = FoodItemForm
    template_name = "fooditem/form.html"
    success_url = reverse_lazy("fooditem:list")

    def get_form_kwargs(self):              #sending user info to form.py using form view function or class
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user =self.request.user
        return super().form_valid(form)

class FoodItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("userauth:login")
    template_name = "fooditem/form.html"
    form_class = FoodItemForm
    success_url = reverse_lazy("fooditem:list")     #reverse_lazy is used when we need only and it shows the error letter but when we used reverse then it shows the errors earlier

    def get_queryset(self):
        return FoodItem.objects.filter(user=self.request.user)

    # only for demo  not necessary to define
    def get_object(self, queryset=None):
        item_id = self.kwargs.get("pk")                #primary key
        item_detail = get_object_or_404(FoodItem, pk=item_id)
        return item_detail

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs





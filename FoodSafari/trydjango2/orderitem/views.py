from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FoodOrderedForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class FoodOrderedCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy("userauth:login")
    form_class = FoodOrderedForm
    template_name = "orderitem/form.html"
    success_url = reverse_lazy("fooditem:list")



    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user =self.request.user
        return super().form_valid(form)
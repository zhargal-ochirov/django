from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView

from .forms import PersonForm
from orders.models import Order, OrderItem


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PersonCreateView(UpdateView):
    model = User
    template_name = 'edit_profile.html'
    form_class = PersonForm
    success_url = reverse_lazy('login')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)




def profile(request):
    user = request.user
    user_orders = Order.objects.filter(account=user.pk)
    order_items = OrderItem.objects.all()
    context = {"user_orders": user_orders, "user": user, "order_items": order_items}
    return render(request, 'profile.html', context)

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import AccountCreateForm
from account.models import User


class AccountCreateView(CreateView):
    model = User
    form_class =  AccountCreateForm
    success_url = reverse_lazy('game:list')
    template_name = 'account/create.html'
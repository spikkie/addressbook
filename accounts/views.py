from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from addressbook.mixins import NextUrlMixin, RequestFormAttachMixin
from .forms import LoginForm

# Create your views here.

class LoginView( NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'login.html'
    default_next = '/posts'

    def form_valid(self, form):
        return redirect('/posts/')


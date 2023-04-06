from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import RegisterUserForm


def index(request):
    return render(request, 'main/index.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin:index')
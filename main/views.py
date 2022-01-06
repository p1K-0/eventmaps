from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from .forms import UserRegistrationForm
from django.urls import reverse


def index(request):
    return render(request, 'main/index.html')

@login_required
def dashboard(request):

    return render(request, 'main/index.html')

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # new_user.groups.add(Group.objects.get(name=request.POST.get('group')))
            login_user = authenticate(request, username=user_form.cleaned_data['username'],
                                      password=user_form.cleaned_data['password'])
            if login_user:
                login(request, login_user)
            return render(request, 'main/user-page.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'user_form': user_form})


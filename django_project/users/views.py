from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)

    if form.is_valid():
      form.save() # saving the user in DB
      
      username = form.cleaned_data.get('username')
      messages.success(request, f"Welcome {username}! You are now able to login.")

      return redirect('login')

  else:
    form = UserRegisterForm()

  # Returns empty form for GET request
  # Returns form with erros if 'is_valid' check fails
  return render(request, 'users/register.html', { 'form': form })


@login_required
def profile(request):
  u_form = UserUpdateForm()
  p_form = ProfileUpdateForm()

  context = {
    'u_form': u_form,
    'p_form': p_form
  }

  return render(request, 'users/profile.html', context)

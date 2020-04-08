from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      messages.success(request, f"Account created for {username}!")
      return redirect('blog-home')

  else:
    form = UserCreationForm()

  # Returns empty form for GET request
  # Returns form with erros if 'is_valid' check fails
  return render(request, 'users/register.html', { 'form': form })

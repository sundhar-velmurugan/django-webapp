from django.shortcuts import render

posts = [
  {
    'author': 'Sundhar',
    'title': 'Blog post 1',
    'content': 'First post content',
    'date_posted': 'August 11, 2020'
  },
  {
    'author': 'Doe',
    'title': 'Blog post 2',
    'content': 'Second post content',
    'date_posted': 'August 12, 2020'
  }
]

def home(request):
  context = {
    'posts': posts
  }

  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', { 'title': 'About' })
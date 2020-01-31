from django.shortcuts import render

posts = [
    {
        'author': 'Stevo',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'Januar 10, 2020'
    },
    {
        'author': 'Steffi',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'Januar 11, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

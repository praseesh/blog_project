from django.shortcuts import render

posts = [
    {
        'author' : 'Steve Jobs',
        'title': 'Microsoft',
        'content': 'My first post content',
        'date_posted': 'August 01, 2027'
    },
    {
        'author' : 'Tesla',
        'title': 'Electric Car',
        'content': 'Is is eco friendly',
        'date_posted': 'January 01, 2021'
    },
]

def home(request):
    context = {
        'posts' : posts
    }

    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

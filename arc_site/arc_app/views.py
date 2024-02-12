from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .models import ContactSubmission
from django.contrib import messages
from .models import ContactSubmission

# Create your views here.
#from django.http import HttpResponse

def home(request):
    return render(request, 'home2.html')

def about(request):
    return render(request, 'about.html')

def aboutex(request):
    return render(request, 'aboutex.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

#def contact(request):
 #   return render(request, 'contact.html')

# for mail
'''def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        message = request.POST.get('contact_content')

        # Save the submission to the database
        submission = ContactSubmission.objects.create(name=name, email=email, message=message)
        submission.save()

        # You can add additional logic here, e.g., send email, etc.

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_view')  # Redirect to the same page after submission

    return render(request, 'contact_form_template.html')  # Replace 'contact_form_template.html' with your actual template name'''


# contact_form_app/views.py


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        theme = request.POST.get('contact_theme')
        description = request.POST.get('contact_description')

        # Save the submission to the database
        submission = ContactSubmission.objects.create(name=name, email=email, theme=theme, description=description)
        submission.save()

        # You can add additional logic here, e.g., send email, etc.

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_view')  # Redirect to the same page after submission

    return render(request, 'contact.html')  # Replace 'contact_form_template.html' with your actual template name


from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post, Subscription
from .forms import CommentForm, PostForm
from mamasplate import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Max, Min
from django.core.exceptions import ObjectDoesNotExist
import os
from blog.utils import render_to_pdf, extract_request_variables
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required


# Create your views here.
def mail(request):
    subscriber = request.POST['recipient_email_address']
    emails = Subscription.objects.filter(address=subscriber)
    if emails:
        pass
    else:
        fan = Subscription(address=subscriber)
        fan.save()


def index(request):
    """The home page for mama's plate"""
    entries = Post.objects.order_by('-date_added')[:3]
    if request.method == 'POST':
        mail(request)
    context = {'posts': entries}
    return render(request, 'blog/index.html', context)


def blog(request):
    """The blog for Mama's plate"""
    entry_list = Post.objects.order_by('-date_added')
    paginator = Paginator(entry_list, 5)
    page = request.GET.get('page')
    entries = paginator.get_page(page)
    context = {'posts': entries}
    return render(request, 'blog/blog.html', context)


# posts
def post(request, entry_id):
    entry = Post.objects.get(id=entry_id)
    comments = entry.comments.order_by('-created_on')
    comment_form = CommentForm()
    entry_list = Post.objects.all()

    if int(entry_id) >= len(entry_list):
        try:
            pre_val = Post.objects.aggregate(Min("id"))['id__min']
            next_val = Post.objects.filter(id__lt=entry_id).order_by("-id")[0:1].get().id
            
        except ObjectDoesNotExist:
            pre_val = Post.objects.aggregate(Min("id"))['id__min']
            next_val = Post.objects.aggregate(Min("id"))['id__min']
       
    elif int(entry_id) == 1:
        try:
            next_val = Post.objects.aggregate(Max("id"))['id__max']
            pre_val = Post.objects.filter(id__gt=entry_id).order_by("id")[0:1].get().id
            
        except ObjectDoesNotExist:
            pre_val = Post.objects.aggregate(Min("id"))['id__min']
            next_val = Post.objects.aggregate(Min("id"))['id__min']

    else:
        try:
            pre_val = Post.objects.filter(id__gt=entry_id).order_by("id")[0:1].get().id
            next_val = Post.objects.filter(id__lt=entry_id).order_by("-id")[0:1].get().id
            
        except ObjectDoesNotExist:
            pre_val = Post.objects.aggregate(Min("id"))['id__min']
            next_val = Post.objects.aggregate(Min("id"))['id__min']

    previous = Post.objects.get(id=pre_val)
    next_post = Post.objects.get(id=next_val)
    context = {'entry': entry,
               'comment_form': comment_form,
               'comments': comments,
               'next': next_post,
               'previous': previous}

    return render(request, 'blog/post.html', context)


# comments
def comment(request, entry_id):
    template_name = 'blog/post.html'
    entry = Post.objects.get(id=entry_id)
    comments = entry.comments.order_by('-created_on')
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = entry
            # Save the comment to the database
            new_comment.save()
            # send mama an email

            subject = "You have a new comment"
            message = 'New comment on ' + entry.title + ' check your blog'
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            # send_mail(subject, message, from_email, to_list, fail_silently=True)

            return HttpResponseRedirect(reverse('the_blog:post', args=[entry.id]))
        else:
            comment_form = CommentForm()
        return render(request, template_name, {'entry': entry,
                                               'comments': comments,
                                               'new_comment': new_comment,
                                               'comment_form': comment_form})


def about(request):
    """The about for Mama's plate"""

    return render(request, 'blog/about.html')


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def render_pdf(request, entry_id):
    entry = Post.objects.get(id=entry_id)
    template_path = 'blog/recipe.html'
    context = {
        "serving": entry.serving,
        "ingredients": entry.ingredients,
        "instructions": entry.instructions,
        "title": entry.title,

    }
    # context = extract_request_variables(request)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' %entry.title

    template = get_template(template_path)
    html = template.render(context)
    if request.POST.get('show_html', ''):
        response['Content-Type'] = 'application/text'
        response['Content-Disposition'] = 'attachment; filename="report.txt"'
        response.write(html)
    else:
        pisaStatus = pisa.CreatePDF(
            html, dest=response, link_callback=link_callback)
        if pisaStatus.err:
            return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err,
                                                                                   html))
    return response


# CRUD Functionality

# New post view (Create new post)
@login_required()
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('the_blog:blog'))
    form = PostForm()
    return render(request, 'blog/create.html', {'form': form})  # Edit a post


@login_required()
def edit(request, pk, template_name='blog/edit.html'):
    entry = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('the_blog:blog'))
    return render(request, template_name, {'form': form})  # Delete post


@login_required()
def delete(request, entry_id):
    template_name = 'blog/post.html'
    entry = get_object_or_404(Post, pk=entry_id)
    if request.method == 'POST':
        entry.delete()
        return HttpResponseRedirect(reverse('the_blog:blog'))
    return render(request, template_name, context={'entry': entry})


def logout_request(request):

    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm, QuestionForm
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'creative_p/post_list.html', {'posts':posts})

def ask_q(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = QuestionForm()
    return render(request, 'creative_p/ask_q.html',{'form':form})


def ans_p(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            ques1 = get_object_or_404(Item, pk=request.POST.get('item_id'))
            post.ques = ques1
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'creative_p/ans_p.html',{'form':form})


def ans_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'creative_p/ans_list.html',{'posts':posts})

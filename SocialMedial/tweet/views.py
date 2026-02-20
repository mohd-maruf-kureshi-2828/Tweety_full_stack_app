from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet, Comment
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')

    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def tweet_search(request):
    query = request.GET.get('q')
    tweets = Tweet.objects.all()

    if query:
        tweets = tweets.filter(
            Q(user__username__icontains=query) |
            Q(text__icontains=query)
        )

    return render(request, 'tweet_list.html', {'tweets': tweets})


# ============================
# AJAX COMMENT (NO RELOAD)
# ============================
@login_required
def add_comment(request, tweet_id):
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, id=tweet_id)
        text = request.POST.get("comment")

        if text:
            comment = Comment.objects.create(
                tweet=tweet,
                user=request.user,
                text=text
            )

            return JsonResponse({
                "status": "success",
                "username": request.user.username,
                "text": comment.text
            })

    return JsonResponse({"status": "error"}, status=400)


# ============================
# AJAX LIKE (NO RELOAD)
# ============================
@login_required
def like_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, id=tweet_id)

        if request.user in tweet.likes.all():
            tweet.likes.remove(request.user)
            liked = False
        else:
            tweet.likes.add(request.user)
            liked = True

        return JsonResponse({
            "liked": liked,
            "total_likes": tweet.likes.count()
        })

    return JsonResponse({"error": "Invalid request"}, status=400)

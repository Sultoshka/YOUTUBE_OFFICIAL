from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Video_model, Comment
from django.shortcuts import render, redirect
from .forms import VideoForm, CommentForm, UserForm
from .models import Video_model, Comment, User
from django.contrib.auth.decorators import login_required

def add_favorite_video(request, video_id):
    video = get_object_or_404(Video_model, id=video_id)
    if video not in request.user.favorite_videos.all():
        request.user.favorite_videos.add(video)
    return redirect('video_detail', pk=video.id)

@login_required
def remove_favorite_video(request, video_id):
    video = get_object_or_404(Video_model, id=video_id)
    if video in request.user.favorite_videos.all():
        request.user.favorite_videos.remove(video)
    return redirect('video_detail', pk=video.id)

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'add_video.html', {'form': form})

def video_list(request):
    videos = Video_model.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = Video_model.objects.get(pk=pk)
    comments = Comment.objects.filter(video=video)
    return render(request, 'video_detail.html', {'video': video, 'comments': comments})

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'add_video.html', {'form': form})

def add_comment(request, pk):
    video = Video_model.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = UserForm()
    return render(request, 'register_user.html', {'form': form})

def favorite_videos(request):
    videos = request.user.favorite_videos.all()
    return render(request, 'favorite_videos.html', {'videos': videos})
# Create your views here.

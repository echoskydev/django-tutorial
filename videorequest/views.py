from django.shortcuts import render, redirect

from .models import Video

from .form import VideoForm
# Create your views here.


def index(request):
    videos = Video.objects.order_by('-date_added')
    context = {'videos': videos}
    return render(request, 'web/index.html', context)


def vrform(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():
            new_req = Video(
                videotitle=request.POST['videoname'], videodesc=request.POST['videodesc'])
            new_req.save()
            return redirect('index')
    else:
        form = VideoForm()

    context = {'form': form}

    return render(request, 'web/vrform.html', context)

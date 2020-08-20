from django.shortcuts import render


def qna(request):
    return render(request, 'community/qna.html')


def notice(request):
    return render(request, 'community/all_notice.html')


def event(request):
    return render(request, 'community/all_event.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from writer.models import 인편
from django.views.generic.edit import CreateView
from .forms import 인편작성폼
from django.utils import timezone
from . import the_campy_sender

# Create your views here.

def index(request) :
    인편_latest = 인편.objects.order_by('-작성일')[:5]
    context = {
    "인편_latest" : 인편_latest
    }
    return render(request,"index.html", context = context)

#class 인편작성(CreateView) :
    #model = 인편
   # fields = ["작성자", "제목", "내용", "작성일"]

def writer(request):
    if request.method == 'GET':
        return render(request, 'letterwrite.html')
    elif request.method == 'POST':
        작성자 = request.POST['작성자']  # 템플릿에서 입력한 name필드에 있는 값을 키값으로 받아옴
        제목 = request.POST['제목']
        내용 = request.POST['내용']

        보낼값 = 인편(  # 모델에서 생성한 클래스를 가져와 객체를 생성
            작성자=작성자,
            제목=제목,
            내용=내용,
        )

        보낼값.save()  # 데이터베이스에 저장
        the_campy_sender.send(작성자, 제목, 내용)

        return render(request, 'letterwrite.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from writer.models import 인편
from django.views.generic.edit import CreateView
from .forms import 인편작성폼
from django.utils import timezone
from . import the_campy_sender
from django.http import JsonResponse
from django.contrib import messages
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
    작성자 = request.POST['작성자']  # 템플릿에서 입력한 name필드에 있는 값을 키값으로 받아옴
    제목 = request.POST['제목']
    내용 = request.POST['내용']
    message_dict = {'작성자': 작성자, '제목': 제목, '내용': 내용}  # error handling 에 필요한 딕셔너리 만들어준거

    #if len(작성자) == 0:
        #return JsonResponse({'message' : '작성자를 입력해주세요'}, status=400)
        #message_dict['error'] = "작성자를 입력해 주세요!"  # 딕셔너리에 error 항목 추가하기
    #if 'error' in message_dict:
       # return render(request, 'letterwrite.html', message_dict)
        # message_dict 를 html 로 넘김(key 값이 탬플릿에서 사용할 변수 이름, value 값이 파이썬 변수가 됨
       # message_dict['error']
    elif request.method == 'POST':
        작성자 = request.POST['작성자']  # 템플릿에서 입력한 name필드에 있는 값을 키값으로 받아옴
        제목 = request.POST['제목']
        내용 = request.POST['내용']

        보낼값 = 인편(  # 모델에서 생성한 클래스를 가져와 객체를 생성 (모델항목과 html 에서 받아온 값을 연결해주는 역할)
            작성자=작성자,
            제목=제목,
            내용=내용,
        )

        보낼값.save()  # 데이터베이스에 저장
        the_campy_sender.send(작성자, 제목, 내용)

        return render(request, 'letterwrite.html')


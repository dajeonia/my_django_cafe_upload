from django.shortcuts import render
from django.http import HttpResponse

from board_matching.models import BoardMatching
from user_setting.models import UserSetting

def getNaverUrl(request):
    naver_id = request.GET.get('id', '')
    try:
        user_id = UserSetting.objects.get(naver_id=naver_id).id
        board = BoardMatching.objects.get(from_board_url="naver_search", user_no=user_id)
        url = board.uploaded_list.split('\n')[0]
        return HttpResponse(url, content_type='text/plane')
    except Exception as e:
        return HttpResponse("NULL", content_type='text/plane')

# Create your views here.

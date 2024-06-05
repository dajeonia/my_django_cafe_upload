from django.http import HttpResponse, JsonResponse
from .main_func import main_function
import os

def test(request):
    main_function()
    return HttpResponse(status=200)

'''
import schedule
from datetime import datetime

def test_schedule_add(request):
    schedule.clear()
    time_list = ["20:08", "20:09", "20:10", "20:11"]
    for time_str in time_list:
        schedule.every().day.at(time_str).do(test_print)
    return HttpResponse("스케줄 추가 완료")

def test_schedule_run(requests):
    schedule_run.delay()
    return HttpResponse("스케줄 실행")

# def test_schedue_off(requests):


def test_schedule_remove(request):
    schedule.clear()
    return HttpResponse("스케줄 제거 완료")

def test_print():
    print(datetime.now())
    print("테스트 출력입니다")
'''

def addCron(request):
    os.system('python manage.py crontab add')
    return HttpResponse(status=200)

def showCron(request):
    os.system('python manage.py crontab show')
    return HttpResponse(status=200)

def removeCron(request):
    os.system('python manage.py crontab remove')
    return HttpResponse(status=200)

from django.http import HttpResponse
from datetime import datetime

def current_datetime(request):
    now = datetime.now()
    return HttpResponse(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")
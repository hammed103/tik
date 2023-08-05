from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@csrf_exempt
@require_POST
def slack_events(request):
    data = json.loads(request.body)
    if data['type'] == 'event_callback' and data['event']['type'] == 'message':
        print(f"Received message: {data['event']['text']}")
    return JsonResponse({'status': 'ok'})

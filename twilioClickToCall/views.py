from django.http import HttpResponse
from django.views import View
from twilio.twiml.voice_response import VoiceResponse


class CallView(View):
    def get(self, request):
        response = VoiceResponse()
        response.dial(request.GET.get('phone_number'))
        return HttpResponse(str(response))

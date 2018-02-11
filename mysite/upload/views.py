from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from upload.models import File
from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib import messages
import requests
import json

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        result = requests.post(url, values).json()

        # result = json.load(response)
        ''' End reCAPTCHA validation '''

        if result['success']:
            School = request.POST.get('School')
            SubName = request.POST.get('SubName')
            SubCode = request.POST.get('SubCode')
            Paper = request.POST.get('Paper')
            Year = request.POST.get('Year')
            Author = request.POST.get('Author')

            myfile = request.FILES['myfile']
            aka =  myfile._size
            if aka > 10200000 :

                return render(request, 'upload/simple_upload.html',{
                    'size_not_in_limit' : True

                })
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            if Author == "" or Author == " ": Author = "Anonymus"
            f = File(uploaded_file_url=uploaded_file_url, School=School, SubName =SubName, SubCode=SubCode, Paper=Paper, Year=Year, Author=Author, pub_date=timezone.now())
            f.save()

            return render(request, 'upload/simple_upload.html', {
                'file_size':  aka,
                'uploaded_file_url': uploaded_file_url,
                'School': School,
                'SubName': SubName,
                'SubCode': SubCode,
                'Paper': Paper,
                'Year': Year,
                'Author': Author
            })
            messages.success(request, 'Thanks for your contributing, Your document has been added!')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    return render(request, 'upload/simple_upload.html')



def api(request):
    data= list(File.objects.values())
    return JsonResponse(data, safe=False)

def index(request):
    return render(request, 'upload/index.html')










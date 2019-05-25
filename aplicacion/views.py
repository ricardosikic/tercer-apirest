from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import CasoSerializer
from .models import User
from .models import Caso


# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class CasoView(viewsets.ModelViewSet):
    serializer_class = CasoSerializer
    queryset = Caso.objects.all()



def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
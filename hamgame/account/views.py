from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from account.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.data.get('email')
            nickname = form.data.get('nickname')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(nickname=nickname, password=raw_password)  # 사용자 인증
            #login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})
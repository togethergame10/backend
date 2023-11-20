from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from account.forms import UserCreationForm

from account.models import User
from game.models import Game, Situation

@csrf_exempt
def signup(request):
    if request.method == "POST": #post 요청 시 form값 확인 후 회원가입
        form = UserCreationForm(request.POST)

        if form.is_valid(): #폼이 정상
            form.save()
            email = form.data.get('email')
            nickname = form.data.get('nickname')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(email=email, nickname=nickname, password=raw_password)  # 사용자 인증
            login(request, user) #로그인
            return redirect('/')
        else:
            return render(request, 'account/signup.html', {'form': form})

    else: #get일때
        form = UserCreationForm()
        return render(request, 'account/signup.html', {'form': form})

def LikeMoreView(request,pk):
    user = User.objects.get(pk=pk)
    liked_list = Game.objects.filter(likes__in=user.like.all())[:2]
    colelcted_list = user.collected_gamelist.all()

    return render(request, 'account/like_more.html', {
        'target_user': user,
        'liked_list': liked_list,
        'collected_list': colelcted_list,
    })


from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from apps.users.forms import LoginForm, DynamicLoginForm
from apps.utils.random_str import generate_random
from apps.utils.yunpian import send_single_sms
from emooc.settings import yp_apikey, REDIS_HOST, REDIS_PORT
import redis


class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data["mobile"]
            # 随机生成数字验证码
            code = generate_random(4, 0)
            re_json = send_single_sms(yp_apikey, code, mobile=mobile)
            if re_json["code"] == 0:
                re_dict["status"] = "success"
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
                r.set(str(mobile), code)
                r.expire(str(mobile), 60 * 5)  # 设置验证码五分钟过期
            else:
                re_dict["msg"] = re_json["msg"]
        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]

        return JsonResponse(re_dict)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class LoginView(View):
    html_path = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        dynamic_login_form = DynamicLoginForm()
        return render(request, self.html_path, {'dynamic_login_form': dynamic_login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user:
                login(request, user)  # 已经完成cookie 和 session 的功能
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, self.html_path, {'msg': '用户名或密码错误', 'login_form': login_form})
        else:
            return render(request, self.html_path, {'login_form': login_form})


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        pass

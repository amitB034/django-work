from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom

from .main import create_pass

class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response


def view_pass(request):
    
    if request.POST:
        # s_alph = request.POST.get("s_alph")
        # c_alph = request.POST.get("c_alph")
        # pass_num = request.POST.get("num")
        number = request.POST.get("number")
        checkbox = request.POST.getlist('wordtype')
        pass_result = create_pass(checkbox,number)
        context = {
            "pass_result" : pass_result
        }
    print(checkbox,number)
    print(pass_result)
    #print(s_alph,c_alph,pass_num,number)
    return render(request,'main.html',context)


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"
    #create_pass()

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")

#class CreatePass():
#    template_name = "accounts:main"
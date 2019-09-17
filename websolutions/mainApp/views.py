from django.core.mail import send_mail
from django.shortcuts import render
from .forms import contact,par_reg
from django.views import View
from django.http import HttpResponse
# Create your views here.


def cleanIt(s):
    for i in range(len(s)):
        if(s[i]==','):
            s = s[:i] + '-' + s[i+1:]
    return s

def home(request):
    #return HttpResponse('<h1>Home</h1>')
    return render(request,'home.html')

def marketing_partners(request):
    return render(request,'marketing-partners.html')

def work(request):
    return render(request,'work.html')

class Contact(View):
    template_name = 'contact-us.html'
    form = contact()
    context = {
        'form': form,
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            organization = form.cleaned_data['organization']
            message = form.cleaned_data['message']
            ref_code = form.cleaned_data['ref_code']
            plan = form.cleaned_data['plan']

            if (ref_code == None):
                ref_code = 'None'
            if (plan == None):
                plan = 'None'
            if (phone == None):
                phone = 'None'
            if (organization == None):
                organization = 'None'


            message = message + "\n" + "phone : " + phone +"\n" + "ref_code : " + ref_code + "\n" + "plan : " + plan + "\n" + "Email : " + email




            x = send_mail(
                'customer@BluePearl-' + name + "@" + organization,
                 message,
                'syedfaizan824@gmail.com',
                ['lazine007@gmail.com'],
                fail_silently=True,
            )
            #print("sent : " , x)

        else:
            pass
            #print('something is wrong with forms!')
        return render(request, self.template_name, self.context)

def services(request):
    return render(request,'services.html')

def pricing(request):
    return render(request,'pricing.html ')

def about_us(request):
    return render(request,'about.html')

class par_registeration(View):
    template_name = 'par_registeration.html'
    form = par_reg()
    context = {
        'form': form,
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = par_reg(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            mobile = form.cleaned_data['mobile']
            platform = form.cleaned_data['platform']
            user_name = form.cleaned_data['user_name']
            audience_num = form.cleaned_data['audience_num']
            link = form.cleaned_data['link']
            message = form.cleaned_data['message']

            if not message:
                message = 'None'

            message = cleanIt(message)
            msg = name + ','
            msg = msg +  email + ','
            msg = msg + phone + ','
            msg = msg + mobile + ','
            msg = msg + platform + ','
            msg = msg + user_name + ','
            msg = msg + audience_num + ','
            msg = msg + link + ','
            msg = msg + message


            x = send_mail(
                'partner@BluePearl',
                 msg,
                'syedfaizan824@gmail.com',
                ['lazine007@gmail.com'],
                fail_silently=True,
            )
            #print("sent : " , x)

        else:
            pass
            #print('something is wrong with forms!')
        return render(request, self.template_name, self.context)


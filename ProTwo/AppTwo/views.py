from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUserForm


# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html")

def help(request):
    my_dict = {"insert_here": 'Hello once more, Here\'s the help from views.py!'}
    return render(request, "AppTwo/help.html", context=my_dict)

# def user(request):
#     users_list = User.objects.order_by('id')
#     user_dict = {'user_records': users_list}
#     return render(request, 'AppTwo/user.html', context=user_dict)

def user(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID!!!")

    return render(request, "AppTwo/user.html", {'form': form})
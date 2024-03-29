from django.shortcuts import render
from base.models import User
from django.shortcuts import redirect
from django.contrib import messages


# def Home(request):
#     return render(request, 'home.html')




def Sign_up(request):

    if request.user.is_anonymous:
        user = None

    else:
        user = request.user

      


    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # mobile = request.POST['mobile']
        # profile = request.FILES['profilepic']


        check = User.objects.filter(email = email).exists()

        if first_name == '' or last_name == '' or email == '' or password == '':
            messages.warning(request,"all fields required")

        elif check == True:
            messages.warning(request,'email already exists')
            

        else:
            User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
                # mobile = mobile
                # profilepic = profile
            )


            return redirect("home")
        

        
    return render(request, "account/Signup.html", context={"user": user})
# Create your views here.

from django.shortcuts import render
from .models import authUser

def index(request):
    users = authUser.objects.all()
    return render(request, 'auth/index.html', {'users': users})

def user_detail(request, user_id):
    user = authUser.objects.get(id=user_id)
    return render(request, 'auth/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authUser.objects.create_user(email=email, password=password)
        return render(request, 'auth/user_detail.html', {'user': user})
    return render(request, 'auth/user_create.html')

def user_update(request, user_id):
    user = authUser.objects.get(id=user_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user.email = email
        user.set_password(password)
        user.save()
        return render(request, 'auth/user_detail.html', {'user': user})
    return render(request, 'auth/user_update.html', {'user': user})

def user_delete(request, user_id):
    user = authUser.objects.get(id=user_id)
    user.delete()
    return render(request, 'auth/user_delete.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authUser.objects.get(email=email)
        if user.check_password(password):
            return render(request, 'auth/user_detail.html', {'user': user})
    return render(request, 'auth/user_login.html')

def user_logout(request):
    return render(request, 'auth/user_logout.html')

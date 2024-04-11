from django.shortcuts import redirect, render
from .models import Members, Trainers, AdministrativeStaff, Goals

# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if Members.login(email, password):
            user = Members.login(email, password)
            response = redirect('my_profile')
            response.set_cookie('email', email)
            response.set_cookie('id', user.member_id)
            response.set_cookie('user_type', 'MEMBER')
            return response
        elif Trainers.login(email, password):
            user = Trainers.login(email, password)
            response = redirect('my_profile')
            response.set_cookie('email', email)
            response.set_cookie('id', user.trainer_id)
            response.set_cookie('user_type', 'TRAINER')
            return response
        elif AdministrativeStaff.login(email, password):
            user = AdministrativeStaff.login(email, password)
            response = redirect('my_profile')
            response.set_cookie('email', email)
            response.set_cookie('id', user.admin_staff_id)
            response.set_cookie('user_type', 'ADMINSTAFF')
            return response

        return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if Members.find_member_with_email(email=email):
            return render(request, 'register.html', {'msg': 'This email already existed in our database'})

        Members.register(first_name=first_name,
                         last_name=last_name, email=email, password=password)
        return redirect('/login/')
    else:
        return render(request, 'register.html')


def sign_out(request):
    return render(request, 'login.html')


def member_dashboard(request, id):
    member = Members.find_member_with_id(id)
    goals = Members.find_goals_with_member_id(id)
    if not member == None:
        return render(request, 'member_profile.html', {'user_type': 'member', 'user': member, 'goals': goals})
    else:
        return render(request, 'member_profile.html', {'msg': 'User not found'})


def my_profile(request):
    if 'email' in request.COOKIES:
        id = int(request.COOKIES['id'])
        # display my dashboard
        if request.COOKIES['user_type'] == 'MEMBER':
            user = Members.find_member_with_id(id)
            goals = Members.find_goals_with_member_id(id)
            if user:
                return render(request, 'my_profile.html', {'user': user, 'user_type': 'MEMBER', 'goals': goals})
        if request.COOKIES['user_type'] == 'TRAINER':
            user = Trainers.find_trainer_with_email(email)
            if user:
                return render(request, 'my_profile.html', {'user': user, 'user_type': 'TRAINER'})
        if request.COOKIES['user_type'] == 'ADMINSTAFF':
            user = AdministrativeStaff.find_admin_staff_with_email(email)
            if user:
                return render(request, 'my_profile.html', {'user': user, 'user_type': 'ADMINSTAFF'})
    else:
        return redirect('/login/')


def update_info(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        password = request.POST.get('password')

        Members.update_info(int(request.COOKIES['id']), first_name, last_name, email, password, weight, height)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')

def add_goal(request):
    if request.method == 'POST':
        type_of_exercise = request.POST.get('type_of_exercise')
        goal_time = request.POST.get('goal_time')
        goal_weight = request.POST.get('goal_weight')
        reached = request.POST.get('reached') is not None

        Members.add_goal(int(request.COOKIES['id']), type_of_exercise, goal_time, goal_weight, reached)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')
    

def edit_goal(request):
    if request.method == 'POST':
        goal_id = request.POST.get('goal_id')
        type_of_exercise = request.POST.get('type_of_exercise')
        goal_time = request.POST.get('goal_time')
        goal_weight = request.POST.get('goal_weight')
        reached = request.POST.get('reached') is not None

        Members.edit_goal(goal_id, int(request.COOKIES['id']), type_of_exercise, goal_time, goal_weight, reached)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')
    

def delete_goal(request):
    if request.method == 'POST':
        goal_id = request.POST.get('goal_id')

        Members.delete_goal(goal_id, int(request.COOKIES['id']))
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')
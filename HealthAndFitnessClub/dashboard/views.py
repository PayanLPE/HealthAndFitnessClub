from django.shortcuts import redirect, render
from .models import Members, Trainers, AdministrativeStaff, Equipments, RoomBookings, FitnessClasses, FitnessClassMembers, TrainingSessions, Payments

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
    response = redirect('/login')
    response.delete_cookie('email')
    response.delete_cookie('id')
    response.delete_cookie('user_type')
    return response


def member_dashboard(request, id):
    member = Members.find_member_with_id(id)
    goals = Members.find_goals_with_member_id(id)
    classes = FitnessClassMembers.get_classes_with_member_id(id)
    sessions = TrainingSessions.get_sessions_by_member_id(id)

    if not member == None:
        return render(request, 'member_profile.html', {'user_type': 'member', 'user': member, 'goals': goals, 'classes': classes, 'sessions': sessions})
    else:
        return render(request, 'member_profile.html', {'msg': 'User not found'})


def my_profile(request):
    if 'email' in request.COOKIES:
        id = int(request.COOKIES['id'])
        # display my dashboard
        if request.COOKIES['user_type'] == 'MEMBER':
            user = Members.find_member_with_id(id)
            goals = Members.find_goals_with_member_id(id)
            classes = FitnessClassMembers.get_classes_with_member_id(id)
            sessions = TrainingSessions.get_sessions_by_member_id(id)
            payments = Payments.find_payments_member_id(id)

            if user:
                return render(request, 'my_profile.html', {'user': user, 'user_type': 'MEMBER', 'goals': goals, 'classes': classes, 'sessions': sessions, 'payments': payments})
        if request.COOKIES['user_type'] == 'TRAINER':
            user = Trainers.find_trainer_with_id(id)
            availabilities = Trainers.find_availabilities_with_trainer_id(id)

            if user:
                return render(request, 'my_profile.html', {'user': user, 'user_type': 'TRAINER', 'availabilities': availabilities})
        if request.COOKIES['user_type'] == 'ADMINSTAFF':
            user = AdministrativeStaff.find_admin_staff_with_id(id)
            equipments = Equipments.find_all_equipments()
            bookings = RoomBookings.find_all_bookings()
            payments = Payments.find_all_payments()
            if user:
                return render(request, 'my_profile.html', {'user': user, 'user_type': 'ADMINSTAFF', 'equipments': equipments, 'bookings': bookings, 'payments': payments})
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

        Members.update_info(int(
            request.COOKIES['id']), first_name, last_name, email, password, weight, height)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def add_goal(request):
    if request.method == 'POST':
        type_of_exercise = request.POST.get('type_of_exercise')
        goal_time = request.POST.get('goal_time')
        goal_weight = request.POST.get('goal_weight')
        reached = request.POST.get('reached') is not None

        Members.add_goal(
            int(request.COOKIES['id']), type_of_exercise, goal_time, goal_weight, reached)
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

        Members.edit_goal(goal_id, int(
            request.COOKIES['id']), type_of_exercise, goal_time, goal_weight, reached)
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


def add_availability(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        Trainers.add_availability(
            int(request.COOKIES['id']), day, start_time, end_time)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def edit_availability(request):
    if request.method == 'POST':
        availability_id = request.POST.get('availability_id')
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        Trainers.edit_availability(availability_id, int(
            request.COOKIES['id']), day, start_time, end_time)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def delete_availability(request):
    if request.method == 'POST':
        availability_id = request.POST.get('availability_id')

        Trainers.delete_availability(
            availability_id, int(request.COOKIES['id']))
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def search_member(request):
    if request.method == 'POST':
        member_name = request.POST.get('member_name')
        first_name, last_name = member_name.split()
        user = Members.find_member_with_name(first_name, last_name)
        id = str(user.member_id)
        return redirect('/members/' + id + '/')
    else:
        return redirect('/my_profile/')


def add_equipment(request):
    if request.method == 'POST':
        equipment_name = request.POST.get('equipment_name')
        last_maintenance = request.POST.get('last_maintenance')
        next_maintenance = request.POST.get('next_maintenance')

        Equipments.add_equipment(
            equipment_name, last_maintenance, next_maintenance, int(request.COOKIES['id']))
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def edit_equipment(request):
    if request.method == 'POST':
        equipment_id = request.POST.get('equipment_id')
        equipment_name = request.POST.get('equipment_name')
        last_maintenance = request.POST.get('last_maintenance')
        next_maintenance = request.POST.get('next_maintenance')

        Equipments.edit_equipment(
            equipment_id, equipment_name, last_maintenance, next_maintenance, int(request.COOKIES['id']))
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def delete_equipment(request):
    if request.method == 'POST':
        equipment_id = request.POST.get('equipment_id')

        Equipments.delete_equipment(equipment_id)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def add_booking(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        date = request.POST.get('date')
        booking_start_time = request.POST.get('booking_start_time')
        booking_end_time = request.POST.get('booking_end_time')

        RoomBookings.add_booking(
            int(request.COOKIES['id']), room_number, date, booking_start_time, booking_end_time)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def edit_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        room_number = request.POST.get('room_number')
        date = request.POST.get('date')
        booking_start_time = request.POST.get('booking_start_time')
        booking_end_time = request.POST.get('booking_end_time')

        RoomBookings.edit_booking(booking_id, int(
            request.COOKIES['id']), room_number, date, booking_start_time, booking_end_time)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def delete_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')

        RoomBookings.delete_booking(booking_id)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def fitness_classes(request):
    if 'email' in request.COOKIES:
        id = int(request.COOKIES['id'])
        classes = FitnessClasses.get_all_classes()

        # display my dashboard
        if request.COOKIES['user_type'] == 'MEMBER':
            return render(request, 'fitness_class.html', {'user_type': 'MEMBER', 'classes': classes})
        if request.COOKIES['user_type'] == 'ADMINSTAFF':
            return render(request, 'fitness_class.html', {'user_type': 'ADMINSTAFF', 'classes': classes})
    else:
        return redirect('/login/')


def join_fitness_classes(request, id):
    if 'email' in request.COOKIES:
        member_id = int(request.COOKIES['id'])
        FitnessClassMembers.add_members_to_class(member_id, id)
        return redirect('/fitness_classes/')
    else:
        return redirect('/fitness_classes/')


def leave_fitness_classes(request, id):
    if 'email' in request.COOKIES:
        member_id = int(request.COOKIES['id'])
        FitnessClassMembers.remove_members_to_class(member_id, id)
        return redirect('/fitness_classes/')
    else:
        return redirect('/fitness_classes/')


def add_class(request):
    if request.method == 'POST':
        trainer_id = request.POST.get('trainer_id')
        day = request.POST.get('day')
        class_start_time = request.POST.get('class_start_time')
        class_end_time = request.POST.get('class_end_time')

        FitnessClasses.add_class(
            trainer_id, day, class_start_time, class_end_time, int(request.COOKIES['id']))
        return redirect('/fitness_classes/')
    else:
        return redirect('/fitness_classes/')


def edit_class(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        trainer_id = request.POST.get('trainer_id')
        day = request.POST.get('day')
        class_start_time = request.POST.get('class_start_time')
        class_end_time = request.POST.get('class_end_time')

        FitnessClasses.edit_class(
            class_id, trainer_id, day, class_start_time, class_end_time, int(request.COOKIES['id']))
        return redirect('/fitness_classes/')
    else:
        return redirect('/fitness_classes/')


def delete_class(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')

        FitnessClasses.delete_class(class_id)
        return redirect('/fitness_classes/')
    else:
        return redirect('/fitness_classes/')


def add_session(request):
    if request.method == 'POST':
        trainer_id = request.POST.get('trainer_id')
        day = request.POST.get('day')
        session_start_time = request.POST.get('session_start_time')
        session_end_time = request.POST.get('session_end_time')

        TrainingSessions.add_session(
            int(request.COOKIES['id']), trainer_id, day, session_start_time, session_end_time)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def edit_session(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        trainer_id = request.POST.get('trainer_id')
        day = request.POST.get('day')
        session_start_time = request.POST.get('session_start_time')
        session_end_time = request.POST.get('session_end_time')

        TrainingSessions.edit_session(
            session_id, int(request.COOKIES['id']), trainer_id, day, session_start_time, session_end_time)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')


def delete_session(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')

        TrainingSessions.delete_session(session_id)
        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')

def pay_bill(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        Payments.create_payment(int(request.COOKIES['id']), amount)

        return redirect('/my_profile/')
    else:
        return redirect('/my_profile/')
    
def authorize_payment(request, id):
    Payments.authorize_payment(id)
    return redirect('/my_profile/')
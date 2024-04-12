import datetime
from django.db import models

# Create your models here.
class Members(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    class Meta:
        managed = False
        db_table = 'members'

    @staticmethod
    def login(email, password):
        return Members.objects.filter(email=email, password=password).first()
    
    @staticmethod
    def register(first_name, last_name, email, password):
        Members.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    
    @staticmethod
    def find_member_with_id(member_id):
        return Members.objects.filter(member_id=member_id).first()
    
    @staticmethod
    def find_member_with_email(email):
        return Members.objects.filter(email=email).first()
    
    @staticmethod
    def find_member_with_name(first_name, last_name):
        return Members.objects.filter(first_name=first_name, last_name=last_name).first()
    
    @staticmethod
    def find_goals_with_member_id(member_id):
        user = Members.find_member_with_id(member_id)
        if user is not None:
            goals = Goals.objects.filter(member_id=member_id)
            return goals
    
    @staticmethod
    def update_info(member_id, first_name, last_name, email, password, weight, height):
        user = Members.find_member_with_id(member_id)
        if user is not None and user.password == password:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.weight = weight
            user.height = height
            
            user.save()
        else:
            return False
    
    @staticmethod
    def add_goal(member_id, type_of_exercise, goal_time, goal_weight, reached):
        Goals.objects.create(member_id=member_id, exercise=type_of_exercise, goal_time=goal_time, goal_weight=goal_weight, reached=reached)

    @staticmethod
    def edit_goal(goal_id, member_id, type_of_exercise, goal_time, goal_weight, reached):
        if not Goals.check_if_goal_belongs_to_member(goal_id, member_id):
            return False
        
        goal = Goals.find_goal_with_id(goal_id)
        if goal is not None:
            goal.exercise = type_of_exercise
            goal.goal_time = goal_time
            goal.goal_weight = goal_weight
            goal.reached = reached
            
            goal.save()
        else:
            return False
        
    @staticmethod
    def delete_goal(goal_id, member_id):
        if Goals.check_if_goal_belongs_to_member(goal_id, member_id):
            goal = Goals.find_goal_with_id(goal_id)
            if goal is not None:
                goal.delete()

class Trainers(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        db_table = 'trainers'

    @staticmethod
    def login(email, password):
        return Trainers.objects.filter(email=email, password=password).first()

    @staticmethod
    def find_trainer_with_id(id):
        return Trainers.objects.filter(trainer_id=id).first()
        
    @staticmethod
    def find_availabilities_with_trainer_id(id):
        user = Trainers.find_trainer_with_id(id)
        if user is not None:
            availabilities = Availabilities.objects.filter(trainer_id=id)
            return availabilities

    @staticmethod
    def add_availability(trainer_id, day, start_time, end_time):
        Availabilities.objects.create(trainer_id=trainer_id, day=day, start_time=start_time, end_time=end_time)

    @staticmethod
    def edit_availability(availability_id, trainer_id, day, start_time, end_time):
        if not Availabilities.check_if_availability_belongs_to_trainer(availability_id, trainer_id):
            return False
        
        availability = Availabilities.find_availability_with_id(availability_id)
        if availability is not None:
            availability.day = day
            availability.start_time = start_time
            availability.end_time = end_time
            
            availability.save()
        else:
            return False
        
    @staticmethod
    def delete_availability(availability_id, trainer_id):
        if Availabilities.check_if_availability_belongs_to_trainer(availability_id, trainer_id):
            availability = Availabilities.find_availability_with_id(availability_id)
            if availability is not None:
                availability.delete() 

class AdministrativeStaff(models.Model):
    admin_staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        db_table = 'administrativestaff'

    @staticmethod
    def login(email, password):
        return AdministrativeStaff.objects.filter(email=email, password=password).first()
    
    @staticmethod
    def find_admin_staff_with_id(id):
        return AdministrativeStaff.objects.filter(admin_staff_id=id).first()

class Goals(models.Model):
    goal_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=False)
    exercise = models.CharField(max_length=255, null=False)
    goal_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    goal_time = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    reached = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'goals'
    
    @staticmethod
    def check_if_goal_belongs_to_member(goal_id, member_id):
        if Goals.objects.filter(goal_id=goal_id, member_id=member_id).first() is None:
            return False
        else:
            return True
        
    @staticmethod
    def find_goal_with_id(goal_id):
        return Goals.objects.filter(goal_id=goal_id).first()
    
class Availabilities(models.Model):
    availability_id = models.AutoField(primary_key=True)
    trainer_id = models.IntegerField(null=False)
    day = models.CharField(max_length=255, null=False)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'availabilities'
    
    @staticmethod
    def check_if_availability_belongs_to_trainer(availability_id, trainer_id):
        if Availabilities.objects.filter(availability_id=availability_id, trainer_id=trainer_id).first() is None:
            return False
        else:
            return True
        
    @staticmethod
    def find_availability_with_id(availability_id):
        return Availabilities.objects.filter(availability_id=availability_id).first()
    
class Equipments(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=255, null=False)
    last_maintenance = models.DateField()
    next_maintenance = models.DateField()

    class Meta:
        managed = False
        db_table = 'equipments'

    @staticmethod
    def find_all_equipments():
        return Equipments.objects.filter()
    
    @staticmethod
    def add_equipment(equipment_name, last_maintenance, next_maintenance):
        Equipments.objects.create(equipment_name=equipment_name, last_maintenance=last_maintenance, next_maintenance=next_maintenance)
    
    @staticmethod
    def edit_equipment(equipment_id, equipment_name, last_maintenance, next_maintenance):
        equipment = Equipments.objects.filter(equipment_id=equipment_id).first()
        equipment.equipment_name = equipment_name
        equipment.last_maintenance = last_maintenance
        equipment.next_maintenance = next_maintenance

        equipment.save()
    
    @staticmethod
    def delete_equipment(equipment_id):
        Equipments.objects.filter(equipment_id=equipment_id).first().delete() 
    
class RoomBookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    room_number = models.IntegerField()
    booking_start_time = models.TimeField()
    booking_end_time = models.TimeField()
    admin_staff_id = models.IntegerField(null=False)

    class Meta:
        managed = False
        db_table = 'roombookings'

    @staticmethod
    def find_all_bookings():
        return RoomBookings.objects.filter()
    
    @staticmethod
    def add_booking(admin_staff_id, room_number, booking_start_time, booking_end_time):
        RoomBookings.objects.create(room_number=room_number, admin_staff_id=admin_staff_id, booking_start_time=booking_start_time, booking_end_time=booking_end_time)
    
    @staticmethod
    def edit_booking(booking_id, admin_staff_id, room_number, booking_start_time, booking_end_time):
        booking = RoomBookings.objects.filter(booking_id=booking_id).first()
        booking.room_number = room_number
        booking.booking_start_time = booking_start_time
        booking.booking_end_time = booking_end_time
        booking.admin_staff_id = admin_staff_id
         
        booking.save()
    
    @staticmethod
    def delete_booking(booking_id):
        RoomBookings.objects.filter(booking_id=booking_id).first().delete() 

class FitnessClasses(models.Model):
    class_id = models.AutoField(primary_key=True)
    trainer_id = models.IntegerField()
    day = models.CharField(max_length=255, null=False)
    class_start_time = models.TimeField()
    class_end_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'fitnessclasses'

    @staticmethod
    def get_all_classes():
        classes = FitnessClasses.objects.filter()
        for c in classes:
            c.trainer_name = Trainers.find_trainer_with_id(c.trainer_id).first_name + ' '+ Trainers.find_trainer_with_id(c.trainer_id).last_name

            participants = FitnessClassMembers.get_all_members(c.class_id)
            names = []
            for p in participants:
                names.append(Members.find_member_with_id(p.member_id).first_name + ' '+ Members.find_member_with_id(p.member_id).last_name)
            c.members = names
        return classes
    
    @staticmethod
    def get_class_with_id(class_id):
        return FitnessClasses.objects.filter(class_id=class_id)
    
    @staticmethod
    def add_class(trainer_id, day, class_start_time, class_end_time):
        availabilities = Availabilities.objects.filter(trainer_id=trainer_id, day=day)

        check = False
        for time in availabilities:
            if time.start_time <= datetime.datetime.strptime(class_start_time, '%I:%M').time() and time.end_time > datetime.datetime.strptime(class_end_time, '%I:%M').time():
                check = True
        if check:
            FitnessClasses.objects.create(trainer_id=trainer_id, day=day, class_start_time=class_start_time, class_end_time=class_end_time)
    
    @staticmethod
    def edit_class(class_id, trainer_id, day, class_start_time, class_end_time):
        availabilities = Availabilities.objects.filter(trainer_id=trainer_id, day=day)

        check = False
        for time in availabilities:
            if time.start_time <= datetime.datetime.strptime(class_start_time, '%I:%M').time() and time.end_time > datetime.datetime.strptime(class_end_time, '%I:%M').time():
                check = True
        if check:
            c = FitnessClasses.objects.filter(class_id=class_id).first()
            c.trainer_id = trainer_id
            c.day = day
            c.class_start_time = class_start_time
            c.class_end_time = class_end_time
            c.save()
    
    @staticmethod
    def delete_class(class_id):
        members = FitnessClassMembers.objects.filter(class_id=class_id)
        for m in members:
            m.delete()
        FitnessClasses.objects.filter(class_id=class_id).first().delete() 
    
class FitnessClassMembers(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.IntegerField(null=False)
    member_id = models.IntegerField(null=False)

    class Meta:
        managed = False
        db_table = 'fitnessclassmembers'

    @staticmethod
    def get_all_members(class_id):
        return FitnessClassMembers.objects.filter(class_id=class_id)
    
    @staticmethod
    def add_members_to_class(member_id, class_id):
        if (FitnessClassMembers.objects.filter(member_id=member_id, class_id=class_id).first() is None):
            FitnessClassMembers.objects.create(member_id=member_id, class_id=class_id)
    
    @staticmethod
    def remove_members_to_class(member_id, class_id):
        if (FitnessClassMembers.objects.filter(member_id=member_id, class_id=class_id).first() is not None):
            FitnessClassMembers.objects.filter(member_id=member_id, class_id=class_id).first().delete()

    @staticmethod
    def get_classes_with_member_id(member_id):
        ids = FitnessClassMembers.objects.filter(member_id=member_id)

        classes = []
        for id in ids:
            c = FitnessClasses.get_class_with_id(id.class_id).first()
            c.trainer_name = Trainers.find_trainer_with_id(c.trainer_id).first_name + " " + Trainers.find_trainer_with_id(c.trainer_id).last_name
            classes.append(c)

        return classes
            
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
    def find_trainer_with_email(email):
        return Trainers.objects.filter(email=email).first()

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
    def find_admin_staff_with_email(email):
        return AdministrativeStaff.objects.filter(email=email).first()

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
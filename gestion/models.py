from django.db import models
from django.utils import timezone

class Employee(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    employment_status_choices = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contractual', 'Contractual'),
    ]

    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100)
    photo_url = models.URLField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default='Unknown')
    hire_date = models.DateField()
    employment_status = models.CharField(max_length=20, choices=employment_status_choices)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    risk_level = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    

class Employment(models.Model):
    EMPLOYMENT_STATUS_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contractual', 'Contractual'),
    ]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    manager = models.ForeignKey(Employee, related_name='subordinates', null=True, blank=True, on_delete=models.SET_NULL)

class AdministrativeInfo(models.Model):
    EMPLOYMENT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('On leave', 'On leave'),
        ('Terminated', 'Terminated'),
    ]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    employee_number = models.CharField(max_length=20, null=True, blank=True)
    social_security_number = models.CharField(max_length=20, null=True, blank=True)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Training(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100, null=True, blank=True)
    training_course = models.CharField(max_length=100)
    skill = models.CharField(max_length=100, null=True, blank=True)
    performance_review = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('employee', 'training_course')

class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('Vacation', 'Vacation'),
        ('Sick leave', 'Sick leave'),
        ('Parental leave', 'Parental leave'),
        ('Other', 'Other'),
    ]

    leave_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Benefits(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    health_insurance = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], null=True, blank=True)
    retirement_plan = models.CharField(max_length=10, choices=[('401k', '401k'), ('Pension', 'Pension'), ('None', 'None')], null=True, blank=True)
    other_benefits = models.TextField(null=True, blank=True)

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_hours = models.TimeField(null=True, blank=True)
    overtime_hours = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

class HealthAndSafety(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    medical_conditions = models.TextField(null=True, blank=True)
    work_accident_history = models.TextField(null=True, blank=True)

class Performance(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    evaluation_date = models.DateField()  # Correction: placement correct de l'attribut
    performance_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    goals = models.TextField(null=True, blank=True)
    development_plan = models.TextField(null=True, blank=True)  # Correction: placement correct de l'attribut
    performance_score = models.IntegerField()
    promotion = models.BooleanField(default=False)
    salary_increase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.evaluation_date}"

class EmploymentTermination(models.Model):
    TERMINATION_REASON_CHOICES = [
        ('Resignation', 'Resignation'),
        ('Layoff', 'Layoff'),
        ('Termination', 'Termination'),
        ('Retirement', 'Retirement'),
        ('Other', 'Other'),
    ]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    termination_date = models.DateField(null=True, blank=True)
    termination_reason = models.CharField(max_length=20, choices=TERMINATION_REASON_CHOICES, null=True, blank=True)
    non_compete_clause = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], null=True, blank=True)




class SatisfactionSurvey(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    survey_date = models.DateField(default=timezone.now)
    feedback = models.TextField()
    satisfaction_score = models.IntegerField()  # Par exemple, de 1 à 10

    def __str__(self):
        return f"Survey for {self.employee} on {self.survey_date}"

class Feedback(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    feedback_date = models.DateField(default=timezone.now)
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback from {self.employee} on {self.feedback_date}"


class Behavior(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    absenteeism_days = models.PositiveIntegerField(default=0)
    overtime_hours = models.PositiveIntegerField(default=0)
    training_engagement = models.FloatField(default=0.0)  # Pourcentage ou autre mesure
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee} - {self.date}"
    


class ActionPlan(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    plan = models.TextField()
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending')
    feedback = models.TextField(blank=True, null=True)

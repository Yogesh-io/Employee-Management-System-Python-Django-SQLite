from django.core.exceptions import ValidationError

def validate_salary(sal):
    if sal < 10000:
        raise ValidationError("Salary Should be greater than 10000")

def validate_name(name):
    name = name.replace(" ","")
    if not name.isalpha():
        raise ValidationError("Use Only Alphabets")


from django.db import models
from django.core.exceptions import ValidationError
def vn(student_name):
    if student_name.isalpha():
        pass
    else:
        raise ValidationError('please enter alphabetics')

class detail(models.Model):
    cho=['science','maths','english']
    student_name=models.CharField(max_length=20,validators=[vn])
    student_class=models.IntegerField(max_length=2)
    main_sub=models.CharField(max_length=10,choices=[(item,item) for item in cho])
    student_Id=models.CharField(max_length=10)
    marks=models.IntegerField(max_length=3)
    Average_marks=models.FloatField(max_length=4)

#name,department,role,education,assescomment,assestype,date=defaultca de,recr,
#result=select,rejected
#active=yes,no
#state chage to active,  education=btech,mba,mca

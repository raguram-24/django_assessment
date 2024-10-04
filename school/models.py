from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255,null=False)
    

class Class(models.Model):
    class_name = models.CharField(max_length=255, null=False)
   
class AssessmentArea(models.Model):
    assessment_name = models.CharField(max_length=255)
    
class Student(models.Model):
    student_name = models.CharField(max_length=255)
    
class Answer(models.Model):
    answers = models.CharField(max_length=1)
    
    
class Award(models.Model):
    award = models.CharField(max_length=255)
   
class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_contents = models.CharField(max_length=255 ,default= "Contents")
    subject_score = models.CharField(max_length=255 , default='75')
   
   
class CorrectAnswer(models.Model):
    correct_answer = models.CharField(max_length=1)
   
    
class Summary(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.DecimalField(max_digits=5, decimal_places=2)
    assessment_area_id = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award_id = models.ForeignKey(Award, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    correct_answer = models.CharField(max_length=50)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.IntegerField()
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=100)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="summary_answer")
    correct_answer_id = models.ForeignKey(CorrectAnswer, on_delete=models.CASCADE)
    
   


    
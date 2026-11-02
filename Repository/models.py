from django.db import models

# Create your models here.

'''
schema : QuestionsDb
Fields : title, language, notes, difficulty_level, sample_input, sample_output, topic, published_date, is_active
'''

class QuestionsDb(models.Model):
    title = models.CharField(max_length=200)

    LANGUAGE_CHOICES = (
        ("python", "python"),
        ("java", "java"),
        ("javascript", "javascript"),
    )
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default="python")

    DIFFICULTY_CHOICE = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    )
    difficulty_level = models.CharField(max_length=100, choices=DIFFICULTY_CHOICE, default="easy")

    topic = models.CharField(max_length=200)

    notes = models.TextField()  # Changed to TextField (or use CharField(max_length=...))

    published_date = models.DateField(auto_now_add=True)  # Fixed typo and changed to DateField

    sample_input = models.TextField()

    sample_output = models.TextField()

    is_active = models.BooleanField(default=True)

class SubmissionsDb(models.Model):
    
    question_id = models.IntegerField()
    
    answer = models.TextField()
    
    points = models.PositiveIntegerField(null=True)
    
    owner = models.CharField(max_length=100)
    
    submission_date = models.DateTimeField(auto_now_add=True)
    
    remarks = models.TextField(null=True)
























# '''
# # from django.db import models

# # class QuestionsDb(models.Model):
# #     title = models.CharField(max_length=255)
# #     language = models.CharField(max_length=100)
# #     notes = models.TextField(blank=True, null=True)
# #     difficulty_level = models.CharField(max_length=50, blank=True, null=True)
# #     sample_input = models.TextField(blank=True, null=True)
# #     sample_output = models.TextField(blank=True, null=True)
# #     topic = models.CharField(max_length=150, blank=True, null=True)
# #     published_date = models.DateField(blank=True, null=True)
# #     is_active = models.BooleanField(default=True)

# #     def __str__(self):
# #         return self.title

# # class submissionsDb(models.model):
# #     questions_id = models.IntegerField()
# #     answer =  models.TextField()
# #     points = models.PositiveIntegerField(null = True)
# #     owner = models.CharField(max_lentgh=100)
# #     submission_date = models.DateTimeField(auto_now_add=True)
# #     remarks = models.TextField(null = True)

# # class SubmissionSerializer(serializers.serializer):
# #     question_id = serializers.IntegerField()
# #     answer = serializers.CharField()
# #     pooints = serializers.charfield(read_only = True)
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


q , r = divmod(34,5)
print(q)
print(r)

class Wilaya(models.Model):
    wilaya_name = models.CharField(max_length=30)
    wilaya_code = models.PositiveIntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    
    def creation_month(self):
        months = [None, 'Janvier', 'Février' , 'Mars','Avril','Mai',
                  'Juin','Juillet','Aout','Septembre','Octobre',
                  "Novembre","Décembre"]
        month = self.created_on.month
        n =  timezone.now() - self.created_on
        f= n.total_seconds() / 60
        
        q ,r = divmod(f, 60)
        return f'{int(q)} heures'
        

    
    def __str__(self):
        return f'{self.wilaya_name}  code: {self.wilaya_code}'
    


class Destination(models.Model):
    destination_name = models.CharField(max_length=100)
    description = models.TextField()
    agency_name = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    super_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on  = models.DateTimeField(default=timezone.now)
    destination_picture = models.ImageField(upload_to='pictures')
    
    
    def __str__(self):
        return f'{self.destination_name}'
    



class Follow(models.Model):
    wilaya_followed = models.ForeignKey(Wilaya, on_delete=models.CASCADE )
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_date = models.DateTimeField(default=timezone.now)
    
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return f'{self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f'{self.choice_text}'
    

class Voter(models.Model):
    question_voted = models.ForeignKey(Question , on_delete=models.CASCADE)
    voter = models.ForeignKey(User , on_delete=models.CASCADE)
    vote_date  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.voter} voted on {self.question_voted}'
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
'''
        months = [None, 'Janvier', 'Février' , 'Mars','Avril','Mai',
                  'Juin','Juillet','Aout','Septembre','Octobre',
                  "Novembre","Décembre"]
        d = datetime.datetime.now()
        s = d.strftime('%m')
        return f'{months[s]}'
'''
class Category(models.Model):
    category = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.category}'
    
    def added_on(self):
        return self.category
    
    def get_date(self):
        months  = [None,'Janvier', 'Fevrier', 'Mars','Avril',
                   'Mai','Juin','Juillet','Aout','Septembre',
                   'Octobre','Novembre','Decembre']
        month = self.post_date.month 
        #month = self.post_date.month -1
        dt = timezone.now() - self.post_date
        new = round(dt.total_seconds() / 60)
        new_dt = divmod(new, 60)
        if new_dt[0] < 1:
            return f'{new_dt[1]} minutes'
        elif new_dt[0] < 24:
            return f'{new_dt[0]} heures'
        elif new_dt[0] < 48:
            return f'un jour'
        elif new_dt[0] < 72:
            return '2 jour'

        else:
            return f'{self.post_date.day} {months[month]} {self.post_date.year}'

   
    
        
        
    
class News(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'{self.title} added in {self.category}'
    
    
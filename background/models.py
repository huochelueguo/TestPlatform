from django.db import models

# Create your models here.



# Create your models here.
class DB_Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.book_name
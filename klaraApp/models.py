from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Appointment(models.Model):

    class Meta:
        unique_together = ('date','timeslot','service')

    TIMESLOT_LIST = (
        (0, '09:00 – 10:30'),
        (1, '11:00 – 12:30'),
        (2, '13:00 – 14:30'),
        (3, '15:00 – 16:30'),
        (4, '17:00 – 18:30'),
        (5, '19:00 – 20:30'),
    )
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=1,verbose_name="Статус",blank=False)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]


    def __str__(self):
        return f"{self.client.username}  {self.time} - {self.date}"

class Service(models.Model):
    work_name = models.ForeignKey("Works",on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.work_name.name

class Works(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название услуги")

    def __str__(self):
        return self.name


class ClientProfile(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
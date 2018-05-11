from django.db import models
from django.utils import timezone


class Transfer(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    money = models.CharField(max_length=200)
    money_off = models.IntegerField(default=0)
    date_off = models.DateTimeField(default=timezone.now)
    FRESHMAN = 'bronze'
    SOPHOMORE = 'silver'
    JUNIOR = 'gold'
    SENIOR = 'platinum'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'bronze'),
        (SOPHOMORE, 'silver'),
        (JUNIOR, 'gold'),
        (SENIOR, 'platinum'),
    )
    procent = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        discount = self.procent
        price = self.money
        if discount > 0:
            recount_of_discount = (discount / 100)
            print(recount_of_discount)
            multiplay_sum_on_coef = float(price) * float(recount_of_discount)
            print(multiplay_sum_on_coef)
            self.money_off = float(price) + float(multiplay_sum_on_coef)
            print(float(self.money))
        super(Transfer, self).save(*args, **kwargs)

    tarif = models.CharField(max_length=10,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

    def is_upperclass(self):
        return self.tarif in (self.JUNIOR, self.SENIOR)

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.money
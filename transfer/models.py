from django.db import models
from django.utils import timezone




class Transuser(models.Model):
    qiwi = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    money_off = models.IntegerField(default=0)
    money_on = models.IntegerField()
    tarif = models.IntegerField(default=0)
    date_off = models.DateTimeField(
        default=timezone.now)
    date_on = models.DateTimeField(
        blank=True, null=True)

    def save(self, *args, **kwargs):
        discount = self.tarif
        price = self.money_on
        if discount > 0:
            recount_of_discount = (discount / 100)
            print(recount_of_discount)
            multiplay_sum_on_coef = float(price) * float(recount_of_discount)
            print(multiplay_sum_on_coef)
            self.money_off = float(price) + float(multiplay_sum_on_coef)
            print(float(self.money_off))
        super(Transuser, self).save(*args, **kwargs)

    def publish(self):
        self.date_on = timezone.now()
        self.save()

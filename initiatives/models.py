from django.db import models
from django.urls import reverse
# Create your models here.


class Initiative(models.Model):
    title = models.CharField("Nomi", max_length=200)
    summary = models.CharField("Qisqacha", max_length=200, blank=True)
    body = models.TextField("Tekst")
    photo = models.ImageField("Foto", upload_to='images/', blank=True)
    result = models.IntegerField("Natija", default=0)
    dcreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('initiative_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Tashabbus"
        verbose_name_plural = "Tashabbuslar"


class Offer(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name='offers')
    offer = models.CharField("Taklif", max_length=200)
    offer_result = models.TextField("Taklif natijalari", blank=True)

    def __str__(self):
        return self.offer

    def get_absolute_url(self):
        return reverse('initiative_list')

    class Meta:
        verbose_name = "Taklif"
        verbose_name_plural = "Takliflar"


class Comment(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField("Izoh", max_length=200)
    email = models.CharField("Email", max_length=200, blank=True)
    fio = models.CharField("fio", max_length=200, blank=True)
    draft = models.BooleanField("Черновик", default=True)


    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
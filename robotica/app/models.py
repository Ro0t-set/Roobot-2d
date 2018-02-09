from django.db import models

# Create your models here.


from django.utils import timezone


class Punti(models.Model):
	nome_mappa= models.CharField(default="", max_length=100)
	nord = models.IntegerField(blank=True, null=True)
	sud = models.IntegerField(blank=True, null=True)
	est = models.IntegerField(blank=True, null=True)
	ovest = models.IntegerField(blank=True, null=True)
	id_temporale= models.IntegerField(blank=True, null=True)
	def __str__(self):
		return str(self.nome_mappa)



class Mappa(models.Model):
	nome_mappa= models.ForeignKey('Punti', blank=True, null=True)

	x = models.IntegerField(blank=True, null=True)
	y = models.IntegerField(blank=True, null=True)

	aggettivo =  models.IntegerField(blank=True, null=True, default=1)
	def __str__(self):
		return str(self.nome_mappa)


class Grafico(models.Model):
	x = models.IntegerField(blank=True, null=True)
	y = models.IntegerField(blank=True, null=True)

	nome_mappa= models.ForeignKey('Punti', blank=True, null=True)

	def __str__(self):
		return str(self.nome_mappa)





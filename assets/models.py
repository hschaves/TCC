from django.db import models

class Notebook(models.Model):
    modelo = models.CharField(max_length=100)
    processador = models.CharField(max_length=100)
    memoria_gb = models.IntegerField()
    armazenamento_gb = models.IntegerField()
    data_compra = models.DateField()
    usuario = models.CharField(max_length=500)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

class Monitor(models.Model):
    modelo = models.CharField(max_length=100)
    tamanho_polegadas = models.FloatField()
    tipo = models.CharField(max_length=50)
    resolucao = models.CharField(max_length=50)
    data_compra = models.DateField()
    usuario = models.CharField(max_length=500)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

class Desktop(models.Model):
    modelo = models.CharField(max_length=100)
    processador = models.CharField(max_length=100)
    memoria_gb = models.IntegerField()
    armazenamento_gb = models.IntegerField()
    data_compra = models.DateField()
    usuario = models.CharField(max_length=500)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

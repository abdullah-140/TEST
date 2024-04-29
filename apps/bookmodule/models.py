from django.db import models

# Create your models here.
class PCS(models.Model):
 id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
 Processor = models.CharField(max_length = 50)
 RAM = models.CharField(max_length = 50)
 Storage = models.CharField(max_length = 50)
 graphics_card = models.CharField(max_length = 50)
 Motherboard	 = models.CharField(max_length = 50)
 Power_Supply = models.CharField(max_length = 50)
 Case = models.CharField(max_length = 50)



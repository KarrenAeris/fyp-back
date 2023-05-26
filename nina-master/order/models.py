from django.db import models
from user.models import User


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    order_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    material_type = models.CharField(choices=[('ABS', 'A'), ('PLA', 'P'), ('PETG', 'PE'), ('TPU', 'T')], max_length=255)
    material_amount = models.IntegerField()
    v_material = models.FloatField()
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Started at')
    finished_at = models.DateTimeField(auto_now_add=True, verbose_name='Finished at')
    status = models.CharField(choices=[('pending', 'p'), ('complete', 'c'), ('rejected', 'r')], default='pending',
                              max_length=255)
    price = models.FloatField(null=True)
    file = models.FileField(upload_to='documents')

    # def save(self, *args, **kwargs):
    #     p_material = {'ABS': 1.08, 'PLA': 1.25, 'PETG': 1.34, 'TPU': 1.25}
    #     m_material = {'ABS': 0.015, 'PLA': 0.018, 'PETG': 0.016, 'TPU': 0.027}
    #     p = p_material[self.material_type]
    #     m = m_material[self.material_type]
    #     c_material = self.v_material * p * m
    #     trunning = self.v_material / 30.15
    #     cenergy = 0.02 * trunning * 150
    #     coverhead = 2 * 1
    #     cprocessing = c_material + cenergy + coverhead
    #     cpre_processing = 2 * 2
    #     cprocess = cpre_processing + cprocessing
    #     ctotal = cprocess + 0.1 + cprocess
    #     super().save(*args, **kwargs)
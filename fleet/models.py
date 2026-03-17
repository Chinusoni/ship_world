from django.db import models

class CourierPartner(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class Carrier(models.Model):
    name = models.CharField(max_length=50) # e.g., "DTDC"
    tracking_url = models.URLField()       # e.g., "https://www.dtdc.in/tracking/tracking_results.asp?trackid="

    def __str__(self):
        return self.name
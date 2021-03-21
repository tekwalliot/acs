from django.db import models

# Create your models here.




class SiteDetails(models.Model):

	capchoise = [('5HP AC', '5HP AC'), ('3HP AC', '3HP AC'), ('7.5HP AC', '7.5HP AC'), ('10HP AC', '10HP AC'), ('5HP DC', '5HP DC'), ('3HP DC', '3HP DC'), ('7.5HP DC', '7.5HP DC'), ('10HP DC', '10HP DC')]
	"""docstring for ClassName"""
	rmsId = models.CharField(max_length=40,null=True,blank=True, help_text='Serial No-1, 2 etc or RMS ID')
	regID = models.CharField(max_length=40,null=True,blank=True, help_text='If any registration ID is there then fill')
	custName = models.CharField(max_length=40,null=True,blank=True, help_text='Customer Name')
	custMob = models.IntegerField(null=True,blank=True, help_text='Customer Contact Number')
	location = models.CharField(max_length=100,null=True,blank=True, help_text='Village, Mandal')
	capacity = models.CharField(max_length=10,null=True,blank=True, choices=capchoise, help_text='5HP AC or 3HP AC or other')
	poNo = models.CharField(max_length=100,null=True,blank=True)
	cmcY = models.CharField(max_length=100,null=True,blank=True, help_text='Year of CMC')

	def __str__(self):   
		return self.rmsId+'-'+self.capacity+'-'+self.custName+'-'+self.regID


class SiteData(models.Model):
	"""docstring for ClassName"""
	rmsId = models.CharField(max_length=40,null=True,blank=True, help_text='RMS ID or Site ID')
	Date = models.DateField(null=True,blank=True, help_text='Date of Data')
	dcenergy = models.FloatField(null=True,blank=True, help_text='Solar DC Energy in KWH')
	prthrs = models.FloatField(null=True,blank=True, help_text='Pump Running Hrs')
	lpd = models.IntegerField(null=True,blank=True, help_text='Total LPD/Flow')

	def __str__(self):   
		return self.rmsId+'-'+str(self.Date)
	
class homeid(models.Model):
	"""docstring for ClassName"""
	homeId = models.CharField(max_length=40,null=True,blank=True)



class meta:   #for admin database actions
	verbose_name = 'SiteDetails'
	erbose_name_plural = 'SiteDetails'

class meta:   #for admin database actions
	verbose_name = 'SiteData'
	erbose_name_plural = 'SiteData'
















	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg


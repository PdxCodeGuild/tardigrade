from django.db import models
from datetime import datetime
from datetime import date
from datetime import timedelta



class Claim(models.Model):
    claim_number = models.CharField(max_length=200, null=True, blank=True)
    lit_dates = models.CharField(max_length=200, null=True, blank=True)
    claimant = models.CharField(max_length=100, null=True, blank=True)
    action_required = models.CharField(max_length=200, null=True, blank=True)
    in_suit = models.CharField(max_length=100, null=True, blank=True)
    dc_assigned = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    date_coverage_letter_sent = models.CharField(max_length=100, null=True, blank=True)
    last_note_date = models.DateField(null=True, blank=True)
    insured_facility = models.CharField(max_length=200, null=True, blank=True)
    coverage_letter = models.CharField(max_length=200, null=True, blank=True)
    settlement_value = models.CharField(max_length=200, null=True, blank=True)
    insurer_policy = models.CharField(max_length=200, null=True, blank=True)
    bulk_insured = models.CharField(max_length=200, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return f'{self.claim_number}'

   
    @property
    def Days_Since_Last_Note(self):
        today = date.today()
        dsln = abs(self.last_note_date - today)
        dsln_stripped = str(dsln).split(",",1)[0]
        dsln_stripped_num = str(dsln_stripped).split(" ")[0]
        return  dsln_stripped_num

    @property
    def Days_Since_Last_Note_Over_60(self):
        today = date.today()
        dsln = abs(self.last_note_date - today)
        dsln_stripped = str(dsln).split(",",1)[0]
        dsln_stripped_num = str(dsln_stripped).split(" ")[0]
        if (int(dsln_stripped_num) > 59):
            return  dsln_stripped_num
        

    @property
    def Follow_Up_Date(self):
        fwp_date = self.last_note_date + timedelta(days=60)
        fwp_date_stripped = str(fwp_date).split(",",1)[0]
        # fwp_string =f'{fwp_date_stripped: %m/%d/%Y}'
        return  fwp_date_stripped

   



class Email(models.Model):
    claimNum = models.CharField(max_length=200, null=True, blank=True)
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE, null=True, blank=True)
    emailSubject = models.CharField(max_length=200, null=True, blank=True)
    emailFrom = models.CharField(max_length=200, null=True, blank=True)
    emailFromAddress = models.CharField(max_length=200, null=True, blank=True)
    emailTo = models.CharField(max_length=200, null=True, blank=True)
    emailBody = models.CharField(max_length=10000, null=True, blank=True)


    def __str__(self):
        return f'{self.claimNum}, {self.claim}'





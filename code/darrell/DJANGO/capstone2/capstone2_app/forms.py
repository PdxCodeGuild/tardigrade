from django import forms
from django.forms import ModelForm
from .models import Claim


#Create a Claim form

class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = ('claim_number', 'lit_dates', 'claimant', 'action_required', 'in_suit', 'dc_assigned', 'state',
         'date_coverage_letter_sent', 'last_note_date', 'insured_facility', 'coverage_letter',
         'settlement_value', 'insurer_policy','bulk_insured','claim_type' )


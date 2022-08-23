from django.shortcuts import render, redirect
from .models import Claim
from .models import Email
from .KishaCaseNotes import kisha_case_notes
from .outlookfilter import outlook_filter
from django.contrib.auth.decorators import login_required
from django.db.models import F
from.forms import ClaimForm
from django.core.paginator import Paginator
import re
#--> Rest
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import ClaimSerializer, EmailSerializer 
from rest_framework.response import Response
#-->
from datetime import datetime
from django.db.models import Sum, Min, Max, Avg, Count
from django.db.models import Q




def splash(request):
    return render(request, 'splash.html')

@login_required
def home(request):
    total_claims = Claim.objects.count()
    # claims_over_60 = [obj for obj in Claim.objects.all() if obj.Days_Since_Last_Note_Over_60]
    # total_claims_over_60 = len(claims_over_60)
    total_emails = Email.objects.count()
    nationwide = Claim.objects.filter(claim_type ='Nationwide').count()
    scottsdale = Claim.objects.filter(claim_type ='Scottsdale').count()

    context = {
        'total_claims': total_claims,
        'total_emails': total_emails,
        'nationwide': nationwide,
        'scottsdale': scottsdale,
        # 'total_claims_over_60': total_claims_over_60


        
    }
    return render(request, 'pages/home.html', context)

@login_required
def about(request):
    return render(request, 'pages/about.html')

@login_required
def claims(request):
    notes = kisha_case_notes()
    # email_to_claim()


    for x in range(len(notes)):
        claim_number = f'#{notes[x]["Claim #"]}'
        lit_dates = notes[x]["Lit Dates"]
        claimant = notes[x]["Claimant"]
        action_required = notes[x]["Action Required"]
        in_suit = notes[x]["In Suit?"]
        dc_assigned = notes[x]["DC Assigned?"]
        state = notes[x]["State"]
        date_coverage_letter_sent = notes[x]["Date Coverage Letter Sent"]
        # days_since_last_note = notes[x]["Days Since Last Note"]
        insured_facility = notes[x]["Insured/Involved Facility"]
        coverage_letter = notes[x]["Coverage Letter"]
        settlement_value = notes[x]["Settlement Value"]
        insurer_policy = notes[x]["Insurer/Policy"]
        bulk_insured = notes[x]["Bulk Insured?"]
        claim_type = notes[x]["Claim Type"]
        last_note_date = notes[x]["Last Note"]



        
        datetime_last_note_date = datetime.strptime(last_note_date, '%m/%d/%Y')
   

        Claim.objects.get_or_create(claim_number=claim_number, lit_dates=lit_dates, claimant=claimant, action_required=action_required, in_suit=in_suit, dc_assigned=dc_assigned,
                                    state=state, date_coverage_letter_sent=date_coverage_letter_sent, insured_facility=insured_facility,
                                    coverage_letter=coverage_letter, settlement_value=settlement_value, insurer_policy=insurer_policy, bulk_insured=bulk_insured, claim_type=claim_type, last_note_date=datetime_last_note_date)
                                   

# gets all of the blog posts from the database and stores them in a variable
  
    claims = Claim.objects.all()
    email_msg = Email.objects.all()

             

    for message in email_msg:
        claim = Claim.objects.filter(claim_number=message.claimNum).first()
        if claim:
            claim_id = claim.id
            claim_instance = Claim.objects.get(id=claim_id) ## this is a claim object filtered by the message
            message_object = Email.objects.get(id=message.id)
            message_object.claim = claim_instance
            message_object.save()

 
      
# creates the context dictionary to send the blog posts to the template
    claims = Claim.objects.all()
    email_msg = Email.objects.all()
    
    p = Paginator(Claim.objects.all().order_by('claim_number'), 10)
    page = request.GET.get('page')
    claims_list = p.get_page(page)
    

    context = {
        'claims': claims,
        'email_msg': email_msg,
        'claims_list': claims_list  
        
    }
    return render(request, 'pages/claims.html', context)





@login_required
def email(request):
    
    filtered_messages = outlook_filter()
        
    
 
    for x in range(len(filtered_messages)):
        regex = r"(#([0-9]{6,7})+(-G[A-Z])*)"
        search = re.search(regex, filtered_messages[x]['Subject'])
        search2 = re.search(regex, filtered_messages[x]['Body'])   

        if (search):
             claimNum = search.group()
            
        elif (search2):
             claimNum = search2.group()
             
        else: 
            claimNum = "No matching claim number"

        emailSubject = filtered_messages[x]['Subject']
        emailFrom = filtered_messages[x]['From: (Name)']
        emailFromAddress = filtered_messages[x]['From: (Address)']
        emailTo = filtered_messages[x]['To: (Name)']
        emailBody = filtered_messages[x]['Body']
        
        # print(claimNum)
        # print("Subject: " + emailSubject)


        
        Email.objects.get_or_create(claimNum=claimNum, emailSubject=emailSubject, emailFrom=emailFrom, emailFromAddress=emailFromAddress, emailTo=emailTo, emailBody=emailBody)
        # Email.objects.all().delete()
    # filtered_messages.clear()

# gets all of the blog posts from the database and stores them in a variable
    # email_msgs = Email.objects.all()
    email_msgs = Email.objects.all()
    # print(len(email_msgs))

# creates the context dictionary to send the blog posts to the template
    context = {
        'email_msgs': email_msgs
    }
    return render(request, 'pages/email.html', context)

@login_required
def claim_details(request, id):
    claim = Claim.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/claim_details.html', {"claim": claim}) 

@login_required
def email_details(request, id):
    email_msg = Email.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/email_details.html', {"email_msg": email_msg}) 


@login_required
def add_claims(request):
    if request.method == 'GET':  # if its a GET request, just display the add.html template
        return render(request, 'pages/add_claims.html')
    elif request.method == 'POST':  # if it's a POST request ..
        claim_number = request.POST['claim_number']
        lit_dates = request.POST['lit_dates']
        claimant = request.POST['claimant']
        action_required = request.POST['action_required']
        in_suit = request.POST['in_suit']
        dc_assigned = request.POST['dc_assigned']
        state = request.POST['state']
        date_coverage_letter_sent = request.POST['date_coverage_letter_sent']
        # days_since_last_note = request.POST['days_since_last_note']
        # follow_up_date = request.POST['follow_up_date']
        insured_facility = request.POST['insured_facility']
        coverage_letter = request.POST['coverage_letter']
        settlement_value = request.POST['settlement_value']
        insurer_policy = request.POST['insurer_policy']
        bulk_insured = request.POST['bulk_insured']
        claim_type = request.POST['claim_type']
        # last_note_date = request.POST['last_note_date']

    # add the new todo item to the database. objects.create() automatically saves the new todo item for us.
    Claim.objects.create(claim_number=claim_number, lit_dates=lit_dates, claimant=claimant, action_required=action_required, in_suit=in_suit, dc_assigned=dc_assigned,
                         state=state, date_coverage_letter_sent=date_coverage_letter_sent, insured_facility=insured_facility,
                         coverage_letter=coverage_letter, settlement_value=settlement_value, insurer_policy=insurer_policy, bulk_insured=bulk_insured, claim_type=claim_type)
    return redirect('claims')


@login_required
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        claims = Claim.objects.filter(claim_number__contains=searched)
        claimants = Claim.objects.filter(claimant__contains=searched)

        return render(request, 'pages/search.html', {'searched':searched, 'claims': claims, 'claimants': claimants}) 
    else:
        return render(request, 'pages/search.html', {})


@login_required
def delete_claim(request, id):
     claim = Claim.objects.get(id = id) ## we are assigning the element to a variable
     claim.delete()
     return redirect('claims') 
     



@login_required
def update_claim(request, id):
     claim = Claim.objects.get(id = id) ## we are assigning the element to a variable
     form = ClaimForm(request.POST or None, instance=claim)
     if form.is_valid():
         form.save()
         return redirect('claims')

     return render(request, 'pages/update_claim.html', {'claim': claim, 'form':form})

def chart(request):
  return render(request, 'pages/chart.html')

@api_view(['GET'])
def claims_api(request, format=None):
    """
    Get a list of claims or create a claim .
    """
    if request.method == 'GET':
        claims = Claim.objects.all()
        serializer = ClaimSerializer(claims, many=True)
        # return Response(serializer.data)
        return Response(serializer.data)
    
    
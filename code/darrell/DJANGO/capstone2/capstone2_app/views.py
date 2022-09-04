from django.shortcuts import render, redirect
from .models import Claim
from .models import Email
from .KishaCaseNotes import kisha_case_notes
from .outlookfilter import outlook_filter
import re



def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


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
        days_since_last_note = notes[x]["Days Since Last Note"]
        # follow_up_date = notes[x]["Follow-Up Date"]
        insured_facility = notes[x]["Insured/Involved Facility"]
        coverage_letter = notes[x]["Coverage Letter"]
        settlement_value = notes[x]["Settlement Value"]
        insurer_policy = notes[x]["Insurer/Policy"]
        bulk_insured = notes[x]["Bulk Insured?"]
        claim_type = notes[x]["Claim Type"]
        # last_note_date = notes[x]["Last Note"]

        Claim.objects.get_or_create(claim_number=claim_number, lit_dates=lit_dates, claimant=claimant, action_required=action_required, in_suit=in_suit, dc_assigned=dc_assigned,
                                    state=state, date_coverage_letter_sent=date_coverage_letter_sent, days_since_last_note=days_since_last_note, insured_facility=insured_facility,
                                    coverage_letter=coverage_letter, settlement_value=settlement_value, insurer_policy=insurer_policy, bulk_insured=bulk_insured, claim_type=claim_type)

# gets all of the blog posts from the database and stores them in a variable
    claims = Claim.objects.all()
    email_msg = Email.objects.all()
    
   
    for x in range(len(email_msg)):
    
        email_claim_no = email_msg[x] ##gets the claim from email
        claim_instance = Claim.objects.filter(claim_number=email_claim_no).first() ## looks for a claim in the database that has the same claim number
        if claim_instance: ## if the claim exists
            claim_instance_id = claim_instance.id
            claim = Claim.objects.get(id=claim_instance_id)
            email = Email.objects.filter(claimNum=claim_instance).first()
            email_instance = Email.objects.get(id=email.id)
            print(claim_instance)
            # email_instance.claim=claim_instance ## links the claim field from the email model to the claim instance
            # email_instance.save()      
            
                 
        
            
            
     
        # for y in range(len(email_msg)):
            
        #     print(claimNum)
        #     # if claim_number == claim:
        #     #      email_msg = Email.objects.filter(claim_number == claim).all()
        #     #      print(email_msg)


# creates the context dictionary to send the blog posts to the template
    context = {
        'claims': claims,
        'email_msg': email_msg
    }
    return render(request, 'pages/claims.html', context)






def email(request):
    
    filtered_messages = outlook_filter()
     
    
    # print(outlook_filter())

    
    
 
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
        days_since_last_note = request.POST['days_since_last_note']
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
                         state=state, date_coverage_letter_sent=date_coverage_letter_sent, days_since_last_note=days_since_last_note, insured_facility=insured_facility,
                         coverage_letter=coverage_letter, settlement_value=settlement_value, insurer_policy=insurer_policy, bulk_insured=bulk_insured, claim_type=claim_type)
    return redirect('claims')

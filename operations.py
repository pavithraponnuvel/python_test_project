
import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,members,organizers,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    
    if type.lower()=='organizer':
        f=open(organizers,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(members,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,members,organizers,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers,'r+')
    else:
        f=open(members,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org, events, Event_ID, Event_Name, Start_Date, Start_Time, End_Date, End_Time, Users_Registered,Capacity, Availability):
    '''Create an Event with the details entered by the organizer'''
    event_data = {
        "ID": Event_ID,
        "Name": Event_Name,
        "Organizer": org,
        "Start Date": Start_Date,
        "Start Time": Start_Time,
        "End Date": End_Date,
        "End Time": End_Time,
        "Users Registered":Users_Registered,  # Initialize as an empty list
        "Capacity": Capacity,
        "Seats Available": Availability
    }
    # for i in range(Users_Registered):
    #         topic = input(f"Enter  Topic {i} name ") #Operator
            
    try:
        with open(events, "r") as f:
            events = json.load(f)
    except JSONDecodeError:
        events = []
    events.append(event_data)

    with open(events, "w") as f:
        json.dump(events, f, indent=4)
    
    return event_data

    
def View_Events(org, events):
    '''Return a list of all events created by the logged-in organizer'''
    
    try:
        with open(events, "r") as f:
            event_data = json.load(f)
    except JSONDecodeError:
        event_data = []
     
    organizer_events = [event for event in event_data if event["Organizer"] == org]
    print(organizer_events)
    return organizer_events


def View_Event_ByID(events,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    try:
      with open(events,"r") as f:
       events=json.load(f)
    except JSONDecodeError:
       return None
    
    for event in events:
     if event.get("ID")==Event_ID:
      return event
    return None
    

def Update_Event(org,events,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, 
    then update the value entered by user for that key for the selected event
    || Return True if successful else False'''

    try:
      with open(events,"r") as f:
       events=json.load(f)
    except JSONDecodeError:
       return False
    for event in events:
     if event.get("ID")==event_id and  event.get("Organizer")==org:
      if detail_to_be_updated in event:
       event[detail_to_be_updated]=updated_detail
       with open(events,"w") as f:
        json.dump(events,f,indent=4)
       return True
      else:
       return False
    return False

    

    

def Delete_Event(org,events,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    try:
      with open(events,"r") as f:
       events=json.load(f)
    except JSONDecodeError:
       return False

    new_events=[event for event in events if not (event.get("Organizer")==org and event.get("ID")==event_ID)]
    if len(new_events)<len(events):
      with open(events,"w") as f:
        json.dump(events,f,indent=4)
      return True
    else:
       return False
     


def Register_for_Event(events,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    try:
      with open(events,"r") as f:
       events=json.load(f)
    except JSONDecodeError:
       return False
    for event in events:
     if event.get("ID")==event_id:
      event["Users Registered"].append(Full_Name)
      with open(events,"w") as f:
        json.dump(events,f,indent=4)
      return True
    return False 

def fetch_all_events(events,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    try:
      with open(events,"r") as f:
       events=json.load(f)
    except JSONDecodeError:
       return False

    filter_events=[]
    for event in events:
     event_datetime=current_time
     if upcoming_ongoing=="upcoming" and event_datetime>now:
      filter_events.append(event)
     elif upcoming_ongoing=="ongoing" and event["End Date"]>=current_time:
      filter_events.append(event)
     elif upcoming_ongoing=="both":
      filter_events.append(event)
    registered_events=[event for event in filter_events if Full_Name in event["Users Registered"]]
    return [{detail:event.get(detail) for detail in event_details} for event in registered_events ]

def Update_Password(members,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    try:
      with open(members,"r") as f:
       members=json.load(f)
    except JSONDecodeError:
       return False
    for member in members:
     if member.get("Full_Name")==Full_Name:
       member["Password"]=new_password
       with open(members,"w") as f:
        json.dump(members,f,indent=4)
       return True
     else:
       return False
    return False

def View_all_events(events):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(events,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
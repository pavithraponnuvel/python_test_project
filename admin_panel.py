#Admin Functioanlity
import json
import random
import datetime
class Admin_Panel:
    
    def __init__(self):
        self.module_details = {}
        self.count = 0
        self.trainer_details = {}
        self.batch_details = {}
        self.student_details = {}

    def admin_login(self,username,password):
        if username=="admin" and password=="admin":
            return True
        return False
    
    def add_module(self):
        self.count=self.count+1
        module_name = input("Enter Module Name :")
        duration = input("Enter Module Duration : ")
        topic_list = []
        topic_size = int(input("Enter the Number of Topics whoch we want to add :"))
        for i in range(1,topic_size+1):
            topic = input(f"Enter  Topic {i} name ") #Operator
            topic_list.append(topic)
        module_items = {"module_name":module_name,"duration":duration,"topics":topic_list}
        self.module_details[self.count] = module_items
        with open("add_module.json","w") as f:
            json.dump(self.module_details,f,indent = 4)
        return self.module_details
    
    def add_trainer(self):
        self.count = self.count+1  
        name = input("Enter Trainer Name :")
        gender = input("Enter Trainer's Gender :")
        qualification = input("Enter Trainer's Qualification :")
        experience = input("Enter Trainer Experience : ")
        mob = int(input("Enter Trainer's Mobile Number :"))
        email = input("Enter Email id : ")
        password = input("Enter Password :")

        trainer_data = {"trainer_name":name,"gender":gender,"qualification":qualification,"experience":experience,"mobile_no":mob,"Email":email,"Password":password}
        self.trainer_details[self.count] = trainer_data
        with open("trainer_details.json","w") as f:
            json.dump(self.trainer_details,f,indent=4)
        return self.trainer_details
    
    def add_batch(self):
        self.count = self.count+1
        std_list = []
        module_name = input("Enter Module Name :")
        trainer_name = input("Enter Trainer Name for That Batch :")
        student_size = int(input("Enter Number of Student  : "))
        for i in range(1,student_size+1):
            std = input("Enter Student {i} Name ")
            std_list.append(std)
        #student_data = input("Enter Student Data : ")
        batch_data = {"module_name":module_name,"trainer_name":trainer_name,"student_data":std_list}
        self.batch_details[self.count]=batch_data
        with open("batch_details.json","w") as f:
            json.dump(self.batch_details,f,indent=4)
        return self.batch_details
    
    def Read_Trainer_Details(self):
        with open("trainer_details.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Trainer_id : {k}  || Trainer Details : {v}")
            print("*"*100)

    def Read_Module_Details(self):
        with open("add_module.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Module_id : {k}  || Module Details : {v}")
            print("*"*100)
#"2023" --> 23
    def add_student(self):
        current_date = datetime.datetime.now()
        exact_date = str(current_date.day)+str(current_date.month)+str(current_date.year)[2:]

        if len(exact_date)==4:
            exact_date = "0"+str(current_date.day)+"0"+str(current_date.month)+str(current_date.year)[2:]
        else:
            exact_date = str(current_date.day)+str(current_date.month)+str(current_date.year)[2:]

        key = "DS"+str(exact_date)
        student_list = []
        student_size = int(input("Enter the Number of Student which you want to add  : "))
        for i in range(1,student_size+1):
            print(f"Enter the Details of Student {i} ")
            name = input(f"Enter name of Student {i} ")
            gender = input(f"Enter Gender of Student {i} ")
            age = input(f"Enter age of Student {i} ")
            qualification = input(f"Enter Qualification of Student {i} ")
            experience = input(f"Enter Experience of Student {i} ")
            mob = input(f"Enter Mobile Number of Student {i} ")
            email = input(f"Enter Email of Student {i} ")
            password = input(f"Enter Password of Student {i} ")
            student_data = {"Studen name ":name,"Student_Gender":gender,"Student_Age":age,"Qualification":qualification,"Experience":experience,"Mobile Number":mob,"Mail Id":email,"Password":password}
            student_list.append(student_data)
        self.student_details[key] = student_list
        with open("student_details.json","w") as f:
            json.dump(self.student_details,f,indent=4)
        return self.student_details
    
    def Read_Student_Details(self):
        with open("student_details.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Batch_id : {k}  || Batch Students : {v}")
            print("*"*100)

    def update_trainer_details(self):
        with open("trainer_details.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Trainer_id : {k}  || Trainer Details : {v}")
            print("*"*100)
        id = (input("Enter the Trainer id which you want to update  :"))
        field = input("Enter the Field which you want to update :")
        updated_value = input("Enter the updated value :")
        data[id][field] = updated_value
        with open("trainer_details.json","w") as f:
            json.dump(data,f,indent=4)
        return data
    
    def remove_module(self):
        with open("add_module.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Module_id : {k}  || Module Details : {v}")
            print("*"*100)
        id = input("Enter Module ID which you want to remove :")
        del data[id]
        with open("add_module.json","w") as f:
            json.dump(data,f,indent=4)
        return data



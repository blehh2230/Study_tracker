import json
from datetime import date
def main_menu():
    choice=0
    print("Welcome to Study Tracker!!")
    while True:
     print("1.Start Study Session")
     print("2.View Statistics")
     print("3.View Streaks")
     print("4.Exit")
     choice=int(input("Enter your choice: "))
     if choice==1:
        print("Starting study session..")
        add_study_session()
     elif choice==2:
        print("Showing Statistics..")
     elif choice==3:
        print("Showing Streaks..")
     elif choice==4:
        print("Thank you! for using study tracker!!")
        break
     else:
        print("Invalid Choice!Try again!")

def load_data():
   with open("data.json","r") as f:
      return json.load(f)

data=load_data()

def save_data():
   with open("data.json","w") as f:
      json.dump(data,f,indent=4)

def add_study_session():
   subject=input("enter your subject name:")
   duration=int(input("enter the duration in minutes:"))
   xp_earned=duration//10

   session={
      "subject":subject,
      "duration":duration,
      "date": str(date.today()),
      "xp_earned":xp_earned
   }

   data["sessions"].append(session)
   data["total_xp"]+=xp_earned
   data["level"]=data["total_xp"]//50

   save_data()
   print("you earned",xp_earned,"XP today!!")


main_menu()
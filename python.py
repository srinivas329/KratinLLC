class Patient:
    def __init__(self,patient_name,age,blood_group,blood_pressure,sugar_level):
        self.patient=patient_name
        for i in self.patient:
            if(i.isdigit()):
                raise NameError
        self.age=age 
        self.blood_group=blood_group[:-1]
        self.sign=blood_group[-1]
        self.s=""
        if(self.sign=="+"):
            self.s="Positive"
        else:
            self.s="Negative"
        self.blood_pressure=blood_pressure 
        self.sugar=sugar_level
        if(not(65<=self.age<=100) or len(str(self.blood_pressure))>3 or len(str(self.sugar))>3):
            raise ValueError
    def details(self):
        return('''patient  : {}
Age(should be 65 to 100 only):{}
blood group(A or B or O or AB): {}    Sign:{}  
Blood pressure(BP) : {}
Diabetes           : {}'''.format(self.patient,self.age,self.blood_group,self.s,self.blood_pressure,self.sugar))
    def bp_Checking(self):
        if(self.blood_pressure>110)and(self.blood_pressure<=140):
            print("""Blood pressure Result:-This is normal. 
------------------------------------------------------------------
** please do this bellow Precations.
---------------------------------------------------------------------------------------
Precations:-
------------
1.As a general goal, aim for at least 30 minutes 
of moderate physical activity every day.
2.Exercise can also help keep elevated blood pressure
from turning into high blood pressure (hypertension). 
3.For those who have hypertension,
regular physical activity can bring blood pressure down to safer levels.""")
        elif(self.blood_pressure<=110):
            print('''Blood pressure Result:- This is Low Blood blood pressure. 
** If you want to over come this problem please do this bellow Precations.
---------------------------------------------------------------------------------------
Precations :-
-----------
1.Eat more salt. Contrary to popular advice, 
low-sodium diets are not good for everyone with blood pressure problems. ...
2.Avoid alcoholic beverages. ...
3.Discuss medications with a doctor. ...
4.Cross legs while sitting. ...
5.Drink water. ...
6.Eat small meals frequently. ...
7.Wear compression stockings. ...
8.Avoid sudden position changes.''') 
        
        elif(self.blood_pressure >140)and(self.blood_pressure<=180):
            print('''Blood pressure Result:-This is symptom for getting blood pressure. 
** If you want to over come this problem please do this bellow Precations.
---------------------------------------------------------------------------------------
Precations:-
------------
1.Lose extra pounds and watch your waistline. 
2.Blood pressure often increases as weight increases. 
3.Exercise regularly. 
4.Eat a healthy diet. 
5.Reduce salt (sodium) in your diet. 
6.Limit alcohol. 
7.Get a good night's sleep. 
8.Reduce stress. 
9.Monitor your blood pressure at home and get regular checkups.''')
        else:
            print('''Blood pressure Result:-It means you have high blood pressure.
 -----------------------------------------------------------------------------
 **If you want to over come this problem please do this bellow Precations.
---------------------------------------------------------------------------------------
TREATMENT:
----------
1.Eating a heart-healthy diet without salt.
2.Getting regular physical activity.
3.Maintaining a healthy weight or losing weight.
4.Limiting alcohol.
5.Not smoking.
6.Getting 7 to 9 hours of sleep daily.
7.immidiatly consult doctore for medicine.''')
    def sugar_checking(self):
        if(self.sugar<=140):
            print('''Blood sugar result:- This is normal keep maiatain like this

Precations:-
------------
1.Lose extra weight. Losing weight reduces the risk of diabetes. ...
2.Be more physically active. There are many benefits to regular physical activity. ...
3.Eat healthy plant foods. Plants provide vitamins, minerals and carbohydrates in your diet. ...
4.Eat healthy fats. ...
5.Skip fad diets and make healthier choices.''')
        elif(self.sugar>140)and(self.sugar<=200):
            print('''Blood sugar result:- Due to this, symptoms of blood sugar 
Precations:-
------------
1.Keep track of your blood sugar levels to see what makes them go up or down.
2.Eat at regular times, and don't skip meals.
3.Choose foods lower in calories, saturated fat, trans fat, sugar, and salt.
4.Track your food, drink, and physical activity.
5.Drink water instead of juice or soda.''')
        else:
            print('''Blood sugar result:- It means High amount of suger in your blood
Precations:-
---------------------------------------------------------------------------------------
1.Follow a balanced diet: Focus on a well-balanced diet that includes(whole grains, lean proteins, healthy fats, and plenty of fruits and vegetables and non-sugary food).
2.Monitor carbohydrate intake: Be mindful of your carbohydrate intake,carbohydrates with a lower glycemic index.
3.Regular physical activity.
4.Medication management: If you have been prescribed medication, such as insulin or oral hypoglycemic agents, follow the prescribed dosage and timing strictly. Ensure you have a proper understanding of how to administer or take your medications correctly. 
5.Regular blood sugar monitoring:Keep track of your readings and identify patterns to make necessary adjustments to your diet, exercise, or medication regimen.
6.Stay hydrated: Drink plenty of water throughout the day to stay hydrated. Avoid sugary beverages and excessive caffeine intake, as they can contribute to elevated blood sugar levels.
7.Stress management: Practice stress-reducing techniques such as deep breathing exercises, meditation, yoga, or engaging in hobbies and activities that help you relax. Stress can contribute to elevated blood sugar levels, so managing stress is crucial.
8.Get enough sleep: Aim for 7-9 hours of quality sleep each night. Poor sleep can affect blood sugar control and insulin sensitivity. Establish a consistent sleep routine and create a sleep-friendly environment.
9.Regular check-ups: Schedule regular check-ups with your healthcare provider to monitor your blood sugar levels, assess your overall health, and make any necessary adjustments to your management plan.
10.Educate yourself: Learn about diabetes management, blood sugar control, and healthy lifestyle practices. Stay informed about new research and advancements in diabetes care. Attend diabetes education classes or support groups to gain further knowledge and support.''')
#-----------------------------------------------------------------------------
# I am taking sugar in blood and bp(blood pressure if this is normal then this peoples are good in health. I feel like this. So that's why I wrote a code for these things.        
       
try:        
    name=input("Enter Name: ")
    a=int(input("Enter Your Age: "))
    b=input("Enter Your Blood Group: ")
    blood_pressure=int(input("Enter Your Blood Pressure(As per Test result): "))
    sugar=int(input("Enter Your Suger Leves(As per Test Result): "))
    obj=Patient(name,a,b,blood_pressure,sugar)
    print(obj.details())
    print("*"*70)
    obj.bp_Checking()
    print("*"*70)
    obj.sugar_checking()
    print("*"*70)
except ValueError:
    print("Please check your age or bp or suger values are may be incorrect....")
except NameError:
    print("please provide correct name or blood group ...")
except:
    print("please make sure the information is correct, please check once....")
finally:
    print("""------------ ** Stay Healthy **------------""")
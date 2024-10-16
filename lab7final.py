name=input("What is your Name: ")
section=input("What is your Section: ")
prelim=float(input("Preliminary Period Grade: "))
if 40<=prelim<=100:
    midterm=float(input("Midterm Period Grade: "))
    if 40<=midterm<=100:
        finals=float(input("Final Period Grade: "))
        if 40<=finals<=100:
            totalgrade=prelim+midterm+finals
            finalgrade=round(totalgrade/3)
            displayfinalgrade=str(finalgrade)
            if finalgrade<75:
                 print("Final Grade:",displayfinalgrade)
                 print("Grade Point: 5.0")
                 print("Percentage Equivalent: <75%")
                 print("General Description: Failed")
            elif 77>=finalgrade>=75:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 3.0")
                print("Percentage Equivalent: 75-77%")
                print("General Description: Passed")
            elif 80>=finalgrade>=78:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 2.75")
                print("Percentage Equivalent: 78-80%")
                print("General Description: Fair")
            elif 83>=finalgrade>=81:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 2.50")
                print("Percentage Equivalent: 81-83%")
                print("General Description: Fairly Satisfactory")
            elif 86>=finalgrade>=84:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 2.25")
                print("Percentage Equivalent: 84-86%")
                print("General Description: Satisfactory")
            elif 89>=finalgrade>=87:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 2.0")
                print("Percentage Equivalent: 87-89%")
                print("General Description: Good")
            elif 92>=finalgrade>=90:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 1.75")
                print("Percentage Equivalent: 90-92%")
                print("General Description: Very Good")
            elif 95>=finalgrade>=93:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 1.50")
                print("Percentage Equivalent: 93-95%")
                print("General Description: Superior")
            elif 98>=finalgrade>=96:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 1.25")
                print("Percentage Equivalent: 96-98%")
                print("General Description: Outstanding")
            elif 100>=finalgrade>=99:
                print("Final Grade:",displayfinalgrade)
                print("Grade Point: 1.0")
                print("Percentage Equivalent: 99-100%")
                print("General Description: Excellent")
            else:
                print("Invalid Final Grade")
        else:
             print("Invalid Input, Please Enter a Valid Grade")
    else:
        print("Invalid Input, Please Enter a Valid Grade")       
else:
    print("Invalid Input, Please Enter a Valid Grade")

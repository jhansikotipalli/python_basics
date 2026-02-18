#student marks and results
maths=int(input("enter maths marks:"))
english=int(input("enter english marks:"))
telugu=int(input("enter telugu marks:"))
science=int(input("enter science marks:"))

if(maths>35 and english>35 and telugu>35 and science>35):
    print("student is pass")
    total=maths+english+telugu+science
    avg=total/4
    if(avg>60):
        print("first class")
    elif(avg>50):
        print("second class")
    else:
        print("third class")
else:
    print("student fail")

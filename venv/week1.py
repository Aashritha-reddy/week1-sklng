class Students:
  def __init__ (s,id,fname,lname,Course,Year,gpa,University,Mobileno):
   s.id=id
   s.fname=fname
   s.lname=lname
   s.Course=Course
   s.Year=Year
   s.gpa=gpa
   s.University=University
   s.Mobileno=Mobileno
def __mail(self):
      print("Email of id number",self.id,"is:", self.id,"@kluniversity.in")
m=Students(190330264,"aashritha","reddy","cse","2nd year",8.9,"KlUniversity" , 9390321321 )
n=Students(190330462,"sharu","reddy","cse","2nd year",9.5,"KlUniversity",9876543210)
print(m.id,m.fname,m.lname,m.Course,m.Year,m.gpa,m.University,m.Mobileno)
print(n.id,n.fname,n.lname,n.Course,n.Year,n.gpa,n.University,n.Mobileno)
m.mail()
n.mail()
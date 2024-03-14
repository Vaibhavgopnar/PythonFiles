# Using Regex
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email=input("Enter your Email : ")

if re.search(email_condition, email):
    print("Right Email")
else:
    print("Wrong Email")

# Using Iteration
# k,j,d=0,0,0
# if len(email) >= 6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@")==1):
#             if (email[-4]==".") ^ (email[-3]=="."):
#                 for i in email:
#                     if i==i.isspace():
#                         k=1
#                     elif i.isalpha():
#                         if i==i.upper():
#                             j=1
#                     elif i.isdigit():
#                         continue
#                     elif i=="_" or i=="." or i=="@":
#                         continue
#                     else:
#                         d=1
#                 if k==1 or j==1 or d==1:
#                     print("Wrong Email 5")
#                 else:
#                     print("Right Email")
#             else:
#                 print("Wrong Email 4")
#         else:
#             print("Wrong Email 3")            
#     else:
#         print("Wrong Email 2")
# else:
#     print("wrong Email 1")



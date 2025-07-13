import subprocess
import ipaddress
import socket 

l=["ping","-n","4"] #This is for windows . 4 represents number of packets used for testing
# use ["ping","-c","4"] for linux/mac
var = input("enter the ip or domain:")
try:
    ipaddress.ip_address(var) #used for validating ip address
    print("Valid ip")
except ValueError:
    try:
        var=socket.gethostbyname(var) # if the user enters domain . returns ip address
    except socket.gaierror:
        print("Invalid Ip, Please try again ")
        exit()
l.append(var)
obj = subprocess.run(l,capture_output=True,text=True) 
#capture_output = True is used to get ouput in python , else you get output in console
#text=True makes the output into a string . output is bytes by default
print(obj.stdout)
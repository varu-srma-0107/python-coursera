print("how many kms do you run today?")
###input function takes a string input
#so convert it to the float
kms = input ()
print ("Ok so you run "+kms+"kms" )
miles= float( kms)/1.609

print (f"And it is equal to {miles} Miles")


print(type(kms))
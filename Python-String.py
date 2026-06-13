#single Line String
a= "Introduction:"
print(a)

#Multiple Line String
b="""Hi! I am Tanjim. I am studying at KBTU. 
I am doing my BSc in Robotics and Mechatronics"""


# String is an Array of Char
print(b[0])
print(b[6])
print(b[7])
print(b[1])
print(b[5])
print(b[4])
print(b[3])
print(b[2::5])

#len() function return the length of string

print(len(a))

# Check a phrase in string

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")



  txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

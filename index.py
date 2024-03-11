print("Ayush Raj CC Lab Mst")
name = input("Enter your Name: ")
email = input("Enter your Email Id: ")
phone = input("Enter your Phone Number: ")
cgpa = input("Enter your current cgpa: ")

print("Enter your 3 Hobbies")
hobbies = []
for i in range(3):
    hobby = input()
    hobbies.append(hobby)

print("Enter 3 Project Names")
projects = []
for i in range(3):
    project = input()
    projects.append(project)

company = input("Enter company to apply: ")

print("...............RESUME................")
print("Name:", name)
print("I", name, "want to join your company", company, "for SDE position")
print("My Contact info:", phone, ",", email)
print("Current CGPA:", cgpa)
print("My Hobbies:", hobbies)
print("My Projects:", projects)

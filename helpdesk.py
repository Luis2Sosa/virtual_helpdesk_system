def info():
    return "We are a company dedicated to offering the best service in the region. We have been providing general assistance to all our clients since 1994."
def hours():
    return "Our business hours are from 8 AM to 6 PM, Monday through Friday, except holidays."
def support():
    return "We have support 24 hours a day, 7 days a week"
def contact():
    return "Our contact number is 1800-357-7777"


options = {
    "company info": info,
    "working hours": hours,
    "tech support": support,
    "contact": contact     
}

print("TechEase Support Inc.")
print("---------------------\n")

while True:
    print("Please select an option:\n")
    print("Company info")
    print("Working hours")
    print("Tech support")
    print("report issue")
    print("Contact")
    print("Exit\n")
    
    try:
        option = input("Greetings! What do you want to know?\n").lower()
        if option == "report issue":
            problems = input("Give a brief description of the problem.\n")
            print("Your issue has been recorded...\n")
            continue
            
        elif option == "exit":
            print("Thank you for choosing us. We hope you have a happy rest of the day.")
            break
        
        control = options.get(option, lambda: "invalid option")
        print(control())
        
    except FileNotFoundError:
        print("error: not found")
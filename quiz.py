print("welcome to our 10 basic computer questions")
score = 0
play = input("Do you want to play the game Yes/No ")
if play.upper() != "YES":
    exit()
print("What does CPU stand for?")
print("A) Central Processing Unit")
print("B) Computer Personal Unit")
print("C) Centralized Processing Unit")
print("D) Computer Power Unit")
answer=input("Answer is ")
if answer.upper() == 'A':
     score +=1

print("Which of the following is an operating system? ")
print("A) Microsoft Word")
print("B) Google Chrome")
print("C) Windows 10")
print("D) Adobe Photoshop")
answer=input("Answer is ")
if answer.upper() == 'C':
     score +=1

print("What is the primary function of RAM?")
print("A) Store data permanently")
print("B) Store data temporarily")
print("C) Process data")
print("D) Connect to the internet") 
answer=input("Answer is ")
if answer.upper() == 'B':
     score +=1      

print("What does URL stand for? ")
print("A) Uniform Resource Locator")
print("B) Universal Resource Link")
print("C) Uniform Retrieval Locator")
print("D) Universal Retrieval Link")
answer=input("Answer is ")
if answer.upper() == 'A':
     score +=1

print("Which device is used to input text into a computer? ")
print("A) Monitor")
print("B) Keyboard")
print("C) Printer")
print("D) Scanner")
answer=input("Answer is ")
if answer.upper() == 'B':
     score +=1

print("What is the main function of an operating system? ")
print("A) To connect to the internet")
print("B) To manage hardware and software resources")
print("C) To create documents")
print("D) To store files")
answer=input("Answer is ")
if answer.upper() == 'B':
     score +=1

print("Which of the following is a web browser? ")
print("A) Microsoft Excel")
print("B) Mozilla Firefox")
print("C) Adobe Reader")
print("D) Notepad")
answer=input("Answer is ")
if answer.upper() == 'B':
     score +=1

print("What is phishing? ")
print("A) A type of software")
print("B) An attempt to obtain sensitive information")
print("C) A form of online shopping")
print("D) A method of coding")
answer=input("Answer is ")
if answer.upper() == 'B':
     score +=1

print("What does the term cloud computing refer to? ")
print("A) Using remote servers to store and manage data")
print("B) Using a physical hard drive")
print("C) Connecting multiple computers in a network")
print("D) None of the above")
answer=input("Answer is ")
if answer.upper() == 'A':
     score +=1

print("Which file extension is commonly associated with Microsoft Word documents? ")
print("A) .jpg")
print("B) .docx")
print("C) .xlsx")
print("D) .pptx")
answer=input("Answer is ")
if answer.upper() == 'B':
     score +=1

percentage = (score / 10) * 100
print(f"You have scored {score} out of 10. Your percentage score is {percentage}%")

if score > 6:
    print("Congratulations, you have passed the test!")
else:
    print("You have not yet passed the test. Please redo the test to meet 70%.")
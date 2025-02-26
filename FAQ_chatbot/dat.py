import csv

# Define your FAQ data
faq_data = [
    # Admission-related questions
    ["What is the admission process?", 
     "You can apply online through our university portal. Ensure you meet the requirements before applying."],
    ["Are scholarships available?", 
     "Yes, we offer a variety of scholarships based on merit and financial need. Check our scholarships page for more details."],
    ["What documents are required for admission?", 
     "You will need to submit your academic transcripts, proof of identity, and any additional documents depending on the program."],
    ["Can international students apply?", 
     "Yes, we welcome international students! Visit our international admissions page for specific requirements."],
    
    # Course-related questions
    ["What courses are offered?", 
     "We offer various courses in Engineering, Business, Arts, and Sciences. Check our website for the full list."],
    ["Do you offer online courses?", 
     "Yes, we have several online programs. Visit our e-learning section for details."],
    
    # Financial questions
    ["What is the tuition fee?", 
     "Tuition fees vary depending on the program. Visit the finance section on our website for details."],
    ["Are there payment plans available?", 
     "Yes, we offer flexible payment plans. Contact our finance office for more information."],
    
    # Campus-related questions
    ["Where is the campus located?", 
     "Our campus is located at 123 University Avenue, City, Country."],
    ["What are the campus facilities?", 
     "Our campus offers modern classrooms, libraries, sports facilities, dormitories, and dining halls."],
    
    # Contact-related questions
    ["How can I contact the admissions office?", 
     "You can reach the admissions office via email at admissions@university.edu or call 123-456-7890."],
    ["How can I contact the finance office?", 
     "You can contact the finance office at finance@university.edu or call 987-654-3210."],
    
    # Miscellaneous
    ["What are the university's working hours?", 
     "The university operates from 8 AM to 5 PM, Monday to Friday."],
    ["Is there a library?", 
     "Yes, we have a well-equipped library with both physical and digital resources."],
    ["What extracurricular activities are available?", 
     "We offer various clubs, sports teams, and cultural activities. Check our website for a full list."],
    ["Do you have student housing?", 
     "Yes, we provide on-campus housing facilities for students. Visit the housing section of our website for more details."]
]

# File path for the CSV
file_path = "university_faq.csv"

# Write data to CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Question", "Answer"])  # Header
    writer.writerows(faq_data)

print(f"CSV file '{file_path}' created successfully!")

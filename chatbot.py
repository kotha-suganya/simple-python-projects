import re

def chatbot():
    print("🎓 Bot: Hi! I’m your Pragati Engineering College Assistant 🤖. I am here to clear all your doubts regarding the college. Type 'bye' anytime to exit.")
    print("🎓 Bot: You can either type your question (e.g., 'exam date', 'fees') or use the menu below:")
    print("1. Courses Offered\n2. Admission Process\n3. Fees & Scholarships\n4. Exam & Results\n5. Hostel & Facilities\n6. Contact College\n7. Branches offered\n8. Placements\n9. Alumni\n10. Exit")

    state = None  # to track context if needed

    while True:
        user_input = input("You: ").lower().strip()

        # ---- Exit condition ----
        if user_input == "bye" or user_input == "10":
            print("🎓 Bot: Goodbye! 👋 All the best with your studies.")
            break

        # ---- Menu options ----
        if user_input == "1" or "course" in user_input:
            print("🎓 Bot: We offer B.Tech and M.Tech programs.")
        elif user_input == "2" or "admission" in user_input:
            print("🎓 Bot: Admission details are available online at https://pragati.ac.in/.")
        elif user_input == "3" or "fee" in user_input or "scholarship" in user_input:
            print("🎓 Bot: Fees vary by course. Scholarships are available for meritorious and economically weaker students. Fees reimbursements are also provided by the government of Andhra Pradesh to some students based on the competitive exam rankings")
        elif user_input == "4" or "exam" in user_input or "result" in user_input:
            print("🎓 Bot: Semester exams are held in November & May. Results are published within 30 days after exams.")
        elif user_input == "5" or "hostel" in user_input or "facility" in user_input:
            print("🎓 Bot: The college has hostel for boys , a library , Canteen, computer labs , and sports facilities .")
        elif user_input == "6" or "contact" in user_input:
            print("🎓 Bot: You can reach us at https://pragati.ac.in/contact/.")
        elif user_input == "7" or "Branches" in user_input :
            print("🎓 Bot: The college offers many branches such as ECE, EEE, MECH, CIVIL, CSE, CSE(AI), CSE(DS), CSE(AI&ML), CS, IT .")
        elif user_input == "8" or "Placements" in user_input:
            print("🎓 Bot: You can reach us at https://pragati.ac.in/career-development-centre/placement-statistics/.")
        elif user_input == "9" or "Alumni" in user_input:
            print("🎓 Bot: You can reach us at https://pragati.ac.in/alumni/ .")


        # ---- Regex greetings ----
        # elif re.search(r"\bhi|hello|hey\b", user_input):
        elif re.search(r"\b(hi|hello|hey)\b", user_input):

            print("🎓 Bot: Hello! 👋 How can I help you with your college doubts?")
        elif re.search(r"\b(thanks|thank you)\b", user_input):
            print("🎓 Bot: You’re welcome! 😊")

        # ---- Unknown input ----
        else:
            print("🎓 Bot: Sorry, I didn’t understand that. Please use the menu (1–10).")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

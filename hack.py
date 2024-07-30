from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

# Assume you have a list of question-answer pairs based on your content
content_qa_pairs = [
    ("What is the eligibility criteria?", "K L Deemed to be University accepts Uni-GAUGE score for B.Tech admissions. \nEligibility requires a pass in 10+2 or equivalent examination with 60% and above in aggregate and 60% and above in Group subjects. \nStudents with Physics, Chemistry, and Mathematics (PCM) are eligible for all B.Tech programs including Bio-Technology. \nStudents with Physics, Chemistry, and Biology (PCB) are eligible for B.Tech. \nFor BCA, Class 12 with a minimum of 55% aggregate in a relevant stream from a recognized school is required. \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)"),
    ("What is the admission process?", "Admission to KL Deemed to be University is based on a valid score in either KLEEE (B.Tech), KLECET (B.Tech Lateral Entry), or KLMAT (Management), an in-house KL University entrance exam. \nAside from engineering and management programs, the admission process is based on a merit score followed by the Personal Interview (PI) round. \nKey points: \n1. The online application form is for admission into different programs offered at KL University in Hyderabad and Vijayawada. \n2. Application Fee is Rs.1000/-. \n3. Please submit a working Email ID for all future correspondence. \n4. NRI/PIO/OCI candidates are also eligible to apply. \n5. You can edit your application form except for your Email ID and mobile number. \n6. Your choice of program preference is for statistical purposes only. The final decision on the program choice will be made during counseling. \n7. Entrance Exam, counseling, and course commencement dates will be scheduled as per the Government norms. \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)"),
    ("What are the documents required for admission?", "The documents required for admission are: primary and secondary education marks memos, Aadhar card, memos of competitive exams if participated, and KLEEE entrance score sheet. \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)"),
    ("What kind of scholarship opportunities are available?", "In the realm of engineering scholarships, notable programs include: \n- *KLEEE 2021 Ranks*: Offer varying fee concessions based on rank brackets in subjects like CSE, AI&DS, and BT. \n- *JEE MAINS Percentile*: Determined by percentile scores, with higher percentiles leading to greater fee reductions. \n- *CBSE and AP/TS State Intermediate Board*: Scholarships based on CGPA or percentage scores from these boards. \n- *Other State Boards*: Similar scholarships based on CGPA or percentage scores from other state boards. \n- *AP/TS EAMCET or Any Other CET Ranks*: Concessions determined by ranks in relevant entrance tests. Conditions apply, including the need to maintain the same CGPA or percentage score for continued eligibility. \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)"),
    ("What are the available courses and fee structure?", "- The BTech program at Koneru Lakshmaiah Education Foundation University offers three branches: Computer Science and Engineering (CSE), Computer Science and Information Technology (CSIT), and Electronics and Communication Engineering (ECE).  \n- The fee structure for each branch without concession is as follows:   \n- *For CSE*:     \n- *Admission Fee (One Time)*: INR 15,000     \n- *Tuition Fee (Semester 1 & 2)*: INR 127,500 each     \n- *Total*: INR 270,000 for the first year, decreasing to INR 255,000 for subsequent years.   \n- *For CSIT*:     \n- *Admission Fee (One Time)*: INR 15,000     \n- *Tuition Fee (Semester 1 & 2)*: INR 125,000 each     \n- *Total*: INR 265,000 for the first year, decreasing to INR 250,000 for subsequent years.   \n- *For ECE*:     \n- *Admission Fee (One Time)*: INR 15,000     \n- *Tuition Fee (Semester 1 & 2)*: INR 120,000 each     \n- *Total*: INR 255,000 for the first year, decreasing to INR 240,000 for subsequent years.  \n- Additionally, Koneru Lakshmaiah Education Foundation University offers a regular Bachelor of Computer Applications (BCA) program with four specializations. It is a three-year, full-time program with an industry-oriented curriculum divided into six semesters. The total fee for the BCA program is INR 4.65 lakh, including tuition fees for all academic years and a one-time admission fee of INR 15,000. \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)"),
    ("Where is the campus located and timings to visit the campus?", "Address: Miyapur Rd, near Saibaba temple, ALEAP Industrial Area, Bowrampet, Hyderabad, Telangana 500043 \nVisiting Hours : 9AM - 5PM(Monday-Saturday) \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)"),
    ("What are the housing options available?", "The fee varies depending on the room that the student opts for. There are single-bed and double-bed sharing with AC and Non-AC facilities. \nFor Non AC double sharing room – INR 1.10 LPA \nFor Non AC single sharing room – INR 1.20 LPA \nFor AC double sharing room – INR 1.20 LPA \nFor AC single sharing room – INR 1.35 LPA \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)"),
    ("What kind of companies are students placed into?", "Placements: KL University placements 2023 are in progress and have recorded 2893 placements with 4602 offers as of now. \nAt KL University, the highest package was INR 58 LPA, which was bagged by the MBA batch. \nA total of 374 recruiters participated in KL University placements in 2023. \nDuring the 2022 placements of KL University, the 269 companies visited campus. \nSome of the top recruiters were Accenture, Amazon, Airtel, HDFC, Byjus, Wipro, ICICI, and Dell. \nA 100% placement rate is provided by the college. \nThe highest package was 76 LPA, the lowest package was 5 LPA, and the average package was 10 LPA. \nPlacements at KL University offer abundant opportunities for students, ensuring they benefit from attractive employment packages. \nRenowned companies such as Qualcomm, Microsoft, Google, and Tata Consultancy Services actively recruit students from the university, further enhancing the quality and diversity of placement opportunities available. \nFor more details, please visit the [KLH website](https://klh.edu.in/bachupally/)")
]



def get_gemini_response(question):
    # First, check if the question matches any predefined content question
    for q, a in content_qa_pairs:
        if question.lower() in q.lower():
            return a  # Return the answer from your content
        
    # If the question doesn't match predefined content, use the generative model
    response = chat.send_message(question, stream=True)
    return response

## initialize our Streamlit app
st.set_page_config(page_title="FAQ KLH")

st.header("📝KLH FAQ ChatBot")

user_input = st.text_input("🤖 How can I help you? ", key="input")
submit = st.button("Ask ❓")

if submit and user_input:
    response = get_gemini_response(user_input)
    st.subheader("Sure! Here's what you're looking for:")
    if isinstance(response, str):  # Check if response is already a string
        st.write(response)
    else:
        for chunk in response:
            st.write(chunk.text)

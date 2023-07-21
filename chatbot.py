from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>EDU BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to KJ's EduBOT! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br> Which of the following user groups do you belong to?<br><br> 1.&emsp;First Year Admission Query</br>2.&emsp;Direct Second Year Admission Query </br>3.&emsp;M Tech Query</br>4.&emsp;P.H.D Query</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;First Year Admission Query</br>2.&emsp;Direct Second Year Admission Query </br>3.&emsp;M.Tech Query</br>4.&emsp;Ph.D Query</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;First Year Admission Query</br>2.&emsp;Direct Second Year Admission Query </br>3.&emsp;M.Tech Query</br>4.&emsp;Ph.D Query</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Direct Second Year Admission Query </br>3.&emsp;M.Tech Query</br>4.&emsp;Ph.D Query </br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Direct Second Year Admission Query </br>3.&emsp;M.Tech Query</br>4.&emsp;Ph.D Query </br>",


"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"What is the process of cancellation of admission?",
"1.	Apply online for the cancellation <br> 2.Fill proforma O for Cancellation in duplicate. (Available in the Admission Brochure given by ARA)<br>3.Attach a copy of retention certificate and photocopies of receipts.<br> 4.Submit the form in the Admission Cell. <br>5.	Collect original documents.<br>6.Fees will be refunded after deducting the cancellation charges as per rules specified by ARA.",


"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information K J SOMAIYA Institute of Technology college.",

"What else can you do?",
"I can help you know more about K.J. Somaiya",
    
    "1",
    "<b>STUDENT First Year Query <br>The following are frequently searched terms related to student in K J Somaiya college. Please select one from the options below : <br> <br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/first-year-bachelor-of-engineering#cutoff'">👉Department Details</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/first-year-bachelor-of-engineering#feesstructure'">👉Fees</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/first-year-bachelor-of-engineering'">👉Cut-off</a> </b><br><br><b> <a href="'https://www.somaiya.edu.in/en/hostel-housing/'">👉Hostel</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/placement'">👉Placement</a> </b><br><br> <b> <a href="'https://kjsit.somaiya.edu.in/en/admission/first-year-bachelor-of-engineering#documentsrequired'"> 👉Documents Required</a></b>",

    "2",
    "<b>STUDENT Direct Second Year Query <br>The following are frequently searched terms related to student in K J Somaiya college. Please select one from the options below : <br> <br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/second-year-bachelor-of-engineering#admittedstudents'">👉Department Details</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/second-year-bachelor-of-engineering#feesstructure'">👉Fees</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/second-year-bachelor-of-engineering'">👉Cut-off</a> </b><br><br><b> <a href="'https://www.somaiya.edu.in/en/hostel-housing/'">👉Hostel</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/placement'">👉Placement</a></b><br><br> <b> <a href="'https://kjsit.somaiya.edu.in/en/admission/second-year-bachelor-of-engineering#documentsrequired'"> 👉Documents Required</a></b>",
    

    "3",
    "<b>M.Tech Query <br>The following are frequently searched terms related to student in K J Somaiya college. Please select one from the options below : <br> <br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/pg-artificial-intelligence'">👉Department Details</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/pg-artificial-intelligence'">👉Fees</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/pg-artificial-intelligence'">👉Seat-Distribution</a> </b><br><br><b> <a href="'https://www.somaiya.edu.in/en/hostel-housing/'">👉Hostel</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/placement'">👉Placement</a> </b><br><br> <b> <a href="'https://kjsit.somaiya.edu.in/en/admission/pg-artificial-intelligence'"> 👉Documents Required</a></b> " ,


    "4",
    "<b>Ph.D Query <br>The following are frequently searched terms related to student in K J Somaiya college. Please select one from the options below : <br> <br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/phd'">👉Department Details</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/phd#admissionprocess'">👉Admission Process</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/phd#pet'">👉PET-TEST Details</a> </b><br><br><b> <a href="'https://www.somaiya.edu.in/en/hostel-housing/'">👉Hostel</a> </b><br><br><b> <a href="'https://kjsit.somaiya.edu.in/en/admission/phd#prog-duration'">👉Program Details</a> </b><br><br> <b> <a href="'https://kjsit.somaiya.edu.in/en/admission/pg-artificial-intelligence'"> 👉Documents Required</a></b>",
    
]

trainer.train(conversation)

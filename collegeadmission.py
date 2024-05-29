class AdmissionChatbot:
    def __init__(self):
        self.context = {}
        self.base_url="www.nvmscollege.edu.in"

    def greet(self):
        return "Hello! I'm here to help you with college admissions. How can I assist you today?"

    def farewell(self):
        return "Goodbye! If you have any more questions, feel free to ask. Have a great day!"

    def respond(self, user_input):
        responses = {
            "hello":"welcome to nvms college ",
            "admission procedure": "The admission procedure involves filling out an  application, submitting required documents.if any queries ,feel free to approach",
            "requirements": "The admission requirements include a completed application form, high school transcripts and also personal documents",
            "deadlines": "The application deadlines is on jun31st 2024",
            "scholarships": "We offer various scholarships based on merit and need. You can apply for scholarships along with your admission application.",
            "how do your college support students in placements":"we in our college provide placement training from 2nd year itself and help them in cracking placements and also other exams also",
            "contact information": "you can contact us on (xxxxxxxxxx) or nvmscolllege@edu.in",
            "thank you":"Thank you for approaching us and will be happy to have you in nvms family"
        }

        user_input_lower = user_input.lower()
        for key, response in responses.items():
            if key in user_input_lower:
                return response
        
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"

    def remember_context(self, key, value):
        self.context[key] = value

    def recall_context(self, key):
        return self.context.get(key, None)

    def ask_questions(self):
        questions = [
            "Which program are you interested in?",
            "Do you have any specific questions about the admission process?",
            "Would you like information on scholarships?"
        ]

        answers = {}
        for question in questions:
            print(question)
            answer = input()
            answers[question] = answer
            self.remember_context(question, answer)
        
        return answers

    def handle_interaction(self):
        print(self.greet())
        while True:
            user_input = input()
            if "bye" in user_input.lower():
                print(self.farewell())
                break
            response = self.respond(user_input)
            print(response)
            if response.startswith("The admission procedure"):
                print("Would you like more details on any specific step?")
            elif response.startswith("The application deadlines"):
                print("Do you need more information about any specific deadline?")

# Running the chatbot
chatbot = AdmissionChatbot()
chatbot.handle_interaction()

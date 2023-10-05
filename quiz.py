def ask_question(question, answer, question_number):
    while True:
        user_answer = input(f"Q{question_number}) {question} ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            return True
        elif user_answer.lower() == "":
            return False
        else:
            print("Incorrect...")
            print(f"The correct answer is: \"{answer}\".\n")
            return True

def main():
    readiness_answers = ["yes", "y", "si", "ja", "yeah", "affirmative"]

    questions = [
        "What does the acronym 'AI' stand for?",
        "Which British mathematician and logician is often considered one of the pioneers of AI and created the Turing Test?",
        "What type of machine learning algorithm is designed to classify data into distinct categories, such as spam or not spam emails?",
        "Which AI technique involves training a computer program to mimic the cognitive functions of the human brain, including learning and problem-solving?",
        "What is the name of the AI system developed by IBM that defeated human champions in the game show Jeopardy!?",
        "Which famous AI application, introduced by IBM in 1997, defeated chess world champion Garry Kasparov?",
        "What is the concept of giving an AI system the ability to make decisions, learn from experiences, and improve its performance over time?",
        "Which programming language is widely used for implementing AI algorithms and models, known for its simplicity and readability?",
        "In computer vision, what is the name of the task where an AI system identifies and locates objects within an image or video?",
        "Which subfield of AI is focused on enabling computers to understand, interpret, and generate human language?"
    ]

    answers = [
        "artificial intelligence",
        "alan turing",
        "naive bayes classifier",
        "neural networks",
        "watson",
        "deep blue",
        "machine learning",
        "python",
        "object detection",
        "natural language processing"
    ]

    correct_answers = 0

    print("\nWelcome to the AI Quiz!")

    ready_answer = input("Are you ready? ").lower()

    while ready_answer == "":
        ready_answer = input("Are you ready? ").lower()
    if ready_answer in readiness_answers:
        print("\nOkay, here it comes!")

        for i in range(len(questions)):
            question_number = i + 1
            while not ask_question(questions[i], answers[i], question_number):
                pass
            correct_answers += 1

        print(f"\nYou got {correct_answers} out of {len(questions)} correct!")

    else:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()

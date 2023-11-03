
class Question:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

    def ask_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

        user_choice = int(input("Enter the number of your choice: "))
        if user_choice == self.correct_choice:
            print("Correct!\n")
            return True
        else:
            print("Incorrect!\n")
            return False

def main():
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 1),
        Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 2),
        Question("Which famous scientist developed the theory of relativity?", ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"], 3)
    ]

    score = 0
    for question in questions:
        if question.ask_question():
            score += 1

    print(f"You scored {score}/{len(questions)}!")

if __name__ == "__main__":
    main()

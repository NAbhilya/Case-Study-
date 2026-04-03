# -----------------------------------------------------------
# Intelligent Tutoring System using Knowledge-Based Agent
# Author: N. Abhilya | Roll No: 2023004396
# -----------------------------------------------------------

# Step 1: Knowledge Base (15 Questions and Answers)
knowledge_base = {
    "What is AI?": "Artificial Intelligence is the simulation of human intelligence in machines.",
    "What is Machine Learning?": "Machine Learning is a part of AI that learns from data.",
    "What is Deep Learning?": "Deep Learning uses nn with many layers to learn patterns.",
    "What is NLP?": "NLP means Natural Language Processing, which helps computers understand human language.",
    "What is a Knowledge-Based Agent?": "It is an agent that uses stored knowledge and rules to make decisions.",
    "What is Computer Vision?": "Computer Vision allows computers to understand and process images and videos.",
    "What is an Expert System?": "An Expert System is an AI that mimics the decision-making of a human expert.",
    "What is Reinforcement Learning?": "Reinforcement Learning teaches through rewards or penalties.",
    "What is a Neural Network?": "A Neural Network mimics the human brain to recognize patterns.",
    "What is a Chatbot?": "A chatbot is a program that can talk with users and answer questions.",
    "What is the Turing Test?": "The Turing Test checks if a machine can think like a human.",
    "What is Data Mining?": "Data Mining finds patterns and useful information from large data sets.",
    "What is a Perceptron?": "A Perceptron is the simplest neural network for binary classification.",
    "What is a Search Algorithm?": "A Search Algorithm finds solutions by exploring different options.",
    "What is Heuristic Function?": "A Heuristic Function estimates the cost or distance to reach a goal."
}

# Step 2: Initialize score and track wrong answers
student_score = 0
wrong_answers = []

print("🤖 Welcome to the AI Intelligent Tutoring System!\n")

# Step 3: Ask questions to the user
for question, correct_answer in knowledge_base.items():
    print(f"Question: {question}")
    user_answer = input("Your Answer: ")

    # Step 4: Check answer
    if user_answer.lower() in correct_answer.lower():
        print("✅ Correct! Great job!\n")
        student_score += 1
    else:
        print(f"❌ Incorrect. Correct answer: {correct_answer}\n")
        wrong_answers.append(question)

# Step 5: Show final score
print("--------------------------------------------------")
print(f"Your total score: {student_score}/{len(knowledge_base)}")
print("--------------------------------------------------")

# Step 6: Performance feedback
if student_score == len(knowledge_base):
    print("🎉 Excellent! You mastered all topics.")
elif student_score >= len(knowledge_base) * 0.7:
    print("👍 Good job! Revise the topics you missed.")
elif student_score >= len(knowledge_base) * 0.4:
    print("📘 You are learning well! Focus on weak areas.")
else:
    print("💪 Keep practicing! Start from the basics.")

# Step 7: Suggestions to improve
if wrong_answers:
    print("\n🔍 Topics you need to review:")
    for q in wrong_answers:
        print(f" - {q}")
    print("\n📈 Suggestions to improve:")
    print("1️⃣ Revisit notes or short videos on these topics.")
    print("2️⃣ Practice more questions daily for 20 minutes.")
    print("3️⃣ Ask teachers or AI chatbot for help.")
    print("4️⃣ Try explaining these topics to your friends.")
    print("5️⃣ Study regularly with small breaks for better memory.")
else:
    print("\n✅ Great! You answered all correctly. Keep learning advanced AI topics!")

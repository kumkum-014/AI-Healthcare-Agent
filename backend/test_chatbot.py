from chatbot import ask_healthcare_agent


question = input("You: ")


answer = ask_healthcare_agent(question)


print("\nAI Healthcare Assistant:")
print(answer)
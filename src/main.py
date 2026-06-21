from query import ask

print("\nDocument Q&A Bot")
print("Type 'exit' to quit\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        break

    answer, citations = ask(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")
    for citation in citations:
        print("-", citation)

    print("\n" + "=" * 60 + "\n")
#create variable answer
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

#make variable answer in lowercase without whitespaces
answer = answer.lower().strip()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

questions = ["How to print in Python?",
             "How to create list in Python?",
             "How to print datatype of a variable?"]
options = [["1. print(Hello World)",
           "2. printf('Hello World')",
           "3. print('Hello World');",
           "4. print('Hello World')"],
           ["1. my_list = [hello, world]",
           "2. my_list = ['hello', 'world']",
           "3. my_list = ['hello', 'world'];",
           "4. my_list.value['hello', 'world']"],
           ["1. a.type()",
            "2. type.a()",
            "3. type(a)",
            "4. type.a"]]

amount = int(0)

def question(Qindex, Wamount, Qnum, ans):
    print("\n")
    print(Qnum, "question for", Wamount, "Rupees")
    print(questions[Qindex])
    print("Options are:")
    for i in options[Qindex]:
        print(i)
    userInput = int(0)

    while True:
        userInput = int(input("--> "))
        if userInput >=1 and userInput <= 4:
            break
        print("Invalid input: Answer again...")
    match userInput:
        case _ if userInput == ans:
            print("Right! You got", Wamount, "rupees.")
            return Wamount
        case _:
            print("Wrong. You got", amount, "rupees.")
            return 0

print("Welcome to Kaun Banega Crorepati!!!")

first_prize = question(0, 100000, "First", 4)
if first_prize == 0:
    exit
else:
    second_prize = question(1, 500000, "Second", 2)
    if second_prize == 0:
        print("You won total of", first_prize, "rupees")
        exit
    else:
        third_prize = question(2, 1000000, "Third", 3)
        print("You won total of", first_prize+second_prize+third_prize, "rupees.")

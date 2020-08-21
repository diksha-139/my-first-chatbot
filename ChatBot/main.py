from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot("Misty")


conversation = [
    "Hello",
    "Hi there!",
    "What is your name?",
    "my name is Misty, i am created by diksha.",

    "How are you doing?",
    "I'm doing great.",
    "That is good to hear.",
    "Thank you.",
    "You're welcome.",
    "Which language you speak?",
    "I mostly speak english language.",
    "Where do you live?",
    "i live in kochi, a beautiful city ."

]

trainer = ListTrainer(bot)
# # now training the bot with the help of trainer

trainer.train(conversation)
# answer = bot.get_response('what is your name?')
# print(answer)
# print("Talk to Misty Bot...")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer= bot.get_response(query)
#     print("misty : ", answer)


main = Tk()

main.geometry("500x650")
main.title('My Chat Bot')
img = PhotoImage(file="images.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot= bot.get_response(query)
    msgs.insert(END,"You: "+query)
    msgs.insert(END,"Misty : "+str(answer_from_bot))
    textF.delete(0, END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height =20)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

# creating text field
textF=Entry(main, font=("Ariel", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask from Misty", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

main.mainloop()

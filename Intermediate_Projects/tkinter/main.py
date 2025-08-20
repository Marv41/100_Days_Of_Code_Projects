import tkinter



# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500,height=300)
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# window.mainloop()




def add(*args):
    result = 0
    for arg in args:
        result += arg

    return result
# print(add(1,2,3,7))

def calulate(**kwargs):
    print(kwargs)

calulate(add=3, multiply=5)





from tkinter import *
import random

root=Tk()
root.title("Countries and Capitals")
root.geometry("400x400")
root.configure(background="light blue")

enter_capital = Entry(root)
enter_capital.place(relx= 0.7,rely = 0.1, anchor = CENTER)

label1 = Label(root, text="Capital Goes Here:")
label1.place(relx= 0.3,rely = 0.1, anchor = CENTER)

enter_country = Entry(root)
enter_country.place(relx= 0.7,rely = 0.2, anchor = CENTER)

label2 = Label(root, text="Country Goes Here:")
label2.place(relx= 0.3,rely = 0.2, anchor = CENTER)

capital_list = Label(root)
random_number_label = Label(root)
capital = Label(root)

country_list = Label(root)
random_number_label1 = Label(root)
country = Label(root)

list1 = []
list2 = []
def add():
    friend_name = enter_capital.get()
    list1.append(friend_name)
    capital_list["text"] = "Capital List: " + str(list1)
    
    friend_name2 = enter_country.get()
    list2.append(friend_name2)
    country_list["text"] = "Country List: " + str(list2)
    
def random_number():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    capital["text"] = "Capital: " + str(generated_random_number)
    
    length = len(list2)
    random_no1 = random.randint(0, length-1)
    random_number_label1["text"] = str(random_no1)
    generated_random_number1 = list2[random_no1]
    country["text"] = "Country: " + str(generated_random_number1)
    
def reset_lists():
        list1 = []
        list2 = []
        capital_list["text"] = ""
        capital_list["text"] = ""
        country_list["text"] = ""
        capital["text"] = ""
        country["text"] = ""
        random_number_label["text"] = ""
        random_number_label1["text"] = ""
    
btn = Button(root, text="Add to Capital and Country List", command = add)
btn.place(relx= 0.5,rely = 0.3, anchor = CENTER)

capital_list.place(relx= 0.5,rely = 0.4, anchor = CENTER)

country_list.place(relx= 0.5,rely = 0.5, anchor = CENTER)

btn1 = Button(root, text="What Will Your Country And Captial Be?  ", command = random_number)
btn1.place(relx= 0.5,rely = 0.6, anchor = CENTER )

random_number_label.place(relx= 0.3,rely = 0.7, anchor = CENTER)
capital.place(relx= 0.3,rely = 0.8, anchor = CENTER)

random_number_label1.place(relx= 0.7,rely = 0.7, anchor = CENTER)
country.place(relx= 0.7,rely = 0.8, anchor = CENTER)

reset_btn = Button(root, text="Reset Lists", command = reset_lists)
reset_btn.place(relx= 0.5,rely = 0.9, anchor = CENTER)

root.mainloop()
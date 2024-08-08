import requests as r
from bs4 import BeautifulSoup
import tkinter as tk

window = tk.Tk()
window.title("Ana Menü")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)

label = tk.Label(text="Press one of the buttons")
label.config(bg="black", fg="red", padx=20, pady=20)
label.pack()

target_url1 = "https://atilsamancioglu.com/"
target_url2 = "https://atilsamancioglu.com/courses/"
target_url3 = "https://atilsamancioglu.com/blog/"
target_url4 = "https://atilsamancioglu.com/press/"
found_links1 = []
found_links2 = []
found_links3 = []
found_links4 = []


def make_requests(url):
    response = r.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    return soup


def get_api1(url=target_url1):
    news = make_requests(url)
    for new in news.find_all('a'):
        found_new = new.get('href')
        if found_new is not None:
            if target_url1 in found_new and found_new not in found_links1:
                found_links1.append(found_new)
                print(found_new)
                get_api1(found_new)


def get_api2(url=target_url2):
    news = make_requests(url)
    for new in news.find_all('a'):
        found_new = new.get('href')
        if found_new is not None:
            if target_url2 in found_new and found_new not in found_links2:
                found_links1.append(found_new)
                print(found_new)
                get_api1(found_new)


def get_api3(url=target_url3):
    news = make_requests(url)
    for new in news.find_all('a'):
        found_new = new.get('href')
        if found_new is not None:
            if target_url3 in found_new and found_new not in found_links3:
                found_links1.append(found_new)
                print(found_new)
                get_api1(found_new)


def get_api4(url=target_url4):
    news = make_requests(url)
    for new in news.find_all('a'):
        found_new = new.get('href')
        if found_new is not None:
            if target_url4 in found_new and found_new not in found_links4:
                found_links1.append(found_new)
                print(found_new)
                get_api1(found_new)


button1 = tk.Button(text="First button", command=get_api1)
button1.config(padx=20, pady=20)
button1.pack()

button2 = tk.Button(text="Second button", command=get_api2)
button2.config(padx=20, pady=20)
button2.pack()

button3 = tk.Button(text="Third button", command=get_api3)
button3.config(padx=20, pady=20)
button3.pack()

button4 = tk.Button(text="Fourth button", command=get_api4)
button4.config(padx=20, pady=20)
button4.pack()

'''
def stopping_button():
    return None

stop_button = tk.Button(text="Stop process", command=stopping_button)
stop_button.config(padx=20, pady=20)
stop_button.pack()

#i tried to end code with a button but it did not worked
'''

window.mainloop()








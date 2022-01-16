# simple covid gui monitor.py
import tkinter as tk
import requests
import json
from tkinter import *

from matplotlib import pyplot as plt


def get_data():
    url = "https://corona.lmao.ninja/v2/all"
    response = requests.get(url)
    data = response.json()
    return data

def get_data_country():
    url = "https://corona.lmao.ninja/v2/countries"
    response = requests.get(url)
    data = response.json()
    return data

def get_data_patient(country):
    url = "https://corona.lmao.ninja/v2/countries/"+country
    response = requests.get(url)
    data = response.json()
    return data

def get_data_death(country):
    url = "https://corona.lmao.ninja/v2/historical/"+country+"/deaths"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    root = tk.Tk()
    root.title("COVID-19")
    root.geometry("600x400")
    root.resizable(0, 0)
    root.configure(background='#f4f4f4')
    #root.iconbitmap(r"icon.ico")
    #graph of the data of selected country from dropdown
    def graph():
        country = country_list.get()
        data = get_data_death(country)
        x = []
        y = []
        for i in range(len(data)):
            x.append(data[i]['date'])
            y.append(data[i]['deaths'])
        fig = plt.figure(figsize=(10,5))
        plt.plot(x,y)
        plt.title("COVID-19 Death Graph")
        plt.xlabel("Date")
        plt.ylabel("Deaths")
        plt.show()
    graph_button = Button(root, text="Graph", command=graph)
    graph_button.place(x=400, y=300)
    #graph of the data of selected country from dropdown
    def graph_country():
        country = country_list.get()
        data = get_data_patient(country)
        x = []
        y = []
        for i in range(len(data)):
            x.append(data[i]['date'])
            y.append(data[i]['confirmed'])
        fig = plt.figure(figsize=(10,5))
        plt.plot(x,y)
        plt.title("COVID-19 Graph")
        plt.xlabel("Date")
        plt.ylabel("Confirmed")
        plt.show()
    graph_button = Button(root, text="Graph", command=graph_country)
    graph_button.place(x=400, y=350)
    #country list
    country_list = tk.StringVar(root)
    country_list.set("Select Country")
    country_list_menu = tk.OptionMenu(root, country_list, *get_data_country())
    country_list_menu.place(x=400, y=250)
    #country list
    country_list = tk.StringVar(root)
    country_list.set("Select Country")
    root.mainloop()

if __name__ == '__main__':
    main()
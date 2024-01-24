#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import seaborn as sns
import matplotlib.pyplot as plt

def load():
    try:
        global df, label_data, df1
        file = root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select a file',
                                                   filetypes=(('Csv files (*.csv)', '*.csv'), ('All files (*.*)', '*.*')))
        df = pd.read_csv(file, error_bad_lines=False, header=None, skiprows=7)
        df.rename(columns={1: 'Current', 14: 'Voltage'}, inplace=True)
        df.drop(df.index[0], inplace=True)
        try:
            df1 = df.loc[:, ['Voltage', 'Current']]
        except:
            messagebox.showwarning('Error', 'File already converted.')

        label_data.grid_forget()
        label_data = Label(root, text='file -->  ' + file)
        label_data.grid(row=1, column=0)
        df1 = df1.astype(dtype={'Voltage':'float64', 'Current':'float64'})
        df1.set_index('Voltage', inplace=True)
        df1.to_csv(file)
    except FileNotFoundError:
        messagebox.showerror('Error 404', 'File not found!')


    ax = sns.lineplot(x='Voltage', y='Current', data=df1)
    ax.set(xlabel="Voltage (V)", ylabel="Current (A)")
    plt.show()



root = Tk()
root.title("I-V curve")
sns.color_palette("colorblind")
sns.set_style("whitegrid")

label_data = Label(root, text='')
label_data.grid(row=1, column=0)

label1 = Label(root, text="""This script cleans the measurement data obtained with the SMU as a csv file.
Note: For GRIFO internal use only.
**WARNING** This script will overwrite the original file. Please make a copy if needed.
                                                                                        Author: Michael Sun""", padx=15)
label1.grid(row=3, column=0)

button1 = Button(root, text="Clean data", command=load)
button1.grid(row=0, column=0)

root.mainloop()

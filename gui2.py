import tkinter as tk
from tkinter import *
import pandas as pd
import sys

df1=pd.read_csv('Form1.csv',error_bad_lines=False, encoding='utf8')
df2=pd.read_csv('form2.xlsx',lineterminator='\n',error_bad_lines=False, encoding = "ISO-8859-1")

root = tk.Tk()
text = tk.Text(root)
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

def insert():
	
	for j in range (1,327):
		#ans.append(e[j-1].get())
		df1.Answers[j]=e[j-1].get()
		
		text.configure(font=("Times New Roman", 20, "bold"))
		#df1.index1[j]=e[j-3].get()

	df1.to_csv('AnsForm1.xlsx')
	
	#print (ans)
	for j in range (1,327):
		for k in range (3,5):
			#print(df2.iloc[k,1])
			#index.append(df2.index[k])
			if df2.iloc[k,1]==df1.iloc[j,1]:
				#ans.append(df1.Answers[j])
				df2.answers[j]=e[j-1].get()

	#print (ans)			
	#index.appen
	df2.to_csv('AnsForm2.xlsx')

submit = tk.Button(frame_main, text="Submit", bg="red", fg="Black", command=insert)
submit.grid(row=3, column=0, pady=5, sticky='nw')

# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas)
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

##vsb1 = tk.Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
##vsb1.grid(row=1, column=1, sticky='ns')
##canvas.configure(xscrollcommand=vsb1.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

# Add 9-by-5 buttons to the frame
rows = 327

lab = [tk.Label() for i in range(rows)]
e = [tk.Entry() for i in range(rows)]
for i in range(0, rows):
    lab[i] = tk.Label(frame_buttons, text=df1.iloc[i+1,2], wraplength=1000, justify='left', anchor='w', pady=5, borderwidth=2, relief='raised')
    lab[i].grid(row=i, column=0, sticky='news')
    e[i] = tk.Entry(frame_buttons)
    e[i].grid(row=i, column=1, sticky='news')

# Update buttons frames idle tasks to let tkinter calculate buttons sizes
frame_buttons.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
first5columns_width = max([lab[j].winfo_width() for j in range(0, 14)])
first5rows_height = sum([lab[i].winfo_height() for i in range(0, 30)])
frame_canvas.config(width=first5columns_width + vsb.winfo_width() + e[0].winfo_width() +10,
                    height=first5rows_height)

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
root.mainloop()

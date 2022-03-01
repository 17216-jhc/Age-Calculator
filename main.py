''' AGE Calculator
Source: https://www.askpython.com/python-modules/tkinter/age-calculator --> Minimum Viable Product (Starting Code)
 '''
# ____________   IMPORTS ________________
# Getting current date from import date function from datetime module
from datetime import date
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ____________   FUNCTIONS ________________
#clear text box
def clearBox(self):
    self.txt1.delete("1.0", "end")

def get_age():
    # gets the three entries
    d= int(e_date.get())
    m = month_chosen.current()
    #m = e_month.get()
    y=int(e_year.get())


    calc_age = find_age(d, m, y)
    display_calc_age(calc_age)

def find_age(d, m, y):
    # find the age ( difference between current and date of birth )
    age = today.year-y-((today.month, today.day)<(m,d))
    return age

def display_calc_age(age):
    tbox_age.config(state='normal')

    #age calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_age.delete('1.0', tk.END)
    tbox_age.insert(tk.END,age)
    tbox_age.config(state='disabled')

def date_check(question,low,high):
  error = "please enter an interger between \ {} and {}".format(low, high)
  valid=False
  while not valid:
    try:
      response=int(input(question))
      if 1 <= response <= 31:
        return(response)
      else:
        print(error)
    except ValueError:
      print(error)

def validation():
  # gets the three entries
  d = e_date.get()
  m = month_chosen.current()
  #m = e_month.get()
  y = e_year.get()
  y_int = int (e_year.get())
  msg = ''

  is_leapyear = y_int % 4 == 0 and (y_int % 100 != 0 or y_int % 400 == 0) 

  if len(d) == 0 or len (y) == 0:
      msg = 'day, month and / or year can\'t be empty'
      calc_age = ' '
      display_calc_age(calc_age)
  else:
    try:
      if
      if any(ch.isdigit() for ch in d) == False:
        msg = 'day must be a NUMBER, EG: 5, not five or fifth'
        calc_age = ' '
        display_calc_age(calc_age)
      elif m == 0:
        msg = 'choose an appropriate MONTH'
        calc_age = ' '
        display_calc_age(calc_age)
      elif any(ch.isdigit() for ch in y) == False:
        msg = 'year must be a NUMBER, EG: 2005, not two thousand and five'
        calc_age = ' '
        display_calc_age(calc_age)
      else:
        #msg = 'Success!'
        day = int(d)
        month = m #month is already in number from list position
        year = int(y)
        #Checks if day is possible in a month
        if day == 0 or year == 0 or day > 31:
          msg = 'Day or Year must exist - there are only 31 days and more than 0 days in this month idiot you ritared person'
          calc_age = ' '
          display_calc_age(calc_age)
        else:
            #checks if year is over the current year
          if year > today.year:
            msg = 'Year cannot be over current year' 
            calc_age = ' '
            display_calc_age(calc_age)
            
          elif month == 2: #checks if month is feb.
              if day > 28:
                msg = 'Day or Year must exist - there are only 28 days in February'
                calc_age = ' '
                display_calc_age(calc_age)
              else:
                calc_age = find_age(day, month, year)
                display_calc_age(calc_age)
          elif month in (4, 6, 9, 11):
              if day > 30:
                msg = 'Day or Year must exist - there are only 30 days in This month'
                calc_age = ' '
                display_calc_age(calc_age)
              else:
                calc_age = find_age(day, month, year)
                display_calc_age(calc_age)
          else:
            calc_age = find_age(day, month, year)
            display_calc_age(calc_age)
            
    except Exception as ep:
      messagebox.showerror('error', ep)

  if msg != '':
    messagebox.showinfo('message', msg)

def exit():
  window.destroy()

# ____________   MAIN  ________________

# Create a object which stores today’s whole date using datetime function
today = date.today()

# Creating a custom window
window = tk.Tk()
window.geometry("500x230")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Age Calculator!')

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")

# Labels for date, month and year
lb_date = tk.Label(window,text = "Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_month = tk.Label(window,text = "Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_year = tk.Label(window,text = "Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")

# Entry boxes for date, month and year
e_date = tk.Entry(window,width=5)

# Combobox creation
n = tk.StringVar()
month_chosen = ttk.Combobox(window, textvariable = n, width=14, state="readonly")

# Adding combobox drop down list
month_chosen['values'] = ('Select a month...', 
                          'January', 
                          'February',
                          'March',
                          'April',
                          'May',
                          'June',
                          'July',
                          'August',
                          'September',
                          'October',
                          'November',
                          'December')
# Shows Select a month as a default value
month_chosen.current(0)
#e_month = tk.Entry(window,width=5)

e_year = tk.Entry(window,width=5)

# Button to calculate age 
btn_calculate_age = tk.Button(window,text="Calculate Age!",font=("Arial",13), command=validation)

# Label for text box that will display the calculated age
lb_calculated_age = tk.Label(window,text="The Calculated Age is:   ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")

tbox_age=tk.Text(window,width=5,height=0,state="disabled",bg="lightgreen",font=('Arial',24,"bold"))

# Button to exit application
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)

# Placing the elements on the screen
lb_heading.place(x=70,y=5)
lb_subheading.place(x=10,y=40)
lb_date.place(x=20,y=80)
lb_month.place(x=20,y=105)
lb_year.place(x=20,y=130)
e_date.place(x=120,y=80)
#e_month.place(x=120,y=105)
month_chosen.place(x=120,y=105)
e_year.place(x=120,y=130)
btn_calculate_age.place(x=30,y=170)
lb_calculated_age.place(x=230,y=70)
tbox_age.place(x=350,y=100)
btn_exit.place(x=300,y=170)

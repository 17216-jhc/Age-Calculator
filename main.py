''' AGE Calculator
Source: https://www.askpython.com/python-modules/tkinter/age-calculator
Date: 22/01/2022
 '''
# Creating a custom window
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Age Calculator!')

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")

# Labels for date, month and year


# Entry boxes for date, month and year


# Button to calculate age 


# Label for text box that will display the calculated age


# Button to exit application


# Placing the elements on the screen
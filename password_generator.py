# ----------------------------------------------------------------
# Name: Sharangan Nedunchelian
# Date: Nov 15 2025
# File: password_generator.py
# Function: Generate a random password for the user
# ----------------------------------------------------------------

#Import necessary modules
import random
import string 
import tkinter as tk

# Create window

root = tk.Tk()
root.geometry("400x300")
root.title("Random Password Generator")
title = tk.Label(root, text= "Random Password Generator", )
title.pack()

plength = tk.Label(root, text = "Password Length")
plength.pack()
plength_button = tk.Entry(root)
plength_button.pack()

difficultyL = tk.Label(root, text= "Difficulty")
difficultyB = tk.StringVar()

easyB = tk.Radiobutton(root, text= "Easy", variable= difficultyB, value = "easy") # difficultyB = tk.StringVar() this is a string variable to store the diff tkinter has a easier way to see if a value has been pressed then stores the value
mediumB = tk.Radiobutton(root, text= "Medium", variable= difficultyB, value = "medium")
hardB = tk.Radiobutton(root, text= "Hard", variable= difficultyB, value = "hard")
easyB.pack()
mediumB.pack()
hardB.pack()


def main():

      lower = True
      upper = True
      punctuation = True
      digit = True
      strengthN = 0
      typeC = 0
      strength = ""     
      difficulty = difficultyB.get()
      if difficulty == "":
            passwordL.config(text= "Enter a difficulty")
            return
      try:
            char_num = int(plength_button.get())
            if char_num <= 0:
                  passwordL.config(text= "Enter a number greater than 0")
                  return
      except ValueError:
            passwordL.config(text= "Enter a valid number")
            return # return stops the function from continuing since the number is not valid
      if char_num > 15:
            strengthN += 5
      elif char_num >= 12: 
            strengthN += 3
      elif char_num >= 8:
            strengthN += 1

      password = ''
      if difficulty == 'easy':
            for i in range(char_num):
                  password = password + random.choice(string.ascii_lowercase)
                  
      elif difficulty == 'medium':
            for i in range(char_num):
                  password = password + random.choice(string.ascii_letters + string.digits)
                  
      else:
            for i in range(char_num):
                  password = password + random.choice(string.ascii_letters+string.digits+string.punctuation)

      for i in range(len(password)):
            if password[i] in string.punctuation and punctuation:
                  typeC += 1
                  strengthN +=2
                  punctuation = False
            elif password[i].isdigit() and digit:
                  typeC += 1
                  strengthN += 1
                  digit = False
            elif password[i].isupper() and upper:
                  typeC += 1
                  strengthN += 1
                  upper = False
            elif password[i].islower() and lower:
                  typeC += 1
                  strengthN += 1
                  lower = False
      if typeC == 4:
            strengthN += 3
      elif typeC == 3:
            strengthN += 2
      elif typeC == 2:
            strengthN += 1


      if strengthN >= 10:
            strength = "Strong"
      elif strengthN >= 5:
            strength = "Medium"
      else:
            strength = "Weak"

      passwordL.config(text = "Password: " + password)
      strengthL.config(text= "Strength: " + strength)
      


generateB = tk.Button(root, text = "Generate", command= main)
generateB.pack()

passwordL = tk.Label(root, text= "Password: ")
passwordL.pack()

strengthL = tk.Label(root, text = "Strength: ")
strengthL.pack()

def copy_password():
      root.clipboard_clear()
      root.clipboard_append(passwordL.cget("text"))
      root.update()
      copyL.config(text = "Password Copied")


copyB = tk.Button(root, text = "Copy Password", command = copy_password)
copyL = tk.Label(root, text = "")

copyB.pack()
copyL.pack()

root.mainloop()

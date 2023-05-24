from tkinter import *
from tkinter import ttk
import sv_ttk

window = Tk()
window.title('BMI Calculator')
window.minsize(width=300, height=250)
window.config(padx=8, pady=12)


def calculate():
    if weight_input.index('end') == 0 or height_input.index('end') == 0:
        result_text.config(text='Please do not leave blank!', foreground='red')
    else:
        try:
            weight = int(weight_input.get())
            height = int(height_input.get())

            score = round(weight / (height / 100) ** 2, 2)
            if score < 18.5:
                result = 'Under Weight'
                color = '#70CC00'
            elif 18.50 <= score <= 24.99:
                result = 'Normal'
                color = '#00CC00'
            elif 25 <= score <= 29.9:
                result = 'Over Weight'
                color = '#00B800'
            elif 30 <= score <= 34.9:
                result = 'Obesity (Class I)'
                color = '#FFA500'
            elif 35 <= score <= 39.9:
                result = 'Obesity (Class II)'
                color = '#FF6633'
            else:
                result = 'Extreme Obesity'
                color = '#CC0000'

            result_text.config(text=f'Your Body Mass Index is {score}. This is considered {result}.', foreground=color)
        except:
            result_text.config(text='Please enter a valid number!', foreground='red')


weight_text = ttk.Label(text='Enter Your Weight (kg)')
weight_text.pack(pady=4)

weight_input = ttk.Entry(width=30)
weight_input.pack()

height_text = ttk.Label(text='Enter Your Height (cm)')
height_text.pack(pady=4)

height_input = ttk.Entry(width=30)
height_input.pack()

calculate_btn = ttk.Button(text='Calculate', command=calculate)
calculate_btn.pack(pady=8)

result_text = ttk.Label()
result_text.pack(pady=8)

sv_ttk.set_theme('dark')
window.mainloop()

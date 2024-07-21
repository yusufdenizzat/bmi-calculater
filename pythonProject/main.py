import tkinter

window =tkinter.Tk()
window.title("BMI Calculater")
window.minsize(width=300,height=300)
window.config(pady=10)
#weight

weight_label = tkinter.Label(text="Please enter your weight",pady=5)
weight_label.pack()
weight_entry = tkinter.Entry(width=10)
weight_entry.pack()

#height

height_label = tkinter.Label(text="Please enter your height")
height_label.pack()
height_entry= tkinter.Entry(width=10)
height_entry.pack()


def bmi_cal():

    try:

        a = int(weight_entry.get())
        b = int(height_entry.get())/100
        bmi = a/(b**2)
        if bmi<=18.4:
            underweight = tkinter.Label(text=f"BMI:{bmi} = UNDERWEIGHT ")
            underweight.pack()
        elif 18.4<bmi<=24.9:
            normal = tkinter.Label(text=f"BMI:{bmi} = NORMAL")
            normal.pack()
        elif 24.9<bmi<=39.9:
            overweight = tkinter.Label(text=f"BMI:{bmi} = OVERWEIGHT")
            overweight.pack()
        elif 39.9<bmi:
            obese =tkinter.Label(text=f"BMI:{bmi} = OBESE")
            obese.pack()

    except:
        error =tkinter.Label(text="Please enter a number")
        error.pack()

my_button = tkinter.Button(text="calculate",command=bmi_cal,pady=10)
my_button.pack()




tkinter.mainloop()
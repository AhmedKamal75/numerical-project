import time
from tkinter import *

from phase_2 import bisection, false_position, fixed_point, newton_raphson, secant_method

DEFAULT_GUESS = 1.0
DEFAULT_ITERATIONS = 50
DEFAULT_RELATIVE_ERROR = 0.00001
DEFAULT_FROM = -50.0
DEFAULT_TO = 50.0


def make_temp_window(title, output):
    temp_window = Tk()
    temp_window.title(title)
    temp_window.geometry("400x200")
    output_text = Text(temp_window)
    output_text.delete(1.0, END)
    output_text.insert(END, output)
    output_text.pack(pady=20, padx=20)
    temp_window.mainloop()


def start_2():
    main_window = Tk()
    main_window.title("Root Finder")
    main_window.geometry("700x400")

    def calculate():
        n = options.index(choice.get())
        title = options[n]
        string_function = pythonify_str_fun(str(text_box.get(1.0, END)).strip())
        x_guess = float(x_guess_entry.get())
        ite = int(iter_entry.get())
        ero = float(error_entry.get())
        x_from = float(from_entry.get())
        x_to = float(to_entry.get())

        def fun(x):
            return eval(string_function)

        start_time = time.time()
        result = 0.0
        if n == 0:
            result = bisection.solve(xl=x_from, xu=x_to, func=fun, steps=ite, goal_relative_error=ero)
        elif n == 1:
            result = false_position.solve(xl=x_from, xu=x_to, func=fun, steps=ite, goal_relative_error=ero)
        elif n == 2:
            result = fixed_point.solve(g=fun, x0=x_guess, x_from=x_from, x_to=x_to, iter_max=ite, es=ero)  # needs g(x)
        elif n == 3:
            result = newton_raphson.solve(fun=fun, x0=x_guess, iter_max=ite, es=ero)
        elif n == 4:
            result = secant_method.solve(fun=fun, x0=x_from, x1=x_to, iter_max=ite, es=ero)
        else:
            pass
        exec_time = time.time() - start_time
        print(title)
        print(f"x = {result}")
        print(f"t = {exec_time}")
        output = "x = " + str(result) + "\ntime taken: " + str(exec_time) + " sec"
        make_temp_window(title, output)

    input_frame = Frame(main_window)
    fx_label = Label(input_frame, text="f(x) = ")
    fx_label.grid(row=0, column=0)
    text_box = Text(input_frame, width=80, height=2)
    text_box.grid(row=0, column=1)
    input_frame.pack(pady=20)

    frame1 = Frame(main_window)
    frame1.pack(pady=20)
    x_guess_label = Label(frame1, text="initial guess x = ")
    x_guess_label.grid(row=0, column=0)
    iter_label = Label(frame1, text="number of iterations: ")
    iter_label.grid(row=1, column=0)
    error_label = Label(frame1, text="goal relative error: ")
    error_label.grid(row=2, column=0)
    from_label = Label(frame1, text="from x = ")
    from_label.grid(row=3, column=0)
    to_label = Label(frame1, text="to x = ")
    to_label.grid(row=4, column=0)

    x_guess_entry = Entry(frame1)
    x_guess_entry.grid(row=0, column=1)
    x_guess_entry.delete(0, END)
    x_guess_entry.insert(0, str(DEFAULT_GUESS))
    iter_entry = Entry(frame1)
    iter_entry.grid(row=1, column=1)
    iter_entry.delete(0, END)
    iter_entry.insert(0, str(DEFAULT_ITERATIONS))
    error_entry = Entry(frame1)
    error_entry.grid(row=2, column=1)
    error_entry.delete(0, END)
    error_entry.insert(0, str(DEFAULT_RELATIVE_ERROR))
    from_entry = Entry(frame1)
    from_entry.grid(row=3, column=1)
    from_entry.delete(0, END)
    from_entry.insert(0, str(DEFAULT_FROM))
    to_entry = Entry(frame1)
    to_entry.grid(row=4, column=1)
    to_entry.delete(0, END)
    to_entry.insert(0, str(DEFAULT_TO))

    choices_frame = Frame(main_window)
    choices_frame.pack(pady=20)

    options = ["Bisection", "False Position", "Fixed Point", "Newton-Raphson", "Secant_method"]
    choice = StringVar()
    choice.set(options[0])
    drop_down_menu = OptionMenu(choices_frame, choice, *options)
    drop_down_menu.grid(row=0, column=0)

    confirm_button = Button(choices_frame, text="Confirm", command=calculate)
    confirm_button.grid(row=0, column=1)

    main_window.mainloop()


def pythonify_str_fun(str_fun):
    symbols = ["e", "sin", "cos", "log", "tan", "pi"]
    for symbol in symbols:
        str_fun = str_fun.replace(symbol, "math." + symbol)
    return str_fun

# g(x) =
# "e**(-x)"
# "(2*x+3)**(0.5)"
# "1.2*x**4"
# "(x**4 + 2)/3"
# f(x) =
# "e**(-x) - x"
# "x**3 - 0.165*x**2 + 3.993*10**-4"
# "x**2 - 4"

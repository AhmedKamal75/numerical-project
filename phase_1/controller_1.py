import time
from tkinter import *

from phase_1 import jacobi, seidel, build_equation, gauss, gauss_jordan, lu_deco

DEFAULT_ITERATIONS = 100
DEFAULT_RELATIVE_ERROR = 0.05


def make_temp_window(title, content):
    temp_window = Tk()
    temp_window.title(title)
    temp_window.geometry("700x400")
    output_text = Text(temp_window)
    output_text.delete(1.0, END)
    output_text.insert(END, content)
    output_text.pack(pady=20, padx=20)
    temp_window.mainloop()


def get_iterations_relative_error(title, A, b):
    temp_window = Tk()
    temp_window.title("iterations and goal relative error")
    temp_window.geometry("300x200")

    def extraction():
        global Xs
        temp_window.quit()
        ite = int(iter_entry.get())
        ero = float(error_entry.get())
        print(f"iterations = {ite}")
        print(f"iterations = {ero}")
        solution = ""
        start_time = time.time()
        if title == "Jacobi Solution":
            Xs = jacobi.solve(A, b, iterations=ite, goal_relative_error=ero)
        elif title == "Gauss-Seidel Solution":
            Xs = seidel.solve(A, b, iterations=ite, goal_relative_error=ero)
        exec_time = time.time() - start_time
        for i, x in enumerate(Xs):
            solution = solution + str(i) + ": " + str(x) + "\n"
        solution = str(solution) + "\ntime = " + str(exec_time) + " sec"
        print(solution)
        make_temp_window(title=title, content=solution)
        return

    frame1 = Frame(temp_window)
    frame1.pack(pady=20)
    iter_label = Label(frame1, text="number of iterations: ")
    iter_label.grid(row=0, column=0)
    error_label = Label(frame1, text="goal relative error: ")
    error_label.grid(row=1, column=0)

    iter_entry = Entry(frame1)
    iter_entry.grid(row=0, column=1)
    iter_entry.delete(0, END)
    iter_entry.insert(0, str(DEFAULT_ITERATIONS))
    error_entry = Entry(frame1)
    error_entry.grid(row=1, column=1)
    error_entry.delete(0, END)
    error_entry.insert(0, str(DEFAULT_RELATIVE_ERROR))

    confirm_button = Button(temp_window, text="Confirm", command=extraction)
    confirm_button.pack(pady=20)

    temp_window.mainloop()


def start_1():
    main_window = Tk()
    main_window.title("Linear Equations solver")
    main_window.geometry("700x400")

    def calculate():
        n = options.index(choice.get())
        A, b, variables = build_equation.get_A_b(str_equations=text_box.get(1.0, END).split(","))
        print(A)
        print(b)
        print(variables)
        if n == 0:
            title = "Gauss Solution"
            start_time = time.time()
            solution = list(gauss.solve(A, b).flatten())
            exec_time = time.time() - start_time
            solution = str(solution) + "\ntime = " + str(exec_time) + " sec"
            print(title)
            print(solution)
            print("###############################")
            make_temp_window(title=title, content=solution)
        elif n == 1:
            title = "Gauss-Jordan Solution"
            start_time = time.time()
            solution = list(gauss_jordan.solve(A, b).flatten())
            exec_time = time.time() - start_time
            solution = str(solution) + "\ntime = " + str(exec_time) + " sec"
            print(title)
            print(solution)
            print("###############################")
            make_temp_window(title=title, content=solution)
        elif n == 2:
            title = "LU Solution"
            start_time = time.time()
            solution = list(lu_deco.solve(A, b))
            exec_time = time.time() - start_time
            solution = str(solution) + "\ntime = " + str(exec_time) + " sec"
            print(title)
            print(solution)
            print("###############################")
            make_temp_window(title=title, content=solution)
        elif n == 3:
            title = "LU Decomposition"
            start_time = time.time()
            l, u = lu_deco.doolittle(A)
            exec_time = time.time() - start_time
            solution = "L = \n" + str(l) + "\nU = \n" + str(u)
            solution = str(solution) + "\ntime = " + str(exec_time) + " sec"
            print(title)
            print(solution)
            print("###############################")
            make_temp_window(title=title, content=solution)
        elif n == 4:
            title = "Cholesky Decomposition"
            start_time = time.time()
            solution = lu_deco.cho(A)
            exec_time = time.time() - start_time
            solution = str(solution) + "\ntime = " + str(exec_time) + " sec"
            print(title)
            print(solution)
            print("###############################")
            make_temp_window(title=title, content=solution)
        elif n == 5:
            title = "Jacobi Solution"
            get_iterations_relative_error(title, A, b)
        elif n == 6:
            title = "Gauss-Seidel Solution"
            get_iterations_relative_error(title, A, b)
        else:
            print("something went wrong")

    text_box = Text(main_window, width=80, height=15)
    text_box.pack(pady=20)

    choices_frame = Frame(main_window)
    choices_frame.pack(pady=20)

    options = ["Gauss", "Gauss and jordan", "LU(solution)", "LU(doolittle)", "Cholesky", "Jacobi", "Seidel"]
    choice = StringVar()
    choice.set(options[0])
    drop_down_menu = OptionMenu(choices_frame, choice, *options)
    drop_down_menu.grid(row=0, column=0)

    confirm_button = Button(choices_frame, text="Confirm", command=calculate)
    confirm_button.grid(row=0, column=1)

    main_window.mainloop()

# string_equations = ["3x2 + 2x1 + 4x3 = -10.0001", "8x1 + x2 + 3x3 = 12", "-3x2 + 2x3  = 8"]
# string_equations = ["4x0 +6x1 +2x2 - 2x3 = 8", "2x0 +5x2 - 2x3 = 4", "-4x0 - 3x1 - 5x2 +4x3 = 1",
#                     "8x0 +18x1 - 2x2 +3x3 = 40"]  # answer = {-13.5,8.66666667,7,2}
# string_equations = ["10x1 + 3x2 -5x3 -1 = -2x1", "x1 + 5x2 +3x3 = 28", "3x1 + 7x2 + 13x3 = 76"]  # answer = {1,3,4}

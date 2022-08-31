import phase_1.controller_1
import phase_1.build_equation
import phase_2.controller_2

from tkinter import *


def run():
    main_window = Tk()
    main_window.title("project")
    main_window.geometry("200x200")

    def lineq():
        phase_1.controller_1.start_1()
        # main_window.quit()

    def root():
        phase_2.controller_2.start_2()
        # main_window.quit()

    lineq_button = Button(main_window, text="Linear Equations Solver", command=lineq)
    lineq_button.pack(pady=20)
    root_button = Button(main_window, text="Root Finder", command=root)
    root_button.pack(pady=20)

    main_window.mainloop()


if __name__ == '__main__':
    run()

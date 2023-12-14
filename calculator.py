import tkinter as tk
from tkinter import ttk

class CalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.first_var = tk.StringVar()
        self.second_var = tk.StringVar()
        self.result_var = tk.StringVar()
        ttk.Label(self, text="First number:").pack(padx=20, pady=20)
        ttk.Entry(self, textvariable=self.first_var).pack(padx=20, pady=20)

        ttk.Label(self, text="Second number:").pack(padx=20, pady=20)
        ttk.Entry(self, textvariable=self.second_var).pack(padx=20, pady=20)

        self.calc_option = tk.StringVar()
        self.calc_option.set("add")
        ttk.Label(self, text="Choose operation:").pack(padx=20, pady=20)
        ttk.Combobox(self, textvariable=self.calc_option, values=("add", "subtract", "multiply", "divide")).pack(padx=20, pady=20)

        ttk.Button(self, text="Calculate", command=self.calculate).pack(padx=20, pady=20)

        ttk.Label(self, textvariable=self.result_var).pack(padx=20, pady=20)

    def calculate(self):
        try:
            first = int(self.first_var.get())
            second = int(self.second_var.get())

            if self.calc_option.get() == "add":
                result = first + second
            elif self.calc_option.get() == "subtract":
                result = first - second
            elif self.calc_option.get() == "multiply":
                result = first * second
            elif self.calc_option.get() == "divide":
                result = first / second
            else:
                self.result_var.set("Error: Invalid operation.")
                return

            self.result_var.set(f"Result: {result}")
        except ValueError:
            self.result_var.set("Error: Please enter two numbers.")

if __name__ == "__main__":
    app = CalcApp()
    app.mainloop()
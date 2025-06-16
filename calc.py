import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    """A simple GUI to add numbers consecutively."""

    def __init__(self):
        super().__init__()
        self.title("Speed Entry Calculator")
        self.geometry("300x250")
        self.configure(padx=20, pady=20)

        self.numbers = []
        self.total = 0

        self.create_widgets()
        self.bind("<Return>", lambda event: self.add_number())

    def create_widgets(self):
        header = ttk.Label(self, text="Speed Entry Calculator",
                           font=("Helvetica", 16, "bold"))
        header.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.entry = ttk.Entry(self, justify="center", width=15)
        self.entry.grid(row=1, column=0, columnspan=2, pady=5)

        add_button = ttk.Button(self, text="Add", command=self.add_number)
        add_button.grid(row=1, column=2, padx=5)

        self.history_label = ttk.Label(self, text="", anchor="center")
        self.history_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.total_label = ttk.Label(self, text="0",
                                     font=("Helvetica", 14))
        self.total_label.grid(row=3, column=0, columnspan=3, pady=10)

        clear_button = ttk.Button(self, text="Clear", command=self.reset)
        clear_button.grid(row=4, column=2, pady=(10, 0))

    def add_number(self):
        value = self.entry.get()
        try:
            number = int(value)
            self.numbers.append(number)
            self.total += number
            self.update_labels()
        except ValueError:
            pass  # ignore invalid input
        self.entry.delete(0, tk.END)

    def update_labels(self):
        history = " + ".join(str(num) for num in self.numbers)
        self.history_label.config(text=history)
        self.total_label.config(text=str(self.total))

    def reset(self):
        self.numbers.clear()
        self.total = 0
        self.update_labels()

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

import tkinter as tk
from tkinter import messagebox

class SimpleInterestCalculator:
    def __init__(self,root):
        self.root = root
        self.root.title ("SIMPLE INTEREST CALCULATOR")
        self.root.geometry("300x400")
        self.create_calculate_page()

    def create_calculate_page(self):
        tk.Label(self.root , text="principle Amount").pack(pady=5)
        self.principle_amount_entry = tk.Entry(self.root)
        self.principle_amount_entry.pack(pady=5)
        tk.Label(self.root, text="Interest rate (%)").pack(pady=5)
        self.interest_rate_entry = tk.Entry(self.root)
        self.interest_rate_entry.pack(pady=5)
        tk.Label(self.root, text="Time(years)").pack(pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=5)
        (tk.Button(self.root , text="Calculate Interest" , command=self.simple_interest).pack(pady=5))

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)

    def simple_interest(self):
        try:
            principle = float(self.principle_amount_entry.get())
            interest = float(self.interest_rate_entry.get())
            time = float(self.time_entry.get())
            if principle <= 0 or interest <= 0 or time <= 0:
                raise ValueError
            calculate = (principle * interest * time) / 100
            self.result_label.config(text=f"Simple Interest: ₹{calculate:.2f}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid positive numbers for all fields.")
            self.result_label.config(text="")


if __name__=="__main__":
    root= tk.Tk()
    app = SimpleInterestCalculator(root)
    root.mainloop()


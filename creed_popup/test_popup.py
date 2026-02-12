# test_popup.py
import tkinter as tk

root = tk.Tk()
root.title("Test")
root.geometry("400x200")

label = tk.Label(root, text="If you see this, Tkinter works.", font=("Segoe UI", 14))
label.pack(pady=40)

root.mainloop()

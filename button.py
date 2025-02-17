import tkinter as tk

root = tk.Tk()
root.withdraw()
def close_popup():
    popup.destroy()

popup = tk.Toplevel()
popup.title("alert")

label = tk.Label(popup, text="i am hacking you")
label.pack(pady=20)

custom_button = tk.Button(popup, text="oh no", command=close_popup)
custom_button.pack(pady=10)

popup.mainloop()

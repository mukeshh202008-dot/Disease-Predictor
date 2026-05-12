import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    comments = text_comments.get("1.0", tk.END).strip()

    if name == "" or email == "" or comments == "":
        messagebox.showwarning("Warning", "All fields are required!")
    else:
        messagebox.showinfo("Success", "Feedback submitted successfully!")


root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x350")

tk.Label(root, text="Name").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Comments").pack(pady=5)
text_comments = tk.Text(root, width=30, height=5)
text_comments.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()

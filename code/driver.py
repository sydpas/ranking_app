import tkinter as tk
from tkinter import messagebox

def friends(name, rank, reason):
    name_list = []
    rank_list = []
    reason_list = []

    if name and rank and reason:
        name_list.append(name)
        rank_list.append(rank)
        reason_list.append(reason)

    return list(zip(name_list, rank_list, reason_list))  # returns a list of tuples with name, rank, reason


def display_results():
    name = name_entry.get()
    rank = rank_entry.get()
    reason = reason_entry.get()

    # check if all inputs are provided
    if not name or not rank or not reason:
        messagebox.showwarning("Input Error", "Please fill in all fields before submitting.")
        return

    # get the ranking data
    result = friends(name, rank, reason)

    # add new rank without removing previous
    for name, rank, reason in result:
        listbox.insert(tk.END, f"{name} has a rank of {rank} because {reason}.")

    # clear all fields after submission
    name_entry.delete(0, tk.END)
    rank_entry.delete(0, tk.END)
    reason_entry.delete(0, tk.END)

# exit function for the app
def exit_app():
    window.quit()

# creating the main window
try:
    window = tk.Tk()
    window.title("Ranking App")

    label = tk.Label(window, text="Ranking App", font=("Comic Sans MS", 18), background="khaki1",relief="ridge")
    label.pack(pady=10)

    # name entry
    name_label = tk.Label(window, text="Name:", font=("Comic Sans MS", 12))
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack(pady=5)

    # rank entry
    rank_label = tk.Label(window, text="Rank (1-100):", font=("Comic Sans MS", 12))
    rank_label.pack()
    rank_entry = tk.Entry(window)
    rank_entry.pack(pady=5)

    # reason entry
    reason_label = tk.Label(window, text="Why?:", font=("Comic Sans MS", 12))
    reason_label.pack()
    reason_entry = tk.Entry(window)
    reason_entry.pack(pady=5)

    # displaying results
    listbox = tk.Listbox(window, width=50, height=10, font=("Comic Sans MS", 12), background="SkyBlue2")
    listbox.pack(pady=10)

    # button to add ranking
    show_button = tk.Button(window, text="Add Ranking", command=display_results, font=("Comic Sans MS", 8),
                            background='hot pink')
    show_button.pack(pady=5)

    # button to exit
    exit_button = tk.Button(window, text="Exit", command=exit_app, font=("Comic Sans MS", 8), background="mediumorchid1")
    exit_button.pack(pady=5)

    # running the app
    window.mainloop()

except Exception as e:
    print("Error occurred:", e)
    messagebox.showerror("Error", f"An error occurred: {e}")

import tkinter as tk
from tkinter import messagebox

ranking_data = []


def friends(name, rank, reason):
    name_list = []
    rank_list = []
    reason_list = []

    if name and rank and reason:
        name_list.append(name)
        rank_list.append(rank)
        reason_list.append(reason)

    return list(zip(name_list, rank_list, reason_list))  # returns a list of tuples with name, rank, reason


def add_ranking():
    # getting user input
    name = name_entry.get()
    rank = rank_entry.get()
    reason = reason_entry.get()

    # check if all inputs are provided
    if not name or not rank or not reason:
        messagebox.showwarning("STOP!!!", "PLEASE fill in all fields before submitting.")
        return

    # storing data
    ranking_data.append((name, rank, reason))

    # clear all fields after submission
    name_entry.delete(0, tk.END)
    rank_entry.delete(0, tk.END)
    reason_entry.delete(0, tk.END)


def open_next_window():
    global window  # access all data

    next_window = tk.Toplevel(window)
    next_window.title("ranking results!")
    next_window.geometry("400x400")

    label_next = tk.Label(next_window, text="ranking app", font=("Comic Sans MS", 26))
    label_next.pack(pady=10)

    # display rankings
    listbox = tk.Listbox(next_window, width=50, height=10, font=("Comic Sans MS", 12), background="SkyBlue2")
    listbox.pack(pady=10)

    # add new rank without removing previous
    for name, rank, reason in ranking_data:
        listbox.insert(tk.END, f"{name} has a rank of {rank} because {reason}!")
        # tk.END adds new entry to bottom

    # close button
    close_button = tk.Button(next_window, text="exit", command=next_window.destroy, font=("Comic Sans MS", 10),
                             background="red4", fg="white")
    close_button.pack(pady=5)

    window.withdraw()
    next_window.mainloop()


# exit function for the app
def exit_app():
    window.quit()


# creating the main window
window = tk.Tk()
window.title("ranking app")
window.geometry("300x350")

label = tk.Label(window, text="ranking app", font=("Comic Sans MS", 26))
label.pack(pady=10)

# name entry
name_label = tk.Label(window, text="name:", font=("Comic Sans MS", 12))
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# rank entry
rank_label = tk.Label(window, text="rank (1-100):", font=("Comic Sans MS", 12))
rank_label.pack()  # adds label to available position
rank_entry = tk.Entry(window)  # creates an input field for rank
rank_entry.pack(pady=5)  # gives 5 pixels of padding above and below

# reason entry
reason_label = tk.Label(window, text="why?", font=("Comic Sans MS", 12))
reason_label.pack()
reason_entry = tk.Entry(window)
reason_entry.pack(pady=5)

# button to add ranking
add_button = tk.Button(window, text="add ranking", command=add_ranking, font=("Comic Sans MS", 10),
                        background='hot pink')
add_button.pack(pady=5)

# button to add ranking
show_button = tk.Button(window, text="next", command=open_next_window, font=("Comic Sans MS", 10),
                        background='DeepPink4',fg='white')
show_button.pack(pady=5)


# running the app
window.mainloop()

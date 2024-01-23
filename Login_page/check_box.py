from tkinter import ttk
from tkinter import *

value = 0
value2 = 0
data_list = []

def check_window(account):
    """
    Create a new window, which contain information about deleting account. If admin confirm it's return value 1,
    """
    root = Tk()
    frm = ttk.Frame(root, padding=10)

    def confirm_button():
        global value
        value = 1
        root.destroy()
        return value

    def none_button():
        global value
        value = 2
        root.destroy()

    frm.grid()
    ttk.Label(frm, text="Are you sure, that you want delete this account!").grid(column=0, row=0, columnspan=2)
    ttk.Label(frm, text=f"{account}").grid(column=0, row=1, columnspan=2)
    btn1 = ttk.Button(frm, text="Yes", command=confirm_button)
    btn1.grid(column=0, row=2)
    btn2 = ttk.Button(frm, text='No', command=none_button)
    btn2.grid(column=1, row=2)
    root.mainloop()


def update_window(account_name):
    root = Tk()
    frm = ttk.Frame(root, padding=10)

    def confirm_button():
        global value2
        global data_list
        data_list = []
        value2 = 1
        new_email = email.get()
        new_password = password.get()
        data_list = [value2, new_email, new_password]
        root.destroy()

    def none_button():
        global value2
        value2 = 2
        root.destroy()

    frm.grid()
    ttk.Label(frm, text=f'Update {account_name}').grid(column=0, row=0, columnspan=2)
    ttk.Label(frm, text="If you don't want change value, leave it empty!").grid(column=0, row=1, columnspan=2)
    ttk.Label(frm, text='New email:').grid(row=2)
    email = ttk.Entry(frm)
    email.grid(column=1, row=2)
    ttk.Label(frm, text='New password:').grid(row=3)
    password = ttk.Entry(frm)
    password.grid(column=1, row=3)

    btn1 = ttk.Button(frm, text="Yes", command=confirm_button)
    btn1.grid(column=0, row=4)
    btn2 = ttk.Button(frm, text='No', command=none_button)
    btn2.grid(column=1, row=4)

    root.mainloop()


def update_account(account_name):
    update_window(account_name)
    return data_list


def confirm(text):
    check_window(text)
    return value

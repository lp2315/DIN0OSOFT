import tkinter as tk

from tkinter import ttk

import keyboard

leif_version = "0.9 beta"

##############

##############          ROOT PROPERTIES

root = tk.Tk()
root.title("LEIF version " + leif_version)
root.geometry("480x420")
root.resizable(False, False)

usr_Line = tk.StringVar(root)

root.rowconfigure(0, weight=38)
root.rowconfigure(1, weight=6)

##############

##############          ADJUSTABLES

# fonts

log_font = {'font': ['Terminal', 10]}

usr_font = {'font': ['Bahnschrift', 12, '']}

# padds - L T B R

frm_padd = {'padding': [1, 2, 1, 0]}

btn_padd = {'padding': [4, 4, 4, 4]}

inp_padd = {'padding': [0, 0, 0, 0]}

grid_padd = {'pady': 2, 'padx': 4, 'sticky': 'nsew'}

# tk dicts

log_dict = {**log_font,
            'bg': 'black', 'fg': '#48f3e5'}

##############

##############          STYLES

usr_Style = ttk.Style()

# Frame style

usr_Style.configure(
    "Frm.TFrame"
)

usr_Style.configure(
    "LFrm.TLabelframe"
)


# Entry style

usr_Style.configure(
    "Inp.TEntry"
)

usr_Style.map(
    "Inp.TEntry",
    foreground=[('background', 'cyan'),
                ('focus', 'black')],
    background=[('background', 'light gray'),
                ('focus', 'yellow')]
)

# Buttons style

usr_Style.configure(
    "Btn.TButton",
    **usr_font,
    **btn_padd,
    background='black',
    foreground='black',
    relief='raised'
)

usr_Style.map(
    "Snd.Btn.TButton",
)

usr_Style.map(
    "Tst.Btn.TButton",
)

# Scrollbar style

usr_Style.configure(
    "Scl.Vertical.TScrollbar",
    background='black',
    darkcolor='red',
    arrowcolor='blue',
    arrowsize=50
)


##############

##############          FRAMES


LogFrame = ttk.Frame(
    root,
    **frm_padd,
    style='Frm.TFrame',
    height=320, width=480
)

InpFrame = ttk.LabelFrame(
    root,
    **frm_padd,
    height=100, width=480,
    style='LFrm.TLabelframe',
    text="LEIF Terminal version " + leif_version,
    labelanchor='n',
)

# placement

InpFrame.grid_columnconfigure(0, weight=40)
InpFrame.grid_columnconfigure(1, weight=8)
InpFrame.grid_rowconfigure(0, weight=50)
InpFrame.grid_rowconfigure(1, weight=50)

LogFrame.grid(row=0, column=0, **grid_padd)
InpFrame.grid(row=1, column=0, **grid_padd)

##############

##############          TERMINAL

Logg = (
    tk.Text(
        LogFrame,
        **log_dict,
        state='disabled')
)

InpLine = (
    ttk.Entry(
        InpFrame,
        **usr_font,
        style="Inp.TEntry",
        exportselection=False,
        textvariable=usr_Line,
        takefocus=True)
)

StatusBar = (
    ttk.Label(InpFrame,
              style='TLabel',
              text='<< Status Bar >>',
              **log_font)
)


###############

###############         ACTIONS / KEYMAP


def loggtoggler():
    if Logg.cget('state') == 'disabled':
        Logg.configure(state='normal')
    else:
        Logg.configure(state='disabled')


def send():
    loggtoggler()
    msg = ">>> " + usr_Line.get() + '\n'
    Logg.insert('0.0', msg)
    InpLine.delete(first=0, last=len(msg))
    loggtoggler()


keyboard.add_hotkey('Enter', send)

###############

###############         BUTTONS / SCROLLS


SendBtn = (
    ttk.Button(InpFrame,
               style='Btn.TButton',
               text='Send',
               command=send)
)

TestBtn = (
    ttk.Button(InpFrame,
               style='Btn.TButton',
               text='Test',
               command=None, )
)


LogScrl = (
    ttk.Scrollbar(LogFrame,
                  style="Scl.Vertical.TScrollbar",
                  orient='vertical',
                  command=Logg.yview())
)

Logg.configure(yscrollcommand=LogScrl.set)

##############

##############          PLACEMENT


Logg.place(anchor='nw', relheight=1.0, relwidth=0.95)

LogScrl.place(relheight=1.0, relx=0.95)

InpLine.grid(row=1, column=0, **grid_padd)

StatusBar.grid(row=2, column=0, **grid_padd)

SendBtn.grid(row=1, column=1, **grid_padd)

TestBtn.grid(row=2, column=1, **grid_padd)

###############

###############         INIT

root.mainloop()

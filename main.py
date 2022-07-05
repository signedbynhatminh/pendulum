import tkinter as tk
from doctest import master
from tkinter import messagebox
#creat a function to call when clicking the clik me button
from tkinter.constants import CENTER


from PIL import ImageTk, Image
from tkinter import *

import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    window = tk.Tk()

    value=DoubleVar()
    m=DoubleVar()
    m_slider_label = tk.Label(window, text="MASS")
    m_slider_label.grid(column=0, row=0, sticky=E, padx=5, pady=5)
    m_sliders = tk.Scale(window, from_=0, to=100, variable=value, orient= HORIZONTAL)
    m_sliders.grid(column=1, row=0, sticky=E, padx=5, pady=5)
    m_slidere=tk.Entry(window, textvariable=value)
    m_slidere.grid(column=2, row=0, sticky=E, padx=5, pady=5)


    value=DoubleVar()
    g=DoubleVar()
    g_slider_label = tk.Label(window, text="G")
    g_slider_label.grid(column=0, row=1, sticky=E, padx=5, pady=5)
    g_sliders = tk.Scale(window, from_=0, to=20, variable=value, orient= HORIZONTAL)
    g_sliders.grid(column=1, row=1, sticky=E, padx=5, pady=5)
    g_slidere=tk.Entry(window, textvariable=value)
    g_slidere.grid(column=2, row=1, sticky=E, padx=5, pady=5)

    value=DoubleVar()
    l=DoubleVar()
    l_slider_label = tk.Label(window, text="LENGTH")
    l_slider_label.grid(column=0, row=2, sticky=E, padx=5, pady=5)
    l_sliders=tk.Scale(window, from_=1, to=20, variable=value, orient=HORIZONTAL)
    l_sliders.grid(column=1, row=2, sticky=E, padx=5, pady=5)
    l_slidere=tk.Entry(window, textvariable=value)
    l_slidere.grid(column=2, row=2, sticky=E, padx=5, pady=5)

    value=DoubleVar()
    ag=DoubleVar()
    ag_slider_label = tk.Label(window, text="INITIAL ANGLE")
    ag_slider_label.grid(column=0, row=3, sticky=E, padx=5, pady=5)
    ag_sliders = tk.Scale(window, from_=1, to=20, variable=value, orient=HORIZONTAL)
    ag_sliders.grid(column=1, row=3, sticky=E, padx=5, pady=5)
    ag_slidere=tk.Entry(window, textvariable=value)
    ag_slidere.grid(column=2, row=3, sticky=E, padx=5, pady=5)

    p_slider_label = tk.Label(window, text="PERIOD")
    p_slider_label.grid(column=0, row=4, sticky=E, padx=5, pady=5)
    p_slider = tk.Entry(window)
    p_slider.grid(column=1, row=4, sticky=E, padx=5, pady=5)


    #make it loop until an event happens
    window.mainloop()



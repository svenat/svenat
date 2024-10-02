import tkinter
import PyTouchBar

root = tkinter.Tk()
PyTouchBar.prepare_tk_windows(root)
lbl = tkinter.Label(root, text="Button")
lbl.pack()
root.mainloop()
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

from controllers.loginController import LoginController

loginController = LoginController()


def LoginApp():
    def onSubmitData():
        webPath = webPathVar.get()
        companyID = companyIDVar.get()
        # loginController.writeFile(webPath, companyID)
        loginController.checkValue(webPath, companyID)

    window = tb.Window(themename='cosmo')
    window.title('Virtualist BD Attendance Access')
    window.geometry('450x150+500+200')
    window.resizable(False, False)
    custom_font = tb.font.Font(family="Arial", size=10, weight="bold")

    mainFrame = tb.Frame(window)
    mainFrame.pack(fill=BOTH, expand=True, anchor="center")

    frame1 = tb.Frame(mainFrame)
    frame1.pack(fill=X, pady=5)
    webPathLabel = tb.Label(frame1, text="Web Path:", bootstyle='default', font=custom_font)
    webPathLabel.pack(side="left", padx=10)
    webPathVar = StringVar()
    webPathEntry = tb.Entry(frame1, bootstyle='default', textvariable=webPathVar)
    webPathEntry.pack(fill=X, padx=10)

    frame2 = tb.Frame(mainFrame)
    frame2.pack(fill=X, pady=5)
    companyIDLabel = tb.Label(frame2, text="Company ID:", bootstyle='default', font=custom_font)
    companyIDLabel.pack(side="left")
    companyIDVar = StringVar()
    companyIDEntry = tb.Entry(frame2, bootstyle='default', textvariable=companyIDVar)
    companyIDEntry.pack(fill=X, padx=10)

    style = tb.Style(theme='cosmo')
    style.configure('TButton', font=('Helvetica', 10))
    button = tb.Button(mainFrame, text="Save!", style='TButton', command=onSubmitData)
    button.pack(pady=15)

    window.mainloop()

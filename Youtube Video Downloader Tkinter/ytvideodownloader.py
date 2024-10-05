import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widgets(): # to create tkinter widgets
    label = Label(main, text = "Youtube Video Downloader",
                  padx = 15, pady = 15,
                  font = "Helvetica 12",
                  bg = "red",
                  fg = "white")
    label.grid(row = 1, column = 1,
               pady = 10, padx = 5,
               columnspan = 3)
    
    linkLabel = Label(main, text = "Youtube Link:",
                      bg = "red",
                      pady = 5, padx = 5)
    linkLabel.grid(row = 2, column = 0,
                   pady = 5, padx = 5)
    
    main.linkText = Entry(main, width = 35,
                          textvariable = link,
                          font = "Helvetica 10")
    main.linkText.grid(row = 2, column = 1,
                       pady = 5, padx = 5,
                       columnspan = 2)
    
    folderLabel = Label(main, text = "Save To:",
                        bg = "red",
                        pady = 5, padx = 9)
    folderLabel.grid(row = 3, column = 0,
                     pady = 5, padx = 5)
    
    main.folderText = Entry(main, width = 27,
                            textvariable = path,
                            font = "Helvetica 10")
    main.folderText.grid(row = 3, column = 1,
                        pady = 5, padx = 5)
    
    browseButton = Button(main, text = "Browse",
                          command = Browse, 
                          width = 10,
                          bg = "red",
                          font = "Helvetica, 10",
                          relief = GROOVE)
    browseButton.grid(row = 3, column = 2,
                      pady = 1, padx = 1)
    
    downloadButton = Button(main, text = "Download Video",
                            command = Download,
                            width = 20,
                            bg = "red",
                            pady = 10, padx = 15,
                            font = "Helvetica, 10",
                            relief = GROOVE)
    downloadButton.grid(row = 4, column = 1,
                        pady = 20, padx = 20)

def Browse(): # to select folder
    directory = filedialog.askdirectory(initialdir = "DOWNLOAD PATH",
                                        title = "Save Video")
    path.set(directory)

def Download(): # to download video to selected folder
    yt_link = link.get()
    folder = path.get()
    getVideo = YouTube(yt_link)
    videoStream = getVideo.streams.get_highest_resolution()
    videoStream.download(folder)
    messagebox.showinfo("VIDEO SUCCESSFULLY DOWNLOADED")


main = tk.Tk()
main.geometry("520x280")
main.resizable(False, False)
main.title("Youtube Video Downloader")
main.config(background = "lightyellow")

link = StringVar()
path = StringVar()

Widgets()

main.mainloop()
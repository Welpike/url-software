# Welpike - https://welpike.github.io
# see https://github.com/Welpike/url-software

from tkinter import *
from tkinter import messagebox
from webbrowser import open as webbrowser_open
from urllib.parse import urlparse, quote

welpike_redirect_url = urlparse("https://welpike.github.io/url/url.html")


def copy_url(url):
    window.clipboard_clear()
    window.clipboard_append(url)
    window.update()


def generate():
    url = input.get()
    delay = input_delay.get()
    if not delay:
        delay = 2
    url_input_parse = urlparse(url)

    if url_input_parse.hostname:
        if url_input_parse.scheme:
            url = quote(url, safe='')
            output_url = welpike_redirect_url._replace(query=f"redirect={url}&delay={delay}").geturl()
            with open("links_list.txt", "a",) as file:
                file.write(f"{output_url} \n")
                file.close()
            copy_url(output_url)
            messagebox.showinfo("welpike-url-software", f"Here is the link : {output_url} \n N.B : the link is in your "
                                                        f"clipboard now !")
        else:
            messagebox.showerror("welpike-url-software", "Error, the protocol (http, https) is missing.")
    else:
        messagebox.showerror("welpike-url-software", "Error, please enter a valid url.")


def show_history():
    history_output = ""
    try:
        with open("links_list.txt", "r") as file:
            history = file.readlines()
            file.close()
            if not history:
                messagebox.showinfo("welpike-url-software", "The history is empty.")
            else:
                for link in history:
                    history_output += f" {link}"
                messagebox.showinfo("welpike-url-software", f"Links generated : {history_output}")
    except FileNotFoundError:
        with open("links_list.txt", "w+") as file:
            file.write("")
            file.close()
        messagebox.showerror("welpike-url-software", "The file that contains history has been removed. \n A new file has"
                                                     " been created.")


def delete_history():
    with open("links_list.txt", "w") as file:
        file.write("")
        file.close()
        messagebox.showinfo("welpike-url-software", "History removed.")


def about_github():
    webbrowser_open("https://github.com/Welpike/url-software")


def about_help():
    webbrowser_open("https://github.com/Welpike/url-software/issues")


def about_welpike():
    webbrowser_open("https://welpike.github.io/")


def about_software():
    webbrowser_open("https://welpike.github.io/url/download.html")


window_bg = "#1F1F1F"
window_font_family = "Monospace"
window_font_color = "#FFFFFF"
window_font_size = 20
window_font_size_small = 16

window = Tk()

window.title("welpike-url-software")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background=window_bg)

frame = Frame(window, bg=window_bg)

label_frame = Frame(frame, bg=window_bg, pady=20)
label = Label(label_frame, text='welpike-url-software', font=(window_font_family, window_font_size), bg=window_bg,
              fg=window_font_color)
label.pack()
label_frame.pack()

input_frame = Frame(frame, bg=window_bg, pady=20)
input = Entry(input_frame, font=(window_font_family, window_font_size_small), bg=window_bg, fg=window_font_color)
input.pack()
input_frame.pack()

input_delay_frame = Frame(frame, bg=window_bg, pady=20)
input_delay = Entry(input_delay_frame, font=(window_font_family, window_font_size_small), bg=window_bg,
                    fg=window_font_color)
input_delay.pack()
input_delay_frame.pack()

button_frame = Frame(frame, bg=window_bg, pady=20)
button = Button(button_frame, text="Generate an url", font=(window_font_family, window_font_size_small), bg=window_bg,
                fg=window_font_color, command=generate)
button.pack()
button_frame.pack()

frame.pack()

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Generate", command=generate)
file_menu.add_command(label="Exit", command=window.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

history_menu = Menu(menu_bar, tearoff=0)

history_menu.add_command(label="Show history", command=show_history)
history_menu.add_command(label="Delete history", command=delete_history)

menu_bar.add_cascade(label="History", menu=history_menu)

about_menu = Menu(menu_bar, tearoff=0)

about_menu.add_command(label="Help", command=about_help)
about_menu.add_command(label="About Welpike", command=about_welpike)
about_menu.add_command(label="About software", command=about_software)
about_menu.add_command(label="Source code", command=about_github)

menu_bar.add_cascade(label="About", menu=about_menu)

window.config(menu=menu_bar)

window.mainloop()

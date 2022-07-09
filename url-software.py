# Welpike - https://welpike.github.io
# see https://github.com/Welpike
from urllib.parse import urlparse, quote

welpike_redirect_url = urlparse("https://welpike.github.io/url.html")
print("Welcome in the Welpike's redirect urls generator.")

while True:
    url_input = input("Enter an url : ")
    url_input_parse = urlparse(url_input)

    if url_input_parse.scheme:
        url = quote(url_input, safe='')
        print("Redirect url : ", welpike_redirect_url._replace(query=f"redirect={url}").geturl())
        print()
        print()
        print("Software developed by Welpike - https://welpike.github.io")
        print("This software needs python 3.9 or higher and the urllib.parse library.")
        break
    else:
        print("Please enter a protocol (http or https).")

from main import *
from tkinter import * #importing tk library to make a window

window = Tk() #initializing window

window['bg'] = '#000000'
window.geometry('600x600') #window parametrs
window.title('Spread calculator')

canvas = Canvas(window, height=600, width=600, background="black") #making a layer to work with
canvas.pack()


def btn_binance_click(): #defining functions that stand for clicking the buttons to check btc prices
    get_crypto_price(url_binance, accept_locator_binance, price_locator_binance, binance_label)


def btn_bybit_click():
    get_crypto_price(url_bybit, None, price_locator_bybit, bybit_label)


def btn_okx_click():
    get_crypto_price(url_okx, accept_locator_okx, price_locator_okx, okx_label)


def btn_binance_bybit_click(): #defining functions that stand for clicking buttons to check spread between exchanges
    try:
        binance_price_str = binance_label.cget("text") #get the text content of the binance label
        bybit_price_str = bybit_label.cget("text") #get the text content of the bybit label

        binance_price = float(re.search(r'\d[\d.,]*', binance_price_str).group().replace(',', '')) #extract and convert the numeric value from the Binance label text
        bybit_price = float(re.search(r'\d[\d.,]*', bybit_price_str).group().replace(',', '')) #the same with bybit

        spread = binance_price - bybit_price #substract one from another

        spread_label_binance_bybit.config(text=f"Spread: {spread:.2f}$") #update the label with the calculated spread

    except Exception as e:
        spread_label_binance_bybit.config(text=f"An error occurred: {e}") #handle exceptions by updating the label with an error message


def btn_bybit_okx_click():
    try:
        bybit_price = float(re.search(r'\d[\d.,]*', bybit_label.cget("text")).group().replace(',', ''))
        okx_price = float(re.search(r'\d[\d.,]*', okx_label.cget("text")).group().replace(',', ''))

        spread = bybit_price - okx_price

        spread_label_bybit_okx.config(text=f"Spread: {spread:.2f}$")

    except Exception as e:
        spread_label_bybit_okx.config(text=f"An error occurred: {e}")


def btn_binance_okx_click():
    try:
        binance_price = float(re.search(r'\d[\d.,]*', binance_label.cget("text")).group().replace(',', ''))
        okx_price = float(re.search(r'\d[\d.,]*', okx_label.cget("text")).group().replace(',', ''))

        spread = binance_price - okx_price

        spread_label_binance_okx.config(
            text=f"Spread: {spread:.2f}$")

    except Exception as e:
        spread_label_binance_okx.config(text=f"An error occurred: {e}")


frame = Frame(window, bg='grey') #making a frame in canva
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)


frame.grid_rowconfigure(1, weight=1) #configure rows to expand proportionally when extra vertical space is available
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(5, weight=1)



btn_binance = Button(frame, text='BTC price on Binance',
                     bg='yellow', font='Terminal', command=btn_binance_click) #defining buttons that stand for getting price of btc
btn_binance.grid(row=0, column=0, pady=(0, 10)) #defining their place with grid

binance_label = Label(frame, text="", pady=10, padx=100, bg='white') #defining white spaces or so-called labels where price is displayed
binance_label.grid(row=1, column=0, pady=(0, 10))


btn_bybit = Button(frame, text='BTC price on Bybit', bg='yellow',
                   font='Terminal', command=btn_bybit_click)
btn_bybit.grid(row=2, column=0, pady=(0, 10))

bybit_label = Label(frame, text="", pady=10, padx=100, bg='white')
bybit_label.grid(row=3, column=0, pady=(0, 10))


btn_okx = Button(frame, text='BTC price on OKX', bg='yellow',
                 font='Terminal', command=btn_okx_click)
btn_okx.grid(row=4, column=0, pady=(0, 10))

okx_label = Label(frame, text="", pady=10, padx=100, bg='white')
okx_label.grid(row=5, column=0, pady=(0, 10))



btn_binance_bybit = Button(frame, text='BIN/BYB', bg='green', font='Terminal', command=btn_binance_bybit_click)
btn_binance_bybit.grid(row=7, column=0, pady=(0, 10))

spread_label_binance_bybit = Label(frame, text="", pady=10, padx=30, bg='white')
spread_label_binance_bybit.grid(row=7, column=1, pady=(0, 10))


btn_bybit_okx = Button(frame, text='BYB/OKX', bg='green', font='Terminal', command=btn_bybit_okx_click) #defining buttons for calculating spreads
btn_bybit_okx.grid(row=8, column=0, pady=(0, 10)) #defining their location

spread_label_bybit_okx = Label(frame, text="", pady=10, padx=30, bg='white') #defining white spaces or so-called labels where spread is displayed
spread_label_bybit_okx.grid(row=8, column=1, pady=(0, 10)) #defining place for labels


btn_binance_okx = Button(frame, text='BIN/OKX', bg='green', font='Terminal', command=btn_binance_okx_click)
btn_binance_okx.grid(row=9, column=0, pady=(0, 10))

spread_label_binance_okx = Label(frame, text="", pady=10, padx=30, bg='white')
spread_label_binance_okx.grid(row=9, column=1, pady=(0, 10))



window.mainloop() #mainloop for the app

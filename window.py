from main import *
from tkinter import *

window = Tk()

window['bg'] = '#000000'
window.geometry('600x600')
window.title('Spread calculator')

canvas = Canvas(window, height=600, width=600, background="black")
canvas.pack()


def btn_binance_click():
    get_crypto_price(url_binance, accept_locator_binance,
                     price_locator_binance, binance_label)


def btn_bybit_click():
    get_crypto_price(url_bybit, None, price_locator_bybit, bybit_label)


def btn_okx_click():
    get_crypto_price(url_okx, accept_locator_okx, price_locator_okx, okx_label)


frame = Frame(window, bg='grey')
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)


frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(5, weight=1)


btn_binance = Button(frame, text='BTC price on Binance',
                     bg='yellow', font='Terminal', command=btn_binance_click)
btn_binance.grid(row=0, column=0, pady=(0, 10))

binance_label = Label(frame, text="", pady=10, padx=100, bg='white')
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


window.mainloop()

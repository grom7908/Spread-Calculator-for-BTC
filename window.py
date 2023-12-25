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
                     price_locator_binance)


def btn_bybit_click():
    get_crypto_price(url_bybit, None, price_locator_bybit)


def btn_okx_click():
    get_crypto_price(url_okx, accept_locator_okx, price_locator_okx)


frame = Frame(window, bg='grey')
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)


btn_binance = Button(frame, text='BTC price on Binance',
                     bg='yellow', font='Terminal', command=btn_binance_click)
btn_binance.pack(pady=50)

btn_bybit = Button(frame, text='BTC price on Bybit',
                   bg='yellow', font='Terminal', command=btn_bybit_click)
btn_bybit.pack(pady=50)

btn_okx = Button(frame, text='BTC price on OKX',
                 bg='yellow', font='Terminal', command=btn_okx_click)
btn_okx.pack(pady=50)


window.mainloop()

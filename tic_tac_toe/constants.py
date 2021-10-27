SYMBOLS = ("X", "O")

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]


USER_TEMPLATE = (
    ("name", lambda *args, **kwargs: input("ВВЕДИТЕ ВАШЕ ИМЯ")),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
)
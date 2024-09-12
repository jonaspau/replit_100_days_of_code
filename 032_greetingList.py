from random import randint


greetings = [
    "Hei",
    "salut",
    "hola",
    "ciao",
    "hallo",
    "tjenare",
    "goddag",
    "hoi",
    "cześć",
    "你好",
    "こんにちは",
    "안녕",
    "नमस्ते",
    "สวัสดี",
    "مرحبا",
    "oi",
    "Γεια σου",
    "merhaba",
    "halo"
]


end = len(greetings)-1
greeting = greetings[randint(0, end)]

print(f"{greeting}!\nJag är en bot, Anna heter jag.")

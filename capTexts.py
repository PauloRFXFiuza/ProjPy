'''
This function returns a text entered by the user in uppercase and without spaces at the beginning and end of the text.
Esta função retorna um texto digitado pelo usuário com letras maiúsculas e sem espaços no início e no fim do texto.
'''
def capText(text):
    text = text.capitalize()
    text = text.strip()
    return text

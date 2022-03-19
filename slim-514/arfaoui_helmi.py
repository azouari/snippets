class ListMustBeofLength10Exeption(Exception):
    """Raise exception if len of list > 10"""


def get_values():
    values = input("Entrer les 10 temperatures en celcus: ")
    values = [int(value) for value in values.split()]
    if len(values) != 10:
        raise ListMustBeofLength10Exeption("List must have a length of 10")
    return values

if __name__ == '__main__':
    celcius = get_values()
    fahrenheit = [(x*9)/5 + 32 for x in celcius]
    print(f"La liste des temperatures en c: {celcius}\nLa liste des temp en f: {fahrenheit}")

    '''Example:
       python arfaoui_helmi.py
       Entrer les 10 temperatures en celcus: 10 20 30 40 50 60 70 80 90 100
       La liste des temperatures en c: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
       La liste des temp en f: [50.0, 68.0, 86.0, 104.0, 122.0, 140.0, 158.0, 176.0, 194.0, 212.0] 
       
       python arfaoui_helmi.py
       Entrer les 10 temperatures en celcus: 10 20 30 40
    Traceback (most recent call last):
  File "/Users/ahmedzouari/vscode/snippets/slim-514/arfaoui_helmi.py", line 13, in <module>
    celcius = get_values()
  File "/Users/ahmedzouari/vscode/snippets/slim-514/arfaoui_helmi.py", line 9, in get_values
    raise ListMustBeofLength10Exeption("List must have a length of 10")
__main__.ListMustBeofLength10Exeption: List must have a length of 10
    '''

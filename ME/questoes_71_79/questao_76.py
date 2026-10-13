import traceback

def processar(lista):
    for x in lista:
        try:
            print(float(x))
        except (TypeError,ValueError):
            traceback.print_exc()

processar([10,"20","abc",None])

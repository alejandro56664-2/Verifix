'''
Tabla de equivalencias creada para el parser modificado de CLARA
y habilitar el funcionamiento de Verifix con Python.
'''
equivalences = {
    'Eq': '==',
    'NotEq': '!=',
    'Not': '!',
    'And': 'and',
    'Or': 'or',
    'Lt': '<',
    'Gt': '>',
    'LtE': '<=',
    'GtE': '>=',
    'Mod': '%',
    'Add': '+',
    'Sub': '-',
    'Mult': '*',
    'Div': '/',
    'FloorDiv': '//',
    'Pow': '**',
    'AssAdd': '+=',
    'AssMult': '*=',
    'AssDiv': '/=',
    'In': 'in',
    'USub': '-'
}

def convert(name):
    equivalent = equivalences.get(name)
    if not equivalent:
        raise Exception(f"Key '{name}' does not exist in equivalences table!")
    return equivalent


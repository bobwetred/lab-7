class RomanNumeralInterpreter(object):
    def __init__(self):
        self.grammar = {
            'and' : "&",
            'or' : "|",
            'not' : "~",
                        
        }
    def interpret(self, list):
        numbers = map(self.grammar.get, list)  # строки в значения
        return numbers


def main():

    u = '''A or A
B and B
not C '''
    bufer = ''
    list1 = list()
    for i in u:
        if (i != ' ') and (i != '\n'):
            bufer += i
        if (i == ' ') or (i == '\n'):
            list1.append(bufer)
            bufer = ''
    interp = RomanNumeralInterpreter()
    list1 = interp.interpret (list1)

main()
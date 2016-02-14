from re import findall

def cpf_formatter(cpf):
    cpf = findall('\d', cpf)
    if len(cpf) != 11:
        return "error!"
    cpf.insert(3, '.')
    cpf.insert(7, '.')
    cpf.insert(11, '-')
    return ''.join(cpf)

import re

def cpf_formatter(cpf):
    cpf = findall('\d', cpf)
    if len(cpf) != 11:
        return "error!"
    cpf.insert(3, '.')
    cpf.insert(7, '.')
    cpf.insert(11, '-')
    return ''.join(cpf)
    
def ip_validate(ip):
    is_internal_ip = re.search('177\.8\.106\.', ip)
    return bool(is_internal_ip)

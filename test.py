from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('28630498', webservice=WebService.APICEP)

print(address)
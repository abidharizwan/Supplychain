import json

from web3 import *
from django.template import Library

from sam1 import settings

register = Library()
blockchain_address = 'HTTP://127.0.0.1:7545'
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = settings.STATIC_ROOT+'\\blocks\\build\\contracts\\supply.json'
deployed_contract_addressa = web3.eth.accounts[4]

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)


@register.filter(is_safe=False)
def material_info(value_, arg):
    value = 'None'
    try:
        blocknumber = web3.eth.get_block_number()
        for i in range(blocknumber, 0, -1):
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            c = decoded_input[1]
            if int(c['ida']) == int(value_):
                if str(arg) == 'namea':
                    value = c['namea']
                elif str(arg) == 'categorya':
                    value = c['categorya']
                elif str(arg) == 'descriptiona':
                    value = c['descriptiona']
                elif str(arg) == 'suppliera':
                    mlid = c['suppliera']
                    from myapp.models import Supplier
                    value = Supplier.objects.get(LOGIN_id=mlid).companyname
                elif str(arg) == 'quantitya':
                    value = c['quantitya']
                elif str(arg) == 'origina':
                    value = c['origina']
                elif str(arg) == 'costa':
                    value = c['costa']
                elif str(arg) == 'productiondatea':
                    value = c['productiondatea']
                elif str(arg) == 'certificatea':
                    value = c['certificatea']
                return value
    except:
        return value

@register.filter(is_safe=False)
def product_info(value_, arg):
    value = 'None'
    try:
        blocknumber = web3.eth.get_block_number()
        for i in range(blocknumber, 0, -1):
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            c = decoded_input[1]
            if int(c['ida']) == int(value_):
                if str(arg) == 'namea':
                    value = c['namea']
                elif str(arg) == 'categorya':
                    value = c['categorya']
                elif str(arg) == 'descriptiona':
                    value = c['descriptiona']
                elif str(arg) == 'specificationa':
                    value = c['specificationa']
                elif str(arg) == 'unitofmeasurementa':
                    value = c['unitofmeasurementa']
                elif str(arg) == 'manufacture_ida':
                    mlid = c['manufacture_ida']
                    from myapp.models import Manufacture
                    value = Manufacture.objects.get(LOGIN_id=mlid).name
                elif str(arg) == 'typea':
                    value = c['typea']

                return value
    except:
        return value

@register.filter(is_safe=False)
def convert_to(value):
    # value = 'None'
    try:
        from datetime import datetime

        timestamp = int(value) / 1000
        date = datetime.utcfromtimestamp(timestamp)
        # value = date
        return str(date)
    except Exception as e:
        print(e)
        return '0'

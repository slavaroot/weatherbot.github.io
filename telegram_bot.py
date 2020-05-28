import requests
from pprint import pprint

# response = requests.get('https://api.telegram.org/bot857328939:AAErdqGLGe93RRQ40s7ck-KnHO84AVHjoy4/getMe')
#
# pprint(response.json())

# json_response = {'ok': True,
#  'result': {'can_join_groups': True,
#             'can_read_all_group_messages': False,
#             'first_name': 'weatherrootslv_bot',
#             'id': 857328939,
#             'is_bot': True,
#             'supports_inline_queries': False,
#             'username': 'weatherrootslv_bot'}}


# for i in json_response.keys():
#     pprint(i)
#     pprint(json_response[i])



# for i in json_response.values():
#     pprint(i)

# pprint(json_response['result'])
# pprint(json_response['result']['first_name'])



# for i in json_response.items():
#     pprint(i[0])
#     pprint(i[1])

# for key, value in json_response.items():
#     pprint(key)
#     pprint(value)

# for index, key in enumerate(json_response.items()):
#     print(index, key)
#     print(index, key[0], key[1])

# for index, (key, value) in enumerate(json_response.items()):
#     print(index, key, value)

# for index, (key, value) in enumerate(json_response.items()):
#     print(index, key, value)
#
#     print(type(value) == dict)
#
#
#     if type(value) == dict:
#
#         for i in value:
#             print(i)




#TODO изучить массивы,множества, json, поизвлекать данные из них. Изучить библиотеку requests
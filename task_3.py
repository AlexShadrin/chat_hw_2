import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(CURRENT_DIR, 'source_data', 'file.yaml')
data = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_quantity': 4,
    'items_price': {
        'computer': '100€-1500€',
        'keyboard': '10€-90€',
        'mouse': '2€-8€',
        'printer': '99€-500€'
    }
}

with open(filename, 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open(filename) as f_n:
    print(f_n.read())
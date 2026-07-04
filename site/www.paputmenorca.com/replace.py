import os
import glob

replacements = {
    'CONTÁCTANOS': 'CONTACT US',
    'HACER PEDIDO': 'PLACE ORDER',
    'PEDIDOS GRANDES': 'LARGE ORDERS',
    'TIENDA': 'SHOP',
    'EVENTOS': 'EVENTS',
    'CHIRINGUITO': 'BEACH BAR',
    'Andén de poniente S/N, Puerto de Mahón, Menorca': 'Andén de poniente S/N, Port of Mahón, Menorca',
    'Avinguda de Josep A. Clavé, 35, Mahón, Menorca': 'Avinguda de Josep A. Clavé, 35, Mahón, Menorca',
    'CONTACTO': 'CONTACT',
    'COOKIES': 'COOKIES',
    'POLÍTICA DE PRIVACIDAD': 'PRIVACY POLICY',
    'TODO LEGAL': 'LEGAL',
    'SOBRE PAPUT': 'ABOUT PAPUT',
    'Usamos cookies para mejorar tu experiencia y analizar el uso de nuestra web.': 'We use cookies to improve your experience and analyze the use of our website.',
    'RECHAZAR': 'DECLINE',
    'ACEPTAR': 'ACCEPT',
}

base_dir = os.path.dirname(os.path.abspath(__file__))

for filepath in glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for k, v in replacements.items():
        new_content = new_content.replace(k, v)
        # Also replace lowercase / title case if needed, but exact matches first
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filepath}')

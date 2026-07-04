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
    'Doble cheddar, bacon, pepinillos y salsa Macatol.': 'Double cheddar, bacon, pickles, and Macatol sauce.',
    'Cheddar, mermelada de bacon y mayonesa de cebolla caramelizada.': 'Cheddar, bacon jam, and caramelized onion mayonnaise.',
    'Lechuga, tomate, cheddar y mayonesa.': 'Lettuce, tomato, cheddar, and mayonnaise.',
    'Cheddar, bacon y mayonesa.': 'Cheddar, bacon, and mayonnaise.',
    'Contramuslo de pollo rebozado, lechuga, cheddar y mayo sweet chili.': 'Crispy chicken thigh, lettuce, cheddar, and sweet chili mayo.',
    'Lechuga, queso de Mahón, sobrasada, miel y mayo romero.': 'Lettuce, Mahón cheese, sobrasada, honey, and rosemary mayo.',
    'Queso provolone fundido, champiñones salteados, cebolla caramelizada y mayo trufa.': 'Melted provolone cheese, sautéed mushrooms, caramelized onion, and truffle mayo.',
    'Rúcula, scamorza, guanciale, tomate seco y mayo pesto.': 'Arugula, scamorza, guanciale, sun-dried tomato, and pesto mayo.',
    'Burger de Heura, cheddar vegano, lechuga, tomate, cebolla morada y salsa Bahiana vegana.': 'Heura burger, vegan cheddar, lettuce, tomato, red onion, and vegan Bahian sauce.',
    'LA CLÁSICA': 'THE CLASSIC',
    'FORA FÚA (VEGANA)': 'FORA FÚA (VEGAN)',
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

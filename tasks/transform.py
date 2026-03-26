from datetime import datetime

def transform(data):
    """
    transformamos la data de randomuser
    """
    transform_data = []
    
    for item in data:
        nombre = item.get('name', {}).get('common', 'N/A')
        capital = item.get('capital')[0] if item.get('capital') else 'N/A'
        region = item.get('region', 'N/A')
        poblacion = item.get('population', 0)
        
        transform_data.append((nombre, capital, region, poblacion))

    return transform_data
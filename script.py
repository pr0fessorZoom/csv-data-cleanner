import pandas as pd

# Función para procesar el archivo CSV
def process_csv(file_path, output_file):
    # Leer el archivo CSV
    df = pd.read_csv(file_path)
    
    # Agrupar por Address y concatenar los nombres que tienen la misma Address
    grouped_addresses = df.groupby('Address')['Name'].apply(lambda x: ', '.join(x)).reset_index()
    
    # Crear una columna que indique si la Address es repetida o única
    grouped_addresses['Status'] = grouped_addresses['Name'].apply(lambda x: 'repetida' if ',' in x else 'única')
    
    # Guardar los resultados en un solo archivo CSV
    grouped_addresses.to_csv(output_file, index=False)

# Ruta al archivo CSV de entrada
file_path = 'prueba_addresses.csv'

# Ruta al archivo CSV de salida
output_file = 'addresses_status.csv'

# Llamada a la función
process_csv(file_path, output_file)

print(f"Archivo guardado en: {output_file}")

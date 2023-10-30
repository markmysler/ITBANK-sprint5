def create_html_file(data):
    # Open the HTML file in write mode
    with open('resumen.html', 'w') as file:
        # Write the HTML header
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<title>Resumen</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        
        # Write the user's info
        file.write('<h1>Informacion del usuario</h1>\n')
        file.write('<p>Numero de cuenta: {}</p>\n'.format(data['numero']))
        file.write('<p>Nombre: {}</p>\n'.format(data['nombre']))
        file.write('<p>Apellido: {}</p>\n'.format(data['apellido']))
        file.write('<p>DNI: {}</p>\n'.format(data['dni']))
        file.write('<p>Tipo de cuenta: {}</p>\n'.format(data['tipo']))
        
        # Write the list of transactions
        file.write('<h2>Transacciones</h2>\n')
        file.write('<ul>\n')
        for transaction in data['transacciones']:
            file.write('<li>\n')
            file.write('<p>Estado: {}</p>\n'.format(transaction['estado']))
            file.write('<p>Tipo: {}</p>\n'.format(transaction['tipo']))
            file.write('<p>Fecha: {}</p>\n'.format(transaction['fecha']))
            file.write('<p>Numero: {}</p>\n'.format(transaction['numero']))
            file.write('<p>Mensaje: {}</p>\n'.format(transaction['msj']))
            file.write('</li>\n')
        file.write('</ul>\n')
        
        # Write the HTML footer
        file.write('</body>\n')
        file.write('</html>\n')
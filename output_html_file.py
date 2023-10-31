def create_html_file(data):
    html = '''
    <html>
    <head>
        <title>Resumen ITBANK</title>
        <style>
            .container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }}
            
            .user-info {{
                margin-bottom: 20px;
            }}
            
            .transactions {{
                list-style-type: none;
				padding: 0;
            }}
            
            .transaction {{
                border: 1px solid #ccc;
				padding: 10px;
				margin-bottom: 10px;
				width: 30vw;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Informacion del usuario</h1>
            <div class="user-info">
                <p>Numero de cuenta: {numero}</p>
                <p>Nombre: {nombre}</p>
                <p>Apellido: {apellido}</p>
                <p>DNI: {dni}</p>
                <p>Tipo de cuenta: {tipo}</p>
            </div>
            <h2>Transacciones</h2>
            <ul class="transactions">
                {transactions}
            </ul>
        </div>
    </body>
    </html>
    '''

    transaction_html = ''
    for transaction in data['transacciones']:
        transaction_html += '''
        <li class="transaction">
            <p>Estado: {estado}</p>
            <p>Tipo: {tipo}</p>
            <p>Fecha: {fecha}</p>
            <p>Numero: {numero}</p>
            <p>Mensaje: {msj}</p>
        </li>
        '''.format(**transaction)

    html = html.format(transactions=transaction_html, **data)
    with open('resumen.html', 'w') as file:
        file.write(html)

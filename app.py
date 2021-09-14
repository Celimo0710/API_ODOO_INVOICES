# Importador de facturas a Odoo
# Autor: Célimo Ureña Araya
# Para: SIACOOP RL

# ---importar funciones desde archivos o librerías---
#       bill: funciones para facturas de gastos
#       invoices: funciones para facturas de venta
#       Flask: funciones para ejecutar el servidor
#       Jsonify: estructurador formato Json
#       request: objeto obtenido de la respuesta a través de un método

import bill as compra
import invoices as venta
from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta para la creación de factura de compra


@app.route('/compra', methods=['POST'])
def compras():
    try:
        # Variables locales para definir localización
        provincia = ""
        canton = ""
        # Variables locales para definir compañía asociada a la factura
        empresa_id = 0
        empresa_nombre = ""  # Variable para test
        # Validación de las entradas de los datos para la localización
        if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Provincia'] == "1":
            provincia = "San José"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "01":
                canton = "SAN JOSE"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "02":
                canton = "ESCAZU"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "03":
                canton = " DESAMPARADOS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "04":
                canton = "PURISCAL"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "05":
                canton = "TARRAZU"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "06":
                canton = "ASERRI"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "07":
                canton = "MORA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "08":
                canton = "GOICOECHEA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "09":
                canton = "SANTA ANA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "10":
                canton = "ALAJUELITA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "11":
                canton = "CORONADO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "12":
                canton = "ACOSTA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "13":
                canton = "TIBAS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "14":
                canton = "MORAVIA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "15":
                canton = "MONTES DE OCA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "16":
                canton = "TURRUBARES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "17":
                canton = "DOTA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "18":
                canton = "CURRIDABAT"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "19":
                canton = "PEREZ ZELEDON"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "20":
                canton = "LEON CORTES"
        if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Provincia'] == "2":
            provincia = "Alajuela"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "01":
                canton = "ALAJUELA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "02":
                canton = "SAN RAMON"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "03":
                canton = "GRECIA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "04":
                canton = "SAN MATEO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "05":
                canton = "ATENAS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "06":
                canton = "NARANJO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "07":
                canton = "PALMARES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "08":
                canton = "POAS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "09":
                canton = "OROTINA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "10":
                canton = "SAN CARLOS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "11":
                canton = "ALFARO RUIZ"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "12":
                canton = "VALVERDE VEGA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "13":
                canton = "UPALA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "14":
                canton = "LOS CHILES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "15":
                canton = "GUATUSO"
        if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Provincia'] == "3":
            provincia = "Cartago"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "01":
                canton = "CARTAGO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "02":
                canton = "PARAISO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "03":
                canton = "LA UNION"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "04":
                canton = "JIMENEZ"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "05":
                canton = "TURRIALBA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "06":
                canton = "ALVARADO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "07":
                canton = "OREAMUNO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "08":
                canton = "EL GUARCO"
        if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Provincia'] == "4":
            provincia = "Heredia"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "01":
                canton = "HEREDIA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "02":
                canton = "BARVA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "03":
                canton = "SANTO DOMINGO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "04":
                canton = "SANTA BARBARA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "05":
                canton = "SAN RAFAEL"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "06":
                canton = "SAN ISIDRO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "07":
                canton = "BELEN"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "08":
                canton = "FLORES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "09":
                canton = "SAN PABLO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "10":
                canton = "SARAPIQUI"
        if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Provincia'] == "5":
            provincia = "Guanacaste"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "01":
                canton = "LIBERIA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "02":
                canton = "NICOYA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "03":
                canton = "SANTA CRUZ"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "04":
                canton = "BAGACES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "05":
                canton = "CARRILLO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "06":
                canton = "CAÑAS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "07":
                canton = "ABANGARES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "08":
                canton = "TILARAN"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "09":
                canton = "NANDAYURE"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "10":
                canton = "LA CRUZ"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "11":
                canton = "HOJANCHA"
        if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Provincia'] == "6":
            provincia = "Puntarenas"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "01":
                canton = "PUNTARENAS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "02":
                canton = "ESPARZA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "03":
                canton = "SANTA CRUZ"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "04":
                canton = "MONTES DE ORO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "05":
                canton = "OSA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "06":
                canton = "AGUIRRE"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "07":
                canton = "GOLFITO"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "08":
                canton = "COTO BRUS"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "09":
                canton = "PARRITA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "10":
                canton = "CORREDORES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "11":
                canton = "GARABITO"
        if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Provincia'] == "7":
            provincia = "Limón"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "01":
                canton = "LIMON"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "02":
                canton = "POCOCI"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "03":
                canton = "SIQUIRRES"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "04":
                canton = "TALAMANCA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "05":
                canton = "MATINA"
            if request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Canton'] == "06":
                canton = "GUACIMO"
        # Validación de las entradas con el identificador de las empresas
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CTPZ":
            empresa_id = 6
            empresa_nombre = "Corporación Académica Tecnológica CR PZ S.A."
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "EHLB":
            empresa_id = 9
            empresa_nombre = "CATEC Libería"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "EHSC":
            empresa_id = 11
            empresa_nombre = "CATEC Santa Cruz"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "GTGF":
            empresa_id = 8
            empresa_nombre = "CATEC Golfito"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "EHNC":
            empresa_id = 10
            empresa_nombre = "CATEC Nicoya"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CTCN":
            empresa_id = 7
            empresa_nombre = "CATEC Ciudad Nelly"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CDECT":
            empresa_id = 13
            empresa_nombre = "CDE Cartago"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CDELB":
            empresa_id = 14
            empresa_nombre = "CDE Liberia"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CDELM":
            empresa_id = 15
            empresa_nombre = "CDE Limón"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CTCG":
            empresa_id = 4
            empresa_nombre = "CATEC Cartago"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CTLM":
            empresa_id = 5
            empresa_nombre = "CATEC Limón"
        # Objeto json para la estructura del proveedor
        new_proveedor = {
            "name": request.json[0]['FacturaCompra']['Emisor']['Nombre'],
            "vat": request.json[0]['FacturaCompra']['Emisor']['Identificacion']['Numero'],
            "city": provincia,
            "street": canton,
            "street2": request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['Distrito'] +
            " " +
            request.json[0]['FacturaCompra']['Emisor']['Ubicacion']['OtrasSenas'],
            "zip": request.json[0]['FacturaCompra']['Emisor']['Telefono']['CodigoPais'],
            "phone": request.json[0]['FacturaCompra']['Emisor']['Telefono']['NumTelefono'],
            "mobile": request.json[0]['FacturaCompra']['Emisor']['Telefono']['NumTelefono'],
            "email": request.json[0]['FacturaCompra']['Emisor']['CorreoElectronico']
        }
        # Validación si el proveedor existe dentro de la base de datos para no sobreescribirlo
        # Hace una comparación de la cédula física o jurídica dentro de la base de datos
        # Si este no existe, crea un nuevo registro, no actualiza los datos
        try:
            if new_proveedor['vat'] != compra.proveedor_existe(new_proveedor)[0]['vat']:
                print("Cliente existe")
        except:
            compra.proveedor(new_proveedor)
        # Captura del ID proveedor en caso de existir ya en la base de datos
        try:
            id = compra.proveedor_existe(new_proveedor)[0]['id']
        except:
            print("Error al capturar ID de proveedor")
        # Objeto json para la estructura de la factura
        new_invoice = {
            'name': request.json[0]['FacturaCompra']['Clave'],
            'date': request.json[0]['FacturaCompra']['FechaEmision'],
            'ref': request.json[0]['FacturaCompra']['CodigoActividad'],
            'narration': request.json[0]['FacturaCompra']['NumeroConsecutivo'],
            'state': "draft",
            'type': "in_invoice",
            'type_name': "Invoice",
            'to_check': 'False',
            'journal_id': [1, "Diario de Ingresos (CRC)"],
            'company_id': int(empresa_id),
            "currency_id": [39, "CRC"],
            "invoice_line_ids": [],
            "partner_id": int(id),
            "extract_state": "no_extract_requested"
        }
        # Crea la factura utilizando la estructura de new_invoice y devuelve el número de factura
        try:
            id_factura = compra.factura(new_invoice)
        except:
            print("Factura no creada")
        # Por cada elemento dentro de items en la estructura json del request, realiza un objeto json
        # identificado como new_product, si este producto existe no es ccreado nuevamente, tampoco se
        # actualiza dentro de la base de datos, sin embargo al crear las líneas dentro de la factura
        # los montos son obtenidos desde la factura de venta. ---------------------------------------
        for item in request.json[0]['FacturaCompra']['Items']:
            # Objeto json para la estructura del producto
            new_product = {
                'name': request.json[0]['FacturaCompra']['Items'][item]['Linea']['Cuenta'],
                'description': request.json[0]['FacturaCompra']['Items'][item]['Linea']['Detalle'],
                'default_code': request.json[0]['FacturaCompra']['Items'][item]['Linea']['CodigoCabys'],
                'list_price': request.json[0]['FacturaCompra']['Items'][item]['Linea']['PrecioUnitario'],
                'lst_price': request.json[0]['FacturaCompra']['Items'][item]['Linea']['PrecioUnitario'],
                'type': request.json[0]['FacturaCompra']['Items'][item]['Linea']['Tipo']
            }
            # Validación si el producto existe dentro de la base de datos para no sobreescribirlo
            # Hace una comparación de los nombres dentro de la base de datos, si este no existe,
            # crea un nuevo registro, no actualiza los datos. -----------------------------------
            try:
                if str(new_product['name']) == str(compra.producto_existe(new_product)[0]['name']):
                    id_producto = compra.producto_existe(new_product)[0]['id']
                    print("Producto Existente ")
                else:
                    print("Error intencional")
            except:
                id_producto = compra.producto(new_product)
                print("Producto no existente")
            # Creación de las líneas dentro de la factura creada anteriormente, identificada con
            # el id_factura, requiere tener un id de la factura y id de producto para que se cree.
            try:
                # Objeto json para la estructura de cada línea asociada a la factura
                # No se debe modificar los valores en cero de estos montos, Odoo calcula
                # automáticamente los montos y totales por cantidad y precio unitario.
                new_line = {
                    'move_id': id_factura,
                    'product_id': id_producto,
                    'quantity': float(request.json[0]['FacturaCompra']['Items'][item]['Linea']['Cantidad']),
                    'price_unit': float(request.json[0]['FacturaCompra']['Items'][item]['Linea']['PrecioUnitario']),
                    'account_id': 19,
                    'tax_ids': [1],
                    'tax_line_id': 1,
                    'name': request.json[0]['FacturaCompra']['Items'][item]['Linea']['Detalle'],
                    'journal_id': 1,
                    'exclude_from_invoice_tab': False,
                    'debit': 0.0,
                    'credit': 0.0,
                    'discount': 0.0,
                    'balance': 0.0,
                    'amount_currency': 0.0,
                    'price_subtotal': 0.0,
                    'price_total': 0.0,
                    'reconciled': False,
                    'blocked': False
                }
                # Inserción de la nueva línea dentro de la factura mediante la función en venta
                compra.linea(new_line)
            except:
                print("No se creó la linea")
        # Factura OK
        return jsonify({"message_test": "FACTURA COMPRA INGRESADA CORRECTAMENTE"})
    except:
        # Factura FAIL
        return jsonify({"message_test": "FALLO AL INGRESAR LA FACTURA DE COMPRA, CAMPOS INCORRECTOS"})

# Ruta para la creación de factura de venta


@app.route('/venta', methods=['POST'])
def ventas():
    try:
        # Variables locales para definir localización
        provincia = ""
        canton = ""
        # Variables locales para definir compañía asociada a la factura
        empresa_id = 0
        empresa_nombre = ""  # Variable para test
        # Validación de las entradas de los datos para la localización
        if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Provincia'] == "1":
            provincia = "San José"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "01":
                canton = "SAN JOSE"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "02":
                canton = "ESCAZU"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "03":
                canton = " DESAMPARADOS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "04":
                canton = "PURISCAL"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "05":
                canton = "TARRAZU"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "06":
                canton = "ASERRI"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "07":
                canton = "MORA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "08":
                canton = "GOICOECHEA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "09":
                canton = "SANTA ANA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "10":
                canton = "ALAJUELITA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "11":
                canton = "CORONADO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "12":
                canton = "ACOSTA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "13":
                canton = "TIBAS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "14":
                canton = "MORAVIA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "15":
                canton = "MONTES DE OCA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "16":
                canton = "TURRUBARES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "17":
                canton = "DOTA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "18":
                canton = "CURRIDABAT"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "19":
                canton = "PEREZ ZELEDON"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "20":
                canton = "LEON CORTES"
        if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Provincia'] == "2":
            provincia = "Alajuela"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "01":
                canton = "ALAJUELA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "02":
                canton = "SAN RAMON"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "03":
                canton = "GRECIA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "04":
                canton = "SAN MATEO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "05":
                canton = "ATENAS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "06":
                canton = "NARANJO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "07":
                canton = "PALMARES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "08":
                canton = "POAS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "09":
                canton = "OROTINA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "10":
                canton = "SAN CARLOS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "11":
                canton = "ALFARO RUIZ"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "12":
                canton = "VALVERDE VEGA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "13":
                canton = "UPALA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "14":
                canton = "LOS CHILES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "15":
                canton = "GUATUSO"
        if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Provincia'] == "3":
            provincia = "Cartago"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "01":
                canton = "CARTAGO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "02":
                canton = "PARAISO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "03":
                canton = "LA UNION"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "04":
                canton = "JIMENEZ"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "05":
                canton = "TURRIALBA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "06":
                canton = "ALVARADO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "07":
                canton = "OREAMUNO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "08":
                canton = "EL GUARCO"
        if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Provincia'] == "4":
            provincia = "Heredia"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "01":
                canton = "HEREDIA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "02":
                canton = "BARVA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "03":
                canton = "SANTO DOMINGO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "04":
                canton = "SANTA BARBARA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "05":
                canton = "SAN RAFAEL"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "06":
                canton = "SAN ISIDRO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "07":
                canton = "BELEN"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "08":
                canton = "FLORES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "09":
                canton = "SAN PABLO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "10":
                canton = "SARAPIQUI"
        if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Provincia'] == "5":
            provincia = "Guanacaste"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "01":
                canton = "LIBERIA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "02":
                canton = "NICOYA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "03":
                canton = "SANTA CRUZ"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "04":
                canton = "BAGACES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "05":
                canton = "CARRILLO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "06":
                canton = "CAÑAS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "07":
                canton = "ABANGARES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "08":
                canton = "TILARAN"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "09":
                canton = "NANDAYURE"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "10":
                canton = "LA CRUZ"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "11":
                canton = "HOJANCHA"
        if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Provincia'] == "6":
            provincia = "Puntarenas"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "01":
                canton = "PUNTARENAS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "02":
                canton = "ESPARZA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "03":
                canton = "SANTA CRUZ"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "04":
                canton = "MONTES DE ORO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "05":
                canton = "OSA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "06":
                canton = "AGUIRRE"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "07":
                canton = "GOLFITO"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "08":
                canton = "COTO BRUS"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "09":
                canton = "PARRITA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "10":
                canton = "CORREDORES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "11":
                canton = "GARABITO"
        if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Provincia'] == "7":
            provincia = "Limón"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "01":
                canton = "LIMON"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "02":
                canton = "POCOCI"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "03":
                canton = "SIQUIRRES"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "04":
                canton = "TALAMANCA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "05":
                canton = "MATINA"
            if request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Canton'] == "06":
                canton = "GUACIMO"
        # Validación de las entradas con el identificador de las empresas
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CTPZ":
            empresa_id = 6
            empresa_nombre = "Corporación Académica Tecnológica CR PZ S.A."
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "EHLB":
            empresa_id = 9
            empresa_nombre = "CATEC Libería"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "EHSC":
            empresa_id = 11
            empresa_nombre = "CATEC Santa Cruz"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "GTGF":
            empresa_id = 8
            empresa_nombre = "CATEC Golfito"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "EHNC":
            empresa_id = 10
            empresa_nombre = "CATEC Nicoya"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CTCN":
            empresa_id = 7
            empresa_nombre = "CATEC Ciudad Nelly"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CDECT":
            empresa_id = 13
            empresa_nombre = "CDE Cartago"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CDELB":
            empresa_id = 14
            empresa_nombre = "CDE Liberia"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CDELM":
            empresa_id = 15
            empresa_nombre = "CDE Limón"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CTCG":
            empresa_id = 4
            empresa_nombre = "CATEC Cartago"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CTLM":
            empresa_id = 5
            empresa_nombre = "CATEC Limón"
        # Objeto json para la estructura del cliente
        new_cliente = {
            "name": request.json[0]['FacturaVenta']['Receptor']['Nombre'],
            "vat": request.json[0]['FacturaVenta']['Receptor']['Identificacion']['Numero'],
            "city": provincia,
            "street": canton,
            "street2": request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['Distrito'] +
            " " +
            request.json[0]['FacturaVenta']['Receptor']['Ubicacion']['OtrasSenas'],
            "zip": request.json[0]['FacturaVenta']['Receptor']['Telefono']['CodigoPais'],
            "phone": request.json[0]['FacturaVenta']['Receptor']['Telefono']['NumTelefono'],
            "mobile": request.json[0]['FacturaVenta']['Receptor']['Telefono']['NumTelefono'],
            "email": request.json[0]['FacturaVenta']['Receptor']['CorreoElectronico']
        }
        # Validación si el cliente existe dentro de la base de datos para no sobreescribirlo
        # Hace una comparación de la cédula física o jurídica dentro de la base de datos
        # Si este no existe, crea un nuevo registro, no actualiza los datos
        try:
            if new_cliente['vat'] != venta.cliente_existe(new_cliente)[0]['vat']:
                print("Cliente existe")
        except:
            venta.cliente(new_cliente)
        # Captura del ID cliente en caso de existir ya en la base de datos
        try:
            id = venta.cliente_existe(new_cliente)[0]['id']
        except:
            print("Error al capturar ID de cliente")
        # Objeto json para la estructura de la factura
        new_invoice = {
            'name': request.json[0]['FacturaVenta']['Clave'],
            'date': request.json[0]['FacturaVenta']['FechaEmision'],
            'ref': request.json[0]['FacturaVenta']['CodigoActividad'],
            'narration': request.json[0]['FacturaVenta']['NumeroConsecutivo'],
            'state': "draft",
            'type': "out_invoice",
            'type_name': "Invoice",
            'to_check': 'False',
            'journal_id': [1, "Diario de Ingresos (CRC)"],
            'company_id': int(empresa_id),
            "currency_id": [39, "CRC"],
            "invoice_line_ids": [],
            "partner_id": int(id),
            "extract_state": "no_extract_requested"
        }
        # Crea la factura utilizando la estructura de new_invoice y devuelve el número de factura
        try:
            id_factura = venta.factura(new_invoice)
        except:
            print("Factura no creada")
        # Por cada elemento dentro de items en la estructura json del request, realiza un objeto json
        # identificado como new_product, si este producto existe no es ccreado nuevamente, tampoco se
        # actualiza dentro de la base de datos, sin embargo al crear las líneas dentro de la factura
        # los montos son obtenidos desde la factura de venta. ---------------------------------------
        for item in request.json[0]['FacturaVenta']['Items']:
            # Objeto json para la estructura del producto
            new_product = {
                'name': request.json[0]['FacturaVenta']['Items'][item]['Linea']['Cuenta'],
                'description': request.json[0]['FacturaVenta']['Items'][item]['Linea']['Detalle'],
                'default_code': request.json[0]['FacturaVenta']['Items'][item]['Linea']['CodigoCabys'],
                'list_price': request.json[0]['FacturaVenta']['Items'][item]['Linea']['PrecioUnitario'],
                'lst_price': request.json[0]['FacturaVenta']['Items'][item]['Linea']['PrecioUnitario'],
                'type': request.json[0]['FacturaVenta']['Items'][item]['Linea']['Tipo']
            }
            # Validación si el producto existe dentro de la base de datos para no sobreescribirlo
            # Hace una comparación de los nombres dentro de la base de datos, si este no existe,
            # crea un nuevo registro, no actualiza los datos. -----------------------------------
            try:
                if str(new_product['name']) == str(venta.producto_existe(new_product)[0]['name']):
                    id_producto = venta.producto_existe(new_product)[0]['id']
                    print("Producto Existente ")
                else:
                    print("Error intencional")
            except:
                id_producto = venta.producto(new_product)
                print("Producto no existente")
            # Creación de las líneas dentro de la factura creada anteriormente, identificada con
            # el id_factura, requiere tener un id de la factura y id de producto para que se cree.
            try:
                # Objeto json para la estructura de cada línea asociada a la factura
                # No se debe modificar los valores en cero de estos montos, Odoo calcula
                # automáticamente los montos y totales por cantidad y precio unitario.
                new_line = {
                    'move_id': id_factura,
                    'product_id': id_producto,
                    'quantity': float(request.json[0]['FacturaVenta']['Items'][item]['Linea']['Cantidad']),
                    'price_unit': float(request.json[0]['FacturaVenta']['Items'][item]['Linea']['PrecioUnitario']),
                    'account_id': 19,
                    'tax_ids': [1],
                    'tax_line_id': 1,
                    'name': request.json[0]['FacturaVenta']['Items'][item]['Linea']['Detalle'],
                    'journal_id': 1,
                    'exclude_from_invoice_tab': False,
                    'debit': 0.0,
                    'credit': 0.0,
                    'discount': 0.0,
                    'balance': 0.0,
                    'amount_currency': 0.0,
                    'price_subtotal': 0.0,
                    'price_total': 0.0,
                    'reconciled': False,
                    'blocked': False
                }
                # Inserción de la nueva línea dentro de la factura mediante la función en venta
                venta.linea(new_line)
            except:
                print("No se creó la linea")
        # Factura OK
        return jsonify({"message_test": "FACTURA INGRESADA CORRECTAMENTE"})
    except:
        # Factura FAIL
        return jsonify({"message_test": "FALLO AL INGRESAR LA FACTURA, CAMPOS INCORRECTOS"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3030)

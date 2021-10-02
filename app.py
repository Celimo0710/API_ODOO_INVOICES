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
import CONTANTES as cons
from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta para la creación de factura de compra


@app.route('/compra', methods=['POST'])
def compras():
    try:
        # Variables locales para definir localización
        provincia = ""
        canton = ""
        journal = 0
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
            journal = 9
            empresa_nombre = "Corporación Académica Tecnológica CR PZ S.A."
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "EHLB":
            empresa_id = 9
            journal = 86
            empresa_nombre = "CATEC Libería"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "EHSC":
            empresa_id = 11
            journal = 100
            empresa_nombre = "CATEC Santa Cruz"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "GTGF":
            empresa_id = 8
            journal = 37
            empresa_nombre = "CATEC Golfito"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "EHNC":
            empresa_id = 10
            journal = 93
            empresa_nombre = "CATEC Nicoya"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CTCN":
            empresa_id = 7
            journal = 30
            empresa_nombre = "CATEC Ciudad Nelly"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CDECT":
            empresa_id = 13
            journal = 58
            empresa_nombre = "CDE Cartago"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CDELB":
            empresa_id = 14
            journal = 65
            empresa_nombre = "CDE Liberia"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CDELM":
            empresa_id = 15
            journal = 72
            empresa_nombre = "CDE Limón"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CTCG":
            empresa_id = 4
            journal = 16
            empresa_nombre = "CATEC Cartago"
        if request.json[0]['FacturaCompra']['Receptor']['Nombre'] == "CTLM":
            empresa_id = 5
            journal = 23
            empresa_nombre = "CATEC Limón"
        # Cambio de empresa del Usuario
        print(compra.usuario(int(empresa_id)))
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
            'name': request.json[0]['FacturaCompra']['ClaveCATEC'],
            'date': request.json[0]['FacturaCompra']['FechaEmision'],
            'ref': request.json[0]['FacturaCompra']['NumeroConsecutivo'],
            'narration': request.json[0]['FacturaCompra']['Clave'],
            'state': "draft",
            'type': "in_invoice",
            'type_name': "Invoice",
            'to_check': 'False',
            'journal_id': journal,
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
                'name': item['Linea']['Detalle'],
                'description': item['Linea']['Detalle'],
                'default_code': item['Linea']['CodigoCabys'],
                'list_price': item['Linea']['PrecioUnitario'],
                'lst_price': item['Linea']['PrecioUnitario'],
                'type': item['Linea']['Tipo']
            }
            #'name': item['Linea']['Detalle'],
            #    'description': item['Linea']['Detalle'],
            #    'default_code': item['Linea']['CodigoCabys'],
            #    'list_price': item['Linea']['PrecioUnitario'],
            #    'lst_price': item['Linea']['PrecioUnitario'],
            #    'type': item['Linea']['Tipo']
            # Validación si el producto existe dentro de la base de datos para no sobreescribirlo
            # Hace una comparación de los nombres dentro de la base de datos, si este no existe,
            # crea un nuevo registro, no actualiza los datos. -----------------------------------
            try:
                if str(new_product['name']) == str(compra.producto_existe(new_product)[0]['name']):
                    id_producto = compra.producto_existe(new_product)[0]['id']
                    compra.producto_update(new_product, id_producto)
                    print("Producto existente y actualizado")
                else:
                    print("Error intencional")
            except:
                id_producto = compra.producto(new_product)
                print("Producto no existente", id_producto)
            # Creación de las líneas dentro de la factura creada anteriormente, identificada con
            # el id_factura, requiere tener un id de la factura y id de producto para que se cree.
            try:
                # Objeto json para la estructura de cada línea asociada a la factura
                # No se debe modificar los valores en cero de estos montos, Odoo calcula
                # automáticamente los montos y totales por cantidad y precio unitario.

                # Declaración de impuestos
                impuesto = 1
                cuenta = 19
                if empresa_id == 6:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC21
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC22
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC24
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC23
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC25
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC26
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE41
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE42
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE43
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE44
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE45
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE46
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE47
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE48
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE49
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE410
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE411
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE412
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE413
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE414
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE415
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE416
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE417
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE418
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE419
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE420
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE421
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE422
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE423
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE424
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE425
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE426
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE427
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE428
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE429
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE430
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE431
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE432
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE433
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE434
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE435
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE436
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE437
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE438
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE439
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE440
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE441
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE442
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE443
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE444
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE445
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE446
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE447
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE448
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE449
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE450
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE451
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE452
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE453
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE454
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE455
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE456
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE457
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE458
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE459
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE460
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE461
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE462
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE471
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE472
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE473
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE474
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE475
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE476
                if empresa_id == 9:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC91
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC92
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC94
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC93
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC95
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC96
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE121
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE122
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE123
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE124
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE125
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE126
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE127
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE128
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE129
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE1210
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE1211
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE1212
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE1213
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE1214
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE1215
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE1216
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE1217
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE1218
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE1219
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE1220
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE1221
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE1222
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE1223
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE1224
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE1225
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE1226
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE1227
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE1228
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE1229
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE1230
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE1231
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE1232
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE1233
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE1234
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE1235
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE1236
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE1237
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE1238
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE1239
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE1240
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE1241
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE1242
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE1243
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE1244
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE1245
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE1246
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE1247
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE1248
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE1249
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE1250
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE1251
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE1252
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE1253
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE1254
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE1255
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE1256
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE1257
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE1258
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE1259
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE1260
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE1261
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE1262
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE1271
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE1272
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE1273
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE1274
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE1275
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE1276
                if empresa_id == 11:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC1101
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC1102
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC1104
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC1103
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC1105
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC1106
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE141
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE142
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE143
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE144
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE145
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE146
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE147
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE148
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE149
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE1410
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE1411
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE1412
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE1413
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE1414
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE1415
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE1416
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE1417
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE1418
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE1419
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE1420
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE1421
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE1422
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE1423
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE1424
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE1425
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE1426
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE1427
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE1428
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE1429
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE1430
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE1431
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE1432
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE1433
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE1434
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE1435
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE1436
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE1437
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE1438
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE1439
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE1440
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE1441
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE1442
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE1443
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE1444
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE1445
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE1446
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE1447
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE1448
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE1449
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE1450
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE1451
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE1452
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE1453
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE1454
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE1455
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE1456
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE1457
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE1458
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE1459
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE1460
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE1461
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE1462
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE1471
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE1472
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE1473
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE1474
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE1475
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE1476
                if empresa_id == 8:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC51
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC52
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC54
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC53
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC55
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC56
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE71
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE72
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE73
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE74
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE75
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE76
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE77
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE78
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE79
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE710
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE711
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE712
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE713
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE714
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE715
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE716
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE717
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE718
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE719
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE720
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE721
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE722
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE723
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE724
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE725
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE726
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE727
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE728
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE729
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE730
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE731
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE732
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE733
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE734
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE735
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE736
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE737
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE738
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE739
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE740
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE741
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE742
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE743
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE744
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE745
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE746
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE747
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE748
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE749
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE750
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE751
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE752
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE753
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE754
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE755
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE756
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE757
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE758
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE759
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE760
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE761
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE762
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE771
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE772
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE773
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE774
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE775
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE776
                if empresa_id == 10:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC101
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC102
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC104
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC103
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC105
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC106
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE131
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE132
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE133
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE134
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE135
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE136
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE137
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE138
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE139
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE1310
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE1311
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE1312
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE1313
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE1314
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE1315
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE1316
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE1317
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE1318
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE1319
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE1320
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE1321
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE1322
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE1323
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE1324
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE1325
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE1326
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE1327
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE1328
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE1329
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE1330
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE1331
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE1332
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE1333
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE1334
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE1335
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE1336
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE1337
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE1338
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE1339
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE1340
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE1341
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE1342
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE1343
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE1344
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE1345
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE1346
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE1347
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE1348
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE1349
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE1350
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE1351
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE1352
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE1353
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE1354
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE1355
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE1356
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE1357
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE1358
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE1359
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE1360
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE1361
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE1362
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE1371
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE1372
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE1373
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE1374
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE1375
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE1376
                if empresa_id == 7:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC41
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC42
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC44
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC43
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC45
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC46
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE61
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE62
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE63
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE64
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE65
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE66
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE67
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE68
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE69
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE610
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE611
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE612
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE613
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE614
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE615
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE616
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE617
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE618
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE619
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE620
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE621
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE622
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE623
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE624
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE625
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE626
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE627
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE628
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE629
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE630
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE631
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE632
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE633
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE634
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE635
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE636
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE637
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE638
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE639
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE640
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE641
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE642
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE643
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE644
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE645
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE646
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE647
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE648
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE649
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE650
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE651
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE652
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE653
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE654
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE655
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE656
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE657
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE658
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE659
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE660
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE661
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE662
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE671
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE672
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE673
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE674
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE675
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE676
                if empresa_id == 13:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC61
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC62
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC64
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC63
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC65
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC66
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE91
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE92
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE93
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE94
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE95
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE96
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE97
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE98
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE99
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE910
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE911
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE912
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE913
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE914
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE915
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE916
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE917
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE918
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE919
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE920
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE921
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE922
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE923
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE924
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE925
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE926
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE927
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE928
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE929
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE930
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE931
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE932
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE933
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE934
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE935
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE936
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE937
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE938
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE939
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE940
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE941
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE942
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE943
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE944
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE945
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE946
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE947
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE948
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE949
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE950
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE951
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE952
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE953
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE954
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE955
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE956
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE957
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE958
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE959
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE960
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE961
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE962
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE971
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE972
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE973
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE974
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE975
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE976
                if empresa_id == 14:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC71
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC72
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC74
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC73
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC75
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC76
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE101
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE102
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE103
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE104
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE105
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE106
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE107
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE108
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE109
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE1010
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE1011
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE1012
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE1013
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE1014
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE1015
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE1016
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE1017
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE1018
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE1019
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE1020
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE1021
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE1022
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE1023
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE1024
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE1025
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE1026
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE1027
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE1028
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE1029
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE1030
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE1031
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE1032
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE1033
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE1034
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE1035
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE1036
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE1037
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE1038
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE1039
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE1040
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE1041
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE1042
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE1043
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE1044
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE1045
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE1046
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE1047
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE1048
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE1049
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE1050
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE1051
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE1052
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE1053
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE1054
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE1055
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE1056
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE1057
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE1058
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE1059
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE1060
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE1061
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE1062
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE1071
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE1072
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE1073
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE1074
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE1075
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE1076
                if empresa_id == 15:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC81
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC82
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC84
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC83
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC85
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC86
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE111
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE112
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE113
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE114
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE115
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE116
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE117
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE118
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE119
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE1110
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE1111
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE1112
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE1113
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE1114
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE1115
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE1116
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE1117
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE1118
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE1119
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE1120
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE1121
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE1122
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE1123
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE1124
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE1125
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE1126
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE1127
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE1128
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE1129
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE1130
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE1131
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE1132
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE1133
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE1134
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE1135
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE1136
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE1137
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE1138
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE1139
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE1140
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE1141
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE1142
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE1143
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE1144
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE1145
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE1146
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE1147
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE1148
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE1149
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE1150
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE1151
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE1152
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE1153
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE1154
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE1155
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE1156
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE1157
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE1158
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE1159
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE1160
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE1161
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE1162
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE1171
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE1172
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE1173
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE1174
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE1175
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE1176
                if empresa_id == 4:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC11
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC12
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC14
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC13
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC15
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC16
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE31
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE32
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE33
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE34
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE35
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE36
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE37
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE38
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE39
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE310
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE311
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE312
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE313
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE314
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE315
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE316
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE317
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE318
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE319
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE320
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE321
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE322
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE323
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE324
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE325
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE326
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE327
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE328
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE329
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE330
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE331
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE332
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE333
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE334
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE335
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE336
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE337
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE338
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE339
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE340
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE341
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE342
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE343
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE344
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE345
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE346
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE347
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE348
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE349
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE350
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE351
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE352
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE353
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE354
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE355
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE356
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE357
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE358
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE359
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE360
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE361
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE362
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE371
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE372
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE373
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE374
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE375
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE376
                if empresa_id == 5:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPC31
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPC32
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        impuesto = cons.IMPC34
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '02':
                        impuesto = cons.IMPC33
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        impuesto = cons.IMPC35
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '04':
                        impuesto = cons.IMPC36
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "1":
                        cuenta = cons.PCE51
                    if item['Linea']['Cuenta'] == "2":
                        cuenta = cons.PCE52
                    if item['Linea']['Cuenta'] == "3":
                        cuenta = cons.PCE53
                    if item['Linea']['Cuenta'] == "4":
                        cuenta = cons.PCE54
                    if item['Linea']['Cuenta'] == "5":
                        cuenta = cons.PCE55
                    if item['Linea']['Cuenta'] == "6":
                        cuenta = cons.PCE56
                    if item['Linea']['Cuenta'] == "7":
                        cuenta = cons.PCE57
                    if item['Linea']['Cuenta'] == "8":
                        cuenta = cons.PCE58
                    if item['Linea']['Cuenta'] == "9":
                        cuenta = cons.PCE59
                    if item['Linea']['Cuenta'] == "10":
                        cuenta = cons.PCE510
                    if item['Linea']['Cuenta'] == "11":
                        cuenta = cons.PCE511
                    if item['Linea']['Cuenta'] == "12":
                        cuenta = cons.PCE512
                    if item['Linea']['Cuenta'] == "13":
                        cuenta = cons.PCE513
                    if item['Linea']['Cuenta'] == "14":
                        cuenta = cons.PCE514
                    if item['Linea']['Cuenta'] == "15":
                        cuenta = cons.PCE515
                    if item['Linea']['Cuenta'] == "16":
                        cuenta = cons.PCE516
                    if item['Linea']['Cuenta'] == "17":
                        cuenta = cons.PCE517
                    if item['Linea']['Cuenta'] == "18":
                        cuenta = cons.PCE518
                    if item['Linea']['Cuenta'] == "19":
                        cuenta = cons.PCE519
                    if item['Linea']['Cuenta'] == "20":
                        cuenta = cons.PCE520
                    if item['Linea']['Cuenta'] == "21":
                        cuenta = cons.PCE521
                    if item['Linea']['Cuenta'] == "22":
                        cuenta = cons.PCE522
                    if item['Linea']['Cuenta'] == "23":
                        cuenta = cons.PCE523
                    if item['Linea']['Cuenta'] == "24":
                        cuenta = cons.PCE524
                    if item['Linea']['Cuenta'] == "25":
                        cuenta = cons.PCE525
                    if item['Linea']['Cuenta'] == "26":
                        cuenta = cons.PCE526
                    if item['Linea']['Cuenta'] == "27":
                        cuenta = cons.PCE527
                    if item['Linea']['Cuenta'] == "28":
                        cuenta = cons.PCE528
                    if item['Linea']['Cuenta'] == "29":
                        cuenta = cons.PCE529
                    if item['Linea']['Cuenta'] == "30":
                        cuenta = cons.PCE530
                    if item['Linea']['Cuenta'] == "31":
                        cuenta = cons.PCE531
                    if item['Linea']['Cuenta'] == "32":
                        cuenta = cons.PCE532
                    if item['Linea']['Cuenta'] == "33":
                        cuenta = cons.PCE533
                    if item['Linea']['Cuenta'] == "34":
                        cuenta = cons.PCE534
                    if item['Linea']['Cuenta'] == "35":
                        cuenta = cons.PCE535
                    if item['Linea']['Cuenta'] == "36":
                        cuenta = cons.PCE536
                    if item['Linea']['Cuenta'] == "37":
                        cuenta = cons.PCE537
                    if item['Linea']['Cuenta'] == "38":
                        cuenta = cons.PCE538
                    if item['Linea']['Cuenta'] == "39":
                        cuenta = cons.PCE539
                    if item['Linea']['Cuenta'] == "40":
                        cuenta = cons.PCE540
                    if item['Linea']['Cuenta'] == "41":
                        cuenta = cons.PCE541
                    if item['Linea']['Cuenta'] == "42":
                        cuenta = cons.PCE542
                    if item['Linea']['Cuenta'] == "43":
                        cuenta = cons.PCE543
                    if item['Linea']['Cuenta'] == "44":
                        cuenta = cons.PCE544
                    if item['Linea']['Cuenta'] == "45":
                        cuenta = cons.PCE545
                    if item['Linea']['Cuenta'] == "46":
                        cuenta = cons.PCE546
                    if item['Linea']['Cuenta'] == "47":
                        cuenta = cons.PCE547
                    if item['Linea']['Cuenta'] == "48":
                        cuenta = cons.PCE548
                    if item['Linea']['Cuenta'] == "49":
                        cuenta = cons.PCE549
                    if item['Linea']['Cuenta'] == "50":
                        cuenta = cons.PCE550
                    if item['Linea']['Cuenta'] == "51":
                        cuenta = cons.PCE551
                    if item['Linea']['Cuenta'] == "52":
                        cuenta = cons.PCE552
                    if item['Linea']['Cuenta'] == "53":
                        cuenta = cons.PCE553
                    if item['Linea']['Cuenta'] == "54":
                        cuenta = cons.PCE554
                    if item['Linea']['Cuenta'] == "55":
                        cuenta = cons.PCE555
                    if item['Linea']['Cuenta'] == "56":
                        cuenta = cons.PCE556
                    if item['Linea']['Cuenta'] == "57":
                        cuenta = cons.PCE557
                    if item['Linea']['Cuenta'] == "58":
                        cuenta = cons.PCE558
                    if item['Linea']['Cuenta'] == "59":
                        cuenta = cons.PCE559
                    if item['Linea']['Cuenta'] == "60":
                        cuenta = cons.PCE560
                    if item['Linea']['Cuenta'] == "61":
                        cuenta = cons.PCE561
                    if item['Linea']['Cuenta'] == "62":
                        cuenta = cons.PCE562
                    if item['Linea']['Cuenta'] == "63":
                        cuenta = cons.PCE571
                    if item['Linea']['Cuenta'] == "64":
                        cuenta = cons.PCE572
                    if item['Linea']['Cuenta'] == "65":
                        cuenta = cons.PCE573
                    if item['Linea']['Cuenta'] == "66":
                        cuenta = cons.PCE574
                    if item['Linea']['Cuenta'] == "67":
                        cuenta = cons.PCE575
                    if item['Linea']['Cuenta'] == "68":
                        cuenta = cons.PCE576
                new_line = {
                    'move_id': id_factura,
                    'product_id': id_producto,
                    'quantity': float(item['Linea']['Cantidad']),
                    'price_unit': float(item['Linea']['PrecioUnitario']),
                    'account_id': int(cuenta),  # Apunte Contable, se debe colocar depende de la empresa
                    'tax_ids': int(impuesto),
                    'tax_line_id': int(impuesto),
                    'name': item['Linea']['Detalle'],
                    'journal_id': journal,
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
        journal = 0
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
            journal = 8
            empresa_nombre = "Corporación Académica Tecnológica CR PZ S.A."
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "EHLB":
            empresa_id = 9
            journal = 85
            empresa_nombre = "CATEC Libería"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "EHSC":
            empresa_id = 11
            journal = 99
            empresa_nombre = "CATEC Santa Cruz"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "GTGF":
            empresa_id = 8
            journal = 36
            empresa_nombre = "CATEC Golfito"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "EHNC":
            empresa_id = 10
            journal = 92
            empresa_nombre = "CATEC Nicoya"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CTCN":
            empresa_id = 7
            journal = 29
            empresa_nombre = "CATEC Ciudad Nelly"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CDECT":
            empresa_id = 13
            journal = 57
            empresa_nombre = "CDE Cartago"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CDELB":
            empresa_id = 14
            journal = 64
            empresa_nombre = "CDE Liberia"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CDELM":
            empresa_id = 15
            journal = 71
            empresa_nombre = "CDE Limón"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CTCG":
            empresa_id = 4
            journal = 15
            empresa_nombre = "CATEC Cartago"
        if request.json[0]['FacturaVenta']['Emisor']['Nombre'] == "CTLM":
            empresa_id = 5
            journal = 22
            empresa_nombre = "CATEC Limón"
        # Objeto json para la estructura del cliente
        print(venta.usuario(int(empresa_id)))
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
            'name': request.json[0]['FacturaVenta']['ClaveCATEC'],
            'date': request.json[0]['FacturaVenta']['FechaEmision'],
            'ref': request.json[0]['FacturaVenta']['NumeroConsecutivo'],
            'narration': request.json[0]['FacturaVenta']['Clave'],
            'state': "draft",
            'type': "out_invoice",
            'type_name': "Invoice",
            'to_check': 'False',
            'journal_id': journal,
            'company_id': int(empresa_id),
            "currency_id": [39, "CRC"],
            #"invoice_line_ids": [],
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
                'name': item['Linea']['Cuenta'],
                'description': item['Linea']['Detalle'],
                'default_code': item['Linea']['CodigoCabys'],
                'list_price': item['Linea']['PrecioUnitario'],
                'lst_price': item['Linea']['PrecioUnitario'],
                'type': item['Linea']['Tipo']
            }
            # Validación si el producto existe dentro de la base de datos para no sobreescribirlo
            # Hace una comparación de los nombres dentro de la base de datos, si este no existe,
            # crea un nuevo registro, no actualiza los datos. -----------------------------------
            #'name': item['Linea']['Cuenta'],
            #    'description': item['Linea']['Detalle'],
            #    'default_code': item['Linea']['CodigoCabys'],
            #    'list_price': item['Linea']['PrecioUnitario'],
            #    'lst_price': item['Linea']['PrecioUnitario'],
            #    'type': item['Linea']['Tipo']
            try:
                if str(new_product['name']) == str(venta.producto_existe(new_product)[0]['name']):
                    id_producto = venta.producto_existe(new_product)[0]['id']
                    venta.producto_update(new_product, id_producto)
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
                # Declaración de impuestos
                impuesto = 1
                cuentaventa = 19
                if empresa_id == 6:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV21
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV22
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV25
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV26
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV23
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV24
                    # Cuenta Contable
                    if item['Linea']['Cuenta'] == "4.1.01":
                        cuentaventa = cons.PCI41
                    if item['Linea']['Cuenta'] == "4.1.02":
                        cuentaventa = cons.PCI42
                    if item['Linea']['Cuenta'] == "4.2.01":
                        cuentaventa = cons.PCI43
                    if item['Linea']['Cuenta'] == "4.2.02":
                        cuentaventa = cons.PCI44
                    if item['Linea']['Cuenta'] == "4.2.03":
                        cuentaventa = cons.PCI45
                    if item['Linea']['Cuenta'] == "4.3.01":
                        cuentaventa = cons.PCI46
                    if item['Linea']['Cuenta'] == "4.5.01":
                        cuentaventa = cons.PCI47
                    if item['Linea']['Cuenta'] == "4.5.02":
                        cuentaventa = cons.PCI48
                    if item['Linea']['Cuenta'] == "4.5.03":
                        cuentaventa = cons.PCI49
                    if item['Linea']['Cuenta'] == "4.7.01":
                        cuentaventa = cons.PCI410
                    if item['Linea']['Cuenta'] == "4.7.02":
                        cuentaventa = cons.PCI411
                    if item['Linea']['Cuenta'] == "4.9.01":
                        cuentaventa = cons.PCI412
                if empresa_id == 9:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV91
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV92
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV95
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV96
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV93
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV94
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI121
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI122
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI123
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI124
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI125
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI126
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI127
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI128
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI129
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI1210
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI1211
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI1212
                if empresa_id == 11:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV1101
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV1102
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV1105
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV1106
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV1103
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV1104
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI121
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI122
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI123
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI124
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI125
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI126
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI127
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI128
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI129
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI1210
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI1211
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI1212
                if empresa_id == 8:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV51
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV52
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV55
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV56
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV53
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV54
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI141
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI142
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI143
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI144
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI145
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI146
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI147
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI148
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI149
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI1410
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI1411
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI1412
                if empresa_id == 10:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV101
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV102
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV105
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV106
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV103
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV104
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI131
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI132
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI133
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI134
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI135
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI136
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI137
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI138
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI139
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI1310
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI1311
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI1312
                if empresa_id == 7:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV41
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV42
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV45
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV46
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV43
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV44
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI61
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI62
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI63
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI64
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI65
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI66
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI67
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI68
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI69
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI610
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI611
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI612
                if empresa_id == 13:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV61
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV62
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV65
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV66
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV63
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV64
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI91
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI92
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI93
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI94
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI95
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI96
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI97
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI98
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI99
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI910
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI911
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI912
                if empresa_id == 14:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV71
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV72
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV75
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV76
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV73
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV74
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI101
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI102
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI103
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI104
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI105
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI106
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI107
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI108
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI109
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI1010
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI1011
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI1012
                if empresa_id == 15:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV81
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV82
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV85
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV86
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV83
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV84
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI111
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI112
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI113
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI114
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI115
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI116
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI117
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI118
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI119
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI1110
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI1111
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI1112
                if empresa_id == 4:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV11
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV12
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV15
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV16
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV13
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV14
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI31
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI32
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI33
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI34
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI35
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI36
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI37
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI38
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI39
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI310
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI311
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI312
                if empresa_id == 5:
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '08':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV31
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV32
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '01':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV35
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV36
                    if item['Linea']['Impuesto']['CodigoTarifa'] == '03':
                        if item['Linea']['Tipo'] == 'consu':
                            impuesto = cons.IMPV33
                        if item['Linea']['Tipo'] == 'service':
                            impuesto = cons.IMPV34
                    if item['Linea']['Cuenta'] == "1":
                        cuentaventa = cons.PCI51
                    if item['Linea']['Cuenta'] == "2":
                        cuentaventa = cons.PCI52
                    if item['Linea']['Cuenta'] == "3":
                        cuentaventa = cons.PCI53
                    if item['Linea']['Cuenta'] == "4":
                        cuentaventa = cons.PCI54
                    if item['Linea']['Cuenta'] == "5":
                        cuentaventa = cons.PCI55
                    if item['Linea']['Cuenta'] == "6":
                        cuentaventa = cons.PCI56
                    if item['Linea']['Cuenta'] == "7":
                        cuentaventa = cons.PCI57
                    if item['Linea']['Cuenta'] == "8":
                        cuentaventa = cons.PCI58
                    if item['Linea']['Cuenta'] == "9":
                        cuentaventa = cons.PCI59
                    if item['Linea']['Cuenta'] == "10":
                        cuentaventa = cons.PCI510
                    if item['Linea']['Cuenta'] == "11":
                        cuentaventa = cons.PCI511
                    if item['Linea']['Cuenta'] == "12":
                        cuentaventa = cons.PCI512
                new_line = {
                    'move_id': id_factura,
                    'product_id': id_producto,
                    'quantity': float(item['Linea']['Cantidad']),
                    'price_unit': float(item['Linea']['PrecioUnitario']),
                    'account_id': cuentaventa,
                    'tax_ids': impuesto,
                    'tax_line_id': impuesto,
                    'name': item['Linea']['Detalle'],
                    'journal_id': journal,
                    'exclude_from_invoice_tab': True,
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
                print(venta.linea(new_line))
            except:
                print("No se creó la linea")
        # Factura OK
        return jsonify({"message_test": "FACTURA INGRESADA CORRECTAMENTE"})
    except:
        # Factura FAIL
        return jsonify({"message_test": "FALLO AL INGRESAR LA FACTURA, CAMPOS INCORRECTOS"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3030)

# Factura de compra: bill.py
# Autor: Célimo Ureña Araya

# Funciones para el manejo de datos dentro de las tablas:
#
#   -account.move
#   -account.move.line
#   -res.partner
#   -product.template
#
# Documentación del API ODOO 13:
# https://www.odoo.com/documentation/13.0/developer/misc/api/odoo.html

# Importación de librerías
import ssl
import xmlrpc.client
from flask import jsonify
# URL del servidor
url = "https://desarrollossiacooprl-catec-test-3215387.dev.odoo.com"
# Nombre de la base de datos
# esta sería la base de datos que se muestra en el shell
db = 'desarrollossiacooprl-catec-test-3215387'
# Credenciales de acceso que crea los registros
username = 'desarrollo@siacooprl.com'
password = 'desarrollador'
# Autenticación al servidor
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(
    url), verbose=False, use_datetime=True, context=ssl._create_unverified_context())
version = common.version()
print("version...", version)
# Autenticación del usuario al servidor y conexión a la base de datos
uid = common.authenticate(db, username, password, {})
print("UID...", uid)
# Autenticación al servidor, se utiliza para los modelos de los datos en las consultas
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(
    url), verbose=False, use_datetime=True, context=ssl._create_unverified_context())

# ---Funciones---
# Función para determinar si existe o no un proveedor, devuelve un ID si se encuentra


def proveedor_existe(proveedor):
    try:
        client_read = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [
                                        [['vat', '=', proveedor['vat']]]], {'fields': ['vat', 'id'], 'limit': 1})
        return client_read
    except:
        return False
# Función para crear un proveedor, devuelve un ID del nuevo proveedor


def proveedor(proveedor):
    try:
        nombre = proveedor['name']
        cedula = proveedor['vat']
        ciudad = proveedor['city']
        calle = proveedor['street']
        calle2 = proveedor['street2']
        zip = proveedor['zip']
        telefono = proveedor['phone']
        celular = proveedor['mobile']
        correo = proveedor['email']
        new_partner = models.execute_kw(db, uid, password, 'res.partner', 'create', [
                                        {'name': nombre, 'vat': cedula, 'city': ciudad, 'street': calle, 'street2': calle2, 'zip': zip, 'phone': telefono, 'mobile': celular, 'email': correo}])
        print("proveedor creado...", new_partner)
        return ("proveedor creado...", jsonify(new_partner))
    except:
        return ("proveedor no fue creado...")
# Función para determinar si existe o no un producto, devuelve un ID si se encuentra


def producto_existe(producto):
    try:
        product_read = models.execute_kw(db, uid, password, 'product.template', 'search_read', [
                                         [['name', '=', producto['name']]]], {'fields': ['name', 'id'], 'limit': 1})
        return product_read
    except:
        return False
# Función para crear un producto, devuelve un ID del nuevo producto


def producto(producto):
    try:
        name = producto['name']
        description = producto['description']
        default_code = producto['default_code']
        list_price = producto['list_price']
        lst_price = producto['lst_price']
        type = producto['type']
        new_product = models.execute_kw(db, uid, password, 'product.template', 'create', [
                                        {'name': name, 'description': description, 'default_code': default_code, 'list_price': list_price, 'lst_price': lst_price, 'type': type}])
        print("Producto creado...", new_product)
        return (new_product)
    except:
        return ("Producto no fue creado...")
# Función para crear una factura, devuelve un ID de la nueva factura


def factura(factura):
    try:
        name = factura['name']
        date = factura['date']
        ref = factura['ref']
        narration = factura['narration']
        state = factura['state']  # draft, posted, cancel
        # entry, out_invoice, out_refund, in_invoice, in_refound, out_receipt, in_receipt
        type = factura['type']
        type_name = factura['type_name']
        to_check = factura['to_check']
        company_id = factura['company_id']  # res.company
        invoice_line_ids = factura['invoice_line_ids']  # account.move.line
        partner_id = factura['partner_id']  # res.partner
        # no_extract_requested, not_enough_credit, waiting_extraction, error_status, extract_not_ready, waiting_validation, done
        extract_state = factura['extract_state']
        new_invoice = models.execute_kw(db, uid, password, 'account.move', 'create', [{'name': name, 'date': date, 'invoice_date': date, 'ref': ref, 'narration': narration, 'state': state, 'type': type, 'type_name': type_name, 'to_check': to_check, 'company_id': company_id,
                                        "partner_id": partner_id, 'invoice_line_ids': invoice_line_ids, 'commercial_partner_id': partner_id, 'partner_shipping_id': partner_id, 'partner_shipping_id': partner_id, 'invoice_partner_display_name': partner_id, "extract_state": extract_state, }])
        print("Factura creada...", new_invoice)
        return (new_invoice)
    except:
        return ("Factura no fue creada...")
# Función para crear una línea dentro de una factura, devuelve un ID de la línea creada


def linea(producto):
    try:
        move_id = producto['move_id']
        product_id = producto['product_id']
        quantity = producto['quantity']
        price_unit = producto['price_unit']
        account_id = producto['account_id']
        tax_ids = producto['tax_ids']
        tax_line_id = producto['tax_line_id']
        name = producto['name']
        journal_id = producto['journal_id']
        exclude_from_invoice_tab = producto['exclude_from_invoice_tab']
        debit = producto['debit']
        credit = producto['credit']
        discount = producto['discount']
        balance = producto['balance']
        amount_currency = producto['amount_currency']
        price_subtotal = producto['price_subtotal']
        price_total = producto['price_total']
        reconciled = producto['reconciled']
        blocked = producto['blocked']
        new_line = models.execute_kw(db, uid, password, 'account.move.line', 'create', [{'move_id': move_id, 'product_id': product_id, 'quantity': quantity, 'price_unit': price_unit, 'account_id': account_id, 'tax_ids': tax_ids, 'tax_line_id': tax_line_id, 'name': name, 'journal_id': journal_id,
                                     'exclude_from_invoice_tab': exclude_from_invoice_tab, 'debit': debit, 'credit': credit, 'discount': discount, 'balance': balance, 'amount_currency': amount_currency, 'price_subtotal': price_subtotal, 'price_total': price_total, 'reconciled': reconciled, 'blocked': blocked}])
        print("linea creada...", new_line)
        return (new_line)
    except:
        return ("Línea no fue creada...")

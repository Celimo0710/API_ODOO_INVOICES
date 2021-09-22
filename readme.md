Nombre del proyecto: API_ODOO_INVOICES

API para la integración hacia el módulo de contabilidad en Odoo, el cual recibe una estructura 
en formato JSON e inserta los datos del objeto en la base de datos de Odoo, usando el API integrado
para aplicaciones externas

Links para el envío de estructuras JSON:
server:3030/compra
server:3030/venta

3.142.74.138:3030/compra
3.142.74.138:3030/venta

Este servidor trabaja bajo un ambiente de pruebas, por lo que se requiere instalar las siguientes
dependencias para su correcta ejecución:
-Python 3.9
-Pip
-Flask (instalar desde la terminal con el comando pip install flask)

Para su ejecución desde una terminal con ubicación en la carpeta del archivo app.py, ejecutarlo.

Documentación de ayuda:
https://www.odoo.com/documentation/13.0/developer/misc/api/odoo.html

Notas:
13/09/2021 CU: Aún no auntentica con el APIKEY
13/09/2021 CU: Productos y gastos se registran mediante la inserción de los productos en el JSON

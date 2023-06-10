from xmlrpc import client
import ssl

url = 'https://miurl.odoo.com'
db = 'mibasedatos'
username = 'user@correo.com'
password = 'tupassword'

gcontext = ssl._create_unverified_context()

common = client.ServerProxy("{}/xmlrpc/2/common".format(url),context=gcontext,use_datetime=True)
print(common.version())

uid = common.authenticate(db, username, password,{})
print(uid)

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Nombre del modelo del que deseas obtener los campos
modelo = 'res.company'

# Obtener los campos del modelo
fields = models.execute_kw(db, uid, password, modelo, 'fields_get', [], {'attributes': ['string', 'type']})

# Imprimir los campos ordenadamente
for campo, atributos in fields.items():
    nombre_campo = atributos['string']
    tipo_campo = atributos['type']
    print(f'Campo: {campo}\nNombre: {nombre_campo}\nTipo: {tipo_campo}\n{"-" * 20}')

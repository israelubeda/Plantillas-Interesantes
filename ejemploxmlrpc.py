
from xmlrpc import client
import ssl


url = 'https://aquivalaurl.dev.odoo.com'
db = 'acopen-rut2-6050630'
username = 'admin@acomin.cl'
password = 'pass de api'

gcontext = ssl._create_unverified_context()

common = client.ServerProxy("{}/xmlrpc/2/common".format(url),context=gcontext,use_datetime=True)
print(common.version())

uid = common.authenticate(db, username, password,{})
print(uid)

sock = client.ServerProxy('https://aquivalaurl.dev.odoo.com:8069/xmlrpc/2/object',context=gcontext)
print(sock)


models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
algo = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})

#bbuscamos odoolandia
country = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
country_ids = country.execute_kw(db, uid, password, 'res.country', 'search', [[['name', '=', 'Odoolandia']]],{'offset':10,'limit':5})
if country_ids:
    print('Existe Odoolandia')
else:
    print('No existe Odoolandia')

from suds.client import Client
from xml.dom import minidom

def autenticar():
    #Get xml
    xml= minidom.parse('envelope.xml')
    created=xml.getElementsByTagName("u:Created")[0]
    url='https://cfdidescargamasivasolicitud.clouda.sat.gob.mx/Autenticacion/Autenticacion.svc?wsdl'
    client=Client(url)
    print(client)



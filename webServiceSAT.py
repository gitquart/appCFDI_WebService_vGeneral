from suds.client import Client

url='https://cfdidescargamasivasolicitud.clouda.sat.gob.mx/Autenticacion/Autenticacion.svc?wsdl'
client=Client(url)
print(client)



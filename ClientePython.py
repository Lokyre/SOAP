from zeep import Client
clienteJava = Client("http://localhost:45655/Service1.svc?wsdl")
# Llamar a la función de Java llamada login
resultado = clienteJava.service.Login("Yomi", "111212")

if resultado is True:
    # Aquí puedes acceder a las propiedades del objeto UserInfo si es necesario
    # Otros campos de UserInfo
    print(f'Credenciales correctas para el usuario')
else:
    print('Credenciales incorrectas')

    



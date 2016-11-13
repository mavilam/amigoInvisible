# Amigo Invisible

## Versión 0.1

### Descripción

  Script simple que dado un fichero de entrada con una lista con los correos de los participantes y un mensaje, realizará el sorteo del amigo invisible y enviará un correo a cada participante con el nombre de la persona a la que tendrá que regalar.

### Instrucciones para ejecutarlo

* Configurar dirección de correo con el que van a ser enviado los correos a los participantes. Se configura en las siguientes líneas, cambiando el correo y la contraseña:
```python
username = 'mailtouse@blah.com'
password = 'psw'
```
* El fichero de entrada con los los participantes se estructura con *Nombre:correo* :
```
Pedro:pedro@blah.com
Antonio:antonio@blah.com
Marta:mrt@blah.com
Sara:sara@blah.com
```
* El fichero de entrada con el mensaje llevará la etiqueta *[namefrom]* donde se quiera poner el nombre de la persona a la que le llegará el correo y *[nameto]* donde se quiera poner el nombre de la persona a la que se tiene que regalar:
  ```
  Hola [namefrom] !

  Te ha tocado [nameto]
  ```
* El script se ejecutaría:
```bash
amigo.py [ruta de la lista de contactos] [ruta del mensaje]
```

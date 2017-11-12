# [ESPAÑOL] Amigo Invisible

## Versión 0.1

### Descripción

  Script simple que dado un fichero de entrada con una lista con los correos de los participantes y un mensaje, realizará el sorteo del amigo invisible y enviará un correo a cada participante con el nombre de la persona a la que tendrá que regalar.

### Instrucciones para ejecutarlo

* Configurar dirección de correo con el que van a ser enviado los correos a los participantes. Se configura en las siguientes líneas, cambiando el correo y la contraseña:
	```python
	username = 'mailtouse@blah.com'
	password = 'psw'
	```
	Además hay que activar la opción de gmail "Permitir que las aplicaciones menos seguras accedan a tu cuenta"
	En esta versión solo se pueden enviar los correos desde una dirección de gmail. Las direcciones de los participantes pueden ser de cualquier servidor.
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

# [ENGLISH] Secret Santa

## 0.1 Version

### Description

Basic script that will make the secret santa draw. Given two files by input, one with the list of the people and their mail direcction and another one with a message that will be sent to the participants. The script will send an email to every participant with the name of the person who has to give the present.

### How to execute

* Configurate the email direction that will send all the mails to the participants. The lines to be changed are the following:
    ```python
    username = 'mailtouse@blah.com'
    password = 'psw'
    ```
    In addition it's necessary enable the gmail option "Allowing less secure apps to access your account"
    This version only allow to use a gmail account to send the mails. The mail direcction of the participants are not limited to gmail, it can be any server.
* The first file has the name and mail of every participant. Each participant has to be configurated in a line with the following structure Name:mail :
    ```
    Pedro:pedro@blah.com
    Antonio:antonio@blah.com
    Marta:mrt@blah.com
    Sara:sara@blah.com
   	```
* The second file, has the message that will be sent to every participant. The tag [namefrom] will be replaced with the recipent of the mail. [nameto] will be replaced with the name of the person to be gifted:
    ```
    Hi [namefrom] !

    You has to give the present to [nameto]
    ```
* The script execution:
    ``` bash
    amigo.py [path of the contact list] [path of the message]
    ```

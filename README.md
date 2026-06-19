# TP-integrador-org-empresarial
# Chatbot para Gestión de Vacaciones
el proyecto consiste en un chatbot que realiza la gestión de vacaciones de un empresa con una base de datos en excel
# librerias necesarias 
se usó las librerías PANDAS y OpenPyXL que permiten a python leer y escribir archivos de excel (.xlsx)
se pueden instalar las mismas usando el siguiente comando en la terminal cuando el código no se está ejecutando: pip install pandas openpyxl
asegúrese que la variable "ARCHIVO_EXCEL" contenga la ruta de acceso correcta hacia la base de datos a usar
# como usar el chatbot:
el chatbot es fácil de usar al principio te pregunta si quieres realizar una solicitud o si quieres salir.
si seleccionas la opción 1 procede a pedir el DNI a buscar y si el DNI que diste no está en la base de datos procede a pedir tu nombre y cantidad de días disponibles y te agrega a la base de datos
siguiente te pregunta la cantidad de días solicitados y se asegura que no estes pidiendo más días de la cuenta, si no, te rechaza la solicitud y la registra en "solicitudes"
si la cantidad de días a pedir no supera tus días disponibles entonces te aprueba la solicitud y te pregunta si quieres hacer otra solicitud o si quieres salir
# importante
no ejecutes el chatbot con el archivo de Excel abierto por que va a dar error y los datos que escribas con el chatbot solo se van a guardar una vez le des a "salir"

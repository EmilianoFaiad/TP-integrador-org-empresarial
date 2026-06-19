# TP-integrador-org-empresarial

# Chatbot para Gestión de Vacaciones

El proyecto consiste en un chatbot que realiza la gestión de vacaciones de un empresa con una base de datos en excel.

# Librerias necesarias 

Se usó las librerías PANDAS y OpenPyXL que permiten a python leer y escribir archivos de excel (.xlsx).

Se pueden instalar las mismas usando el siguiente comando en la terminal cuando el código no se está ejecutando: pip install pandas openpyxl

Asegúrese que la variable "ARCHIVO_EXCEL" contenga la ruta de acceso correcta hacia la base de datos a usar.

# Como usar el chatbot:

El chatbot es fácil de usar al principio te pregunta si quieres realizar una solicitud o si quieres salir.

Si seleccionas la opción 1 procede a pedir el DNI a buscar y si el DNI que diste no está en la base de datos procede a pedir tu nombre y cantidad de días disponibles y te agrega a la base de datos.

Siguiente te pregunta la cantidad de días solicitados y se asegura que no estes pidiendo más días de la cuenta, si no, te rechaza la solicitud y la registra en "solicitudes".

si la cantidad de días a pedir no supera tus días disponibles entonces te aprueba la solicitud y te pregunta si quieres hacer otra solicitud o si quieres salir
# Importante

No ejecutes el chatbot con el archivo de Excel abierto por que va a dar error y los datos que escribas con el chatbot solo se van a guardar una vez le des a "salir".

class ExamenPython:
    """
    Classe para el examen de la materia de Python con metodos para cada ejercicio
    """

    # Atributos
    def __init__(self):
        self.cadena = ""
        self.lista_de_strings = []
        self.lista_de_numeros = []

    def invertir_string_por_recursividad(self, string):
        """
        Recibe un string y revisa el caso en el que el string es de 0 o 1 caracter y regresa el mismo string.
        En el caso que no, se llama a si mismo (invertir_string_por_recursividad) con el substring
        desde el 2do caracter hasta el ultimo y concatena el 1er caracter al final. El proceso se repite hasta
        que alcanza el ultimo caracter.

        :param string: Cadena de caracteres
        :return: String invertido
        """
        # Si el string esta vacio o solo tiene 1 cracter regresa el mismo string
        if len(string) <= 1:
            return string

        # Invierte el substring exlcuyendo el 1er caracter y lo concatena al final
        return self.invertir_string_por_recursividad(string[1:]) + string[0]

    def encontrar_anagramas(self, lista):
        """
        Itera sobre cada string de la lista de entrada, ordena los caracteres y utiliza el string ordenado como llave
        en el diccionario de anagramas. Si la llave ya existe se agrega el string a la lista correspondiente de
        anagramas. Si la llave no existe se crea una nuevo grupo. Se convierten los valores del diccionario a tuplas
        y regresa la lista de los anagramas en forma de tuplas.

        :param lista: Lista de strings
        :return: Tuplas con anagramas
        """
        # Crea el diccionario para guardar los anagrams
        diccionario_de_anagramas = {}

        # Itera sobre cada string de la lista
        for string in lista:
            # Ordena los caracteres de string para usarla como llave
            string_ordenado = ''.join(sorted(string))

            # Si existe la llave en el diccionario agrega el string al grupo de anagramas en el diccionario
            if string_ordenado in diccionario_de_anagramas:
                diccionario_de_anagramas[string_ordenado].append(string)
            # Si no existe la llave en el diccionario agrega la llave y agrego el string al nuevo grupo de anagramas
            else:
                diccionario_de_anagramas[string_ordenado] = [string]

        # Convierte los valores del diccionario a tuplas
        anagramas = [tuple(grupo_de_anagramas) for grupo_de_anagramas in diccionario_de_anagramas.values()]

        return anagramas

    def indices_para_suma_del_numero(self, lista_de_numeros, numero):
        """
        Se crea un diccionario (indices) para guardar los numero y sus indices correspondientes. Se itera sobre la
        lista de numeros con enumerate para acceder al numero y al indice. Para cada numero se calcula el complemento
        restandolo del numero deseado (numero). Si el complemento existe en diccionario de indices se regresa una tupla
        con los indices del numero y su complemento. Si no se encuentran numeros para la suma se retorna None.
        :param lista_de_numeros: Lista de numeros
        :param numero: Numero objetivo para la suma
        :return: Indices de dos elementos para las suma o None si no hay elementos para la suma
        """
        indices = {}

        for indice, numero_de_la_lista in enumerate(lista_de_numeros):
            complemento = numero - numero_de_la_lista
            # Si el complemento esta en el diccionario de indices, retorna los idices
            if complemento in indices:
                return (indices[complemento], indice)
            # Si el complemento no esta en la lista de indices, agrega el numero al diccionario con el numero como
            # llave y el indice como valor de la llave
            indices[numero_de_la_lista] = indice

        return None

# Declara la clase para el examen
examen = ExamenPython()

# Ejercicio 1
examen.cadena = input("Ejercicio 1\nInvertir una cadena de caracteres\nEscriba la cadena que desee invertir:\n")
print(f"La cadena invertida de '{examen.cadena}' es '{examen.invertir_string_por_recursividad(string=examen.cadena)}'")

# Ejercicio 2
print("\nEjercicio 2\nEncontrar anagramas de una lista de strings")
try:
    n = int(input("Numero de elementos que contendra la lista: "))
    # Captura los elementos en la lista
    for i in range(0, n):
        examen.lista_de_strings.append(str(input(f"Capture el elemento {i} de la lista: ")))

    print(f"Anagramas de la lista {examen.lista_de_strings}:\n"
          f"{examen.encontrar_anagramas(lista=examen.lista_de_strings)}")
except:
    print("No introdujo un numero entero")

# Ejercicio 3
print("\nEjercicio 3\nEncontrar los indices de 2 numeros en una lista que sumen un numero dado")
try:
    numero = int(input("Capture el numero objetivo para la suma: "))
    n = int(input("Numero de elementos que contendra la lista de numeros: "))
    # Captura los elementos en la lista
    for i in range(0, n):
        examen.lista_de_numeros.append(int(input(f"Capture el numero {i} de la lista: ")))

    print(f"Indices encontrados de la lista {examen.lista_de_numeros} para la suma de {numero}: "
          f"{examen.indices_para_suma_del_numero(lista_de_numeros=examen.lista_de_numeros, numero=numero)}")
except:
    print("No introdujo un numero entero")

"""
Solucion para el analisis de paquetes atraves de reconocimiento de patrones

Se dividiria en las siguientes etapas
        
        Recoleccion de datos
Los paquetes web se capturan y recopilan para su análisis. Se pueden usar herramientas de monitoreo de red o 
rastreadores de paquetes.

        Procesamiento
Los paquetes web recopilados deben preprocesarse para extraer características relevantes para el reconocimiento 
de patrones. Puede ser la extracción de información de encabezado, contenido, marcas de tiempo, ips y otros 
datos relevantes.

        Extraccion de patrones
Una vez procesados los datos, es necesario extraer los patrones. Pueden ser características como el tamaño del paquete, 
las direcciones IP de origen y destino, los protocolos utilizados, las URL a las que se accede y cualquier otro 
dato relevante.

        Entrenamiento de modelo
Un modelo de reconocimiento de patrones, como un algoritmo de aprendizaje automático, debe entrenarse con los datos. 
Los datos serian paquetes que se sabe que son normales o anómalos. El modelo aprende los patrones y características de 
los paquetes normales durante la fase de entrenamiento.

        Deteccion de anomalias
Se utiliza el modelo para detectar anomalías en los paquetes. El modelo examina las características de cada paquete y 
las compara con los patrones que aprendió durante el entrenamiento. Si un paquete se desvía significativamente de los 
patrones aprendidos, se marca como una posible anomalía.

        Generacion de alertas
Cuando se detecta una anomalía, se puede generar una alerta o notificación para informar al personal en el laboratorio. 
La alerta puede incluir detalles sobre la anomalía detectada, información relevante.

        +-------------------+
        |                   |
        |   Recoleccion de  |
        |       datos       |
        |                   |
        +--------+----------+
                 |
                 v
        +--------+----------+
        |                   |
        |   Procesamiento   |
        |                   |
        +--------+----------+
                 |
                 v
        +--------+----------+
        |                   |
        |  Extraccion de    |
        |     patrones      |
        |                   |
        +--------+----------+
                 |
                 v
        +--------+----------+
        |                   |
        |   Entrenamiento   |
        |      de modelo    |<---|
        |                   |    |
        +--------+----------+    |
                 |---------------|
                 v
        +--------+----------+
        |                   |
        |    Deteccion de   |
        |     anomalias     |
        |                   |
        +--------+----------+
                 |
                 v
        +--------+----------+
        |                   |
        |   Generacion de   |
        |      alertas      |
        |                   |
        +-------------------+

La solucion cubre los siguientes puntos
    Automatización y eficiencia en la identificación de anomalías.
    Escalabilidad para manejar grandes volúmenes de datos.
    Detección en tiempo real para una rápida identificación y respuesta.
    Adaptabilidad a nuevas amenazas a través de actualizaciones de modelos y reentrenamiento.
    Consistencia y estandarización en el proceso de detección.
    Reducción de falsos positivos, minimizando alertas innecesarias.
    Postura de seguridad mejorada mediante la identificación proactiva de posibles infracciones de seguridad.

La eficacia de la solución depende de factores como la calidad de los datos, la elección del modelo y el mantenimiento.
La evaluación y las actualizaciones son importantes para que la solución siga siendo efectiva con el paso del tiempo.
"""

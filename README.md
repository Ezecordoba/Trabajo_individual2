# Proyecto: Análisis de Acceso a Internet en Argentina

## Descripción General

Este proyecto tiene como objetivo realizar un análisis completo del acceso a internet en Argentina.

El análisis incluye la evolución del ancho de banda en comparacion con las tecnologías asociadas a companías telefónicas (Dial up), el impacto de tecnologías como fibra óptica y la comparación con otros tipos de accesos. En este trabajo se divide a las provincias en dos grupos: las 5 mas urbanizadas (que coinciden con las 5 mas pobladas) y el resto. Se hará comparaciones entre estos dos grupos y entre las provincias del primero. 
Las 5 provincias mas urbanizadas son, en orden: 
- CABA

- Buenos Aires

- Córdoba

- Santa Fe

- Mendoza. 

Tambien se realizaron analisis sobre la evolucion de los accesos a los distintos rangos de velocidades de conexión con lines históricas. 

## Contenido

- **ETL_y_EDA.ipynb:** En el ETL se realiza el proceso de extracción, transformación y carga de los datos. Se identificaron y trataron datos redundantes, atípicos y nulos, preparando la información para un análisis más limpio y efectivo. En el EDA se lleva a cabo el análisis exploratorio de datos con el objetivo de identificar tendencias y distribuciones. Las conclusiones de este análisis se utilizaron para diseñar el dashboard.
- **creacion_tablas_dimansion.ipynb:** Aquí se crean paso a paso las tablas de dimensión que ayudan a crear un modelo mas organizado y facilitar el manejo del dashboard.
- **Creacion_libros_Excel.py:** Este archivo sirve para poder crear los libros de Excel ´Tablas_de_dimension.xlsx´ y ´Tablas_de_´hecho.xlsx´ que se utilizarán para el dashboard.
- **TP_2_Dashboard.pbix:** Aquí se encuentra el dashboard con las gráficas que permiten analizar los datos procesados.
- **Database:** Carpeta donde se encuentra toda la base de datos. En la carpeta ´Complementarios´ se encuentran los datasets utilizados que no eran obligatorios. En las carpeta ´Tablas_de_dimension´ y ´Tablas_de_hecho´ se encuentran las tablas de dimension y hecho que luego formarán parte de los libros de Excel mediante el archivo ´creacion_tablas_dimansion.ipynb´.


## Proceso ETL

La primera etapa fue el proceso ETL (Extract, Transform, Load), donde se trabajó con múltiples datasets que presentaban datos redundantes, nulos y algunas cadenas de texto no deseadas. El principal problema fue organizar estos datasets y limpiar los datos para dejarlos listos para el análisis. 

Primero se crearon las tablas de dimension y luego se realizó el ETL de las tablas de hecho. EL proceso realizado se puede ver con detalle en ´ETL_y_EDA.ipynb´.

La tabla Penetracion_hogares sufrió ciertas modificaciones, para el tratamiendo del KPI correspondiente, directament sobre Excel, ya que aquí eran mas sencillas de realizar.

## Análisis Exploratorio de Datos (EDA)

En el EDA fue realizado en python. En el se analizó sobre todo la evolución de los distintos rengos de veolocidades y de la Banda Ancha en detrimento del Dial up, así como su penetración en las provincias de Argentina. En este análisis pudo verse la aplastante victoria de la Banda Ancha respecto al Dial up debido a lan también aplastante, victoria de la telefonía movil sobre la telefonía fija. Tambien se pudo analizar como, a medida que pasa el tiempo las conexiones con velocidades por encima de los 30 Mb/s le ganan terreno a aquellas con velocidades mas intermedias o bajas 

## Dashboard

El dashboard fue desarrollado usando Power Bi. El objetivo era mostrar la información mínima y necesaria para el análisis planteado, ya que la meta era construir un MVP (Producto Viable Mínimo) centrado en la evolución de la conectividad en Argentina. Las secciones principales incluyen:

- **Tecnologías:** Una comparación rápida de las tecnologías disponibles es: 

   - La Fibra óptica es la mejor opción si la prioridad es la velocidad y la estabilidad, pero es costosa y aún no está disponible en todas las áreas. 
   - Cablemodem ofrece un buen equilibrio entre velocidad y costo, siendo ideal para áreas urbanas. 
   - ADSL es una opción económica para zonas rurales, pero su velocidad y estabilidad son limitadas. 
   - Wireless es ideal para la movilidad y flexibilidad, pero depende de la cobertura y puede ser más costosa si se usan datos móviles.

    Primero analicemos la linea de tiempo filtrando por las provincias mas urbanizadas podemos ver la clara caida del ADSL, que pierde en cuanto a velocidad y estabilidad, frente a una clara predominancia del Cablemodem y un crecimiento cada vez mayor de la Fibra óptica, aunque todavia por detras de la primera. Esto puede verse respaldado por el gráfico circular (2023-2024) que da un 56% de accesos para Cablemodem, 32,5% para Fibra óptica y un escaso 6,7% para ADSL. Si hacemos el mismo análisis en el resto de provincias podemos ver que la caida en los accesos de ADSL es menos pronunciada debido a que son provincias menos urbanizadas, aunque en los utltimos años siguen predominando mas Cablemodem y la Fibra óptica. Si vemos el gráfico circular podemos ver que, a diferencia del grupo anterior, a Cablemodem le corresponde un 40% de los accesos, 32,8% a la Fibra óptica y un 12,7% a ADSL. 

    Por último se presentan 4 lienas históricas. La primera muestra el crecimeinto de los ingresos de las telefonías fijas, que estan relacionadas con las conecciones por coperativas (Dial up), en la cual se puede ver que el orden de magnitud de los ingresos rondan las centenas de millones. En cambio, en la linea histórica de los ingresos de la telefonpia movil, se muestra que estos acienden a miles de millones. Esto muestra como al correr de los años, las telefonías móviles han predominado frente a las fijas, lo que puede esplicar el por qué la banda ancha ha crecido tanto respecto al Dial up que incluso ha perdido accesos.

- **Velocidades:** En esta hoja se presenta la comparación de los distintos rangos de velocidad de conexión y la velocidad promedio en cada provincia. Para para ambos grupos de provincias puede verse que, desde 2014 a 2024, ha habido un crecimiento muy pronunciado de accesos totales a internet. Tambien, en ambos, puede verse que en 2014 predominaban las conexiones en el rango de [1,6] Mb/s, pero a lo largo de los años esta predomiancia fue rapidamente superada por las conexiones en el rango de Mas 30 Mb/s. La Diferencia entre grupos puede verse la proporción mostrada en la gráfica circular (2023-2024). Para las 5 provincias mas urbanizadas y pobladas, las conecciones estan en un 79,5% en el rango Mas 30 Mb/s, mientras que los demas rangos de velocidades acaparan menos de un 7% cada una. En cambio, en el resto de provincias, el rango de Mas 30 Mb/s abarca el 48,9% de las conexione, el rango [1,6] y [6,10] Mb/s se llevan un 16% cada una y el rango [10,20] otro 10,7%, osea que está mas distribuído. hay tres casos particulares a tratar.
    - Formosa: la provincia mas pobre de Argentina, es particular porque no solo la torta está dividida un 36% y 35% entre los rangos Mas 30 y [1,6] Mb/s respectivamente, y un no despreciable 18% para el rango [6,10] Mb/s, sino que ádemas, el total de accesos ronda los 60000. Esto es bastante mas bajo que en cualquier otra provincia. El hecho de que haya tanta proporcion de velocidades altas muestra la diferencia económica dentro de la poblacion de esta provincia.
    - San Luis: en esta provincia predomina fuertemente las conexiones con velocidades en el rango [20,30] Mb/s, en un 51% (2023-2024).
    - Tierra del Fuego: en esta provincia predomina fuertemente las conexiones con velocidades en el rango [6,10] Mb/s, en un 45% (2023-2024). 

    Por último, se puedes analizar las velocidades de bajada promedio de las conexiones en las distintas provincias. Como puede verse, CABA, la "provincia" mas urbanizada (en realidad no es provincia), tiene la mayor velocidad de bajada promedio con unos 231,48 Mb/s, mientras que Chubut es la que menos con unos 21,09 Mb/s

- **KPI 1:** este KPI analiza el numero de accesos por cada 100 hogares por trimestre, poniendo como objetivo que cada trimestre sea superior en un 2% con el anterior. Esto es importate para analizar porque nos permite llevar un seguimiento sobre el crecimiento de los hogares que contratan internet. Si hacemos un análisis en el total del pais puede verse que no se ha cumplido el objetivo, pero en el ultimo trimestre del 2024 (el segundo) no se alcanzó por un 0,25%. Analizando las 5 provincias mas urbanizadas y pobladas puede verse que el objetivo no fue cumplido por un porcentaje mayor de un 1,33%. En el resto de provincias analizadas como grupo se superar el objetivo por un 0,1%. Caben resaltar las prvincias en las que si se cumplió y superó el objetivo:
    - Catamarca (+0,3%)
    - Chaco (+8,01%)
    - Jujuy (+6,46%)
    - La Pampa (+1,23%)
    - Neuquen (+0,83%)
    - Río Negro (+1,05%)
    - San Luis (+5,75%)
    - Santiago del Estero (+0,78%) 

- **KPI 1:** este KPI analiza el numero de accesos a Fibra óptica por trimestre en todo el pais. Este es importante por que la Fibra óptica es la tecnología que mas a crecido en los últimos años y puede significar el futuro del internet. El objetivo que se impuso fue de que los ingresos de cada trimestre fuera un 2% mayor los del tirmestre anterior. Como puede verse, el objetivo fue alcanzado con creces en casi todos los años posteriores que llegara el crecimeinto mas rápido en 2019. Esto da un buen precedente para el futuro de la conexion a internet ya que es la mejor opcion en cuanto a velocidad y estabilidad, mas allá del costo.  

## Conclusiones

En este trabajo se realizó un análisis sobre el mercado de internet, pasando por un estudio sobre las tecnologias, los rangos de velocidades de conexion y algunos KPI's de interes para este mercado. Sobre las tecnologías se pudo concluir que, si bien Cablemodem y Fibra óptica han sido las tecnologías que mas han crecido en la última década, esta última es la que lo ha hecho mas rápido. Por lo que, para mejorar el mercado es una buena idea seguir promoviendo ese crecimiento de la Fira óptica que parece ser el futuro de la conexion a internet en Argentina. Por el lado de los rangos de velocidades se concluyó que, si bien hay casos particulares en algunas provincias, en promedio, en la última década ha empezado a dominar el mercado las coexiones de mas de 30m Mb/s, cosa que puede estar relacionada directamente con el crecimiento de la Fibra óptica. De los KPI's se puede concluir que, si bien todavia falta para cumplir algunos objetivos, no se esta muy lejos de hacerlo y nuevamente la solucion puede estar en la expanción de la fibra óptica que está habiendo en el mercado. De esta forma el aumento en las instalaciones de este timpo de tecnología, si bien es costosa, puede proporcionar que no solo aumenten los accesos a interet, sinó que tambien la claidad de este. Cosa que siempre es positiva tanto para el usuario, como para las empresas. 

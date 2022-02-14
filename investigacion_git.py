GIT

Es un proyecto de codigo abierto que fue desarrollado originalmente por Linus Torvalds.
Git fue desarrollado pensando en la eficiencia, la confiabilidad y compatibilidad del mantenimiento de versiones
de aplicaciones  de un gran número de archivos de codigo fuente con el propósito de llevar registros de los cambios
en archivos de computadora incluyendo coordinar el trabajo que varias personas realizan sobre archivos compartidos
en un repositorio de código.

Git, presenta una arquitectura distribuida. En lugar de tener un único espacio para todo el historial de versiones 
del software, en Git, la copia de trabajo del código de cada desarrollador es también un repositorio
que puede albergar el historial completo de todos los cambios.

Además de contar con una arquitectura distribuida, Git se ha diseñado teniendo en cuenta el rendimiento,
la seguridad y la flexibilidad.

#Rendimiento
Las características básicas de rendimiento de Git son muy sólidas en comparación con muchas otras alternativas.
La confirmación de nuevos cambios, la ramificación, la fusión y la comparación de versiones anteriores se han optimizado
en favor del rendimiento.
Los algoritmos implementados en Git aprovechan el profundo conocimiento sobre los atributos comunes de los auténticos
árboles de archivos de código fuente, cómo suelen modificarse con el paso del tiempo y cuáles son los patrones de acceso.

Git no se deja engañar por los nombres de los archivos a la hora de determinar cuál debería ser el almacenamiento
y el historial de versiones del árbol de archivos; en lugar de ello, se centra en el contenido del propio archivo.
Al fin y al cabo, los archivos de código fuente se cambian de nombre, se dividen y se reorganizan con frecuencia.
El formato de objeto de los archivos del repositorio de Git emplea una combinación de codificación delta
(que almacena las diferencias de contenido) y compresión, y guarda explícitamente el contenido de los directorios y los objetos de metadatos de las versiones.

Su arquitectura distribuida también permite disfrutar de importantes ventajas en términos de rendimiento.

Seguridad
Git se ha diseñado con la principal prioridad de conservar la integridad del código fuente gestionado.
El contenido de los archivos y las verdaderas relaciones entre estos y los directorios, las versiones, las etiquetas y las confirmaciones,
todos ellos objetos del repositorio de Git, están protegidos con un algoritmo de hash criptográficamente seguro llamado "SHA1".
De este modo, se salvaguarda el código y el historial de cambios frente a las modificaciones accidentales y maliciosas, y se garantiza
que el historial sea totalmente trazable.

Flexibilidad
Git es flexible en varios aspectos: en la capacidad para varios tipos de flujos de trabajo de desarrollo no lineal,
en su eficiencia en proyectos tanto grandes como pequeños y en su compatibilidad con numerosos sistemas y protocolos.

Git se ha ideado para posibilitar la ramificación y el etiquetado como procesos de primera importancia (a diferencia de SVN)
y las operaciones que afectan a las ramas y las etiquetas (como la fusión o la reversión)
también se almacenan en el historial de cambios. No todos los sistemas de control de versiones ofrecen este nivel de seguimiento.

Control de versiones con Git
Git es la mejor opción para la mayoría de los equipos de software actuales.
Aunque cada equipo es diferente y debería realizar su propio análisis, aquí recogemos los principales motivos por los que destaca el
control de versiones de Git con respecto a otras alternativas:

Git es un proyecto de código abierto muy bien respaldado con más de una década de gestión de gran fiabilidad.
Los encargados de mantener el proyecto han demostrado un criterio equilibrado y un enfoque maduro para satisfacer las necesidades a
largo plazo de sus usuarios con publicaciones periódicas que mejoran la facilidad de uso y la funcionalidad.
La calidad del software de código abierto resulta sencilla de analizar y un sinnúmero de empresas dependen en gran medida de esa calidad.

El hecho de que sea de código abierto reduce el coste para los desarrolladores aficionados,
puesto que pueden utilizar Git sin necesidad de pagar ninguna cuota.
En lo que respecta a los proyectos de código abierto, no cabe duda de que Git es el sucesor de las anteriores generaciones de los
exitosos sistemas de control de versiones de código abierto, SVN y CVS
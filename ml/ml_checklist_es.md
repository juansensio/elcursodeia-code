# _Checklist_ para proyectos de Machine Learning

Esta _checklist_ puede guiarte a través de tus proyectos de Machine Learning. Hay ocho pasos principales:

1. Visión global del problema.
2. Obtener los datos.
3. Explorar los datos para obtener insights.
4. Preparar los datos para exponer mejor los patrones subyacentes a los algoritmos de Machine Learning.
5. Explorar muchos modelos diferentes y preseleccionar los mejores.
6. Afinar tus modelos y combinarlos en una gran solución.
7. Presentar tu solución.
8. Lanzar, monitorear y mantener tu sistema.

Obviamente, siéntete libre de adaptar esta lista a tus necesidades.

## Visión global

1. Definir el objetivo en términos de negocio.
2. ¿Cómo se utilizará tu solución?
3. ¿Cuáles son las soluciones/alternativas actuales (si las hay)?
4. ¿Cómo deberías enmarcar este problema (supervisado/no supervisado, online/offline, etc.)?
5. ¿Cómo se debe medir el rendimiento?
6. ¿Está la medida de rendimiento alineada con el objetivo de negocio?
7. ¿Cuál sería el rendimiento mínimo necesario para alcanzar el objetivo de negocio?
8. ¿Qué problemas son comparables? ¿Puedes reutilizar experiencia humana o herramientas?
9. ¿Está disponible la experiencia humana?
10. ¿Cómo resolverías el problema manualmente?
11. Enumera las suposiciones que tú u otros han hecho hasta ahora.
12. Verifica las suposiciones si es posible.
13. Análisis de riesgos

## Obtener los datos

Nota: automatiza tanto como sea posible para que puedas obtener datos frescos fácilmente.

1. Enumera los datos que necesitas y cuánto necesitas.
2. Encuentra y documenta dónde puedes obtener esos datos.
3. Comprueba cuánto espacio ocupará.
4. Verifica las obligaciones legales y obtén la autorización si es necesario.
5. Obtén las autorizaciones de acceso.
6. Crea un espacio de trabajo (con suficiente espacio de almacenamiento).
7. Obtén los datos.
8. Convierte los datos a un formato que puedas manipular fácilmente (sin cambiar los datos en sí).
9. Asegúrate de que la información sensible sea eliminada o protegida (por ejemplo, anonimizada).
10. Verifica el tamaño y tipo de datos (series temporales, muestra, geográficos, etc.).
11. Toma una muestra del conjunto de prueba, ponla a un lado y nunca la mires (¡no espíes los datos!).

## Explorar los datos

Nota: intenta obtener insights de un experto en el campo para estos pasos.

1. Crea una copia de los datos para exploración (reduciéndola a un tamaño manejable si es necesario).
2. Crea un notebook de Jupyter para mantener un registro de tu exploración de datos.
3. Estudia cada atributo y sus características:
   - Nombre
   - Tipo (categórico, int/float, acotado/no acotado, texto, estructurado, etc.)
   - % de valores faltantes
   - Ruido y tipo de ruido (estocástico, valores atípicos, errores de redondeo, etc.)
   - ¿Posiblemente útil para la tarea?
   - Tipo de distribución (Gaussiana, uniforme, logarítmica, etc.)
4. Para tareas de aprendizaje supervisado, identifica el/los atributo(s) objetivo.
5. Visualiza los datos.
6. Estudia las correlaciones entre atributos.
7. Estudia cómo resolverías el problema manualmente.
8. Identifica las transformaciones prometedoras que podrías aplicar.
9. Identifica datos adicionales que serían útiles (vuelve a "Obtener los datos" en la página 502).
10. Documenta lo que has aprendido.

## Preparar los datos

Notas:

- Trabaja con copias de los datos (mantén intacto el conjunto de datos original).
- Escribe funciones para todas las transformaciones de datos que apliques, por cinco razones:
  - Para que puedas preparar fácilmente los datos la próxima vez que obtengas un conjunto de datos fresco
  - Para que puedas aplicar estas transformaciones en proyectos futuros
  - Para limpiar y preparar el conjunto de prueba
  - Para limpiar y preparar nuevas instancias de datos
  - Para facilitar el tratamiento de tus elecciones de preparación como hiperparámetros

1. Limpieza de datos:
   - Corrige o elimina valores atípicos (opcional).
   - Rellena los valores faltantes (por ejemplo, con cero, media, mediana...) o elimina sus filas (o columnas).
2. Selección de características (opcional):
   - Elimina los atributos que no proporcionan información útil para la tarea.
3. Ingeniería de características, donde sea apropiado:
   - Discretiza características continuas.
   - Descompone características (por ejemplo, categóricas, fecha/hora, etc.).
   - Añade transformaciones prometedoras de características (por ejemplo, log(x), sqrt(x), x^2, etc.).
   - Agrega características en nuevas características prometedoras.
4. Escalado de características: estandariza o normaliza las características.

## Preseleccionar modelos prometedores

Notas:

- Si los datos son enormes, es posible que desees muestrear conjuntos de entrenamiento más pequeños para poder entrenar muchos modelos diferentes en un tiempo razonable (ten en cuenta que esto penaliza los modelos complejos como las grandes redes neuronales o los Random Forests).
- Una vez más, intenta automatizar estos pasos tanto como sea posible.

1. Entrena muchos modelos rápidos y simples de diferentes categorías (por ejemplo, lineal, naive Bayes, SVM, Random Forests, red neuronal, etc.) utilizando parámetros estándar.
2. Mide y compara su rendimiento.
   - Para cada modelo, utiliza validación cruzada N-fold y calcula la media y la desviación estándar de su rendimiento.
3. Analiza las variables más significativas para cada algoritmo.
4. Analiza los tipos de errores que cometen los modelos.
   - ¿Qué datos habría utilizado un humano para evitar estos errores?
5. Realiza una ronda rápida de selección e ingeniería de características.
6. Realiza una o dos iteraciones rápidas más de los cinco pasos anteriores.
7. Preselecciona los tres a cinco modelos más prometedores, prefiriendo modelos que cometan diferentes tipos de errores.

## Afinar el sistema

Notas:

- Querrás utilizar tantos datos como sea posible para este paso, especialmente a medida que te acercas al final del ajuste.
- Como siempre, automatiza lo que puedas.

1. Afina los hiperparámetros utilizando validación cruzada.
   - Trata tus elecciones de transformación de datos como hiperparámetros, especialmente cuando no estés seguro de ellas (por ejemplo, ¿debo reemplazar los valores faltantes con cero o con el valor mediano? ¿O simplemente eliminar las filas?).
   - A menos que haya muy pocos valores de hiperparámetros para explorar, prefiere la búsqueda aleatoria sobre la búsqueda en cuadrícula. Si el entrenamiento es muy largo, puedes preferir un enfoque de optimización bayesiana (por ejemplo, utilizando procesos gaussianos previos, como describen Jasper Snoek, Hugo Larochelle y Ryan Adams ([https://goo.gl/PEFfGr](https://goo.gl/PEFfGr)))
2. Prueba métodos de Ensemble. Combinar tus mejores modelos a menudo funcionará mejor que ejecutarlos individualmente.
3. Una vez que estés seguro de tu modelo final, mide su rendimiento en el conjunto de prueba para estimar el error de generalización.

> No ajustes tu modelo después de medir el error de generalización: simplemente comenzarías a sobreajustar el conjunto de prueba.

## Presentar tu solución

1. Documenta lo que has hecho.
2. Crea una buena presentación.
   - Asegúrate de resaltar primero el panorama general.
3. Explica por qué tu solución alcanza el objetivo de negocio.
4. No olvides presentar puntos interesantes que hayas notado en el camino.
   - Describe lo que funcionó y lo que no.
   - Enumera tus suposiciones y las limitaciones de tu sistema.
5. Asegúrate de que tus hallazgos clave se comuniquen a través de visualizaciones hermosas o declaraciones fáciles de recordar (por ejemplo, "el ingreso medio es el predictor número uno de los precios de las viviendas").

## ¡Lanzamiento!

1. Prepara tu solución para producción (conéctala a las entradas de datos de producción, escribe pruebas unitarias, etc.).
2. Escribe código de monitoreo para verificar el rendimiento en vivo de tu sistema a intervalos regulares y activar alertas cuando baje.
   - Ten cuidado también con la degradación lenta: los modelos tienden a "pudrirse" a medida que los datos evolucionan.
   - Medir el rendimiento puede requerir un pipeline humano (por ejemplo, a través de un servicio de crowdsourcing).
   - También monitorea la calidad de tus entradas (por ejemplo, un sensor defectuoso que envía valores aleatorios, o la salida de otro equipo que se vuelve obsoleta). Esto es particularmente importante para los sistemas de aprendizaje en línea.
3. Vuelve a entrenar tus modelos regularmente con datos frescos (automatiza tanto como sea posible).

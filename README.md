waragoncontest
==============

Planeo del problema en waragoncontest.png

Tengo ingredientes A, B y C. El ingrediente D lo vamos a dejar para el final.

Supongamos que tengo una linea horizontal cualquiera con el ingrediente A alineado, eso significa que en las restantes 6 casillas puedo mesclar los tres B y los tres C como quiera.
Esto es simplemente una una permutación de 6 elementos con el primero y el segundo repetido tres veces cada uno, la formula es:

P^{3,3}_{6} = 6! / (3! * 3!) = 20.

La linea que elegimos para empezar puede ser cualquiera de las tres, por lo que este mismo proceso se puede realizar un total de tres veces:

3 * P^{3,3}_{6} = 60

El elemento que elegimos (A) fue uno cualquiera, es el mismo proceso si elegimos B o C, por lo tanto tenemos otras tres posibilidades:

3 * 3 * P^{3,3}_{6} = 180

A su vez usamos solo las combinaciones horizontales, pero la diferencia entre horizontales y verticales es sólo una rotación, por lo que tendremos la misma cantidad de posibilidades horizontales y verticales:

2 * 3^2 * P^{3,3}_{6} = 360


Ahora bien, ahora falta la masita mágica D, esta masita es un comodín, si la reemplazo por cualquier ingrediente no me cambió el estado de ricura del pastel, por lo que en cada pastel rico, de los 360, puedo reemplazar cualquiera de los ingredientes por el mágico D, por lo tanto cada pastel equivale a 3^2=9 recetas ricas (reemplazando el primero, el segundo, etc.)

Por lo tanto tendré

 3^2 * 2 * 3^2 * P^{3,3}_{6} = 9 * 360 = 3240
 
pasteles ricos (ñam!).

El algoritmo general, para un pastel de NxN con N elementos ricos y uno mágico sería:

2 * N^2 * P^{N, N, ..., N (N-1 veces)}_{N*(N-1)}

la permutación sería lapermutación de N*(N-1) elementos (todos menos una fila), en donde tenemos N-1 elementos repetidos N veces cada uno.

Escrito con factoriales será:

2 * N^4 * (N*(N-1))!/( (N!)^(N-1) )

Para utilizarlo correr:

./solucion.py 3

OJO! que no hize ninguna validación de los datos de entrada.





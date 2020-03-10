# Proyecto peliculas con django y nuxt.js
Proyecto donde un usuario puede añadir a sus favoritos diferentes peliculas. 

Para ello se creo en django apis para poder registrar una pelicula, registrar un usuario y vincular una pelicula con el usuario e ir incrementado/decrementado el numéro de favoritos de la película.

Se uso nuxt.js para consumir dichas apis y crear la interfaz gráfica para el usuario.

### Uso del proyecto
Tener instalado pipenv y en un entorno virtual ejecute lo siguiente
```
pipenv install -r requirements.txt
or 
pipenv sync 
```
para instalar las dependecias y luego para levantar el servidor usar 
```
pipenv run dev
```

El servidor de django se encuentra funcionando en 

```
http://127.0.0.1:8020/
```

Para poder ver la interfaz grafica debe entrar en la carpeta `frontend` y ejecutar lo siguiente 

```
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev
```

El servidor de nuxt.js se encuentra funcionando en 

```
http://127.0.0.1:3000/
```

#### Nota
No contiene datos este proyecto para visualizar, por ello debe agregarlo, lo puede hacer a traves de la api o en el admin de django.


 

# guane-intern-fastapi
Prueba tecnica para Guane Entreprises.
Esta api fue construida con el framework FastApi y utiliza MongoDB como base de datos

## 🧾 Documentacion
La documentacion se encuentra en la ruta
`/api/documentation`

## 🚀 Instalación
1. Clona este proyecto.
2. Ve a la carpeta del proyecto
3. Instala las dependencias
`pip install -r requirements.txt`
4. Configurar las variables de ambiente siguiento el archivo de ejemplo (.env.sample)
5. Corre el ambiente local
`uvicorn app.main:app --reload --host localhost --port 8000`


## 🛠 Despliegue
Para el despliegue se utiliza docker y docker-compose.
Por defecto esta configurado que la aplicacion se ejecute en el puerto 8000 y la base de datos mongodb en el puerto 27017.
1. Ve a la carpeta del proyecto
2. Crea el contenedor docker de la aplicacion
`docker-compose up --build -d`
3. Para bajar y eliminar el contenedor
`docker-compose down`



# **Django ORM Relational Models Project**

### **Descripción del Proyecto**
Este proyecto demuestra el uso de las relaciones entre modelos en Django ORM, con ejemplos prácticos de:
- Relaciones **Muchos a Uno**.
- Relaciones **Muchos a Muchos**.
- Relaciones **Uno a Uno**.

El proyecto está dividido en tres aplicaciones separadas para facilitar la organización y el mantenimiento del código:
1. `app_muchos_a_uno`: Relaciones Muchos a Uno.
2. `app_muchos_a_muchos`: Relaciones Muchos a Muchos.
3. `app_uno_a_uno`: Relaciones Uno a Uno.

---

### **Características Principales**
- **Organización Modular**: Cada tipo de relación está implementado en una aplicación independiente.
- **Población de Datos Automatizada**: Script `dataShell.py` para inicializar datos en la base de datos.
- **Interfaces de Usuario Sencillas**: Páginas HTML para visualizar las relaciones y datos almacenados.
- **Escalable**: Fácil de extender para incluir relaciones más complejas o integrar nuevas aplicaciones.

---

### **Requisitos Previos**
- Python 3.8 o superior.
- Django 4.2 o superior.
- Base de datos configurada (SQLite por defecto en `settings.py`).

---

### **Instalación**
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tuusuario/django-orm-relations.git
   cd django-orm-relations
   ```

2. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

3. Realiza las migraciones de las aplicaciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Carga datos iniciales ejecutando el script de población:
   ```bash
   python dataShell.py
   ```

5. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

### **Estructura del Proyecto**
```plaintext
django-orm-relations/
├── app_muchos_a_uno/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       └── muchos_a_uno/
│           └── index.html
├── app_muchos_a_muchos/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       └── muchos_a_muchos/
│           └── index.html
├── app_uno_a_uno/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       └── uno_a_uno/
│           └── index.html
├── dataShell.py
├── manage.py
├── README.md
├── requirements.txt
└── tu_proyecto/
    ├── settings.py
    ├── urls.py
    ├── ...
```

---

### **Población de Datos**
El archivo `dataShell.py` se utiliza para poblar las tablas del proyecto con datos iniciales. Ejecuta este script después de realizar las migraciones para ver ejemplos prácticos en la base de datos.

---

### **Visualización**
Navega a las siguientes rutas para interactuar con las aplicaciones:
1. **Relaciones Muchos a Uno**: [http://localhost:8000/muchos_a_uno/](http://localhost:8000/muchos_a_uno/)
2. **Relaciones Muchos a Muchos**: [http://localhost:8000/muchos_a_muchos/](http://localhost:8000/muchos_a_muchos/)
3. **Relaciones Uno a Uno**: [http://localhost:8000/uno_a_uno/](http://localhost:8000/uno_a_uno/)

---

### **Contribuciones**
¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, abre un *issue* o envía un *pull request*.

---

### **Licencia**
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

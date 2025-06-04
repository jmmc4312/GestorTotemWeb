# 🎓 GestorTotemWeb

**GestorTotemWeb** es una aplicación web desarrollada con Django que permite la gestión de beneficios estudiantiles mediante un sistema tipo tótem digital. Incluye un panel administrativo completo y una interfaz para usuarios finales, facilitando el acceso a información de forma interactiva y centralizada.

## 🧰 Tecnologías utilizadas

- 🐍 **Python 3.13**
- 🌐 **Django 5.x**
- 💾 **SQLite** (base de datos local)
- 💻 **HTML / CSS / JavaScript**
- 🖼️ **Pillow** (para carga y visualización de imágenes)
- 🔧 **Git + GitHub**

## 🎯 Funcionalidades principales

- Gestión de **Totems** (ADMINISTRATIVOS), **Usuarios** (DOCENTES) y **Beneficios**
- Panel de administración completo basado en Django Admin
- Soporte para **imágenes** asociadas a modelos
- Arquitectura MVC
- Interfaces utilizadas a través de los templates de BOOSTRAP

## 📂 Estructura general

intranet/
├── core/
├── static/
├── templates/
├── db.sqlite3
├── manage.py
└── README.md
## 🚀 Cómo ejecutar el proyecto localmente

```bash
git clone https://github.com/jmmc4312/GestorTotemWeb.git
cd GestorTotemWeb
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

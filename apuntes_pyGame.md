## Para niciar un entorno virtual con la version de Python que se quiera utilizaremos el siguiente programa (si no esta instalado en el SO)
    sudo apt install virtualenv

## Para instalar la version que queramos de python
    virtualenv venv --python=python3.7

## Activar el entorno virtual
    source venv/bin/activate

## Desactivar
    deactivate

## Instalar pygame en el entorno activado
    pip install pygame

## Ver lo instalado
    pip freeze

## Lista los elementos de nuestro entorno virtual
    pip list

# Crear archivo con instrucciones para instalar los requisitos de nuestro entorno virtual
    pip3 freeze > requirements.txt

## Para instalar las dependencias del entorno virtual
    pip install -r requirements.txt 






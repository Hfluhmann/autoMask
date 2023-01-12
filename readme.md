## Requisitos:
- Python 3.11 o posterior
- Si pillow y roboflow no se encuentran instalados, instalarlos con los siguientes comandos en la terminal/consola.

```sh
pip install pillow
```
```sh
pip install roboflow - -user
```

## Funcionamiento:
- Tener una carpeta "input" y una carpeta "output".
- Dentro de la carpeta "input" colocar las carpetas con las fotos a procesas ej:(input/GKTK64/foto1.jpg).
- Los resultados se entregarán en carpetas en "output".
- Si se ejecuta el programa con archivos en la carpeta "output" serán eliminados.
- Durante el proceso se creará una carpeta llamada "process". NO editar ni eliminar, el programa la eliminará automaticamente al finalizar.
- Si la carpeta "process" ya existe al iniciar el proceso, este funcionará de todos modos y la eliminará al final de la ejecución.
- En la terminal avisará ejecuciones exitosas, ejecuciones donde no se detecta autos, y errores al abrir archivos, los cuales se saltarán y se continuará.
- El término de la ejecución se avisará en la terminal.

## Ejecución:
- Iniciar masker.exe
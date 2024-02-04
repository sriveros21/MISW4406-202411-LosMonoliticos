## Integrantes grupo Los Monolíticos:
- Helena Patarroyo
- Carlos Tovar
- Sergio Riveros
- Sebastián Arango

## Instrucciones de uso:
### Estructura de proyecto:
El proyecto tiene la siguiente estructura:
- Dentro de la carpeta `src/main/cml` se encuentran los archivos utilizados para desarrollar y construir el diagrama de contexto, ya que mediante la funcionalidad de Gitpod se puede generar los archivos con el menu de opciones, dando click en la opción `Generate graphical context map`. Acá se tienen dos archivos, uno es para la construcción del AS_IS de nombre `propiedadesDeLosAlpes.cml` y otro para la construcción del TO_BE de nombre `propiedadesDeLosAlpes_tobe.cml`. El archivo de `demo.cml` es para fines de ejemplo.
- Dentro de la carpeta `src-gen` se encuentran las imágenes exportadas mediante la funcionalidad anteriormente descrita, y estas imágenes se exportan en tres formatos: `.png, .svg y .gv`. El archivo `.png` es el más utilizado para visualizar el diagrama de contexto.
- Dichos diagramas de contexto tambien se clasifican con el mismo nombre para diferenciar el diagrama AS_IS y el diagrama TO_BE.
- Otros archivos tales como el `.gitignore`, sirve para excluir de los commits de Git ciertos archivos con determinada extensión; `.gitpod.Dockerfile`, sirve para la configuración del ambiente tal y como se ha visto en los tutoriales.

### Dónde encontrar los fragmentos de código:
Los fragmentos de código se encuentran en los archivos con extensión `.cml` que se ubican en el directorio `src/main/cml`, y se dividen por el archivo de AS_IS y el de TO_BE:
- propiedadesDeLosAlpes.cml -> AS_IS
- propiedadesDeLosAlpes_tobe.cml -> TO_BE

### Dónde encontrar las imágenes de Event-Storming:
Las imágenes realizadas para event-storming se encuentran en la ruta `event-storming`, y se clasifican de la siguiente manera:
- Event Storming -AS IS.jpg
- Event Storming -TO BE.jpg

De igual manera, si se desea ver estas imágenes directamente en Miro, se puede utilizar los siguientes links:
- Event Storming -AS IS: <https://miro.com/app/board/uXjVNxn5L0I=/>
- Event Storming -TO BE: <https://miro.com/app/board/uXjVNx-2YZY=/>

----

![Context Mapper](https://raw.githubusercontent.com/wiki/ContextMapper/context-mapper-dsl/logo/cm-logo-github-small.png)
# Context Mapper Demo for Online IDE 
[![Build](https://github.com/ContextMapper/web-ide-demo/actions/workflows/build.yml/badge.svg)](https://github.com/ContextMapper/web-ide-demo/actions) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ContextMapper/web-ide-demo) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Welcome to Context Mapper's demo repository. It illustrates how you can configure your own repository for the usage of Context Mapper in the online IDE [Gitpod](https://www.gitpod.io/).

## Start Using Context Mapper Now
Start the online IDE and use Context Mapper right now:

<a href="https://gitpod.io/#https://github.com/ContextMapper/web-ide-demo" style="padding: 10px;">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" width="150" alt="Push" align="center">
</a>
<br/><br/>

## Open the Demo File
In the folder `src/main/cml` you find a small **[CML demo](./src/main/cml/demo.cml)** (DDD sample application) where you can start to familiarize yourself with our DSL and our tools.
You can find more info's about the tool and a complete documentation on our website [https://contextmapper.org/](https://contextmapper.org/).

## Create Your Own Context Mapping Repository
You can simply fork this repository and click the button above to start the online IDE for your repo.

## Useful Links
 
 * [More example models](https://github.com/ContextMapper/context-mapper-examples)
 * [CML language reference](https://contextmapper.org/docs/language-reference/)
 * [Rapid prototyping tutorial](https://contextmapper.org/docs/rapid-ooad/)
 * [Architectural Refactorings](https://contextmapper.org/docs/architectural-refactorings/)
 * [Generators](https://contextmapper.org/docs/generators/)

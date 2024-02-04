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

### Documentación de las relaciones y tipos de integracion entre contextos:
#### AS_IS:
- El contexto `CommercialRealEstateInformation` se relaciona mediante [D - Downstream] y [ACL - Anticorruption Layer] con `RentalAndSalesListings` debido a que primero se realizan las labores comerciales antes de las labores de renta y venta; en sentido contrario, se tiene una relación [U - Upstream], [OHS - Open Host Service] y [PL - Published Language] debido a que las labores de renta y venta deben ocurrir arriba de las comerciales.
- Lo anterior sucede de igual forma entre los contextos `RentalAndSalesListings` y `TenantInformation`, pues la información de inquilinos es superior a la de rentas, pues se necesita cierta información primero para lograr dicha conexión.
- El contexto de `TenantInformation` tiene una relación de [D - Downstream] y [ACL - Anticorruption Layer] con el contexto `LeaseTransactions` debido a que se tiene primero la información de los inquilinos y luego la de las transacciones de los arrendamientos. En sentido contrario, se tiene una relación de [U - Upstream] por el sentido de la transacción.
- El contexto de `LeaseTransactions` tiene una relación de [D - Downstream] y [ACL - Anticorruption Layer] con el contexto `SalesComparatives` debido a que primero se realizan las transacciones de arrendamiento y luego las comparativas de las ventas; en sentido contrario se tiene [U - Upstream], [OHS - Open Host Service] y [PL - Published Language] debido a que las ventas son los indicadores de los valores y cantidad de arrendamientos ejecutados y operados.
- El contexto de `SalesComparatives` tiene una relación de [SK - Shared Kernel] con el contexto `MarketAndPropertyAnalysis` debido a que cuando se realizan los comparativos de las ventas, se puede hacer un análisis del mercado y de los inmuebles, en mismas proporciones donde uno puede trabajar en común con el otro.
- Los contextos `CommercialRealEstateInformation` y `MarketAndPropertyAnalysis` se relacionan de manera que uno es superior a otro [D - Downstream]/[U - Upstream] ya que dependen de las relaciones comerciales, pues el origen de todo el flujo radica en la negociación comercial y termina en un análisis de mercado. Por otro lado, se tiene una relación [C - Customer]/[S - Supplier] dado que estos deben trabajar juntos y de forma cercana para mostrar resultados y convertir el flujo del trabajo en un ciclo.

#### TO_BE:
- El contexto `MonolithBusinessImplementation` tiene una relación [D - Downstream] hacia `ArchitectureMigration` debido a que es la migración y la actualización tecnológica que se pretende realizar en la visión. También tiene un [ACL - Anticorruption Layer] debido a que los cambios que se hagan arriba no deberían afectar al componente actual. De forma contraria, el contexto `ArchitectureMigration` tiene una relación de [U - Upstream], [OHS - Open Host Service] y [PL - Published Language] debido a que es el contexto superior, describe un contexto superior que provee ciertas funcionalidades y tiene el conocimiento para las funcionalidades.
- El contexto `ArchitectureMigration` tiene una relación con `TimeZoneManagement`, `RemoteWorkBC`, `LegalDifference` y `ServiceLatency` de [SK - Shared Kernel] debido que estos se relacionan en el mismo grado de importancia en el desarrollo de la solución y tienen partes comunes en el dominio del modelo y la evolución de la solución, pues cada una impacta un área diferente pero son necesarias para el crecimiento y la adaptación en los nuevos mercados.
- El contexto `ArchitectureMigration` tiene una relación [D - Downstream] y [ACL - Anticorruption Layer] con `ConquerLatamMarket` debido a que es necesario implementar una nueva arquitectura para empezar a expandirse de la mejor manera y no quedarse cortos en las actividades cuando demanden nuevos servicios, como también para evitar el retroceso de los datos. En sentido contrario, tiene una relación de [U - Upstream], [OHS - Open Host Service] y [PL - Published Language] debido a que es el contexto superior, describe un contexto superior que provee ciertas funcionalidades y tiene el conocimiento para las funcionalidades.
- El contexto 'ConquerLatamMarket' tiene una relación [D - Downstream] y [ACL - Anticorruption Layer] con `GlobalExpansionMenaEneaOceania` debido a que es necesario primero expandirse en la region de Latam, pues tiene similitudes con Colombia, antes de empezar con mercados extranjeros; es importante tener conocimiento de la solución, y tener presente que dicha expansión no debería impactar lo logrado actualmente. En sentido contrario, tiene una relación de [U - Upstream], [OHS - Open Host Service] y [PL - Published Language] debido a que es el contexto superior, describe un contexto superior que provee ciertas funcionalidades y tiene el conocimiento para las funcionalidades, como también que para lograr una expansión global se tuvieron que tener hitos grandes de la solución, lo que la hace viable y capaz de expandirse con todo el conocimiento que tiene desde pasos iniciales.

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

# Proyecto: Máquina de Termoformado

## Descripción

Este proyecto consiste en la simulación de una **Máquina de Termoformado** en Python, con funcionalidades para calentar, formar material y enfriar. La máquina puede operar sobre un stock de material disponible, ajustando su temperatura para realizar las operaciones adecuadas. Se ha implementado siguiendo un enfoque de **Desarrollo Guiado por Pruebas (TDD)**, lo que permite verificar el correcto funcionamiento de la máquina en cada paso.

Además de la lógica de la máquina en Python, también se incluye una base de datos con información de varias máquinas y las operaciones que realizan.

## Funcionalidades Principales

1. **Calentar**: La máquina incrementa la temperatura de 5 en 5 grados hasta alcanzar su temperatura óptima.
2. **Formar**: Si la temperatura es óptima, la máquina puede procesar una cantidad determinada de material, reduciendo el stock disponible.
3. **Enfriar**: La máquina reduce su temperatura en 10 grados hasta alcanzar la temperatura ambiente.
4. **Reporte de Estado**: La máquina puede mostrar su estado actual, incluyendo temperatura y material disponible.

## Base de Datos

El proyecto también incluye una base de datos que almacena las máquinas disponibles y sus respectivas operaciones.

## TDD (Desarrollo Guiado por Pruebas)

### Beneficios de TDD:
- **Menos errores**: El código es probado continuamente, lo que ayuda a identificar problemas antes de que se acumulen.
- **Documentación del código**: Las pruebas sirven como una forma de documentación para el uso y comportamiento esperado de la clase.

### Experiencia usando TDD:
Aunque reconozco que TDD tiene muchos beneficios, no me siento del todo cómodo utilizándolo en esta etapa de mi aprendizaje. En algunos momentos, escribir las pruebas antes del código me resultó confuso, ya que no tenía del todo claro cómo sería la implementación. Sin embargo, entiendo que con más práctica puede ayudarme a mejorar la calidad del código y la forma en la que desarrollo nuevas funcionalidades.

## Bibliografía

Aquí se encuentran algunas de las fuentes que consulté para entender mejor el funcionamiento de una máquina de termoformado:

1. **"¿QUÉ ES UNA MÁQUINA DE TERMOFORMADO?"** - Esta pagina me ayudo a saber como funciona una maquina de termoformado y asi mismo me dio el pie para crear sus principales funcionalidades.[ Pagina ](https://sideco.com.mx/que-es-una-maquina-de-termoformado/#:~:text=Una%20M%C3%A1quina%20de%20Termoformado%20es,de%20hasta%20230%C2%B0%20celsius.)
3. **Guía de termoformado** - Revisé especificaciones de fabricantes para aprender sobre los ajustes de temperatura y material.[ Blog ](https://formlabs.com/latam/blog/termoformado/)
4. **Aprende SQL ahora**-me apoye sobre este video para realizar unas consulta que aun no habiamos dado. [ Video ](https://www.youtube.com/watch?v=uUdKAYl-F7g)

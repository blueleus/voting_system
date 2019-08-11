# Prueba práctica de desarrollo - Sistema de votación

## Objetivo general
Desarrollar un sistema de votación sencillo en entorno web que soporte máximo una pregunta de opción múltiple con única respuesta activa al tiempo, el sistema deberá restringir el envió de una opinión por IP por minuto.

## Resumen
El sistema debe:
* Debe permitir crear la pregunta con sus opciones de respuesta.
* Debe permitir especificar cual pregunta es la activa (Una y solo una al tiempo).
* Debe permitir a través de una interfaz publica realizar la votación.
* En caso que desde la misma IP se intente realizar más de una votación en menos de 1 minuto, deberá notificar que su voto no fue contabilizado.
* Debe mostrar el total de votaciones recibidas por cada opción de respuesta.

Para lo anterior se deberá:
* Modelar la base de datos teniendo en cuenta las 3 leyes básicas de normalización.
* Desarrollar un backend o área de administración que deberá permitir
    * Agregar/editar/eliminar preguntas (solo una pregunta puede estar activa a la vez).
    * Agregar/editar/eliminar opciones de respuesta.
    * Ver el total de votos recibido por respuesta.
    * Área publica (frontend) donde se deberá mostrar la pregunta activa, respuestas y opción para votar.
    * En caso de intentos de votaciones recurrentes por una misma IP el sistema deberá mostrar la alerta de “Votación no permitida” y no contara el voto.
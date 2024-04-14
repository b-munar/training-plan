# Instalacion

1. Clonar repositorio

```bash
git clone https://github.com/b-munar/training-plan

2. 

```bash
docker compose build
docker compose up
```


El servicio de Planes de entrenamiento.

## 1. Get exercises 

Retorna ejercicios.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6550/exercise</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "exercises": [
        {
            "id": "c7cadb54-c7c4-4fd7-89ea-eb72090818d8",
            "name": "exercise1",
            "description": "description 1",
            "timing_minutes": 2.5,
            "image_url": "test_image",
            "muscular_group": "tren inferior"
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 2. Post exercises 

Permite realizar creación de un ejercicio.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6550/exercise</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
  {
    "name": "exercise1",
    "description": "description 1",
    "timing_minutes": 2.5,
    "image_url": "test_image",
    "muscular_group": "tren inferior"
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "id": "c7cadb54-c7c4-4fd7-89ea-eb72090818d8",
    "name": "exercise1",
    "description": "description 1",
    "timing_minutes": 2.5,
    "image_url": "test_image",
    "muscular_group": "tren inferior"
}
```
</td>
</tr>
</tbody>
</table>

## 3. Get training plan of a trainer or user by role 

Retorna planes de entrenamiento ya sea del entrenador o del usuario, esta funcionalidad es controlada mediante el uso del rol proporcionada por el servicio de auth.
Nota: Los servicios contienen listas de otros elementos que se identifican por id, quedeben ser enviados por el front.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6550/training-plan</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "plans": [
        {
            "trainer": "28a3ad77-7d3c-47e3-9c42-858ca3ec5222",
            "user": "29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
            "days": [
                {
                    "day": "Monday",
                    "exercises": [
                        {
                            "id": "066b347d-0636-491e-9243-ba3adf13d112"
                        }
                    ]
                },
                {
                    "day": "Wednesday",
                    "exercises": [
                        {
                            "id": "02a2b11c-a799-4030-be5f-da31508cf3da"
                        },
                        {
                            "id": "559277ec-18bd-483c-88df-44871e5f43ad"
                        }
                    ]
                }
            ]
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 2. Post Traning plan 

Permite realizar creación de un plan de entrenamiento y asignarlo a un usuario especifico.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6550/training-plan</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
  {
        "user":"29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
        "days": [
            {
                "day": "Monday",
                "exercises": [
                    {
                        "id": "a20ba164-1b9d-486e-afd2-5ee5ec4bc06a"
                    }
                ]
            },
            {
                "day": "Wednesday",
                "exercises": [
                    {
                        "id": "aa8ca14e-57a8-44d6-8ebe-421013c47e07"
                    },
                    {
                        "id": "58bcce19-110f-4689-b9dd-33b8e66ac49b"
                    }
                ]
            }
        ]
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "trainer": "28a3ad77-7d3c-47e3-9c42-858ca3ec5222",
    "user": "29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
    "days": [
        {
            "day": "Monday",
            "exercises": [
                {
                    "id": "066b347d-0636-491e-9243-ba3adf13d112"
                }
            ]
        },
        {
            "day": "Wednesday",
            "exercises": [
                {
                    "id": "02a2b11c-a799-4030-be5f-da31508cf3da"
                },
                {
                    "id": "559277ec-18bd-483c-88df-44871e5f43ad"
                }
            ]
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>
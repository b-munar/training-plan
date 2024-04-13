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
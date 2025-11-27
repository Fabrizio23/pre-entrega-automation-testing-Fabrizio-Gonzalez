import  requests
import pytest
from utils.logger import logger

def test_get_user(url_base,encabezado):
    logger.info(f"Solicitud GET a {url_base}/2")
    response = requests.get(f"{url_base}/2", headers=encabezado)

    logger.info(f"Respuesta recibida: {response.status_code}")
    assert response.status_code == 200
    data = response.json()
    
    logger.info(f"Datos del usuario: {data}")
    assert data["data"]["id"] == 2

def test_create_user(url_base,encabezado):
    payload = {
        "name": "Chancleto", 
        "job": "Desarrollador"
    }
    response = requests.post(url_base, headers=encabezado, json=payload)
    logger.info(f"Respuesta recibida: {response.status_code}")
    assert response.status_code == 201

    data = response.json()

    logger.info(f"Datos del usuario creado: {data}")
    assert data["name"] == payload["name"]

def test_delete_user(url_base,encabezado):
    logger.info(f"Solicitud DELETE a {url_base}")
    response = requests.delete(f"{url_base}/2", headers=encabezado)
    
    logger.info(f"Respuesta recibida: {response.status_code}")
    assert response.status_code == 204
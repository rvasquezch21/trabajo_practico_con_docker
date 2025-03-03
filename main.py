from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Crear la instancia de la app
app = FastAPI()

# Modelo para los datos de login
class User(BaseModel):
    username: str
    password: str

# Base de datos simulada de usuarios
fake_users_db = {
    "usuario1": {
        "username": "usuario1",
        "password": "mi_contraseña_segura"
    }
}

# Ruta de login
@app.post("/login")
def login(user: User):
    # Verificar si el usuario existe y la contraseña es correcta
    stored_user = fake_users_db.get(user.username)
    if stored_user is None or stored_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"message": "Login exitoso!"}

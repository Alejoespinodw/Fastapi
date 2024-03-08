""" from fastapi import FastAPI,HTTPException,Body,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import requests
from datetime import datetime,timedelta,timezone
import base64
from pydantic import BaseModel,Field,model_validator
from datetime import datetime,timedelta,timezone


from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Annotated
from pydantic import BaseModel




app = FastAPI()

class Cotizar(BaseModel):
    anio:str
    iva: str
    ceroKM:str
    fechaVigencia:str = Field(datetime.now().strftime('%d/%m/%Y'))
    codInfoAuto: str
    codigoPostal: str
    gnc: str
    modalidad: str
    productor:str
    uso: str
    modelo: str
    marca:str
    version:str


class Emitir(BaseModel):
    presupuesto:str #-----
    productor:str #-----
    apellido:str #----
    nombres:str #----
    tipoDocumento:str #pendiente
    numeroDocumento:str
    sexo:str    #pendiente
    fechaNacimiento: str 
    posicionIva:str 
    email:str 
    prefijo:str 
    telefono:str 
    calle:str 
    numero:str 
    piso:str
    departamento:str
    codigoPostal:str
    identificador:str
    plan:str #pendiente
    patente:str 
    chasis:str
    motor:str 
    fechaVigencia:str = Field(datetime.now().strftime('%d/%m/%Y'))
    ddjj:str 
    porcentajeModalidad:str
    pep:str 
#---------------formaCobro-------------------#    
    formaCobro: str | None = None 
    titular: str | None = None
    gestor:str | None = None #----
    cbu: str |None = None
    tarjeta: str |None = None 
    nroTarjeta:str |None = None
    fechaVencimiento: str | None = None

    @model_validator(mode='after')
    def check(cls, values):
        for k, v in values:
            if not v:
                delattr(values, k)
        return values
 
#--------------------------------------------------MI LOGIN---------------------------------------------------------------------------------------#
SECRET_KEY = "3a8b50ae3f54e9b6f85fe9033261576efc69e2156304887880ef8fed79d74f3f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]

                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#-----------------------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

class Cliente():
    url = 'https://autos-test.apiexperta.com.ar/'
    password = '$3XP3rt4*BR0k3R'
    username = 'wokan'
    headers = {'api-key': '45dca47e-1e76-4c80-8757-48c8e3d03650'}

    def login(self):
        try:
            usuario = {
                "password": self.password,
                "user": self.username,
            }
            path = "login"

            r = requests.post(f'{self.url}{path}', json=usuario)
        
            r.raise_for_status()
            x=r.json()
            self.headers['Authorization'] = f"Bearer {x['jwt']}"
            return True
        except requests.RequestException as e:
            print(f"Error en la solicitud: {e}")                        

    
    def post(self, path, payload):
        r = requests.post(f'{self.url}{path}', headers=self.headers, json=payload)
        print(r.text)

        if r.status_code != 200:
            raise HTTPException(status_code=400,detail=r.text)
        try:
            return r.json()
        
        except requests.RequestException as e:
            print(f"datos incorrectos{e.response.text}")
    

    def get(self, path, params:str | None = None):
        
            r = requests.get(f'{self.url}{path}', headers=self.headers,params=params)
            if r.status_code != 200:
                raise HTTPException(status_code=400,detail=r.text)
            try:  
                return r.json()
            except requests.RequestException as e:
                print(f"aca hay un error{e.response}")


    def custom_get(self, path, params:str | None = None):
        try:
            r = requests.get(f'{self.url}{path}', headers=self.headers,params=params)
            r.raise_for_status()

            return r.content
        except requests.RequestException as e:
            raise HTTPException(status_code=400,detail=f"aca hay un error che{e.response.text}")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------#


#COTIZACIONES
@app.post("/cotizaciones", tags=["cotizacion-controller"])
async def cotizaciones(
    cotizar: Annotated[Cotizar, Body(
        examples=[
            {
                "anio": "2013",
                "iva": "5",
                "ceroKM": "N",
                "fechaVigencia": "27/02/2024",
                "codInfoAuto": "0120444",
                "codigoPostal": "5000",
                "gnc": "N",
                "modalidad": "EX0",
                "productor": "972",
                "uso": "1",
                "modelo": "CRUZE",
                "marca": "CHEVROLET",
                "version": "0120444"
            }
        ]
    )],
    current_user: User = Depends(get_current_active_user)
):
    try:
        cliente = Cliente()
        login = cliente.login()

        if login:
            result = cliente.post("cotizaciones", cotizar.model_dump())            
            return result
        else:
            raise HTTPException(status_code=401, detail="Error de autenticación")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error interno del servidor: {str(e)}")



#EMISIONES
@app.post('/emisiones',tags=["emision-controller"])
async def emisiones(emitir:Annotated[Emitir,Body(
            openapi_examples={
                "cbu": {
                    "summary": "Pago con cbu",
                    "value": {
                        "presupuesto": "2422249",
                        "productor": "972",
                        "apellido": "Lascano",
                        "nombres": "Sebastian",
                        "tipoDocumento": "DNI",
                        "numeroDocumento": "43956432",
                        "sexo": "M",
                        "fechaNacimiento": "10/03/2000",
                        "posicionIva": "5",
                        "email": "sebastian@gmail.com",
                        "prefijo": "351",
                        "telefono": "6196039",
                        "calle": "sarmiento",
                        "numero": "43",
                        "piso": "3",
                        "departamento": "b",
                        "codigoPostal": "1000",
                        "identificador": "Referencia",
                        "plan": "942",
                        "patente": "AZ234DE",
                        "chasis": "1GNCS13Z6M0246432",
                        "motor": "52WVC10329",
                        "fechaVigencia": "29/02/2024",
                        "ddjj": "N",
                        "porcentajeModalidad": "30",
                        "pep": "N",
                        "formaCobro": "BA",
                        "titular": "Alejo Espino",
                        "gestor": "110001",
                        "cbu": "0110599520000001235579",
                    },
                },
                "tarjeta": {
                    "summary": "Pago con tarjeta",
                    "value": {
                        "presupuesto": "2422249",
                        "productor": "972",
                        "apellido": "Lascano",
                        "nombres": "Sebastian",
                        "tipoDocumento": "DNI",
                        "numeroDocumento": "43956432",
                        "sexo": "M",
                        "fechaNacimiento": "10/03/2000",
                        "posicionIva": "5",
                        "email": "sebastian@gmail.com",
                        "prefijo": "351",
                        "telefono": "6196039",
                        "calle": "sarmiento",
                        "numero": "43",
                        "piso": "3",
                        "departamento": "b",
                        "codigoPostal": "1000",
                        "identificador": "Referencia",
                        "plan": "942",
                        "patente": "AZ234DE",
                        "chasis": "1GNCS13Z6M0246432",
                        "motor": "52WVC10329",
                        "fechaVigencia": "29/02/2024",
                        "ddjj": "N",
                        "porcentajeModalidad": "30",
                        "pep": "N",
                        "formaCobro": "BA",
                        "titular": "Alejo Espino",
                        "tarjeta": "74",
                        "nroTarjeta":"4870177368324427",
                        "fechaVencimiento":"03/2024"
                    },
                },
                "cupon": {
                    "summary": "Pago con cupon",
                    "value": {
                        "presupuesto": "2422249",
                        "productor": "972",
                        "apellido": "Lascano",
                        "nombres": "Sebastian",
                        "tipoDocumento": "DNI",
                        "numeroDocumento": "43956432",
                        "sexo": "M",
                        "fechaNacimiento": "10/03/2000",
                        "posicionIva": "5",
                        "email": "sebastian@gmail.com",
                        "prefijo": "351",
                        "telefono": "6196039",
                        "calle": "sarmiento",
                        "numero": "43",
                        "piso": "3",
                        "departamento": "b",
                        "codigoPostal": "1000",
                        "identificador": "Referencia",
                        "plan": "942",
                        "patente": "AZ234DE",
                        "chasis": "1GNCS13Z6M0246432",
                        "motor": "52WVC10329",
                        "fechaVigencia": "29/02/2024",
                        "ddjj": "N",
                        "porcentajeModalidad": "30",
                        "pep": "N",
                        "formaCobro": "CC"
                    },
                },
            },
        ),
    ],
    current_user: User = Depends(get_current_active_user)
):
    payload = emitir.model_dump()
    cliente = Cliente()
    login = cliente.login() 
    

    if login:            
        
        if emitir.formaCobro == "BA":
            payload["titular"]=emitir.titular
            payload["gestor"] = emitir.gestor
            payload["cbu"] = emitir.cbu

            
        elif emitir.formaCobro == "TM":
                payload["titular"] = emitir.titular
                payload["tarjeta"] = emitir.tarjeta
                payload["nroTarjeta"] = emitir.nroTarjeta
                payload["fechaVencimiento"] = emitir.fechaVencimiento
                print(payload)

        
        result = cliente.post("emisiones", payload)
        return result
        
    
        
           



#---------------------------------------------COMMONS----------------------------------------------------------------------------#



@app.get("/commons/marcas",tags=["commons-controller"])
async def marcas(anio:str,current_user: User = Depends(get_current_active_user)):
    try:
        cliente = Cliente()
        login = cliente.login()

        if login:
            params = {"anio": anio}
            result = cliente.get("commons/marcas", params)
            return result
        else:
            raise HTTPException(status_code=401, detail="Error de autenticación")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor ")


@app.get("/commons/modelos",tags=["commons-controller"])
async def modelo(anio:str,marca:str,current_user: User = Depends(get_current_active_user)):
    try:
        cliente =Cliente()
        login = cliente.login()
        if login:
            params = {"anio":anio,
                    "marca":marca}
            result = cliente.get("commons/modelos",params)
            return result
        else:
            raise HTTPException(status_code=401, detail="Error de autenticacion")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
        

@app.get("/commons/versiones",tags=["commons-controller"])
async def versiones(anio:str,
                    ceroKm:str,
                    marca:str,
                    modelo:str,
                    current_user: User = Depends(get_current_active_user)):
    try:
        cliente = Cliente()
        login = cliente.login()
        if login:
            params={"anio":anio,
                    "ceroKm":ceroKm,
                    "marca":marca,
                    "modelo":modelo}
            result = cliente.get("commons/versiones",params)
            return result
        else:
            raise HTTPException(status_code=401, detail="Error de autenticacion")
    except Exception as e:
        raise HTTPException(status_code=500,detail="Error interno del servidor")


@app.get("/commons/bancos",tags=["commons-controller"])
async def marcas(codigo:str,current_user: User = Depends(get_current_active_user)):
    try:
        cliente = Cliente()
        login = cliente.login()
        if login:
            params = {"codigo":codigo}
            result = cliente.get("commons/bancos",params)
            return result
        else:
            raise HTTPException(status_code=401,detail="Error de autenticacion")
    except Exception as e :
        raise HTTPException(status_code=500,detail="Error interno del servidor")


@app.get("/commons/tarjetas",tags=["commons-controller"])
async def tarjetas(current_user: User = Depends(get_current_active_user)):
    cliente = Cliente()
    login = cliente.login()

    if login:

        result = cliente.get("commons/tarjetas")
        return result

@app.get("/commons/forma-pago",tags=["commons-controller"])
async def formapago(productor:str,current_user: User = Depends(get_current_active_user)):
    cliente= Cliente()
    login = cliente.login()
    if login:
        params = {"productor":productor}
        result = cliente.get("commons/forma-pago",params)
        return result



@app.get("/commons/valores-gnc",tags=["commons-controller"])
async def gnc(current_user: User = Depends(get_current_active_user)):
    cliente = Cliente()
    login = cliente.login()
    if login:
        result = cliente.get("commons/valores-gnc")
        return result



@app.get("/commons/modalidades-productor",tags=["commons-controller"])
async def modalidades(productor:str,vigencia:str | None = None,current_user: User = Depends(get_current_active_user)):
    cliente = Cliente()
    login = cliente.login()
    if login:
        params = {"productor":productor,
                  "vigencia":vigencia}
        result = cliente.get("commons/modalidades-productor",params)
        return result

@app.get("/commons/actividades",tags=["commons-controller"])
async def actividades(current_user: User = Depends(get_current_active_user)):
    cliente = Cliente()
    login = cliente.login()
    if login:
        result =cliente.get("commons/actividades")
        return result 

@app.get("/commons/responsabilidades",tags=["commons-controller"])
async def responsabilidades(current_user: User = Depends(get_current_active_user)):
    cliente = Cliente()
    login = cliente.login()
    if login:
        result =cliente.get("commons/responsabilidades")
        return result


@app.get("/commons/sex",tags=["commons-controller"])
async def sex(current_user: User = Depends(get_current_active_user)):
    r=[{"codigo":"M","descripcion":"masculino"},{"codigo":"F","descripcion":"femenino"}]
    return r

@app.get("/commons/tipodocumento",tags=["commons-controller"])
async def document(current_user: User = Depends(get_current_active_user)):
    r = [{"codigo":"DNI","descripcion":"Documento nacional de identidad"}]
    return r



#--------------------------------------------------------------------------------------------------------------------------------------#

    
#DOCUMENTACION





@app.get("/documentacion/frente-poliza",tags=["documentacion-controller"])
async def pdf(poliza:str,productor:str,current_user: User = Depends(get_current_active_user)):
    
    cliente = Cliente()
    login = cliente.login()

    try:
        if login:
            params = {"poliza":poliza,
                    "productor":productor}
            result = cliente.custom_get("documentacion/frente-poliza",params)
            
            with open("POLIZA_COMPLETA5.pdf", "wb") as archivo_pdf:
                archivo_pdf.write(result)
            
            pdf_base64 = base64.b64encode(result).decode("utf-8")
            
            return {"pdf_base64": pdf_base64}
        else:
            raise HTTPException(status_code=401,detail="Error de autenticacion")
    except Exception as e :
        
        raise HTTPException(status_code=500,detail=f"Error interno del servidor: {str(e)}")




@app.get("/documentacion/cupon-pago", tags=["documentacion-controller"])
async def pdf(poliza: str, productor: str,current_user: User = Depends(get_current_active_user)):
    cliente = Cliente()
    login = cliente.login()
    try:
        if login:
            params = {"poliza": poliza, "productor": productor}
            result = cliente.custom_get("documentacion/cupon-pago", params)
        
            with open("cupon_pago.pdf", "wb") as archivo_pdf:
                        archivo_pdf.write(result)

            pdf_base64 = base64.b64encode(result).decode("utf-8")

            return {"pdf_base64": pdf_base64}
            
        else:
            raise HTTPException(status_code=401, detail="Error de autenticación")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
 """




#01874201 nro de poliza ejemplo
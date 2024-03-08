from fastapi import FastAPI,HTTPException,Body,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import base64
from datetime import timedelta
from typing import Annotated

from modelos.esquemas import *
from modelos.cliente import *
from modelos.mylogin import *

app = FastAPI()

#--------------------------------------------------MI LOGIN---------------------------------------------------------------------------------------#

@app.post("/token",tags=["Login"])
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

@app.get("/users/me/", response_model=User,tags=["Login"])
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

#--------------------------------------------------------COTIZACIONES-----------------------------------------------------------------------#
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

#------------------------------------------------------------EMISIONES----------------------------------------------------------------------#
    
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

#------------------------------------------------------COMMONS----------------------------------------------------------------------------#

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

#-------------------------------------------------------------DOCUMENTACION-------------------------------------------------------------------------#

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

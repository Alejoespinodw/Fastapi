""" #creo Login de apiexperta 
@app.post("/login")
def login(username: str, password: str):
    usuario = {
        "username": "wokan",
        "password": "$3XP3rt4*BR0k3R"
    }
    
    url = "https://autos-test.apiexperta.com.ar"
    x = requests.post(url,usuario)
    print(x)
    return x """

""" 
@app.post("/cotizaciones")
async def cotizaciones():
    header ={
        "Authorization":"Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJCcm9rZXIiLCJpYXQiOjE3MDkwNDA1OTksImV4cCI6MTcwOTA0NDQ5OSwiaWQiOiJ3b2thbiIsIm5vbWJyZSI6IldPS0FOIiwidGlwb1VzdWFyaW8iOiJCUk9LRVIiLCJpZFVzdWFyaW8iOiJ3b2thbiIsInJvbGVzIjpbIlJPTF9WRU5UQV9BVVRPUyJdLCJpZFZlbmRlZG9yIjoiMjI0MyIsIm5vbWJyZVZlbmRlZG9yIjoiV09LQU4ifQ.URaNbH1wC_7I-a70n5u8qPQODczqgLvu_B5pFAWfBOHVVXgweEtps79pakpPH9rSN-mPjBcglUOzog12d8TbJjk1kWYjnx7ZAx43kXu37hzCA4t4-0FPKe1UxFtZUC1Ot9g8KsuHx1FVdf4PGd3w4eewWKBKe-7AzqFWrdVY2zQ",
        "api-key":"45dca47e-1e76-4c80-8757-48c8e3d03650"
    }
    payload = {
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
    print(payload)
    url = "https://autos-test.apiexperta.com.ar/cotizaciones"
    r = requests.post(url,headers=header,json=payload)
    return r.text """









""" @app.post("/login")
async def login(user:str,contrasenia:str):
    usuario = {
        "password": "$3XP3rt4*BR0k3R",
        "user": "wokan"
    }
    url = "https://autos-test.apiexperta.com.ar/login"
    r = requests.post(url,json=usuario)
    print(r.json())
    return r.json() """



"""
x=r.json()
print(x["sasras"]["sara"])
"""


"'""""  header ={
        #muestro el token
        
        "api-key":"45dca47e-1e76-4c80-8757-48c8e3d03650"
    }
    
    cotizar_dict = cotizar.model_dump()
    url = "https://autos-test.apiexperta.com.ar/cotizaciones"
    r = requests.post(url,headers=header,json=cotizar_dict)
    return r.text"""


""" x=r.json()

    if 'jwt' in x:
        token = x['jwt']
    else:
        return "sasarsras"

    cotizar_dict = cotizar.model_dump()
    url = "https://autos-test.apiexperta.com.ar/cotizaciones"

    headers = {
        "Authorization": f"Bearer {token}",
        "api-key":"45dca47e-1e76-4c80-8757-48c8e3d03650"
    }
    r = requests.post(url, headers=headers, json=cotizar_dict)
    return r.text """







""" 
@app.post("/login",tags=["login-controller"])
async def login(user:str,contrasenia:str):
    usuario = {
        "password": "$3XP3rt4*BR0k3R",
        "user": "wokan"
    }
    url = "https://autos-test.apiexperta.com.ar/login"
    r = requests.post(url,json=usuario)
    print(r.json())
    return r.json() """








""" def login(self):
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
            print(f"hubo un herror:{e}")
                                  

    
    def post(self, path, payload):
        try:
            r = requests.post(f'{self.url}{path}', headers=self.headers, json=payload)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"hubo un error{e}")
    
    def get(self, path, params):
        try:
            r = requests.get(f'{self.url}{path}', headers=self.headers,params=params)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"aca hay un error{e}")
 """






""" 
 if login:
        
        if emitir.formaCobro == "cbu":
            result = cliente.post("emisiones", emitir.model_dump())
        elif emitir.formaCobro.lower() == "tarjeta":
            result = cliente.post("emisiones", emitir.model_dump())
        else:
            raise HTTPException(status_code=400, detail="error")

    return result """








""" # EMISIONES
@app.post('/emisiones', tags=["emision-controller"])
async def emisiones(emitir: Emitir):
    cliente = Cliente()
    login = cliente.login()
    
    if login:
        forma_cobro = emitir.formaCobro
        if forma_cobro == "CC":
            # Lógica para pago con cupón
            resultado = "Emisión con cupón"
        elif forma_cobro == "TM":
            # Lógica para pago con tarjeta
            resultado = "Emisión con tarjeta"
        elif forma_cobro == "BA":
            # Lógica para pago con CBU
            resultado = "Emisión con CBU"
        else:
            resultado = "Forma de pago no reconocida"
        
        return {"resultado": resultado}
 """








""" @app.get("/documentacion/frente-poliza")
async def pdf(poliza:str,productor:str):
    cliente = Cliente()
    login = cliente.login()
    if login:
        params = {"poliza":poliza,
                  "productor":productor}
        result = cliente.get("documentacion/frente-poliza",params)
        return result
 """












"""     document =result["archivoZip"]

        data = base64.b64decode(document)

        with open("POLIZA_COMPLETA1.pdf", "wb") as archivo_pdf:
            archivo_pdf.write(data)
        return result """

'''  contenido_pdf =result.content
        pdf_base64 = base64.b64encode(contenido_pdf).decode()
        return JSONResponse(content={"pdf_base64": pdf_base64}, status_code=200)'''



























"""requests.RequestException: Esta es la excepción base para todas las excepciones generadas por solicitudes HTTP. 
Se manejan todas las excepciones relacionadas con la comunicación con el servidor.
r.raise_for_status(): Este método comprueba si la respuesta HTTP tiene un código de estado exitoso (2xx). 
Si no es así, se genera un requests.HTTPError, que es capturado por la cláusula except. """



"""Aquí, as e significa que la excepción capturada se asigna a la variable e. Dentro del bloque except, puedes utilizar e para hacer referencia a la excepción capturada. 
En este caso, se utiliza e para imprimir un mensaje de error que incluye información sobre la excepción. 
Sin embargo, podrías usar e para realizar otras acciones, como registrar el error en un archivo de registro, notificar al usuario, etc. 
El nombre e es una convención común, pero podrías elegir cualquier nombre válido para la variable de excepción.

En resumen, as se utiliza para asignar un nombre a la excepción capturada, lo que te permite trabajar con ella dentro del bloque except. """
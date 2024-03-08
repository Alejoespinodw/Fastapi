''''    "anio": "2013",
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
        "version": "0120444" '''



'''
{
{
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
  "titular": "Sebastian Lascano",
  "gestor": "110001",
  "cbu": "0110599520000001235579"
}
}
'''




""" 

{
  "fechaCreacion": "2024-02-29T16:03:04.060575",
  "numeroPoliza": "01870401",
  "cantidadMensualidades": 1,
  "premio": 54008,
  "prima": 43837.4,
  "patente": "BZ234ZT",
  "numeroDocumento": "43956876",
  "hashcia": "45dca47e-1e76-4c80-8757-48c8e3d03650",
  "altaPolizaApi": false,
  "email": "sebastian@gmail.com",
  "inicioVigencia": "2024-02-29",
  "finVigencia": "2025-02-28"
} """



""" if r.status_code != 200:

            raise HTTPException(status_code=400,detail=r.json())
        try:
            return r.json()
        
        except requests.RequestException as e:
            print(f"datos incorrectos{e.response.text}") """

import requests
from fastapi import HTTPException, HTTPException


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
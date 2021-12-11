import { Injectable } from "@angular/core";
import axios from "axios";
@Injectable({
    providedIn: 'root'
})

export class AxiosService{
    urlLogin:string = 'https://ager-auth-app.herokuapp.com/login/';
    urlGetUserByUserName:string = 'https://ager-auth-app.herokuapp.com/buscar/username/';
    constructor() {
        
    }
    getUsername(){
        var username1 = localStorage.getItem("username")
        return axios.get(this.urlGetUserByUserName+username1).then(resp=>{
            console.log(resp.data)
            alert(resp.data)
        })
    }
    logIn(username:string,password:string,){
        let body = {
            "username": username,
            "password": password
        }
        return axios.post(this.urlLogin, body).then(resp =>{
                localStorage.setItem("refresh",resp.data["refresh"])
                localStorage.setItem("access",resp.data["access"])
                alert("Las credenciales son correctas")
                return "correcto"
        }).catch(() => {
            alert("Las credenciales son incorrectas")
          });
    };
    
}
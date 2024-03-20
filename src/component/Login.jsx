import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";


export default function Login({setIsAuth, setActiveUser}){
    const [users, setUsers]= useState([])
    const [name, setName]= useState('')
    const [password, setPassword]= useState('')
    const [error, setError] = useState ('')
    const navigate = useNavigate()




    useEffect(() => {
        fetch('http://localhost:3005/users')
        .then(data => data.json())
        .then(data => setUsers(data))
   },[])

   function login(event){
        event.preventDefault() 
        for (let user of users)
            if (user.name === name && user.password === password){
                setIsAuth(true)
                setError('')
                navigate('/')
                setActiveUser(user.id)
            } else {
                setError('Неверные данные')
            }
        }
   
    

   
   
   return(
        <div>
            <h1>Login</h1>
            <form className="form">
               <input type="text" className="input" placeholder="Name" value={name} onChange={event => setName(event.target.value)} />
               <input type="text" className="input" placeholder="Password" value={password} onChange={event => setPassword(event.target.value)} />
               <button onClick={login}>Login</button>
            </form>
        </div>
    )
}

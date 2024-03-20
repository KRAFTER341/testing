import React, { useState} from "react";
import { useNavigate } from "react-router-dom";


export default function Registration(){
    const [users, setUsers]= useState([])
    const [name, setName]= useState('')
    const [password, setPassword]= useState('')
    const [password2, setPassword2]= useState('')
    const [error, setError] = useState ('')
    const navigate = useNavigate()



   function registration(event){
        event.preventDefault() 
        if (name && password && password === password2){
        const newUser = {name, password , avatarUrl: ''};
        fetch('http://localhost:3005/users',{
            method: 'Post',
            headers:{"content-type":'application/json'},
            body: JSON.stringify(newUser)
        })
    }
}
   
    

   
   
   return(
        <div>
            <h1>Registration</h1>
            <form className="form">
                <p className="error">Error</p>
               <input type="text" className="input" placeholder="Name" value={name} onChange={event => setName(event.target.value)} />
               <input type="text" className="input" placeholder="Password" value={password} onChange={event => setPassword(event.target.value)} />
               <input type="text" className="input" placeholder="Password2" value={password2} onChange={event => setPassword2(event.target.value)} />
               <button onClick={registration}>Registration</button>
               <button onClick={() => navigate('/')}>Back</button>
            </form>
        </div>
    )
}


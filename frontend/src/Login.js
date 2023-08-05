import React, { useState, useEffect, useRef } from 'react';
import './messages.css'

const Login = (props) => {
    const [name, setName] = useState("")

    const changeName = (e) =>{
        setName(e.target.value);
    }

    const login = () => {
        props.setLogin(name);
        props.changedLogged(true);
    }

    const handleKeyDown = (event) => {
        if (event.key == "Enter") {
            login();
        }
    }

    return <>
        Nazwa:
        <input value={name} onChange={changeName} onKeyDown={handleKeyDown}></input>
        <div onClick={login} className='btn'>Wejdź</div>
    </>
}
export default Login;
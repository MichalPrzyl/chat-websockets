import React, { useState, useEffect, useRef } from 'react';
import Login from './Login';
import Message from './Message';
import './messages.css'


let url = `ws://192.168.1.19:8000/ws/test2/`
const chatSocket = new WebSocket(url);

const AppFunction = () => {
    const [logged, setLogged] = useState(false);
    const [login, setLogin] = useState("");

    const [message, setMessage] = useState("");
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        chatSocket.onopen = () => {
            console.log('WebSocket opened')
        }

        chatSocket.onmessage = function (e) {
            let data = JSON.parse(e.data);
            setMessages(messages => [...messages, {
                message: data.message,
                user: data.user
            }])
        }
    }, [])

    // Callback after changeing 'messages' state
    useEffect(() => {
        const scrollableDiv = document.getElementById('scrollable-div');
        if (scrollableDiv != null){
            scroolToDown(scrollableDiv);
        }
    }, [messages])


    // function that moves document to bottom so we can see message input
    const scroolToDown = (scrollableDiv) => {
        scrollableDiv.scrollTo({
            top: 9999999,
            behavior: 'smooth'
        })
    }

    const sendHandler = (e) => {
        chatSocket.send(JSON.stringify({
            'user': login,
            'message': message
        }))
        setMessage("");
    }

    const changeMessage = (e) => {
        setMessage(e.target.value);
    }

    const changedLogged = (value) => {
        setLogged(value)
    }

    const handleKeyDown = (event) => {
        if (event.key == "Enter") {
            sendHandler();
        }
    }

    return <>
        {logged ?
            <div className='app-container'>
                <h1>MP Chat 1.0.0</h1>

                {/* messages */}
                <div className='messages-container' id='scrollable-div'>
                    {messages ?
                        messages.map((element, index) =>
                            <Message
                                key={index}
                                user={element.user}
                                message={element.message}
                                isMyOwnUser={element.user === login}
                            />
                        ) : null}

                    {/* message input */}
                    <input
                        onKeyDown={handleKeyDown}
                        value={message} onChange={changeMessage}
                        className="message-input"
                        autoFocus>
                    </input>

                    <div>
                        <div id='send-btn'
                            onClick={sendHandler}
                            className='btn'>
                            Wyślij</div>
                    </div>
                </div>
            </div>
            :
            <div className='app-container'>
                <Login
                    changedLogged={changedLogged}
                    setLogin={setLogin}
                />
            </div>}


    </>
}
export default AppFunction;
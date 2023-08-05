import './message.css'
const Message = (props) => {
    const { user, message, isMyOwnUser } = props;

    return <>
        <div className={`message-wrapper ${isMyOwnUser ? "my-own-message" : null}`}>
            <div className='user'>{user}</div>
            <div>{message}</div>
        </div>
    </>
}

export default Message;
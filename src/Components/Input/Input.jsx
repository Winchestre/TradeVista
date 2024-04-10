export default function Input({ type, placeholder, name,  }) {
    return (
        <input 
            type={type} 
            name={name} 
            placeholder={placeholder} 
            style={{
                height: '70px',
                width: '100%',
                paddingLeft: '20px',
                border: '1px solid #c9c9c9',
                outline: 'none',
                color: '#5c5c5c',
                fontSize: '16px',
            }}
        />
    )
}
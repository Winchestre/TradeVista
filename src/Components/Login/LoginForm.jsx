import { useState } from "react";
import Input from "../Input/Input";

export default function LoginForm() {
    const [check, setCheck] = useState(false);

    const handleCheck = () => {
        setCheck(!check);
        check === false ? console.log('Checked!') : console.log('Unchecked!');
    }

    return (
        <form action="">
            <div className="flex flex-col gap-3 mt-3">
                <Input type='text' name='username' placeholder='Your Name' />
                <Input type='email' name='email' placeholder='Your Email' />
                <Input type='password' name='password' placeholder='Your Password' />
            </div>
            <div className="flex items-center mt-3 gap-3 text-[#5c5c5c] text-lg font-semibold">
                <input type="checkbox" checked={check} onChange={handleCheck} className="cursor-pointer"/>
                <p>By continuing, i agree to the terms of use & privacy policy</p>
            </div>
            <button 
                style={{
                    width: '540px',
                    height: '72px',
                    color: 'white',
                    background: '#ff4141',
                    marginTop: '20px',
                    border: 'none',
                    fontSize: '24px',
                    fontWeight: '500',
                    cursor: 'pointer'
                }} 
                disabled={check}
                type="submit">Continue</button>
            <p className="mt-4 text-[#5c5c5c] text-lg font-semibold">Already have an account? <span className="text-[#ff4141] font-semibold">Login Here</span></p>
        </form>
    )
}
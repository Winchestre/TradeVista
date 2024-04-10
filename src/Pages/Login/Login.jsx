import LoginForm from "../../Components/Login/LoginForm";

export default function Login() {
    return (
        <div className="w-full bg-[#fce3fe] pt-3">
            <div className="m-auto w-[580px] h-[600px] bg-white py-3 px-5">
                <h1 className="my-6 text-2xl font-semibold">Sign Up</h1>
                <LoginForm />
            </div>
        </div>
    )
}
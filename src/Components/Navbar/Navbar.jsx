import logo from '../../assets/logo.jpg'
import { TiShoppingCart } from "react-icons/ti";
import Header from '../Header/Header';
import Button from '../Button/Button';
import { Link } from 'react-router-dom';
import { menuItems } from '../../Constants/data';

export default function Navbar() {
    return (
        <nav className='flex items-center justify-between border border-b-2 py-6 px-12 shadow-md bg-neutral-100'>
            <Link to='/' className='flex gap-2'>
                <img src={ logo } width='40px' height='40px' alt='log' />
                <Header />
            </Link>
            <ul className='flex gap-8 text-base'>
                {
                    menuItems.map((menuItem, index) => (
                        <li key={index}>
                            <Link to={menuItem.path} className='hover:text-neutral-500'>{menuItem.label}</Link>
                        </li>
                    ))
                }
            </ul>
            <div className='flex items-center gap-2'>
                <Link to='/login'><Button label='Login' color='#394c61' /></Link>
                <Link to='/cart'>
                    <TiShoppingCart style={{
                        width: '25px',
                        height: '25px',
                    }} />
                </Link>
                <div className="count w-[20px] h-[20px] flex justify-center items-center mt-[-28px] ml-[-23px] rounded-full text-xs bg-red-500 text-white">0</div>
            </div>
        </nav>
    )
}
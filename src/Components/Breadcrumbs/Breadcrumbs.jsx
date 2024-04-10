import { Link } from 'react-router-dom'
import { arrow_right } from '../../assets/icons/index'

const Breadcrumbs = ({ menu, subMenu, nextMenu, subNextMenu }) => {
    return (
        <div className="flex items-start justify-start gap-1 mb-3">
            {/* <p className="text-base font-light leading-tight text-black">{menu}</p> */}
            <Link to='/' className="text-base font-light leading-tight text-black hover:text-neutral-500">{menu}</Link>
            <img src={arrow_right} alt='arrow-right' />
            <p className="text-base font-semibold leading-tight text-black">{subMenu}</p>
            {nextMenu && 
                <>
                    <img src={arrow_right} alt="arrow-right" />
                    <p className="text-base font-semibold leading-tight text-black">{nextMenu}</p>
                </>
            }
            {
                subNextMenu &&
                <>
                    <img src={arrow_right} alt="arrow-right" />
                    <p className="text-base font-semibold leading-tight text-black">{subNextMenu}</p>
                </>
            }
        </div>
    )
}

export default Breadcrumbs
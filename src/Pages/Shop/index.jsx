import Breadcrumbs from "../../Components/Breadcrumbs/Breadcrumbs";
import { products } from "../../Constants/data";

export default function Shop() {
    return (
        <div>
            <Breadcrumbs menu='Home' subMenu='Shop' />
            <ul className="grid grid-cols-3 gap-3">
                {
                    products.map(product => (
                        <li key={product.id} className="">
                            <div>
                                <img src={product.imageUrl} alt={product.name} />
                                <div>
                                    
                                </div>
                            </div>
                        </li>
                    ))
                }
            </ul>
        </div>
    )
}
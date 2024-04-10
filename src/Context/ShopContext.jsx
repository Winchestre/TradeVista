import { createContext } from "react";
import { products } from "../Constants/data";

export const ShopContext = createContext(null);

const ShopContextProvider = ({ children }) => {
    const contextValue = { products };

    return (
        <ShopContext.Provider value={contextValue}>
            {children}
        </ShopContext.Provider>
    )
}
export default ShopContextProvider;


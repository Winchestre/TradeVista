import Navbar from "./Components/Navbar/Navbar"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Products from "./Pages/Products/Products"
import ShopCategory from "./Pages/Shop/ShopCategory"
import Cart from "./Components/Cart/Cart"
import Login from "./Pages/Login/Login"
import Shop from "./Pages/Shop"
import Footer from "./Components/Footer/Footer"
import Home from "./Pages"
import About from "./Pages/About/About"
import Market from "./Pages/Market/Market"

function App() {

  return (
    <div className=''>
      <BrowserRouter>
        <Navbar />
        <main className="w-[90%] mx-auto mt-3">
          <Routes>
            <Route path="/" index element={<Home />} />
            <Route path="/shop" element={<Shop />} />
            <Route path="/about" element={<About />} />
            <Route path="/market" element={<Market />} />
            <Route path="/products" element={<Products />}>
              <Route path=":productId" element={<Products />} />
            </Route>
            {/* <Route path="/mens" element={<ShopCategory category="men" />} />
          <Route path="/womens" element={<ShopCategory category="women" />} />
          <Route path="/kids" element={<ShopCategory category="kid" />} /> */}
            <Route path="/cart" element={<Cart />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </main>
      </BrowserRouter>
      <Footer />
    </div>
  ) 
}

export default App

import {Products} from "./components/Products";
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {CreateProducts} from "./components/CreateProducts";
import {Orders} from "./components/Orders";
import { OrderList } from "./components/OrderList";

function App() {
    return <BrowserRouter>
        <Routes>
            <Route path="/" element={<Products/>}/>
            <Route path="/create" element={<CreateProducts/>}/>
            <Route path="/orders" element={<Orders/>}/>
            <Route path="/ordersList" element={<OrderList/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;
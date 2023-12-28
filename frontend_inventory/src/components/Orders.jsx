import {useEffect, useState} from "react";
import {useNavigate} from 'react-router-dom';

export const Orders = () => {
    const [product_id, setId] = useState('');
    const [quantity, setQuantity] = useState();
    const [message, setMessage] = useState('Buy your favorite product');

    const navigate = useNavigate();

    useEffect(() => {
        (async () => {
            try {
                if (product_id) {
                    const response = await fetch(`http://localhost:8001/products/${product_id}`);
                    const content = await response.json();
                    const price = parseFloat(content.price) * parseInt(quantity);
                    setMessage(`Your product price is $${price}`);
                }
            } catch (e) {
                setMessage('Buy your favorite product')
            }
        })();

    }, [product_id, quantity]);

    const submit = async e => {
        e.preventDefault();
    //    const response =  
       await fetch('http://localhost:8000/orders', {
            method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
                product_id, quantity
            })
        });
        // const content = await response.json();
        // console.log("🚀 ~ file: Orders.jsx:32 ~ submit ~ content:", content)
        setMessage('Thank you for your order!');
        navigate(-1);

    }

    return <div className="container">
        <main>
            <div className="py-5 text-center">
                <h2>Checkout form</h2>
                <p className="lead">{message}</p>
            </div>

            <form onSubmit={submit}>
                <div className="row g-3">
                    <div className="col-sm-6">
                        <label className="form-label">Product</label>
                        <input className="form-control"
                               onChange={e => setId(e.target.value)}
                        />
                    </div>

                    <div className="col-sm-6">
                        <label className="form-label">Quantity</label>
                        <input type="number" className="form-control"
                               onChange={e => setQuantity(e.target.value)}
                        />
                    </div>
                </div>
                <hr className="my-4"/>
                <button className="w-100 btn btn-primary btn-lg" type="submit">Buy</button>
            </form>
        </main>
    </div>
}
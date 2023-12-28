import { Wrapper } from "./Wrapper";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export const OrderList = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    (async () => {
      const response = await fetch("http://127.0.0.1:8000/orders");
      const content = await response.json();
      setOrders(content);
    })();
  }, []);

  const del = async (id) => {
    if (window.confirm("Are you sure to delete this record?")) {
      await fetch(`http://127.0.0.1:8001/products/${id}`, {
        method: "DELETE",
      });
      setOrders(orders.filter((p) => p.id !== id));
    }
  };

  return (
    <Wrapper>
      <div className="pt-3 pb-2 mb-3 border-bottom">
        <Link to={`/orders`} className="btn btn-sm btn-outline-secondary">
          Add
        </Link>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">Order ID</th>
              <th scope="col">Product ID</th>
              <th scope="col">Price</th>
              <th scope="col">Fee</th>
              <th scope="col">Total</th>
              <th scope="col">Quantity</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            {orders?.map((order) => {
              return (
                <tr key={order.id}>
                  <td>{order.id}</td>
                  <td>{order.product_id}</td>
                  <td>{Number(order.price).toFixed(2)}</td>
                  <td>{Number(order.fee).toFixed(2)}</td>
                  <td>{Number(order.total).toFixed(2)}</td>
                  <td>{order.quantity}</td>
                  <td>{order.status}</td>
                  <td>
                    <button
                      className="btn btn-sm btn-outline-secondary"
                      onClick={(e) => del(order.id)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </Wrapper>
  );
};

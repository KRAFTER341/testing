import React, {useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";

export default function Cart({ activeUser }){
    const [ carts, setCarts] = useState
    const [allCarts, setAllCarts]= useState
    const navigate = useNavigate()

    useEffect(() => {
        fetch('http://localhost:3005/cart')
        .then(data => data.json())
        .then(data => {
            setAllCarts(data)
            let myCart = [];
            data.forEach(elem => {
                if (elem.user === activeUser){
                    myCart.push(elem)
                }
            })
            setCarts(myCart)
        })
   },[])
   
   const printCarts = carts.map(cart => {
    return(
        <div key={cart.id}>
            <h4>Product: {cart.product}</h4>
            <p>price:{cart.price}</p>
            <hr />
        </div>
    )
   })

   function makeOrder(){
    let products = [];
    let sum = 0;
    carts.forEach(cart => {
        products.push(cart.product);
        sum += cart.price
    })
    const newOrder = {products, user: activeUser, total_price: sum}
    fetch('http://localhost:3005/order',{
        method: 'POST',
        headers:{"content-type":'application/json'},
        body: JSON.stringify(newOrder)
    })
    allCarts.forEach(cart => {
        if (cart.user === activeUser){
            fetch(`http://localhost:3005/cart/${cart.id}`,{
                method: 'DELETE',
                headers:{"content-type":'application/json'},
            })
        }
    })
    navigate('/order')
   }

    return(
        <div>
            <h1>cart</h1>
            {printCarts}
            <button onClick={makeOrder}>Make Order</button>
            <button onClick={() => navigate('/')}>Back
            </button>
        </div>
    )
}
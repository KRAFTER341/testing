import React, { useState, useEffect } from "react";



export default function Products({isAuth, activeUser}){
    const [ products, setProducts] = useState([])

    useEffect(() => {
        fetch('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail        ')
        .then(data => data.json())
        .then(data => console.log(data.drinks))
   },[])


   function addToCart(product) {
    const newCart = {product: product.id, user: 1, price: product.price}
    fetch('http://localhost:3005/cart',{
        method: 'POST',
        headers:{"content-type":'application/json'},
        body: JSON.stringify(newCart)
    })

   }

   const printProducts = products.map(product => {
    return(
        <div key={product.id}>
            <h4>{product.title}</h4>
            <p>{product.description}</p>
            <p>{product.price}</p>
            {isAuth && <button onClick={() => addToCart(product)}>Add to cart</button>}
        </div>
    )
   })
    return(
        <div>
            <h1>Products</h1>
            {printProducts}
        </div>
    )
}
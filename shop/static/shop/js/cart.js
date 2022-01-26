

function AddToCart(id){
    let product_id=id.split(',')[0]
    let user_id=id.split(',')[1]
    let res = fetch('http://127.0.0.1:8000/add')
           .then(response => response.json())
           .then(data => cart_data(data));

    add_item_in_cart(product_id,user_id)

    
}

function add_item_in_cart(product_id,user_id){
    let data={
        'user':user_id,
        'product':product_id,
        'quantity':1
    }

    let res = fetch('http://127.0.0.1:8000/add/', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify(data)
       })
           .then(response => response.json())
           .then(data => item_add_message(data));
}

function item_add_message(data){
    console.log(data)
}



function cart_data(data){
    console.log(data[0].quantity)
}



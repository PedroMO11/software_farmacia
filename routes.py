from models import *
from app import *

shopping_cart = ShoppingCart([], 0)

@app.route('/')
def index():
    return render_template('index.html', products=Product.query.all())

#This route is going to be called within a Javascript function using path parameteres in the URL.

@app.route('/add_to_shopping_cart/<productCode>', methods=['POST'])
def add_to_shopping_cart(productCode):
    #product_code = request.args.get('productCode')
    #quantity = request.args.get('quantity')
    #unit_price = request.args.get('unitPrice')
    item = Item(productCode, 1)
    shopping_cart.items += [item]
    #shopping_cart.total_price += (unit_price*quantity)
    return 'Item added' #TODO: See if we can return something to be interpreted in the HTML page 


@app.route('/remove_item_from_shopping_cart/<productCode>',methods=['POST'])
def remove_item_from_shopping_cart(productCode):
    #product_code = request.args.get('productCode')
    for item in shopping_cart.items:
        if (item.code == productCode):
            shopping_cart.items.remove(item)
    return 'Item removed'


@app.route('/update_item_from_shopping_cart/<productCode>/<quantity>',methods=['POST'])
def update_item_from_shopping_cart(productCode, quantity):
    #product_code = request.args.get('productCode')
    #quantity = request.args.get('quantity')
    for item in shopping_cart.items:
        if (item.code == productCode):
            item.quantity = quantity
    return 'Item updated'

# This route is to finalize the purchase of the products selected in the shopping cart
@app.route('/shop',methods=['POST'])
def shop():
    shopping_cart.finish_purchase()
    return 'Shop finished' #TODO: See if we can return something to be interpreted in the HTML page

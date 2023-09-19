# ManagingInventory
This project pertains to product management in a warehouse. In the project, a class called "Product" has been implemented, which represents products in the warehouse. Each product has a name, price, available quantity, and discount status. Below are the main functions and methods of the "Product" class:

Product Description: The "describe()" method displays information about the product, such as its name, price, available quantity, discount status, availability in the warehouse, and total inventory value.

Adding Units: The "add_units(units)" method allows for adding units of the product to the warehouse. It checks whether the provided value is an integer greater than zero.

Reducing Units: The "reduce_units(units)" method enables the reduction of the quantity of product units in the warehouse. It validates whether the provided value is an integer greater than zero and whether there are enough units in the warehouse.

Price Reduction: The "reduce_price(discount)" method allows for reducing the price of the product by applying a discount. It checks whether the provided discount value falls within the range of 0 to 1.

Checking Warehouse Availability: The "is_in_stock()" method returns information about the availability of the product in the warehouse.

Calculating Inventory Value: The "calculate_inventory_value()" method calculates the total inventory value of the product in the warehouse.

This project can be useful in warehouse product management and inventory monitoring. It allows for adding, reducing units, and changing product prices, facilitating efficient inventory management and offering discounts when appropriate.

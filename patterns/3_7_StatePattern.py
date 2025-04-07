'''
State Pattern
- The State Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes.
- The State Pattern is implemented by defining a set of states that an object can be in and creating state-specific classes for each state.'''


# Step 1: Define the State Interface
class CheckoutState:
    def add_item(self, item):
        pass

    def review_cart(self):
        pass

    def enter_shipping_info(self, info):
        pass

    def process_payment(self):
        pass

# Step 2: Create Concrete State Classes
class EmptyCartState(CheckoutState):
    def add_item(self, item):
        print("Item added to the cart.")
        return ItemAddedState()

    def review_cart(self):
        print("Cannot review an empty cart.")

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info with an empty cart.")

    def process_payment(self):
        print("Cannot process payment with an empty cart.")


class ItemAddedState(CheckoutState):
    def add_item(self, item):
        print("Item added to the cart.")

    def review_cart(self):
        print("Reviewing cart contents.")
        return CartReviewedState()

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info without reviewing the cart.")

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class CartReviewedState(CheckoutState):
    def add_item(self, item):
        print("Cannot add items after reviewing the cart.")

    def review_cart(self):
        print("Cart already reviewed.")

    def enter_shipping_info(self, info):
        print("Entering shipping information.")
        return ShippingInfoEnteredState(info)

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class ShippingInfoEnteredState(CheckoutState):
    def __init__(self, info):
        self.shipping_info = info

    def add_item(self, item):
        print("Cannot add items after entering shipping info.")
        return self

    def review_cart(self):
        print("Cannot review cart after entering shipping info.")
        return self

    def enter_shipping_info(self, info):
        print("Shipping information already entered.")
        return self

    def process_payment(self):
        print("Processing payment with the entered shipping info.")
        return CheckoutCompleteState()


class CheckoutCompleteState(CheckoutState):
    def add_item(self, item):
        print("Cannot add items. Checkout is complete.")
        return self

    def review_cart(self):
        print("Cannot review cart. Checkout is complete.")
        return self

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info. Checkout is complete.")
        return self

    def process_payment(self):
        print("Payment already processed. Checkout is complete.")
        return self


# Step 3: Create the Context Class
class CheckoutContext:
    def __init__(self):
        self.current_state = EmptyCartState()

    def add_item(self, item):
        self.current_state = self.current_state.add_item(item)

    def review_cart(self):
        self.current_state = self.current_state.review_cart()

    def enter_shipping_info(self, info):
        self.current_state = self.current_state.enter_shipping_info(info)

    def process_payment(self):
        self.current_state.process_payment()


# Step 4: Example of Usage
if __name__ == "__main__":
    cart = CheckoutContext()

    cart.add_item("Product 1")
    cart.review_cart()
    cart.enter_shipping_info("123 Main St, City")
    cart.process_payment()


'''How It Works:

Initial State:
The CheckoutContext starts in the EmptyCartState.
The client adds an item to the cart, transitioning the state to ItemAddedState.

Reviewing the Cart:
In the ItemAddedState, the client reviews the cart, transitioning the state to CartReviewedState.

Entering Shipping Info:
In the CartReviewedState, the client enters shipping information, transitioning the state to ShippingInfoEnteredState.

Processing Payment:
In the ShippingInfoEnteredState, the client processes the payment.'''
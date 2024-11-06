class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
    
    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price}, Stock: {self.stock_quantity}"

def login(users):
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:
            if user.username == username and user.password == password:
                print(f"Welcome, {user.role}!")
                return user
        print("Invalid username or password.")
        return None
    except Exception as e:
        print(f"An error occurred during login: {e}")

def admin_menu():
    print("\nAdmin Menu:")
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Delete Product")
    print("4. View Products")
    print("5. Adjust Stock")
    print("6. Logout")

def user_menu():
    print("\nUser Menu:")
    print("1. View Products")
    print("2. Logout")

def add_product(products):
    try:
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        product = Product(product_id, name, category, price, stock_quantity)
        products.append(product)
        print(f"Product '{name}' added successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and stock quantity.")

def edit_product(products):
    product_id = input("Enter product ID to edit: ")
    for product in products:
        if product.product_id == product_id:
            product.name = input("Enter new name: ")
            product.category = input("Enter new category: ")
            product.price = float(input("Enter new price: "))
            product.stock_quantity = int(input("Enter new stock quantity: "))
            print(f"Product '{product.name}' updated successfully.")
            return
    print("Product not found.")

def delete_product(products):
    product_id = input("Enter product ID to delete: ")
    for product in products:
        if product.product_id == product_id:
            products.remove(product)
            print(f"Product '{product.name}' deleted successfully.")
            return
    print("Product not found.")

def view_products(products):
    if not products:
        print("No products available.")
    for product in products:
        print(product)

LOW_STOCK_THRESHOLD = 5

def check_stock_levels(products):
    for product in products:
        if product.stock_quantity < LOW_STOCK_THRESHOLD:
            print(f"Warning: Low stock for {product.name} (ID: {product.product_id}) - Only {product.stock_quantity} left!")

def adjust_stock(products):
    product_id = input("Enter product ID to adjust stock: ")
    for product in products:
        if product.product_id == product_id:
            adjustment = int(input(f"Enter stock adjustment for {product.name} (negative to reduce, positive to increase): "))
            product.stock_quantity += adjustment
            print(f"New stock for {product.name}: {product.stock_quantity}")
            return
    print("Product not found.")

def main():
    users = [
        User("admin", "admin123", "Admin"),
        User("user", "user123", "User")
    ]
    
    products = [
        Product("P001", "Milling Machine", "Machinery", 5000.0, 10),
        Product("P002", "Lathe", "Machinery", 3000.0, 7)
    ]
    
    while True:
        logged_in_user = login(users)
        if not logged_in_user:
            continue
        
        if logged_in_user.role == "Admin":
            while True:
                admin_menu()
                choice = input("Choose an option: ")
                
                if choice == "1":
                    add_product(products)
                elif choice == "2":
                    edit_product(products)
                elif choice == "3":
                    delete_product(products)
                elif choice == "4":
                    view_products(products)
                    check_stock_levels(products)
                elif choice == "5":
                    adjust_stock(products)
                elif choice == "6":
                    break
                else:
                    print("Invalid choice, please try again.")
        
        elif logged_in_user.role == "User":
            while True:
                user_menu()
                choice = input("Choose an option: ")
                
                if choice == "1":
                    view_products(products)
                elif choice == "2":
                    break
                else:
                    print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

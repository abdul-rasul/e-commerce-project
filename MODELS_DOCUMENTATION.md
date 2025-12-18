# Models Documentation

This document describes all the models defined in the Django e-commerce project.

## 📦 Product App Models

### Category
- **Purpose**: Product categories for organization
- **Fields**: name, slug, description, image, is_active
- **Relationships**: One-to-Many with Product

### Brand
- **Purpose**: Product brands/manufacturers
- **Fields**: name, slug, description, logo, is_active
- **Relationships**: One-to-Many with Product

### Product
- **Purpose**: Main product model
- **Key Fields**:
  - Basic: name, slug, sku, description, short_description
  - Pricing: price, compare_price (for discounts)
  - Inventory: stock_quantity, track_inventory
  - Relationships: category, brand
  - Images: main_image
  - Status: status (draft/published/out_of_stock), is_featured, is_active
  - SEO: meta_title, meta_description
- **Properties**:
  - `is_in_stock`: Check if product is available
  - `discount_percentage`: Calculate discount percentage

### ProductImage
- **Purpose**: Additional product images
- **Fields**: product, image, alt_text, is_primary, order
- **Relationships**: Many-to-One with Product

### ProductReview
- **Purpose**: Customer reviews for products
- **Fields**: product, user, rating (1-5), title, comment, is_approved
- **Relationships**: Many-to-One with Product and User

### Wishlist
- **Purpose**: User wishlist items
- **Fields**: user, product, created_at
- **Relationships**: Many-to-One with User and Product
- **Unique Constraint**: One product per user

---

## 🛒 Order App Models

### Cart
- **Purpose**: Shopping cart (supports both authenticated and anonymous users)
- **Fields**: user (nullable), session_key (for anonymous), timestamps
- **Properties**:
  - `total_items`: Total quantity of items
  - `total_price`: Total price of all items

### CartItem
- **Purpose**: Individual items in cart
- **Fields**: cart, product, quantity
- **Properties**:
  - `subtotal`: Price × Quantity
- **Auto-validation**: Prevents adding more than available stock

### Order
- **Purpose**: Customer orders
- **Key Fields**:
  - Order Info: order_number (auto-generated), user, status, payment_status
  - Pricing: subtotal, shipping_cost, tax, total
  - Shipping: Complete shipping address fields
  - Billing: Complete billing address fields (optional)
  - Payment: payment_method, transaction_id
  - Notes: Customer notes
- **Status Choices**: pending, processing, shipped, delivered, cancelled, refunded
- **Payment Status**: pending, paid, failed, refunded

### OrderItem
- **Purpose**: Individual items in an order
- **Fields**: order, product (nullable), product_name, product_sku, quantity, price, subtotal
- **Note**: Stores product info at time of order (product can be deleted later)

---

## 👤 Account App Models

### UserProfile
- **Purpose**: Extended user profile information
- **Fields**:
  - Personal: phone, gender, date_of_birth, avatar
  - Address: Complete address fields
  - Social: bio, website, social media links
  - Preferences: email_notifications, newsletter_subscription
- **Relationships**: One-to-One with User
- **Auto-creation**: Automatically created when User is created (via signals)
- **Properties**:
  - `full_address`: Formatted address string

### Address
- **Purpose**: Multiple addresses per user (billing/shipping)
- **Fields**:
  - Type: address_type (billing/shipping/both)
  - Complete address fields
  - is_default flag
- **Relationships**: Many-to-One with User
- **Auto-logic**: Only one default address per type per user

---

## 📝 Blog App Models

### BlogCategory
- **Purpose**: Blog post categories
- **Fields**: name, slug, description, image, is_active

### BlogTag
- **Purpose**: Blog post tags
- **Fields**: name, slug

### BlogPost
- **Purpose**: Blog posts/articles
- **Key Fields**:
  - Content: title, slug, excerpt, content, featured_image
  - Relationships: author (User), category, tags (Many-to-Many)
  - Status: status (draft/published), is_featured
  - SEO: meta_title, meta_description
  - Statistics: views counter
  - Timestamps: created_at, updated_at, published_at
- **Auto-logic**: Sets published_at when status changes to published
- **Methods**: `increment_views()` for tracking

### BlogComment
- **Purpose**: Comments on blog posts
- **Fields**: post, user (nullable), name, email, comment, is_approved, parent (for nested comments)
- **Supports**: Both authenticated and anonymous users
- **Properties**: `commenter_name` - returns username or name

---

## 🔗 Model Relationships Summary

```
User
├── OneToOne → UserProfile
├── OneToMany → Address
├── OneToMany → Cart
├── OneToMany → Order
├── OneToMany → ProductReview
├── OneToMany → Wishlist
└── OneToMany → BlogPost

Product
├── ManyToOne → Category
├── ManyToOne → Brand
├── OneToMany → ProductImage
├── OneToMany → ProductReview
├── OneToMany → CartItem
├── OneToMany → OrderItem
└── ManyToMany → User (via Wishlist)

Category
└── OneToMany → Product

Brand
└── OneToMany → Product

Cart
└── OneToMany → CartItem

Order
└── OneToMany → OrderItem

BlogPost
├── ManyToOne → User (author)
├── ManyToOne → BlogCategory
├── ManyToMany → BlogTag
└── OneToMany → BlogComment
```

---

## 📊 Database Indexes

The following indexes are automatically created for performance:

- **Product**: `['slug', 'status']`, `['category', 'status']`
- **Order**: `['order_number']`, `['user', 'status']`
- **BlogPost**: `['slug', 'status']`, `['category', 'status']`

---

## 🎯 Next Steps

After defining models, you need to:

1. **Create Migrations**:
   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser** (if not done):
   ```bash
   python manage.py createsuperuser
   ```

4. **Access Admin Panel**:
   - Visit: http://127.0.0.1:8000/admin/
   - All models are registered and ready to use

---

## 💡 Usage Examples

### Creating a Product
```python
from product.models import Product, Category

category = Category.objects.get(name='Electronics')
product = Product.objects.create(
    name='Smartphone',
    price=599.99,
    compare_price=699.99,
    stock_quantity=50,
    category=category,
    status='published'
)
```

### Creating an Order
```python
from order.models import Order, OrderItem
from product.models import Product

order = Order.objects.create(
    user=request.user,
    subtotal=599.99,
    shipping_cost=10.00,
    total=609.99,
    shipping_first_name='John',
    shipping_last_name='Doe',
    # ... other fields
)

OrderItem.objects.create(
    order=order,
    product=product,
    quantity=1,
    price=599.99,
    subtotal=599.99
)
```

### Getting User Wishlist
```python
from product.models import Wishlist

wishlist_items = Wishlist.objects.filter(user=request.user)
products = [item.product for item in wishlist_items]
```

---

**All models are fully integrated with Django Admin for easy management!** 🎉


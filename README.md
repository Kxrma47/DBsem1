# DBsem1




## Table of Contents
- [Overview](#overview)
- [Objects and Relationships](#objects-and-relationships)
- [API Endpoints](#api-endpoints)
  - [Create an Order](#1-create-an-order)
  - [Get Orders for a User](#2-get-orders-for-a-user)
  - [Update an Order](#3-update-an-order-example)
- [User Roles and Actions](#user-roles-and-actions)
- [Object Model Schema](#object-model-schema)

---

## Overview

The food delivery system handles:
- Creation and management of food orders.
- User and order data management.
- Tracking the status of orders (e.g., Created, Paid, Delivered).

---

## Objects and Relationships

### 1. **User**
- **Fields**: `id`, `name`
- **Relationship**: One `User` can place multiple `Orders`.

### 2. **Order**
- **Fields**: `id`, `user_id`, `dish_name`, `status`
- **Relationship**: Each `Order` is associated with one `User`.

---

## API Endpoints

### 1. Create an Order
- **URL**: `/create_order`
- **Method**: `POST`
- **Description**: Creates a new order for a user.

#### cURL Command
```bash
curl -X POST http://127.0.0.1:5000/create_order \
    -H "Content-Type: application/json" \
    -d '{"user_id": 1, "dish_name": "Pizza"}'
```

#### Request Body
```json
{
  "user_id": 1,
  "dish_name": "Pizza"
}
```

---

### 2. Get Orders for a User
- **URL**: `/orders/<user_id>`
- **Method**: `GET`
- **Description**: Retrieves all orders for a specified user.

#### cURL Command
```bash
curl http://127.0.0.1:5000/orders/1
```

- **URL Parameter**:  
  - `user_id`: The ID of the user whose orders you want to fetch.

---

### 3. Update an Order (Example)
- **URL**: `/update_order/<order_id>`  
- **Method**: `PUT`
- **Description**: Updates the status of an order.

#### cURL Command
```bash
curl -X PUT http://127.0.0.1:5000/update_order/1 \
    -H "Content-Type: application/json" \
    -d '{"status": "Paid"}'
```

#### Request Body
```json
{
  "status": "Paid"
}
```

---

## User Roles and Actions

### 1. **Admin**
- Manage users and orders.
- View reports, process payments, and handle deliveries.

### 2. **User**
- Place orders, update orders, and track their order status.

---

## Object Model Schema

The following schema illustrates the relationships between `User` and `Order`:

```plaintext
User (id, name)  --------<  Order (id, user_id, dish_name, status)
```

- **User**: Represents a customer placing orders.
- **Order**: Represents a food order associated with a user.

---
/food_delivery_service/
    ├── app.py
    ├── database.py
    ├── models.py
    ├── schema.sql
    ├── requirements.txt

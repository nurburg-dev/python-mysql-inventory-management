---
title: Inventory Management System
video: https://www.youtube.com/watch?v=7ySVWcFHz98
tags:
  - mysql
  - python
  - rest-api
summary: Build an inventory management API for e-commerce platforms with support for category-based queries, temporary inventory blocking, and automated cleanup.
---

Build an inventory management API for e-commerce platforms with support for category-based queries, temporary inventory blocking, and automated cleanup.

## Setup Instructions

### Database Setup

1. **Initialize the database schema**: Run the SQL script to create the required tables and indexes:
   ```bash
   mysql -h devmysql -u devuser -p devdb < src/db/init.sql
   ```

## API Endpoints

### Items Management

#### Get Item by ID
```
GET /api/items/:id
```

#### Create New Item
```
POST /api/items
```
**Request Body:**
```json
{
  "name": "Product Name",
  "description": "Product Description",
  "quantity": 100,
  "price": 29.99,
  "category": "Electronics"
}
```

#### Get Top Items by Category
```
GET /api/items/category/:category/top
```
Returns top 100 items by quantity in the specified category.

### Inventory Blocking

#### Create Temporary Block
```
POST /api/items/block/temporary
```
**Request Body:**
```json
{
  "itemId": 123,
  "quantity": 5
}
```

#### Convert to Permanent Block
```
POST /api/items/block/permanent
```
**Request Body:**
```json
{
  "blockId": 456
}
```

#### Clean Expired Blocks
```
POST /api/items/cleanup/expired-blocks
```
Removes expired temporary blocks and restores inventory quantities.
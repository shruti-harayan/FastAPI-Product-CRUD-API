# 🚀 FastAPI Product CRUD API

A simple RESTful Product CRUD API built with **FastAPI**. This project demonstrates the fundamentals of building APIs using FastAPI, including CRUD operations, request validation with Pydantic, path and query parameters, and JSON file-based data storage.

---

## 📌 Features

* Create a new product
* Retrieve all products
* Retrieve a single product by ID
* Search a product using query parameters
* Update product details
* Delete a product
* Request validation using Pydantic
* Interactive API documentation using Swagger UI

---

## 🛠️ Technologies Used

* Python 3.x
* FastAPI
* Pydantic
* Uvicorn

---

## 📂 Project Structure

```text
FastAPI-Product-CRUD/
│
├── src/
│   ├── routes/
│   │   └── product.py
│   ├── dtos/
│   │   └── ProductSchema.py
│   ├── utils/
│   │   └── utils.py
│   └── data/
│       └── products.json
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env.example
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-product-crud.git
```

### 2. Navigate to the project

```bash
cd fastapi-product-crud
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the application

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

After starting the server, open:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📬 API Endpoints

| Method | Endpoint            | Description                         |
| ------ | ------------------- | ----------------------------------- |
| GET    | `/product`          | Get all products                    |
| GET    | `/product?pro_id=1` | Get a product using query parameter |
| GET    | `/product/{id}`     | Get product by ID                   |
| POST   | `/product`          | Create a new product                |
| PUT    | `/product/{id}`     | Update an existing product          |
| DELETE | `/product/{id}`     | Delete a product                    |

---

## 📥 Example Request

### Create Product

**POST** `/product`

```json
{
    "name": "Keyboard",
    "price": 1500,
    "quantity": 20
}
```

---

### Update Product

**PUT** `/product/1`

```json
{
    "price": 1800
}
```

---

## 📤 Example Response

```json
{
    "message": "Product updated successfully"
}
```

---

## ✅ HTTP Status Codes

| Status Code | Meaning           |
| ----------- | ----------------- |
| 200         | Success           |
| 201         | Resource Created  |
| 404         | Product Not Found |
| 422         | Validation Error  |

---

## 📚 What I Learned

Through this project, I practiced:

* Building REST APIs with FastAPI
* CRUD Operations
* APIRouter
* Path Parameters
* Query Parameters
* Request Body Validation
* Pydantic Models
* Exception Handling
* JSON File Operations
* RESTful API Design
* Testing APIs using Swagger UI and Postman

---

## 🚀 Future Improvements

* SQLite / PostgreSQL Database Integration
* SQLAlchemy ORM
* JWT Authentication
* User Authentication & Authorization
* Pagination
* Search & Filtering
* Docker Support
* Unit Testing with Pytest
* API Versioning
* Logging
* Deployment on Render or Railway

---

## 👩‍💻 Author

**Shruti Harayan**

If you found this project helpful, feel free to ⭐ the repository.

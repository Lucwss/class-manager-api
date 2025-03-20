Here is a **README template** with clear instructions on how to set up and run your project using **Python 3.12, MongoDB 7.0, Docker, and Poetry**.

---

## 🚀 Class Manager API

A Python-based authentication and user management system, using **FastAPI**, **MongoDB**, **Docker**, and **Poetry**.

### 📋 Prerequisites

Ensure you have the following installed on your machine:

- [Python 3.12](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Installation & Setup

### 1️⃣ Run with Docker 🐳

To quickly set up the development environment using **Docker Compose**, run:

```sh
docker compose -f infra/docker/compose-dev.yaml up -d
```

This will **download necessary images** and **start the system** in the background.

### 2️⃣ Build the Application (Optional) ⚙️

If you want to build the application manually, use:

```sh
docker build --rm -t class-manager-api:version .
```

Then, update the `compose-dev.yaml` file to use your built image.

---

## 🏗️ Local Development (Without Docker)

1️⃣ Clone the repository:

```sh
git clone https://github.com/your-username/class-manager-api.git
cd class-manager-api
```

2️⃣ Install dependencies using Poetry:

```sh
poetry install
```

3️⃣ Set up environment variables (create a `.env` file based on `.env.example`).

4️⃣ Run the application:

```sh
sh start-development.sh
```

---

## 🛢️ Database (MongoDB 7.0)

By default, the application connects to a **MongoDB 7.0** instance. If running locally, you can start MongoDB using:

```sh
docker run --name mongodb -d -p 27017:27017 mongo:7.0
```

Or, use the **MongoDB instance from Docker Compose**.

---

## ✅ Running Tests

To execute tests, run:

```sh
pytest tests/integration/auth/test_sign_in.py or test_sign_up.py
```

---

## 📄 API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---
## 📜 License

This project is licensed under the **MIT License**.

---tured guide for **setup, running, testing, and contributing**. 🚀 Let me know if you need modifications!
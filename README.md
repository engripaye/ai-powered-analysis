---

# 🤖 AI-Powered Sentiment Analysis (Python + Java Integration)

<img width="1536" height="1024" alt="AI Sentiment Analysis Workflow" src="https://github.com/user-attachments/assets/9c8adbc2-7663-44f1-838c-32d082a00873" />

![Java](https://img.shields.io/badge/Backend-Java%20SpringBoot-orange?logo=java\&logoColor=white)
![Python](https://img.shields.io/badge/AI-Python%20FastAPI-blue?logo=python\&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Model-HuggingFace-yellow?logo=huggingface\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A **microservices-based project** that combines the power of **Python (AI)** with **Java (Spring Boot)**.
The Python service uses **Hugging Face Transformers** for **sentiment analysis**, while the Java service provides an API layer that interacts with it.

---

## 📌 Project Architecture

```
 User → Java Spring Boot (8080) → Python FastAPI AI Service (8000) → Hugging Face Model → Response
```

* **Python FastAPI** → Wraps Hugging Face model into a REST API.
* **Java Spring Boot** → Receives user text, calls Python AI service, and returns sentiment.

---

## 🚀 Features

* 🔹 **Sentiment Analysis** → Classifies text as `POSITIVE` or `NEGATIVE`.
* 🔹 **Python AI Microservice** → Built with FastAPI + Hugging Face.
* 🔹 **Java Backend** → Clean REST API powered by Spring Boot.
* 🔹 **Easy Integration** → Connects Python ML with Java ecosystem.

---

## 📂 Project Structure

```
ai-sentiment-project/
│── python-ai-service/
│   ├── app.py
│   ├── requirements.txt
│
│── java-spring-service/
│   ├── src/main/java/com/example/sentiment/
│   │   ├── SentimentApplication.java
│   │   ├── controller/SentimentController.java
│   │   ├── model/SentimentResponse.java
│   ├── pom.xml
```

---

## 🛠️ Setup Instructions

### 1️⃣ Python AI Service

```bash
cd python-ai-service
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

✅ Runs at `http://localhost:8000/analyze`

Test with:

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love Java and Python!"}'
```

---

### 2️⃣ Java Spring Boot Service

```bash
cd java-spring-service
mvn spring-boot:run
```

✅ Runs at `http://localhost:8080/sentiment/analyze`

Test with:

```bash
curl "http://localhost:8080/sentiment/analyze?text=This project is awesome!"
```

Response:

```json
{"label": "POSITIVE", "score": 0.998}
```

---

## 📖 Learning Goals

This project helps you:

* Learn **Python basics** through a real AI model.
* Understand **FastAPI** for building REST services.
* Connect **Java Spring Boot** with external services.
* Build **AI-powered microservices** with cross-language integration.

---

## 🐳 Next Steps (Improvements)

* [ ] Add **Docker Compose** to run Python & Java together.
* [ ] Add **Frontend (React/Thymeleaf)** for user input.
* [ ] Extend to **multi-class sentiment/emotion detection**.
* [ ] Deploy on **cloud platforms (AWS / Azure / GCP)**.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

✨ Built with **Python, Java, and Hugging Face** 🚀

---

Would you like me to also **add a diagram (PNG/Markdown) for the architecture flow** so it looks even more professional on GitHub?

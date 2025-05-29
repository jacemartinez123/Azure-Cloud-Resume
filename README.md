# ☁️ Azure Cloud Resume Challenge – Jace Azeneth Martinez

Welcome to my completed version of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/) – Azure Edition! This project showcases a full-stack, serverless, cloud-native portfolio built to demonstrate hands-on skills with Microsoft Azure.

---

## 🚀 Live Demo

🌐 **[jamdomain.dev](https://www.jamdomain.dev)**  
🧮 Includes a live visitor counter powered by Azure Functions + Cosmos DB

---

## 🧩 Project Overview

This challenge was completed by building a cloud-based resume site hosted on Microsoft Azure. It includes:

| Component         | Tech Used                                |
|------------------|-------------------------------------------|
| **Frontend**      | HTML, CSS, JavaScript                    |
| **Hosting**       | Azure Storage Static Website             |
| **Custom Domain** | [jamdomain.dev](https://www.jamdomain.dev) via Porkbun + Azure DNS |
| **Security**      | HTTPS enforced via Azure CDN             |
| **Backend**       | Azure Functions (Python)                 |
| **Database**      | Azure Cosmos DB (Table API)              |
| **API**           | Serverless Function with HTTP trigger    |
| **Counter**       | Real-time visitor count via JavaScript fetch() |
| **CI/CD**         | Coming Soon with GitHub Actions          |
| **Blog**          | Coming Soon on Dev.to or Hashnode        |

---

## 🔨 How It Works

1. **Static Resume** is written in HTML/CSS and hosted on Azure Storage with static website hosting.
2. **Visitor Counter API** is a Python Azure Function with an HTTP trigger, integrated with Cosmos DB.
3. **Cosmos DB Logic** increments and returns the visitor count.
4. **Frontend JS** fetches and displays the visitor count live on the site.
5. **Security**: HTTPS via Azure CDN and Cosmos DB IP rules.

---

## 📸 Screenshots

| ![Live Site](https://jamdomain.dev/screenshot.png) |
|:--------------------------------------------------:|
| *Live resume site with real-time counter*          |

---

## 🧪 Testing

This project includes unit tests for the Azure Function using Python's `unittest` and `unittest.mock`.

To run tests locally:

```bash
cd visitor-api
python -m unittest test_main.py

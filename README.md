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
| **CI/CD (In Progress)** | GitHub Actions for frontend/backend deployments |
| **Blog (Planned)**| Dev.to or Hashnode for project reflection and learnings |

---

## 🔨 How It Works

1. **Static Resume** is written in pure HTML/CSS and hosted in an Azure Storage account with static website hosting enabled.
2. **Visitor Counter API** is powered by a Python Azure Function with an HTTP trigger that connects to a Cosmos DB Table.
3. **Database Logic** retrieves and increments a counter stored in Cosmos DB.
4. **JavaScript Integration** fetches the current count and displays it live on the site.
5. **Security**: HTTPS is enforced using Azure CDN + firewall rules on Cosmos DB for restricted access.

---

## 📸 Screenshots

| ![Live Site](https://jamdomain.dev/screenshot.png) |
|:--------------------------------------------------:|
| *Live resume site with real-time counter*          |

---

## 🏁 Skills Demonstrated

- Azure Storage & Static Hosting
- Azure Functions (v2 Python model)
- Cosmos DB Table API
- Environment Variable Configuration
- Firewall + Networking in Azure
- JavaScript + API Integration
- Domain Management + DNS
- Debugging, Logging & Permissions
- End-to-end Cloud Deployment Workflow

---

## 📚 Blog Post (Coming Soon)

I'll be writing a blog post walking through my learning experience, challenges, and tips for anyone attempting this project.

---

## 🙌 Acknowledgments

Special thanks to [Forrest Brazeal](https://twitter.com/forrestbrazeal) for creating the original Cloud Resume Challenge, and to the Azure community for the documentation and support that helped along the way.

---

## 📎 License

This project is open source under the MIT License.

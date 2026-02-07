# 🔐 Secure CI/CD Pipeline with Prisma Cloud & Checkov

This repository demonstrates how to **secure and block a CI/CD pipeline using Prisma Cloud (Checkov)** by scanning source code, Dockerfiles, IaC, and container images.  
A deliberately **vulnerable demo application** is used to show how security issues stop the pipeline before production.

---

## 🎯 Purpose

The objective of this project is to:

- Integrate **Prisma Cloud (Checkov)** into GitHub Actions
- Detect security vulnerabilities early in the pipeline
- **Fail and block the pipeline** when policies are violated
- Prevent insecure images from reaching production

---

## 🧱 CI/CD Pipeline Flow

```text
Code Push / Pull Request
        |
        v
Security Scan (Checkov)
(Code, Dockerfile, IaC)
        |
        v
Docker Build + Image Scan
        |
        v
Push to Registry (Blocked if Scan Fails)
        |
        v
Production Deployment (Final Gate)
````

---

## 🧪 Vulnerable Demo Application

The demo application intentionally includes security issues such as:

* Vulnerable base image (e.g. `python:3.8-slim`)
* Running containers as root
* Missing Docker `USER` and `HEALTHCHECK`
* Vulnerable dependencies
* Dockerfile and configuration misconfigurations

These issues are detected by **Checkov** and reported to **Prisma Cloud**.

---

## 🔍 Security Scanning with Prisma Cloud

### Tool Used

* **Checkov** (Prisma Cloud scanning engine)

### Scan Coverage

* Source code
* Dockerfile
* Infrastructure as Code (IaC)
* Container image vulnerabilities
* Secrets and misconfigurations

Scan results are sent to **Prisma Cloud** and also uploaded to GitHub using **SARIF**.

---

## ⚙️ GitHub Actions Pipeline

The pipeline is implemented using **GitHub Actions**.

### 1️⃣ Docker Build & Image Scan

* Builds the Docker image
* Scans the image using Checkov
* Enforces Prisma Cloud policies
* Fails the job if vulnerabilities are found

Common failures:

* Base image CVEs
* OS package vulnerabilities
* Docker security misconfigurations

---

### 2️⃣ Push to Container Registry

* Pushes image to DockerHub / ECR
* Runs **only if image scan passes**
* Automatically blocked when Checkov fails

---

### 3️⃣ Production Deployment

* Runs only on the `main` branch
* Requires successful security scans
* Uses GitHub Environments for production approval
* Deploys to Kubernetes

---

### 4️⃣ Failure Notification

* Executes if any pipeline stage fails
* Provides visibility into failed security checks
* Can be extended for Slack or email alerts

---

## 🛑 How the Pipeline is Blocked

The pipeline is blocked using **Checkov enforcement rules**:

```yaml
use_enforcement_rules: true
# soft_fail: false
```

### Pipeline fails when:

* Prisma Cloud policies are violated
* High or Critical vulnerabilities are detected
* Dockerfile security best practices are missing
* Container image exceeds vulnerability thresholds

A failed scan causes:

* Checkov to exit with a non-zero status
* GitHub Actions job to fail
* Downstream jobs (push & deploy) to stop

---

## 📊 Scan Results Visibility

* GitHub → **Security → Code scanning alerts**
* Prisma Cloud Console

---

## 🔐 Required GitHub Secrets

| Secret Name          | Description                    |
| -------------------- | ------------------------------ |
| `BC_API_KEY`         | Prisma Cloud API key           |
| `DOCKERHUB_USERNAME` | DockerHub username             |
| `DOCKERHUB_TOKEN`    | DockerHub access token         |
| `KUBECONFIG`         | Kubernetes configuration       |
| `SLACK_WEBHOOK_URL`  | (Optional) Slack notifications |

---

## ✅ Expected Outcome

* Vulnerable application **fails security scans**
* Docker image **is not pushed** to the registry
* Production deployment **is blocked**
* Security issues must be fixed before release

---

## 🏁 Conclusion

This project demonstrates how **Prisma Cloud and Checkov enforce security as code**, ensuring that insecure applications **never reach production** through CI/CD pipelines.
 the word 🚀

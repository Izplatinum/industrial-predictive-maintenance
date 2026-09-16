# Industrial Predictive Maintenance Platform

End-to-end predictive maintenance platform combining machine learning, data engineering, cloud infrastructure, Kubernetes, monitoring, autoscaling, and CI/CD.

This project simulates a production-grade industrial monitoring system capable of detecting pump leakage conditions from machine sensor data and serving real-time predictions through a cloud-native architecture.

---

## Project Objective

The goal of this project is to demonstrate how industrial sensor data can be transformed into a complete production-ready predictive maintenance solution.

The system was designed to:

- analyze machine sensor data
- engineer predictive features
- store processed data in PostgreSQL
- visualize operational metrics with Power BI
- train and validate machine-learning models
- identify pump leakage conditions
- expose predictions through a REST API
- containerize the inference service
- deploy the application on Kubernetes
- automatically scale workloads based on CPU usage
- monitor infrastructure and application resources
- automate deployments using CI/CD
- provision cloud infrastructure using Terraform

The emphasis is not only on model development, but on the complete lifecycle from raw industrial data to a deployed and monitored cloud application.

---

## Prediction Target

The model classifies machine conditions into three pump leakage states:

| Class | Condition |
|---|---|
| 0 | No Leakage |
| 1 | Weak Leakage |
| 2 | Severe Leakage |

---

## Architecture

```mermaid
flowchart TD
    A[Industrial Sensor Data] --> B[Data Preparation and EDA]
    B --> C[Feature Engineering]
    C --> D[(PostgreSQL)]

    D --> E[Power BI Dashboard]
    D --> F[Machine Learning Pipeline]

    F --> G[Random Forest Model]
    G --> H[FastAPI Prediction Service]
    H --> I[Docker Container]
    I --> J[Amazon ECR]

    J --> K[Amazon EKS / Kubernetes]

    K --> L[Multiple API Pods]
    K --> M[Horizontal Pod Autoscaler]
    K --> N[AWS Load Balancer]
    K --> O[CloudWatch Container Insights]

    N --> P[Public Prediction API]

    Q[Terraform] --> K
    R[GitHub Actions CI/CD] --> J
    R --> K

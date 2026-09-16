\# Industrial Predictive Maintenance Platform



End-to-end industrial predictive maintenance platform combining machine learning, data engineering, cloud infrastructure, Kubernetes, DevOps, monitoring, autoscaling, and CI/CD.



This project simulates a production-grade predictive maintenance workflow for industrial equipment using sensor data to detect different levels of pump leakage.



\---



\## Project Overview



The objective of this project is to build a complete industrial predictive maintenance system capable of:



\- ingesting and storing machine sensor data

\- performing exploratory data analysis

\- engineering predictive features

\- training and validating machine-learning models

\- detecting pump leakage conditions

\- serving predictions through a REST API

\- containerizing the application

\- deploying it to Kubernetes on AWS EKS

\- automatically scaling workloads

\- monitoring infrastructure and application metrics

\- automating deployments with GitHub Actions



The project was designed to simulate a real production environment rather than only a machine-learning notebook.



\---



\## Target Variable



The machine-learning model predicts three pump leakage states:



| Class | Status |

|---|---|

| 0 | No Leakage |

| 1 | Weak Leakage |

| 2 | Severe Leakage |



\---



\## Architecture



```text

Industrial Sensor Data

&#x20;       |

&#x20;       v

Data Preparation / EDA

&#x20;       |

&#x20;       v

Feature Engineering

&#x20;       |

&#x20;       v

PostgreSQL

&#x20;  |          |

&#x20;  |          +--------------------+

&#x20;  v                               v

Power BI                     Python / ML

Dashboards                        |

&#x20;                                 v

&#x20;                        Random Forest Model

&#x20;                                 |

&#x20;                                 v

&#x20;                             FastAPI

&#x20;                                 |

&#x20;                                 v

&#x20;                              Docker

&#x20;                                 |

&#x20;                                 v

&#x20;                          Amazon ECR

&#x20;                                 |

&#x20;                                 v

&#x20;                        Amazon EKS

&#x20;                     Kubernetes Cluster

&#x20;                                 |

&#x20;                  +--------------+--------------+

&#x20;                  |                             |

&#x20;                  v                             v

&#x20;             Load Balancer              Horizontal Pod

&#x20;                                        Autoscaler

&#x20;                  |

&#x20;                  v

&#x20;           Public REST API

&#x20;                  |

&#x20;                  v

&#x20;             CloudWatch

&#x20;          Container Insights

&#x20;                  |

&#x20;                  v

&#x20;           GitHub Actions

&#x20;               CI/CD


# Project Documentation: Zomato Web Application and Kubernetes Deployment

This document describes the Zomato clone web project and its Kubernetes deployment.

---

## 1. Project Purpose

This project provides a web application for food delivery and restaurant search. The project uses a container image to run the web application. Kubernetes manages the containers across a server cluster.

The project demonstrates three primary technical goals:
- Modern frontend development with React.
- Multi-stage container builds with Docker.
- Declarative service orchestration with Kubernetes.

---

## 2. Technical Architecture

The project has three main architectural layers.

### Frontend Layer
The frontend is a single-page application built with React 18. It uses Sass and Emotion for styling. It uses Material UI components for icons and navigation controls.

### Container Layer
Docker packages the application into a container image. The Dockerfile uses two build stages. The first stage builds the static assets. The second stage runs the production server.

### Kubernetes Layer
Kubernetes orchestrates the application containers. A Deployment controller manages two active pod replicas. A LoadBalancer service routes external network traffic to the pods.

---

## 3. Directory Structure

The project directory contains these key components:

- `src/App.js`: The root component of the React application.
- `src/components/Header/`: The header bar with search inputs and brand logos.
- `src/components/Card/`: Category cards for dining, delivery, and nightlife.
- `src/components/Collections/`: Curated restaurant lists for cities.
- `src/components/Cities/`: Popular localities and dining destinations.
- `src/components/CTA/`: Download links for the mobile application.
- `src/components/AccContainer/`: Collapsible question lists and local guides.
- `src/data.js`: Mock data for cities, questions, and collections.
- `Dockerfile`: Multi-stage Docker build instructions.
- `manifests/Deployment.yml`: Kubernetes Deployment specification for two replicas.
- `manifests/svc.yml`: Kubernetes LoadBalancer Service specification.

---

## 4. Local Development Procedure

Follow these steps to run the application on your computer.

### Prerequisites
Make sure that you install Node.js version 16 or newer. Also make sure that you install the npm package manager.

### Steps
1. Open your command terminal.
2. Go to the project root directory.
3. Install all project dependencies:
   ```bash
   npm install
   ```
4. Start the local development server:
   ```bash
   npm start
   ```
5. Open your web browser.
6. Go to `http://localhost:3000`.
7. Make sure that the application page displays correctly.

---

## 5. Docker Build and Run Procedure

Use Docker to build and run the containerized application.

### Steps
1. Build the Docker image:
   ```bash
   docker build -t zomato-project:latest .
   ```
2. Start the container in the background:
   ```bash
   docker run -d -p 3000:3000 --name zomato-web zomato-project:latest
   ```
3. View the running container list:
   ```bash
   docker ps
   ```
4. Make sure that the container status shows `Up`.
5. If the container stops unexpectedly, examine the container logs:
   ```bash
   docker logs zomato-web
   ```

---

## 6. Kubernetes Deployment Procedure

Deploy the application to your Kubernetes cluster.

### Prerequisites
Make sure that `kubectl` connects to your active Kubernetes cluster context.

### Steps

1. Apply the deployment configuration:
   ```bash
   kubectl apply -f manifests/Deployment.yml
   ```
2. Apply the service configuration:
   ```bash
   kubectl apply -f manifests/svc.yml
   ```
3. Examine the pod status:
   ```bash
   kubectl get pods -l app=swiggy
   ```
4. Make sure that all pods show the `Running` status.
5. Get the external IP address of the service:
   ```bash
   kubectl get svc mysvc
   ```
6. Open the external IP address in your browser on port 3000.

> [!CAUTION]
> If you delete the service manifest, external network access will stop immediately.

# Project Overview: Zomato Web Application and Kubernetes Deployment

## 1. Executive Summary & Purpose
This repository encompasses an end-to-end cloud-native implementation of a responsive Zomato food delivery web portal clone. The primary objective of this project is to showcase how modern component-based single-page user interfaces can be seamlessly bundled into production-ready container images and subsequently orchestrated within an automated Kubernetes cluster environment. It was constructed to facilitate high-availability web delivery while ensuring that modern frontend workflows are maintained.

## 2. Technical Stack and Architecture
The overall architecture of the application can be conceptually divided into the presentation layer, the containerization packaging tier, and the cluster orchestration configuration layer:

- **Frontend User Interface Tier**: The user interface was developed utilizing React 18, styled with Sass and Emotion CSS-in-JS, and complemented with Material UI components for icons and navigation elements. Dynamic culinary datasets, popular localities, curation collections, and FAQ accordions are displayed across several modular UI components.
- **Docker Multi-Stage Build Tier**: In order to optimize container artifact sizes and maintain layer caching benefits, the Dockerfile employs a multi-stage compilation strategy whereby Node.js dependencies are resolved and static production assets are compiled before being transferred to the final runtime container.
- **Kubernetes Cluster Orchestration Tier**: Workloads are orchestrated through declarative YAML specifications that govern pod replicas and network routing through cloud load balancer infrastructure.

## 3. Component Hierarchy and Directory Structure
The internal structure of the React frontend application is organized in a modular fashion to ensure maximum code reusability:

- `src/App.js`: Serves as the centralized root component wherein all primary interface blocks are imported and sequentially rendered.
- `src/components/Header/`: Manages the top-level navigational bar, search input mechanisms, and brand logos.
- `src/components/Card/`: Renders interactive service promotion cards (e.g., Dining, Delivery, Nightlife).
- `src/components/Collections/`: Displays curated city dining collections and trending spots.
- `src/components/Cities/`: Visualizes popular dining destinations and local regions.
- `src/components/CTA/`: Implements call-to-action sections promoting the Zomato mobile application download via SMS or email links.
- `src/components/AccContainer/`: Houses collapsible accordion lists for frequently asked questions and locality explorations.
- `src/data.js`: Houses mock application state including regional city entries, accordion definitions, and collection items.

## 4. Local Development Procedures
Prior to launching the application locally on your workstation, you should verify that you have Node.js (version 16 or newer) as well as the npm package manager properly installed.

To initiate the local development environment:
1. Open your terminal emulator and navigate to the project root directory.
2. In order to download and install all requisite package dependencies, execute the command `npm install` and ensure that no peer dependency conflicts occur.
3. Once dependency resolution has successfully completed, the development server can be initiated by running `npm start`.
4. Check your web browser by navigating to `http://localhost:3000` to verify that the portal renders as expected.

## 5. Containerization with Docker
The repository includes a multi-stage `Dockerfile` designed to facilitate clean container isolation:
- The first stage (`builder`) leverages the `node:16-slim` base image to execute dependency installation and trigger `npm run build`.
- The subsequent production stage (`final`) pulls in the compiled build output from the initial stage, installs production-only runtime modules, and exposes port 3000.

To build and run the Docker container locally:
```bash
# Build the Docker image
docker build -t zomato-project:latest .

# Run the containerized application
docker run -d -p 3000:3000 --name zomato-web zomato-project:latest
```

You should verify that the container is executing properly by issuing the `docker ps` command and checking container log output if any unexpected crash occurs.

## 6. Kubernetes Cluster Deployment Workflow
Cluster workload configuration manifests are maintained inside the `manifests/` directory.

### Deployment Manifest (`manifests/Deployment.yml`)
The deployment configuration specifies that 2 pod replicas should be maintained by the replica set controller. Each replica runs the image `shaikmustafa77/ccitrepo:zomato` and listens on container port 3000.

### Service Manifest (`manifests/svc.yml`)
Network ingress is governed by a `LoadBalancer` service named `mysvc`. It binds incoming public network traffic arriving on port 3000 and subsequently routes traffic to target port 3000 on pods matching the `app: swiggy` selector label.

### Cluster Deployment Steps
Prior to executing deployment operations against your Kubernetes cluster, ensure that `kubectl` is properly authenticated against your target cloud provider cluster context.

1. Deploy the pod replica specification by executing:
   ```bash
   kubectl apply -f manifests/Deployment.yml
   ```
2. Subsequently apply the network service configuration:
   ```bash
   kubectl apply -f manifests/svc.yml
   ```
3. Check the rollout status of your deployment to verify that all pods have achieved the ready state:
   ```bash
   kubectl get pods -l app=swiggy
   ```
4. Ascertain the external IP assigned to your load balancer by inspecting the service status:
   ```bash
   kubectl get svc mysvc
   ```
5. Note: Deleting the service manifest will instantly terminate external ingress routing, which could result in application downtime for active consumers.

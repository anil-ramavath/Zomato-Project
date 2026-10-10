# ASD-STE100 Before and After Examples

This reference provides real-world examples of standard technical text converted into compliant ASD-STE100 (Simplified Technical English).

---

## Example 1: Procedural Deployment Instructions

### Non-STE (Original):
> Prior to executing the deployment script, ensure that the Kubernetes cluster is running properly and that you have verified that all necessary environment variables have been set. Then, initiate the container build process by utilizing the docker build command and subsequently push the resulting artifact to the central container registry.

**Identified STE Violations**:
- "Prior to executing" (unapproved phrase; gerund "-ing").
- "ensure" / "verified" (unapproved words).
- Compound actions joined in single run-on sentences (> 45 words).
- "utilizing" (unapproved; use "use").
- "subsequently push" (use "then push" or separate step).
- Noun string: "central container registry".

### ASD-STE100 (Compliant):
1. Before you run the deployment script, make sure that the Kubernetes cluster is active.
2. Make sure that you set all required environment variables.
3. Build the container image:
   ```bash
   docker build -t zomato-app:latest .
   ```
4. Push the image to the container registry:
   ```bash
   docker push zomato-app:latest
   ```

---

## Example 2: Descriptive Architecture Overview

### Non-STE (Original):
> The application architecture utilizes a microservices paradigm whereby incoming client HTTP web requests are intercepted by an ingress controller and subsequently routed to the appropriate backend service pods which are continuously monitored by a Prometheus metrics collection daemon.

**Identified STE Violations**:
- 38 words (exceeds 25-word limit for descriptive sentences).
- "utilizes" (unapproved; use "uses").
- "whereby" (unapproved connector).
- Passive voice ("are intercepted", "subsequently routed", "are continuously monitored").
- Continuous "-ing" forms ("incoming", "continuously").
- Long noun string: "incoming client HTTP web requests", "Prometheus metrics collection daemon".

### ASD-STE100 (Compliant):
> The application uses a microservices architecture. An Ingress controller receives HTTP requests from clients and routes the traffic to the backend pods. A Prometheus daemon monitors the pods and collects performance metrics.

---

## Example 3: Troubleshooting & Conditional Steps

### Non-STE (Original):
> You should check if the pod terminates unexpectedly with an OutOfMemory error by inspecting the cluster event log, and in such cases, it is recommended to increase the container memory resource limits in your deployment YAML manifest.

**Identified STE Violations**:
- Modal "should" (forbidden; ambiguous).
- Condition placed after action.
- "check if" / "inspecting" (unapproved; use "make sure" / "examine").
- Passive and indirect recommendation ("it is recommended to").
- Sentence length: 39 words.

### ASD-STE100 (Compliant):
> If a pod stops unexpectedly, examine the cluster events for an OutOfMemory error. If the error occurs, increase the memory limit in the deployment manifest.

---

## Example 4: Warnings and Cautions

### Non-STE (Original):
> Note that deleting the persistent volume claim before taking a snapshot will cause immediate and irreversible loss of all application data, which could crash production services.

**Identified STE Violations**:
- Misuse of "Note" for data loss / severe risk.
- Must use CAUTION or WARNING before the action.
- Modal "could" (unapproved).
- Word count: 28 words.

### ASD-STE100 (Compliant):
> **CAUTION: Take a snapshot before you delete the persistent volume claim. If you delete the claim without a snapshot, you will permanently lose all application data.**

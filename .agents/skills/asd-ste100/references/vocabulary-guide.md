# ASD-STE100 Controlled Vocabulary Guide

In ASD-STE100, words have one designated meaning and one approved part of speech. When writing or converting documentation to STE, use the approved terms listed below.

---

## 1. High-Frequency Technical Vocabulary Replacements

| Unapproved / Forbidden Term | Approved Replacement | Notes / Example |
| :--- | :--- | :--- |
| **abort** | `cancel` / `stop` | Cancel the deployment. |
| **allow / permit** | `let` / `allow` (verb) | This setting lets the container communicate. |
| **as well as** | `and` | Download the manifest and the image. |
| **ascertain** | `find` / `determine` | Find the IP address of the node. |
| **attempt** | `try` | Try to reconnect to the cluster. |
| **check** | `examine` / `make sure` | Examine the pod status. / Make sure the service runs. |
| **commence** | `start` | Start the process. |
| **consequently** | `because of this` / `then` | Then the connection closes. |
| **depict / illustrate** | `show` | Figure 2 shows the architecture. |
| **disconnect** | `disconnect` (approved) | Disconnect the network cable. |
| **due to** | `because of` | The node failed because of high memory usage. |
| **employ / utilize** | `use` | Use Helm to install the chart. |
| **ensure / verify** | `make sure` | Make sure that the port is open. |
| **execute** | `run` / `do` | Run the Docker command. |
| **exhibit** | `show` | The logs show error code 500. |
| **in addition to** | `and` / `also` | Install Docker, and install Git. |
| **in order to** | `to` | To build the image, enter: ... |
| **initiate** | `start` | Start the service. |
| **inspect** | `examine` | Examine the certificate expiration date. |
| **modify / alter** | `change` | Change the replica count in the YAML file. |
| **obtain** | `get` | Get the authorization token. |
| **perform** | `do` / `run` | Run the smoke tests. |
| **prior to** | `before` | Before you apply the manifest... |
| **provide** | `give` | The configmap gives the environment variables. |
| **rectify** | `correct` | Correct the syntax error. |
| **require** | `need` / `must` | You must supply an API key. |
| **subsequent to** | `after` | After the build finishes... |
| **terminate** | `stop` / `end` | Stop the background worker. |
| **transmit** | `send` | Send the HTTP request. |
| **via** | `through` / `by` | Route the traffic through the ingress controller. |

---

## 2. Approved Auxiliaries and Modals

| Modal / Auxiliary | Status | Usage in STE |
| :--- | :--- | :--- |
| **can** | Approved | Denotes capability or possibility ("The service can scale to 10 pods."). |
| **must** | Approved | Denotes mandatory requirement ("You must configure the secret."). |
| **will** | Approved | Denotes future fact ("The controller will restart unhealthy pods."). |
| **should** | **Forbidden** | Ambiguous. Replace with *must* (if mandatory) or clarify recommendation. |
| **could / might** | **Forbidden** | Replace with *can* or explicit condition ("If X occurs, Y can happen."). |
| **may** | Restricted | Permitted only for permission ("You may select option A or B."). |

---

## 3. Approved Connectors and Conjunctions

- **Use**: *and*, *or*, *because*, *if*, *when*, *while*, *before*, *after*, *then*.
- **Avoid**:
  - *since* (when used in place of *because* — use *since* only for time references: "since yesterday").
  - *as* (when used in place of *because* or *while*).
  - *whereby*, *thereby*, *inasmuch as*.

---

## 4. Technical Names (TNs) and Technical Verbs (TVs)

ASD-STE100 allows domain-specific Technical Names not listed in the general dictionary if they satisfy these criteria:
1. They are established industry or product terms (e.g., `Kubernetes`, `namespace`, `ConfigMap`, `Ingress`, `Docker`).
2. They cannot be replaced by a common STE noun without loss of precision.
3. They are applied consistently across all documentation.

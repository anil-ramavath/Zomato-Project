# ASD-STE100 Rules Summary Reference

The ASD-STE100 specification organizes rules into 9 main categories. This document summarizes key rules and practical application guidelines.

---

## 1. Words (Rule Group 1)
- **Approved Meaning and Part of Speech**: Words must only be used with their approved meaning and part of speech defined in the STE dictionary.
  - *Example*: "Close" is approved as a verb (*close the valve*), but unapproved as an adjective or adverb (*near*, *nearby*).
  - *Example*: "Oil" is approved as a noun (*lubricating oil*), but unapproved as a verb (*do not oil the hinge* -> *lubricate the hinge with oil*).
- **Technical Names (TNs) and Technical Verbs (TVs)**:
  - Technical Names (names of components, tools, processes, software entities) are permitted even if they are not in the dictionary, provided they are unambiguous and standard in the domain.
  - Examples: *pod*, *deployment*, *Dockerfile*, *Kubernetes*, *hex bolt*.

---

## 2. Noun Clusters (Rule Group 2)
- **Rule 2.1**: A noun cluster (string of consecutive nouns modifying each other) must not contain more than **three nouns**.
- **Rule 2.2**: When breaking up long noun clusters:
  - Use prepositions (*of*, *for*, *to*, *in*).
  - Use hyphens for recognized compound nouns.
  - *Incorrect*: "Container cluster pod autoscaling policy configuration" (6 nouns)
  - *Correct*: "Configuration of the autoscaling policy for cluster pods"

---

## 3. Verbs and Verb Forms (Rule Group 3)
- **Rule 3.1 Permitted Verb Forms**:
  - Present tense (*The container starts automatically.*)
  - Simple past tense (*The node stopped unexpectedly.*)
  - Simple future tense with "will" (*The service will restart.*)
  - Imperative mood (*Enter the command.*)
  - Infinitive (*To build the image, run...*)
  - Past participles only as adjectives (*the damaged cable*, *the stopped container*).
- **Rule 3.2 Prohibited Verb Forms**:
  - Continuous/progressive forms (*is running*, *was checking* -> use *runs*, *checked*).
  - Perfect tenses with *have/has/had* (*has completed* -> *completed* or *is complete*).
  - Conditional modals (*could*, *would*, *should*, *might*).
- **Rule 3.3 Active Voice**:
  - Write sentences in active voice. Identify the agent or subject performing the action.
  - *Passive (Avoid)*: "The image is created by the build script."
  - *Active (STE)*: "The build script creates the image."

---

## 4. Sentences (Rule Group 4)
- **Rule 4.1 Sentence Length**:
  - **Procedural sentences**: 20 words maximum.
  - **Descriptive sentences**: 25 words maximum.
- **Rule 4.2 One Instruction per Sentence**:
  - Each numbered procedural step must contain only one command.
  - If two actions are closely connected and occur at the exact same moment, combine only if essential, but standard practice is separate steps.
- **Rule 4.3 Vertical Lists**:
  - Use vertical bulleted or numbered lists for lists of three or more items.
  - Introduce lists with a clear sentence or clause ending in a colon.

---

## 5. Procedural Writing vs. Descriptive Writing (Rule Group 5)
- **Procedural Writing**:
  - Used for instructions, tutorials, runbooks, and SOPs.
  - Always uses numbered steps.
  - Begins each step with an imperative verb.
  - Does not use narrative paragraphs in procedural sections.
- **Descriptive Writing**:
  - Used for explanations, architecture descriptions, and specifications.
  - Uses short paragraphs (maximum 6 sentences).
  - Can use declarative sentences.

---

## 6. Prepositions and Conjunctions (Rule Group 6)
- **Rule 6.1 Clear Relationships**:
  - Use prepositions that clearly state direction, location, or relationship.
  - Do not omit prepositions to shorten sentences if doing so causes ambiguity.
- **Rule 6.2 Approved Conjunctions**:
  - Use *and*, *or*, *because*, *if*, *when*, *while*, *after*, *before*.
  - Avoid ambiguous conjunctions such as *as*, *since* (when meaning *because*), and *whereby*.

---

## 7. Warnings, Cautions, and Notes (Rule Group 7)
- **Rule 7.1 Precedence**:
  - Place WARNINGs and CAUTIONs immediately **before** the step they apply to, never after.
- **Rule 7.2 Clear Distinctions**:
  - **WARNING**: Informs the user of hazards that can cause death or injury.
  - **CAUTION**: Informs the user of hazards that can damage equipment, corrupt data, or crash systems.
  - **NOTE**: Provides non-mandatory explanatory information. Must not contain instructions or imperative verbs.

---

## 8. Punctuation and Typography (Rule Group 8)
- Use standard punctuation (periods, commas, colons, hyphens).
- Do not use semicolons (`;`) to connect independent clauses; divide them into two sentences.
- Avoid slashes (`/`) meaning "and/or". Write either *and* or *or* explicitly.
- Use uppercase or bold formatting consistently for UI labels, switches, or command flags.

---

## 9. Conditions and Sequences (Rule Group 9)
- Put the condition first:
  - *Format*: `If [condition], [action].`
  - *Reasoning*: The operator must evaluate the condition before executing or considering the action.
  - *Example*: "If the status shows 'CrashLoopBackOff', inspect the pod logs."

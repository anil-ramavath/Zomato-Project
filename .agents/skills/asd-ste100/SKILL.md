---
name: asd-ste100
description: >-
  Apply, audit, and rewrite technical documentation according to ASD-STE100
  (Simplified Technical English) specification standards, vocabulary rules,
  and structural guidelines. Use when writing, converting, or reviewing technical
  documentation, user guides, standard operating procedures (SOPs), manuals, or
  release notes for clarity and international readability.
---

# ASD-STE100 Simplified Technical English Skill

ASD-STE100 (Simplified Technical English) is an international specification designed to make technical texts clear, concise, unambiguous, and easy to translate.

This skill equips the agent to write new documentation in STE or audit and convert existing technical documentation to meet ASD-STE100 standards.

---

## When to Use This Skill

- Writing or editing user documentation, manuals, installation guides, or standard operating procedures.
- Converting ambiguous, verbose, or passive technical writing into direct, clear English.
- Auditing existing documentation for compliance with ASD-STE100 sentence length, noun cluster, and vocabulary limits.
- Preparing documentation intended for non-native English speakers or machine translation.

---

## Core Principles & Rules Summary

### 1. Sentence and Paragraph Limits
- **Procedural sentences (instructions/actions)**: Maximum **20 words**.
- **Descriptive sentences (explanations/descriptions)**: Maximum **25 words**.
- **Paragraphs (descriptive text)**: Maximum **6 sentences**. Do not use paragraphs for procedures (use numbered lists instead).
- **One command per sentence**: Never combine two procedural actions into one sentence with "and".
  - *Bad*: Disconnect the cable and remove the battery. (2 actions)
  - *Good*: 1. Disconnect the cable. 2. Remove the battery.

### 2. Voice and Mood
- **Active voice only**: Always specify who or what performs the action. Avoid passive constructions.
  - *Bad*: The file is written by the server to disk.
  - *Good*: The server writes the file to disk.
- **Imperative mood for procedures**: Begin instructions with a base verb.
  - *Bad*: You should make sure that the switch is set to OFF.
  - *Good*: Set the switch to OFF.

### 3. Noun Clusters (Noun Jamming)
- Maximum of **three consecutive nouns**.
- When four or more nouns appear together, break them up with prepositions or hyphenated modifiers.
  - *Bad*: Storage system data replication error rate (5 nouns)
  - *Good*: Rate of data replication errors in the storage system

### 4. Verbs, Tenses, and Moods
- Use only permitted tenses:
  - **Present simple** (*starts, operates*)
  - **Past simple** (*started, operated*)
  - **Future with "will"** (*will start*)
  - **Imperative** (*start, operate*)
- **Avoid "-ing" forms** (gerunds and present participles) whenever possible. Replace with simple tense or infinitive.
  - *Bad*: Before starting the engine, checking the oil is required.
  - *Good*: Before you start the engine, check the oil.
- Avoid vague modal auxiliaries: **Do not use** *could*, *should*, *might*, *may* (except for permission). Use *must* for obligations or imperative for instructions.

### 5. Conditional Clauses
- Put the condition before the action:
  - *Pattern*: `If [condition], [imperative action].`
  - *Bad*: Turn off the switch if the warning light turns red.
  - *Good*: If the warning light becomes red, turn off the switch.

### 6. Standardized Safety and Callout Levels
- **WARNING**: Risk of injury or death to personnel. Precede the step.
- **CAUTION**: Risk of damage to equipment, software, or data. Precede the step.
- **NOTE**: Informational tip or clarification. Never contains an instruction.

---

## Controlled Vocabulary Cheatsheet

In ASD-STE100, each approved word has only one approved meaning and part of speech.

| Forbidden / Unapproved Word | Approved STE Replacement | Example / Notes |
| :--- | :--- | :--- |
| **ensure / verify / check** | `make sure` / `examine` | "Make sure that the indicator is green." |
| **utilize / employ** | `use` | "Use the supplied tool." |
| **in order to** | `to` | "Press Enter to continue." |
| **prior to** | `before` | "Before you restart the pod..." |
| **subsequent to / following** | `after` | "After the container stops..." |
| **terminate / abort** | `stop` / `cancel` | "Stop the process." |
| **execute / perform** | `do` / `run` | "Run the script." |
| **exhibit / display** | `show` | "The dashboard shows the status." |
| **commence / initiate** | `start` | "Start the service." |
| **terminate / cease** | `stop` | "Stop the engine." |
| **in accordance with** | `in compliance with` / `as specified in` | "Install the node as specified in Table 1." |
| **permit / allow** | `let` / `allow` | "This setting lets users connect." |
| **via** | `through` / `by` | "Send data through port 8080." |
| **as well as** | `and` | "Update the server and the client." |

*(For the comprehensive vocabulary and rule list, see [Vocabulary Guide](./references/vocabulary-guide.md) and [Rules Summary](./references/rules-summary.md))*

---

## Conversion Workflow (Step-by-Step)

When asked to write or rewrite technical text in ASD-STE100, follow these steps:

1. **Analyze Text Type**:
   - Determine whether the section is **Procedural** (steps/tasks) or **Descriptive** (architecture/specs).
2. **Deconstruct Compound Sentences**:
   - Split compound procedural sentences into distinct numbered steps.
   - Separate conditions and place them upfront (`If X, do Y.`).
3. **Replace Unapproved Vocabulary**:
   - Substitute ambiguous or overly complex words with approved STE counterparts (e.g., replace *verify* with *make sure*).
4. **Eliminate Passive Voice and Gerunds**:
   - Rewrite passive clauses into active agent-verb statements.
   - Replace participles and gerunds with finite verbs.
5. **Enforce Word Counts**:
   - Check procedural steps: ≤ 20 words.
   - Check descriptive statements: ≤ 25 words.
   - Shorten or split any sentence exceeding these limits.
6. **Audit Noun Groups**:
   - Break noun strings longer than 3 words using prepositions (*of*, *for*, *in*).
7. **Present the Result**:
   - Provide the STE-compliant text.
   - When requested, provide a brief audit explaining key corrections made (word count, active voice, vocabulary replacement).

---

## Helper Tools & Scripts

- [Audit Script (`audit_ste.py`)](./scripts/audit_ste.py): Fast Python linter to verify word count limits, unapproved vocabulary, and active voice in markdown files:
  ```bash
  python .agents/skills/asd-ste100/scripts/audit_ste.py path/to/document.md
  ```

---

## Detailed References

- [Rules Summary Guide](./references/rules-summary.md): Comprehensive breakdown of the 9 ASD-STE100 rule categories.
- [Vocabulary Guide](./references/vocabulary-guide.md): Extended dictionary of approved terms, unapproved terms, and part-of-speech restrictions.
- [Before and After Examples](./examples/before-after.md): Real-world comparisons across software, DevOps, and hardware documentation.

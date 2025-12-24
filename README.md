# Rin

Rin is an open-source AI agent project focused on exploring how autonomous agents can observe their environment, maintain memory, and make decisions over time.

This project is designed as a learning-first, research-oriented implementation of agent loops, inspired by modern AI systems that combine context, state, and action in an iterative cycle.

---

## 🚀 Project Goals

- Explore agent architectures based on **observe → reason → act** loops  
- Experiment with **short-term and long-term memory** mechanisms  
- Build a modular and extensible codebase for AI agents  
- Document the design decisions clearly so others can learn from them  

This repository is intentionally open-source to encourage transparency, collaboration, and shared learning.

---

## 🧠 Core Concepts

Rin is built around a few key ideas:

- **Observation** — ingesting inputs from the environment (logs, user input, time, state)
- **Memory** — storing and retrieving relevant past context
- **Decision-Making** — choosing actions based on current observations and memory
- **Action** — executing tasks or producing outputs
- **Looping** — repeating this cycle continuously or on a schedule

The focus is not on building a “finished product,” but on understanding *how* intelligent agents are structured.

---

## 🏗️ Project Structure (WIP)

```text
.
├── Core/           # Identity  and handling
├── logs/           # Where the agentic logs stay, all data will be transferred here
├── agents/         # (coming in the future)
├── tools/          # Specialties such as email, calendar, and more
├── memory/         # Agent memory, alongside the database
├── main.py         # where the main handling processes start
├── memory_test.py  # Testing the memory for debugging purposes
└── README.md

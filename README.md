<div align="center">

# Srimedha

**VTU-QFF-HC-0151** &nbsp;|&nbsp; Tier: **Online**

</div>

---

<div align="center">

| | |
| :--- | :--- |
| **Team** | Srimedha |
| **Team ID** | VTU-QFF-HC-0151 |
| **Tier** | Online |
| **Repository** | [vtu-hc-srimedha](https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-srimedha.git) |
| **Organisation** | [vtu-qiskit-fall-fest-2026](https://github.com/vtu-qiskit-fall-fest-2026) |
| **Event** | VTU-QFF Hackathon — VTU-Qiskit Fall Fest 2026 |

</div>

---

## 📌 Table of Contents

- [Team Members](#-team-members-github-ids)
- [Problem Statement](#-problem-statement)    vtu-qiskit-fall-fest-2026
    vtu-hc-srimedha

Repository navigation

    Code
    Pull requests
    Actions
    Projects
    Security and quality
    Insights

vtu-qiskit-fall-fest-2026
vtu-hc-srimedha
Public

tT
cyberhatc
cyberhatc
docs: professional README
9e18ca3
 · 
8 hours ago
Name	Last commit message
	Last commit date
.gitignore
	
Add .gitignore
	
9 hours ago
LICENSE
	
Add LICENSE
	
9 hours ago
README.md
	
docs: professional README
	
8 hours ago
requirements.txt
	
Add requirements.txt
	
9 hours ago
Repository files navigation

    README
    MIT license

Srimedha

VTU-QFF-HC-0151  |  Tier: Online
	
Team 	Srimedha
Team ID 	VTU-QFF-HC-0151
Tier 	Online
Repository 	vtu-hc-srimedha
Organisation 	vtu-qiskit-fall-fest-2026
Event 	VTU-QFF Hackathon — VTU-Qiskit Fall Fest 2026
📌 Table of Contents

    Team Members
    Problem Statement
    Proposed Solution
    Approach & Architecture
    Tech Stack
    Project Structure
    How to Run
    How to Push Code
    Submission Checklist
    Resources
    License

👥 Team Members (GitHub IDs)

    Members are added to this repository as collaborators and must accept the GitHub invitation before they can push. Add your GitHub username below.

# 	Name                	GitHub Username 	Role
1 	SAICHARITHA SRIRANGAM   saicharitha09       Team Lead
  	
2 	AKHIL DAVULA  	        akhil96477       	Developer
❓ Problem Statement

Problem: Malicious Android applications distributed through unofficial websites and messaging platforms can exploit sensitive permissions, deceive users, and compromise mobile financial security. Existing security measures may not adequately address every threat, particularly when applications or devices are compromised and traditional cryptographic systems face potential future quantum attacks

Why it matters: Mobile financial fraud can result in financial losses, stolen credentials, and compromised personal information. QuantumShield aims to address these risks through APK security analysis, simulated financial transaction risk assessment, and post-quantum-secure communication, helping demonstrate a proactive approach to protecting users in an evolving cybersecurity landscape.

Track / Category: Online  · Track 1 / Track 2 ·
💡 Proposed Solution

Solution: QuantumShield is a mobile security prototype that analyzes Android APKs for potentially risky indicators, assesses risks in simulated financial transactions, and demonstrates secure communication using post-quantum cryptography. It also uses Qiskit to demonstrate quantum algorithms and illustrate potential threats to traditional public-key cryptographic systems.

Key idea:Integrate APK security analysis, transaction risk assessment, and post-quantum cryptography with a Qiskit-based quantum experiment in one security platform.

Why this works: QuantumShield addresses mobile financial security risks through a combination of application analysis, transaction risk assessment, and post-quantum cryptography. It identifies potentially risky indicators in Android APKs, evaluates simulated financial transactions against predefined risk rules, and demonstrates how post-quantum key establishment can help protect communications against future quantum-related cryptographic threats. Its Qiskit experiment illustrates the potential impact of quantum algorithms on traditional public-key cryptography.
🧩 Approach & Architecture

    Input — what data goes in and in what format
    APK files: Android application packages (.apk) uploaded for static security analysis.
    Transaction data: Simulated transaction details, such as transaction amount and predefined risk indicators.
    Security messages: Test messages exchanged between the client and security service.
    Quantum experiment parameters: Small integer values used to demonstrate quantum factorization concepts with Qiskit.
    
    Preprocessing — cleaning, feature extraction, encoding
    - Extract APK metadata and requested permissions.
    - Identify potentially risky permission combinations and other available static indicators.
    - Validate transaction inputs and convert them into structured features.
    - Prepare test messages for cryptographic processing.
    - Configure the quantum circuit with the selected factorization example.

    Quantum core — the circuit, ansatz, or algorithm used
    Use Qiskit to construct and simulate a small-scale demonstration of Shor's algorithm, illustrating how quantum      computation can factor selected small integers.
    Use an appropriate post-quantum cryptography implementation, such as ML-KEM, to demonstrate shared-secret establishment between the client and security service.
    Keep the quantum experiment separate from APK detection: Qiskit demonstrates the quantum threat, while the security     analysis and cryptographic components address different parts of the problem.
    PostUse Qiskit to construct and simulate a small-scale demonstration of Shor's algorithm, illustrating how quantum computation can factor selected small integers.
Use an appropriate post-quantum cryptography implementation, such as ML-KEM, to demonstrate shared-secret establishment between the client and security service.
Keep the quantum experiment separate from APK detection: Qiskit demonstrates the quantum threat, while the security analysis and cryptographic components address different parts of the problem.

-processing — decoding, measurement, scoring
Convert extracted APK indicators into an explainable risk assessment using predefined rules.
Evaluate transaction features and determine whether the simulated transaction should proceed, trigger additional verification, or be flagged for review.
Process quantum circuit measurement results to identify candidate factors in the demonstration.
Derive a shared secret through ML-KEM and use it with authenticated encryption to protect test messages

    Output — what the user finally gets
    The platform will provide:
- APK security report: Detected indicators, explanations, and an estimated risk level.
- Transaction risk result: An indication of whether the simulated transaction is allowed, requires verification, or should be flagged.
- Secure communication demonstration: Results showing successful key establishment and protected message exchange.
- Quantum experiment results: Circuit visualization, measurement results, and the factorization demonstration.
- Security dashboard: A consolidated view of findings and results from the different components.

🛠️ Tech Stack
Layer 	Technology
Language 	Python 3.11+
Quantum SDK 	Qiskit >=1.0, Qiskit Aer, Qiskit Runtime
Optimisation 	Qiskit Optimization / COBYLA / SPSA
Simulation 	AerSimulator (statevector / noisemodel)
Environment 	JupyterLab / VS Code, venv
Version control 	Git + GitHub
📁 Project Structure

vtu-hc-srimedha/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project metadata (optional)
├── .gitignore
├── notebooks/             # Jupyter notebooks for experiments
│   └── exploration.ipynb
├── src/
│   ├── __init__.py
│   ├── circuit.py         # Quantum circuit construction
│   ├── optimizer.py       # Optimization loop
│   └── main.py            # Entry point
├── data/                  # Datasets (use Git LFS for large files)
├── tests/                 # Unit tests
│   └── test_circuit.py
└── docs/                  # Notes, diagrams, reports

🚀 How to Run
Prerequisites

    Python 3.11 or newer
    Git
    A GitHub account (you need collaborator access to this repo)

1. Clone the repository

git clone https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-srimedha.git
cd vtu-hc-srimedha

2. Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows (PowerShell)

3. Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

4. Run

python -m src.main

Or launch the notebook workflow:

jupyter lab

5. Run the tests

pytest -q

🔁 How to Push Code

    Full walkthrough: Git & Collaboration Handbook — collaboration workflow, branches, pull requests, reviews and conflict resolution.

Configure Git (first time only)

git config --global user.name  "Your Name"
git config --global user.email "you@example.com"

Everyday workflow

# 1. Get the latest changes
git checkout main
git pull origin main

# 2. Create a branch for your work
git checkout -b feature/my-task

# 3. Commit your work
git add .
git commit -m "feat: add variational circuit for the search problem"

# 4. Push the branch
git push -u origin feature/my-task

# 5. Open a Pull Request on GitHub and request a review
#    https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-srimedha/compare/main...feature/my-task

# 6. After approval, merge into main
git checkout main
git pull origin main
git branch -d feature/my-task

Commit message convention
Prefix 	Meaning
feat: 	New feature
fix: 	Bug fix
docs: 	Documentation only
test: 	Adding or fixing tests
refactor: 	Code restructure, no behaviour change
chore: 	Build/config/dependency changes
Useful commands

git status              # what changed
git log --oneline -10   # recent commits
git diff                # review changes before committing
git stash               # shelve changes temporarily
git pull --rebase       # update your branch on top of main

Collaborating on the same repo

    Never push directly to main — open a Pull Request.
    Pull before you push to avoid rejected commits.
    Commit often with clear messages.
    Resolve conflicts locally: git pull --rebase, fix the files, then git add + git rebase --continue.
    Ask for a review before merging — a second pair of eyes catches bugs fast.

✅ Submission Checklist

    Repository created and public
    All team members added as collaborators and invitations accepted
    README.md updated with project details, problem statement and solution
    Team members listed under Team Members
    requirements.txt committed and project runs from a clean clone
    Code pushed to main and the latest main builds successfully
    Notebooks committed with cleared outputs (or use nbstrip)
    README includes a demo screenshot / video link
    Short project summary submitted on the hackathon portal

📚 Resources
Resource 	Link
🔁 Git & collaboration handbook 	Git & Collaboration Handbook
❓ Problem statements, solutions & terms 	Problem Statements, Solutions & Terms
📄 README writing guide 	README Guide & Template
⚛️ Qiskit documentation 	https://docs.quantum.ibm.com/
⚛️ Qiskit Runtime & primitives 	https://quantum.cloud.ibm.com/docs/
🧪 Qiskit Aer simulator 	https://docs.quantum.ibm.com/guides/simulator
💻 IBM Quantum Platform 	https://quantum.cloud.ibm.com/
🎓 Qiskit textbook 	https://qiskit.qotlabs.org/learning/
📋 GitHub Docs 	https://docs.github.com/
📄 License

Released under the MIT License. See LICENSE for details.

Srimedha · Team ID VTU-QFF-HC-0151 · Tier Online · Built with ⚛️ Qiskit for the VTU-QFF Hackathon

⬆ Back to Top
About

VTU-QFF-HC-0151 | Srimedha | Tier: Online
Resources
Readme
MIT license
Activity
Custom properties
Stars
0 stars
Watchers
0 watching
Forks
0 forks
Report repository
Releases
No releases published
Packages
No packages published
Contributors
1 (1)

    @cyberhatc
    cyberhatcdevil_Mike


- [Proposed Solution](#-proposed-solution)
- [Approach & Architecture](#-approach--architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [How to Push Code](#-how-to-push-code)
- [Submission Checklist](#-submission-checklist)
- [Resources](#-resources)
- [License](#-license)

---

## 👥 Team Members (GitHub IDs)

> Members are added to this repository as **collaborators** and must accept the
> GitHub invitation before they can push. Add your GitHub username below.

| # | Name | GitHub Username | Role |
| :-- | :--- | :--- | :--- |
| 1 | _Add your name_ | _your-github-username_ | _Team Lead_ |
| 2 | _Add your name_ | _your-github-username_ | _Developer_ |
| 3 | _Add your name_ | _your-github-username_ | _Developer_ |

<!--
Optional: add a plain list instead of the table above.
- @username1
- @username2
-->

---

## ❓ Problem Statement

<!--
State the problem you are solving. Be specific: what is broken or missing,
who experiences it, and why does it matter. Link to the official problem
statement from the brief if one applies.
-->

**Problem:** _Describe the problem in 2–3 sentences._

**Why it matters:** _Explain the impact or opportunity._

**Track / Category:** _Online / Offline · Track 1 / Track 2 · <domain>_

---

## 💡 Proposed Solution

<!--
Describe your solution. Keep it concrete: the core idea, the user flow, and
the quantum/ML technique you are applying.
-->

**Solution:** _In 2–3 sentences, describe what you built._

**Key idea:** _The one-line technical summary of your approach._

**Why this works:** _How your approach addresses the problem statement._

---

## 🧩 Approach & Architecture

<!--
Walk through how it works. A simple pipeline diagram in text or Mermaid is ideal.
-->

```mermaid
flowchart LR
    A[Input Data] --> B[Preprocessing]
    B --> C[Quantum Circuit / Model]
    C --> D[Post-processing]
    D --> E[Output]
```

1. **Input** — _what data goes in and in what format_
2. **Preprocessing** — _cleaning, feature extraction, encoding_
3. **Quantum core** — _the circuit, ansatz, or algorithm used_
4. **Post-processing** — _decoding, measurement, scoring_
5. **Output** — _what the user finally gets_

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| Language | Python 3.11+ |
| Quantum SDK | Qiskit `>=1.0`, Qiskit Aer, Qiskit Runtime |
| Optimisation | Qiskit Optimization / COBYLA / SPSA |
| Simulation | AerSimulator (statevector / noisemodel) |
| Environment | JupyterLab / VS Code, `venv` |
| Version control | Git + GitHub |

---

## 📁 Project Structure

```text
vtu-hc-srimedha/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project metadata (optional)
├── .gitignore
├── notebooks/             # Jupyter notebooks for experiments
│   └── exploration.ipynb
├── src/
│   ├── __init__.py
│   ├── circuit.py         # Quantum circuit construction
│   ├── optimizer.py       # Optimization loop
│   └── main.py            # Entry point
├── data/                  # Datasets (use Git LFS for large files)
├── tests/                 # Unit tests
│   └── test_circuit.py
└── docs/                  # Notes, diagrams, reports
```

---

## 🚀 How to Run

### Prerequisites

- Python 3.11 or newer
- [Git](https://git-scm.com/downloads)
- A GitHub account (you need collaborator access to this repo)

### 1. Clone the repository

```bash
git clone https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-srimedha.git
cd vtu-hc-srimedha
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows (PowerShell)
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run

```bash
python -m src.main
```

Or launch the notebook workflow:

```bash
jupyter lab
```

### 5. Run the tests

```bash
pytest -q
```

---

## 🔁 How to Push Code

> Full walkthrough: **[Git & Collaboration Handbook](../vtu-hc-guide-git-and-collaboration)** — collaboration
> workflow, branches, pull requests, reviews and conflict resolution.

### Configure Git (first time only)

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

### Everyday workflow

```bash
# 1. Get the latest changes
git checkout main
git pull origin main

# 2. Create a branch for your work
git checkout -b feature/my-task

# 3. Commit your work
git add .
git commit -m "feat: add variational circuit for the search problem"

# 4. Push the branch
git push -u origin feature/my-task

# 5. Open a Pull Request on GitHub and request a review
#    https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-srimedha/compare/main...feature/my-task

# 6. After approval, merge into main
git checkout main
git pull origin main
git branch -d feature/my-task
```

### Commit message convention

| Prefix | Meaning |
| :--- | :--- |
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `test:` | Adding or fixing tests |
| `refactor:` | Code restructure, no behaviour change |
| `chore:` | Build/config/dependency changes |

### Useful commands

```bash
git status              # what changed
git log --oneline -10   # recent commits
git diff                # review changes before committing
git stash               # shelve changes temporarily
git pull --rebase       # update your branch on top of main
```

### Collaborating on the same repo

- **Never push directly to `main`** — open a Pull Request.
- **Pull before you push** to avoid rejected commits.
- **Commit often** with clear messages.
- **Resolve conflicts** locally: `git pull --rebase`, fix the files, then `git add` + `git rebase --continue`.
- **Ask for a review** before merging — a second pair of eyes catches bugs fast.

---

## ✅ Submission Checklist

- [ ] Repository created and **public**
- [ ] All team members added as **collaborators** and invitations accepted
- [ ] `README.md` updated with project details, problem statement and solution
- [ ] Team members listed under [Team Members](#-team-members-github-ids)
- [ ] `requirements.txt` committed and project runs from a clean clone
- [ ] Code pushed to `main` and the latest `main` builds successfully
- [ ] Notebooks committed with **cleared outputs** (or use `nbstrip`)
- [ ] `README` includes a demo screenshot / video link
- [ ] Short project summary submitted on the hackathon portal

---

## 📚 Resources

| Resource | Link |
| :--- | :--- |
| 🔁 Git & collaboration handbook | [Git & Collaboration Handbook](../vtu-hc-guide-git-and-collaboration) |
| ❓ Problem statements, solutions & terms | [Problem Statements, Solutions & Terms](../vtu-hc-guide-problem-and-solution) |
| 📄 README writing guide | [README Guide & Template](../vtu-hc-guide-readme-template) |
| ⚛️ Qiskit documentation | https://docs.quantum.ibm.com/ |
| ⚛️ Qiskit Runtime & primitives | https://quantum.cloud.ibm.com/docs/ |
| 🧪 Qiskit Aer simulator | https://docs.quantum.ibm.com/guides/simulator |
| 💻 IBM Quantum Platform | https://quantum.cloud.ibm.com/ |
| 🎓 Qiskit textbook | https://qiskit.qotlabs.org/learning/ |
| 📋 GitHub Docs | https://docs.github.com/ |

---

## 📄 License

Released under the [MIT License](LICENSE). See `LICENSE` for details.

---

<div align="center">

**Srimedha** · Team ID `VTU-QFF-HC-0151` · Tier `Online`
· Built with ⚛️ Qiskit for the VTU-QFF Hackathon

[⬆ Back to Top](#srimedha)

</div>

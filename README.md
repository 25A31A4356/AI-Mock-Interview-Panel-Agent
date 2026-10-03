# AI Mock Interview Panel Agent 🎯

> **Autonomous Enterprise Multi-Persona Technical & Behavioral Interview Simulation System**

An enterprise-grade, single-page conversational interview simulator powered by multi-persona AI agents, real-time speech interaction, interactive code execution, and deep diagnostic competency evaluation using the STAR (Situation, Task, Action, Result) methodology.

---

## 🌟 Key Features

### 1. Multi-Persona Panel Dynamics
- **System Architect (Elena Vance)**: Deep-dive probing into scalability, distributed systems trade-offs, concurrency, cache invalidation, and data modeling.
- **Engineering Manager (Marcus Zhao)**: Pragmatic evaluation of engineering leadership, agile execution, conflict resolution, technical debt management, and ownership.
- **Talent & Culture Lead (Sarah Jenkins)**: Behavioral assessment, team dynamics, communication clarity, ethics, empathy, and organizational alignment.

### 2. Live Interactive Studio
- **Adaptive Question Flow**: Dynamic questioning engine that generates follow-up counter-questions based on the depth, clarity, and keywords in candidate responses.
- **Web Speech API Integration**:
  - Hands-free voice dictation (Speech-to-Text) with live input streaming.
  - Distinct synthetic text-to-speech voices for each panelist persona.
- **Embedded Code Workspace**:
  - In-browser code editor with syntax indentation and multi-language support (JavaScript, Python, Go, Java).
  - Safe sandboxed runtime execution with console output streaming.
- **Real-Time Stress & Timer Controls**:
  - Configurable 3-minute per-question countdown with visual pacing indicators.
  - Question skip / next panelist delegation controls.

### 3. STAR Diagnostic Scorecard & Analytics
- **Comprehensive Competency Matrix**:
  - Technical Architecture & Problem Solving
  - System Design & Scalability
  - Behavioral & Cross-Functional Collaboration
  - Communication Precision & Executive Presence
- **STAR Breakdown**: Granular scoring of Situation, Task, Action, and Result components.
- **Actionable AI Feedback**: Highlighted strengths, targeted improvement vectors, and personalized study recommendations.
- **Export Capabilities**: Clean printable PDF / HTML audit report generation.

---

## 🚀 Quick Start

### Option 1: One-Click Local Server (Recommended)
Run the bundled lightweight Python server to automatically launch the application in your default browser:

```bash
python run.py
```
*The application will automatically open at `http://127.0.0.1:8000`.*

### Option 2: Direct Browser Launch
Open `index.html` directly in any modern web browser (Google Chrome, Microsoft Edge, or Mozilla Firefox):

```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

---

## 🛠️ Architecture & Tech Stack

- **Zero-Dependency Architecture**: Entirely self-contained in a single reactive `index.html` bundle.
- **UI & Design System**: Tailwind CSS (CDN), Lucide SVG Icons, dark enterprise slate palette inspired by modern developer platforms (Linear / Stripe).
- **Speech Engine**: Native Web Speech Recognition (`webkitSpeechRecognition`) and SpeechSynthesis API.
- **Local Server**: Pure standard-library Python `http.server` with reusable socket configuration.

---

## 📄 License
MIT License. Built for technical interview preparation, competitive mock trials, and engineering competency assessments.

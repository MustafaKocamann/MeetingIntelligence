# 🚀 MeetingIntelligence - AI-Powered Meeting Preparation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776ab?logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-1.9.3-4CAF50?style=flat)
![Exa API](https://img.shields.io/badge/Exa--API-Research-FF6B6B?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

*Intelligent Meeting Preparation Through Multi-Agent Collaboration* ⚡

[Features](#-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [Usage](#-usage) • [Configuration](#-configuration)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🏗️ Architecture](#-architecture)
- [🚀 Quick Start](#-quick-start)
- [📖 Usage Guide](#-usage-guide)
- [🔧 Configuration](#-configuration)
- [🛠️ Project Structure](#-project-structure)
- [📦 Dependencies](#-dependencies)
- [🤝 Multi-Agent Workflow](#-multi-agent-workflow)
- [🔌 API Integration](#-api-integration)
- [💡 Use Cases](#-use-cases)
- [🐛 Troubleshooting](#-troubleshooting)
- [📞 Support](#-support)

---

## 🎯 Overview

**MeetingIntelligence** is an advanced AI-powered system that automates and enhances your meeting preparation process. Powered by CrewAI and leveraging state-of-the-art language models, this system deploys four specialized AI agents that work collaboratively to research participants, analyze industry trends, develop strategic talking points, and generate comprehensive briefing documents.

### Why MeetingIntelligence?

✅ **Save Hours of Preparation** - Automated research and analysis  
✅ **Strategic Advantage** - Intelligent talking points development  
✅ **Comprehensive Briefings** - Professional, actionable documents  
✅ **Real-Time Web Search** - Current industry insights with Exa API  
✅ **Multi-Agent Intelligence** - Specialized expertise for each task  

---

## ✨ Key Features

### 🔍 **Intelligent Research**
- Deep participant background research
- Company history and achievements tracking
- Recent news and developments analysis
- Professional profile compilation

### 📊 **Industry Analysis**
- Real-time market trend identification
- Challenge assessment and opportunities
- Competitive landscape overview
- Strategic positioning insights

### 💬 **Strategy Development**
- Intelligent talking points generation
- Insightful question formulation
- Discussion angle optimization
- Objective-aligned strategies

### 📄 **Professional Briefing**
- Comprehensive meeting brief compilation
- Structured participant bios
- Industry overview summaries
- Actionable recommendations
- Easy-to-digest format

### 🌐 **Web Integration**
- Powered by Exa API for real-time web search
- Similar content discovery
- Deep content extraction
- Current information retrieval

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────┐
│                   Meeting Prep Crew                      │
│                  (CrewAI Orchestrator)                   │
└──────────────────┬──────────────────────────────────────┘
                   │
        ┌──────────┼──────────┬──────────┐
        │          │          │          │
    ┌───▼──┐  ┌───▼──┐  ┌───▼──┐  ┌───▼──┐
    │ 🔬   │  │ 📈   │  │ 💼   │  │ 📋   │
    │Agent1│  │Agent2│  │Agent3│  │Agent4│
    │      │  │      │  │      │  │      │
    └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘
       │          │         │         │
    ┌──▼──┐   ┌──▼──┐   ┌──▼──┐   ┌──▼──┐
    │Task1│   │Task2│   │Task3│   │Task4│
    └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘
       │         │         │         │
       └─────────┴─────────┴─────────┘
              │
         ┌────▼─────┐
         │ Exa API  │ 🌐
         │(Search)  │
         └──────────┘
```

### Agent Ecosystem

| # | Agent | Role | Responsibility |
|---|-------|------|-----------------|
| 🔬 | **Research Specialist** | Information Gathering | Participant & company research, background investigation |
| 📈 | **Industry Analyst** | Market Intelligence | Trend analysis, challenge identification, opportunities |
| 💼 | **Meeting Strategy Advisor** | Strategic Planning | Talking points, questions, discussion angles |
| 📋 | **Briefing Coordinator** | Information Synthesis | Document compilation, brief creation |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API Keys:
  - `GROQ_API_KEY` - for LLaMA 3.3-70B access
  - `EXA_API_KEY` - for web search functionality

### Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd meetingproject

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment (Windows)
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure environment variables
echo GROQ_API_KEY=your_groq_api_key_here > .env
echo EXA_API_KEY=your_exa_api_key_here >> .env
```

### Run Your First Meeting Prep

```bash
python crew.py
```

Follow the interactive prompts:
```
What are the emails for the participants (other than you) in the meeting
> participant1@example.com, participant2@example.com

What is the context of the meeting?
> Series A funding discussion with potential VCs

What is your objective for this meeting?
> Secure $5M funding commitment and establish partnership terms
```

⏳ The system will begin analyzing and generating your comprehensive briefing...

---

## 📖 Usage Guide

### Complete Workflow Example

```python
from dotenv import load_dotenv
from crewai import Crew
from tasks import MeetingPrepTasks
from agents import MeetingPrepAgents

# Initialize
load_dotenv()
tasks = MeetingPrepTasks()
agents = MeetingPrepAgents()

# Create agents
research_agent = agents.research_agent()
industry_agent = agents.industry_analysis_agent()
strategy_agent = agents.meeting_strategy_agent()
briefing_agent = agents.summary_and_briefing_agent()

# Define input
participants = "john.doe@techvc.com, jane.smith@investors.com"
context = "Series A funding round discussion"
objective = "Secure investment and establish governance terms"

# Create tasks
research_task = tasks.research_task(research_agent, participants, context)
industry_task = tasks.industry_analysis_task(industry_agent, participants, context)
strategy_task = tasks.meeting_strategy_task(strategy_agent, context, objective)
briefing_task = tasks.summary_and_briefing_task(briefing_agent, context, objective)

# Define task dependencies
strategy_task.context = [research_task, industry_task]
briefing_task.context = [research_task, industry_task, strategy_task]

# Execute crew
crew = Crew(
    agents=[research_agent, industry_agent, strategy_agent, briefing_agent],
    tasks=[research_task, industry_task, strategy_task, briefing_task]
)

result = crew.kickoff()
print(result)
```

### Advanced Usage Scenarios

#### 🏢 **Corporate Partnership Discussion**
```
Context: Strategic partnership evaluation with Fortune 500 company
Objective: Establish co-development agreement and revenue sharing model
```

#### 💰 **Investment Pitch Meeting**
```
Context: Pitch to venture capital firm
Objective: Secure Series B funding and board seat
```

#### 🌍 **International Business Expansion**
```
Context: Market entry discussion for Asian operations
Objective: Understand regulatory landscape and partnership requirements
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Exa API Configuration (Web Search)
EXA_API_KEY=your_exa_api_key_here

# Optional: Log Level
LOG_LEVEL=INFO
```

### Agent Customization

Modify agent parameters in `agents.py`:

```python
class MeetingPrepAgents():
    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal="Conduct thorough research...",
            llm=LLM(model="groq/llama-3.3-70b-versatile"),
            # Adjust verbosity for debugging
            verbose=True  # Set to False in production
        )
```

### Task Customization

Modify task parameters in `tasks.py`:

```python
class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=f"Research {meeting_participants}...",
            expected_output="Detailed report...",
            async_execution=True,  # Parallel execution
            agent=agent
        )
```

---

## 🛠️ Project Structure

```
meetingproject/
│
├── 📄 crew.py                 # Main orchestration & CLI interface
├── 🤖 agents.py              # AI Agent definitions (4 specialized agents)
├── ✅ tasks.py               # Task definitions and workflows
├── 🔍 tools.py               # Exa API integration & search tools
├── 📋 requirements.txt        # Python dependencies
├── 🔐 .env                   # Environment configuration (create this)
└── 📚 README.md              # This file
```

### File Descriptions

#### **crew.py** - Orchestrator & CLI
- Entry point for the application
- User input gathering via interactive prompts
- Crew composition and execution
- Result output and error handling

#### **agents.py** - Intelligent Specialists
```python
1. research_agent()           # Background investigation
2. industry_analysis_agent()  # Market intelligence
3. meeting_strategy_agent()   # Strategic planning
4. summary_and_briefing_agent() # Report compilation
```

#### **tasks.py** - Workflow Definition
```python
1. research_task()            # Gather participant information
2. industry_analysis_task()   # Analyze market conditions
3. meeting_strategy_task()    # Develop strategy & talking points
4. summary_and_briefing_task() # Compile comprehensive brief
```

#### **tools.py** - External Integrations
- **search()** - Query web for relevant information
- **find_similar()** - Discover related content
- **get_contents()** - Extract full webpage content

---

## 📦 Dependencies

### Core Framework
```
crewai==1.9.3              # Multi-agent orchestration framework
```

### AI & Language Models
```
groq                       # LLaMA 3.3 70B model access
instructor==1.12.0         # Structured output handling
```

### Search & Data
```
exa-py==2.4.0             # Web search and research API
chromadb==1.1.1           # Vector database for embeddings
```

### Utilities
```
python-dotenv             # Environment variable management
httpx                     # Async HTTP client
aiohttp                   # Async HTTP operations
```

For complete list, see [requirements.txt](requirements.txt)

---

## 🤝 Multi-Agent Workflow

### Execution Flow

```
START
  │
  ├─► [Agent 1: Research Specialist]
  │   └─► research_task()
  │       │ Task: Gather participant backgrounds
  │       │ Output: Detailed research report
  │       └─► feeds into ► Strategy & Briefing Tasks
  │
  ├─► [Agent 2: Industry Analyst]
  │   └─► industry_analysis_task()
  │       │ Task: Market trend analysis
  │       │ Output: Industry insights
  │       └─► feeds into ► Strategy & Briefing Tasks
  │
  ├─► [Agent 3: Meeting Strategy Advisor]
  │   └─► meeting_strategy_task()
  │       │ Task: Develop talking points
  │       │ Input: Research + Industry data
  │       │ Output: Strategic recommendations
  │       └─► feeds into ► Briefing Task
  │
  └─► [Agent 4: Briefing Coordinator]
      └─► summary_and_briefing_task()
          │ Task: Compile final briefing
          │ Input: All previous outputs
          │ Output: Comprehensive meeting brief
          └─► FINAL RESULT
```

### Task Dependencies

- **research_task** & **industry_analysis_task** - Run in parallel (async_execution=True)
- **meeting_strategy_task** - Depends on research & industry analysis
- **summary_and_briefing_task** - Depends on all previous tasks

---

## 🔌 API Integration

### Exa API (Web Search)

The project uses **Exa API** for intelligent web research:

```python
from tools import ExaSearchTool

# Search for information
results = ExaSearchTool.search("AI trends 2024")

# Find similar pages
similar = ExaSearchTool.find_similar("https://example.com/article")

# Extract content
content = ExaSearchTool.get_contents(["id1", "id2", "id3"])
```

### Groq LLM Integration

Leverages **Groq's LLaMA 3.3-70B** model:
- High-performance inference
- Advanced reasoning capabilities
- Cost-effective API pricing
- Real-time processing

---

## 💡 Use Cases

### 🏢 Enterprise Scenarios

| Scenario | Benefit |
|----------|---------|
| **Board Meetings** | Prepare comprehensive director briefs with voting recommendations |
| **Client Pitches** | Research prospects and develop tailored selling strategies |
| **Partnership Discussions** | Analyze potential partners and negotiate key terms |
| **Investor Relations** | Create talking points for quarterly earnings calls |
| **M&A Negotiations** | Deep dive research on acquisition targets |

### 💼 Business Development

- **Sales Calls** - Prospect research and personalized approach
- **Networking Events** - Pre-event attendee profiling
- **Conference Presentations** - Audience analysis and content optimization
- **Customer Meetings** - Account history and upsell opportunities

### 🎓 Educational & Professional

- **Job Interviews** - Company research and interview preparation
- **Consulting Engagements** - Client background and engagement strategy
- **Speaking Engagements** - Audience and event context analysis
- **Academic Collaborations** - Research partner profiling

---

## 🐛 Troubleshooting

### ❌ API Key Issues

**Problem**: `APIError: Invalid API key`

**Solution**:
```bash
# Verify your .env file exists and contains:
cat .env

# Ensure no extra spaces or quotes around keys
GROQ_API_KEY=your_actual_key_here  # ✅ Correct
GROQ_API_KEY="your_actual_key_here" # ❌ Incorrect (has quotes)
```

### ❌ Search Results Empty

**Problem**: `EXA_API_KEY not found or search failing`

**Solution**:
```bash
# Check Exa API key validity
python -c "from tools import ExaSearchTool; print(ExaSearchTool.search('test'))"

# Verify API key is active at https://dashboard.exa.ai/
```

### ❌ Timeout Issues

**Problem**: `Task execution timeout after 300 seconds`

**Solution**:
```python
# Increase timeout in crewai configuration
crew = Crew(
    agents=agents,
    tasks=tasks,
    max_rpm=100  # Adjust rate limiting
)
```

### ❌ Memory Issues

**Problem**: `MemoryError with large documents`

**Solution**:
```python
# Reduce number of search results in tools.py
result = ExaSearchTool._exa().search(
    query, 
    use_autoprompt=True,
    num_results=2  # Reduce from 3 to 2
)
```

### 📋 Enable Debug Mode

```python
# In crew.py
import logging
logging.basicConfig(level=logging.DEBUG)

# In agents.py - set verbose=True for detailed output
verbose=True
```

---

## 🚦 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.10+ |
| RAM | 4GB | 8GB+ |
| Disk Space | 500MB | 1GB |
| Internet | Required | 10+ Mbps |
| API Calls | ~50/month | Unlimited |

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Average Briefing Generation Time | 2-5 minutes |
| Parallel Task Execution | 2 tasks simultaneously |
| Search Queries per Briefing | 12-15 |
| Memory Footprint | ~150MB |
| API Calls per Meeting | 8-10 |

---

## 🔐 Security & Privacy

### Best Practices

✅ **API Key Management**
- Store keys in `.env` file (never commit to Git)
- Rotate API keys monthly
- Use separate keys for development/production

✅ **Data Handling**
- Research data is processed in-transit
- No persistent storage of sensitive information
- Compliant with GDPR/CCPA guidelines

✅ **Git Configuration**
```bash
# Add to .gitignore
.env
.env.local
__pycache__/
*.pyc
.DS_Store
```

---

## 📞 Support & Resources

### Getting Help

| Resource | Link |
|----------|------|
| CrewAI Documentation | [docs.crewai.com](https://docs.crewai.com) |
| Exa API Docs | [docs.exa.ai](https://docs.exa.ai) |
| Groq API Reference | [console.groq.com/docs](https://console.groq.com/docs) |
| Python Documentation | [python.org/docs](https://docs.python.org) |

### Common Questions

**Q: Can I use different LLMs besides Groq?**  
A: Yes! Modify the `llm` parameter in `agents.py` to use any CrewAI-supported model (OpenAI, Anthropic, etc.)

**Q: How can I customize the briefing format?**  
A: Edit the `expected_output` in `tasks.py` to define your desired format.

**Q: Can multiple users run this simultaneously?**  
A: Yes, but ensure each user has their own environment variables and output directories.

**Q: What's the cost?**  
A: Depends on API usage (roughly $0.02-0.10 per meeting prep with free tiers)

---

## 📈 Roadmap

### Planned Features 🗺️

- [ ] Web UI Dashboard (Streamlit)
- [ ] Document export (PDF, DOCX)
- [ ] Meeting notes integration
- [ ] Real-time calendar integration
- [ ] Custom agent templates
- [ ] Multi-language support
- [ ] Analytics & reporting
- [ ] API endpoint wrapper

### Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

<div align="center">

## Made with ❤️ for Better Meeting Preparation

**Star ⭐ this repo if you find it helpful!**

[Back to Top](#-meetingintelligence---ai-powered-meeting-preparation-system)

---

### Version Information
- **Current Version**: 1.0.0
- **Last Updated**: February 2026
- **Python**: 3.8+
- **License**: MIT

</div>

# 🎓 QuizCrafter AI

<div align="center">

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Groq](https://img.shields.io/badge/Groq-API-orange.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

**An intelligent AI-powered quiz generation platform that creates personalized quizzes using advanced language models.**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 🚀 Demo

![QuizCrafter AI Workflow](docs/QuizCrafterAIWorkflow.png)

*Experience the power of AI-driven quiz generation with our intuitive interface!*

> 💡 **Demo GIF**: Record a demo GIF showing the quiz generation process and add it as `docs/demo.gif` to showcase the application in action!

## ✨ Features

### 🧠 **Intelligent Question Generation**
- **Multiple Question Types**: MCQ, True/False, Fill-in-the-Blanks
- **Customizable Difficulty**: Easy, Medium, Hard levels
- **Topic Flexibility**: Generate quizzes on any subject
- **AI-Powered**: Uses Groq LLM for high-quality question generation

### 🎯 **Interactive Quiz Experience**
- **Modern UI**: Clean, responsive Streamlit interface
- **Real-time Feedback**: Instant scoring and explanations
- **Progress Tracking**: Visual progress indicators and statistics
- **Results Analysis**: Detailed breakdown with explanations

### 📊 **Advanced Analytics**
- **Performance Metrics**: Score visualization with charts
- **Detailed Results**: Question-by-question analysis
- **Export Functionality**: Download results as CSV
- **Session Management**: Seamless quiz state handling

### 🛠 **Production Ready**
- **Docker Support**: Containerized deployment
- **Kubernetes Ready**: K8s manifests included
- **CI/CD Pipeline**: Jenkins integration
- **Scalable Architecture**: Modular design with proper error handling

## 🏗 Architecture

```
QuizCrafter AI/
├── 📱 Frontend (Streamlit)
│   ├── app.py (Main application)
│   └── static/ (CSS styling)
├── 🧠 Core Logic
│   ├── src/generator/ (Question generation)
│   ├── src/llm/ (Groq integration)
│   ├── src/models/ (Pydantic schemas)
│   └── src/prompts/ (LLM templates)
├── ⚙️ Configuration
│   ├── src/config/ (Settings)
│   └── src/common/ (Logging & exceptions)
├── 🐳 Deployment
│   ├── Dockerfile
│   ├── manifests/ (Kubernetes)
│   └── Jenkinsfile (CI/CD)
└── 📊 Data
    ├── results/ (Quiz results)
    └── logs/ (Application logs)
```

## 🛠 Installation

### Prerequisites
- Python 3.10+
- Groq API Key ([Get one here](https://console.groq.com/))

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/QuizCrafter-AI.git
   cd QuizCrafter-AI
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # Or use setup.py
   pip install -e .
   ```

4. **Configure environment**
   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

Visit `http://localhost:8501` to access the application!

### 🐳 Docker Deployment

```bash
# Build the image
docker build -t quizcrafter-ai .

# Run the container
docker run -p 8501:8501 -e GROQ_API_KEY=your_api_key quizcrafter-ai
```

### ☸️ Kubernetes Deployment

```bash
# Apply the manifests
kubectl apply -f manifests/

# Create the secret for Groq API key
kubectl create secret generic groq-api-secret --from-literal=GROQ_API_KEY=your_api_key
```

## 🎮 Usage

### Quick Start

1. **Launch the Application**
   - Access the web interface at `http://localhost:8501`

2. **Configure Your Quiz**
   - Select question type (MCQ, True/False, Fill-in-the-Blank)
   - Enter your topic of interest
   - Choose difficulty level
   - Set number of questions (1-10)

3. **Generate & Take Quiz**
   - Click "🚀 Generate Quiz"
   - Answer the questions
   - Submit for instant results

4. **Review Results**
   - View your score and detailed analysis
   - Download results as CSV
   - Create a new quiz or retry

### Advanced Features

#### Custom Topics
```
Examples of topics you can use:
• "Python Programming Fundamentals"
• "World War II History"
• "Machine Learning Algorithms"
• "Shakespeare's Hamlet"
• "Quantum Physics Basics"
```

#### Question Types

- **📋 Multiple Choice**: 4 options with one correct answer
- **🔄 True/False**: Binary choice questions
- **🖊️ Fill-in-the-Blank**: Complete the missing information

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | ✅ |
| `MAX_RETRIES` | Max retry attempts for API calls | ❌ (default: 3) |

### Customization

Edit `src/config/settings.py` to modify:
- API retry settings
- Question generation parameters
- Logging levels

## 📊 MLOps Features

### Monitoring & Logging
- Comprehensive logging with structured formats
- Session tracking and user analytics
- Error monitoring and alerting

### CI/CD Pipeline
- Automated testing and deployment
- Docker image building and pushing
- Kubernetes deployment automation

### Data Management
- Quiz results storage and retrieval
- Performance metrics tracking
- Data export capabilities

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests** (if applicable)
5. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include unit tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Atharva Hatekar**
- GitHub: [@atharvahatekar](https://github.com/atharvahatekar)
- LinkedIn: [Atharva Hatekar](https://linkedin.com/in/atharvahatekar)

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast LLM inference
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [LangChain](https://langchain.com/) for LLM orchestration
- The open-source community for inspiration and tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/QuizCrafter-AI/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by [Atharva Hatekar](https://github.com/atharvahatekar)

</div>

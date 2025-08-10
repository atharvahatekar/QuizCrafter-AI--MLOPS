# Contributing to QuizCrafter AI

Thank you for your interest in contributing to QuizCrafter AI! 🎉

## How to Contribute

### 🐛 Reporting Bugs

1. Check if the issue already exists in our [Issues](https://github.com/atharvahatekar/QuizCrafter-AI/issues)
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Environment details (OS, Python version, etc.)

### 💡 Suggesting Features

1. Open a new issue with the "enhancement" label
2. Describe the feature and its benefits
3. Provide use cases and examples

### 🔧 Code Contributions

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/QuizCrafter-AI.git
   ```
3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**
5. **Test your changes**
6. **Commit with clear messages**
   ```bash
   git commit -m "Add: Brief description of changes"
   ```
7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Create a Pull Request**

## Development Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

2. **Set up environment**
   ```bash
   cp .env.example .env
   # Add your API keys
   ```

3. **Run tests**
   ```bash
   pytest
   ```

## Code Style

- Follow PEP 8
- Use type hints where possible
- Add docstrings to functions and classes
- Keep functions focused and small
- Write meaningful variable names

## Pull Request Guidelines

- Include a clear description of changes
- Link to relevant issues
- Add tests for new functionality
- Update documentation if needed
- Ensure all tests pass

## Questions?

Feel free to open an issue for any questions or reach out to the maintainers.

Thank you for contributing! 🚀

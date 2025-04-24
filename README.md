# 🧠 Runtime Error Insight Agent

A developer-first tool that captures runtime errors, queries an AI agent (like ChatGPT), and returns actionable insights including root cause analysis and potential resolutions.

## 🎯 Goal

**Automate error debugging** by integrating intelligent analysis into your development workflows and CI/CD pipelines.

---

## 🚀 Features

- 📦 **Capture Runtime Errors**  
  Automatically intercept uncaught exceptions and stack traces.

- 🤖 **Query AI for Insight**  
  Send the captured error to a local or cloud-based AI agent (e.g., ChatGPT, Ollama, LM Studio) for analysis.

- 📋 **Get Useful Output**  
  Returns:
  - Root cause summary
  - Suggested fixes or resolutions
  - Links to helpful documentation (optional)

---

## 🧰 Integration Options

### ✅ **As a CLI Tool**
Use it in CI/CD pipelines to auto-analyze errors on failure.

```bash
$ error-insight analyze --log error.log


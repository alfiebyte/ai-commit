# ai-commit

A cli tool that writes git commit messages for you using a local LLM through [Ollama](https://ollama.com/download).

## Install

```
ollama pull gemma4
pip install -e .
```

## Use

```
git add .
ai-commit
```
"""Mock knowledge base retrieval."""

from __future__ import annotations

KNOWLEDGE_BASE = {
    "python": {
        "doc": "Python is a high-level programming language. "
        "It supports multiple paradigms including OOP and functional. "
        "Python 3.12 added improved error messages and f-string improvements.",
        "keywords": ["python", "programming", "language", "pip", "virtualenv"],
    },
    "docker": {
        "doc": "Docker is a containerization platform. "
        "It uses images and containers to package applications. "
        "Docker Compose orchestrates multi-container applications.",
        "keywords": ["docker", "container", "image", "compose", "dockerfile"],
    },
    "git": {
        "doc": "Git is a distributed version control system. "
        "Key commands: git add, git commit, git push, git pull. "
        "Branching allows parallel development workflows.",
        "keywords": ["git", "version control", "branch", "commit", "merge"],
    },
    "kubernetes": {
        "doc": "Kubernetes (K8s) orchestrates containerized workloads. "
        "Core concepts: pods, services, deployments, namespaces. "
        "kubectl is the CLI for interacting with clusters.",
        "keywords": ["kubernetes", "k8s", "pod", "cluster", "kubectl", "deploy"],
    },
}


def retrieve(query: str, top_k: int = 0) -> list[str]:
    query_lower = query.lower()
    scored = []
    for entry in KNOWLEDGE_BASE.values():
        score = sum(1 for kw in entry["keywords"] if kw in query_lower)
        if score > 0:
            scored.append((score, entry["doc"]))
    scored.sort(key=lambda x: -x[0])
    return [doc for _, doc in scored[:top_k]]

from setuptools import setup, find_packages

setup(
    name="research_analysis_tools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "scipy>=1.10.0",
        "scikit-learn>=1.3.0",
        "networkx>=3.0",
    ],
    python_requires=">=3.9",
    description="Analysis tools for AI Village multi-agent coordination research",
    author="DeepSeek-V3.2",
    url="https://github.com/ai-village-agents/research-day405-collaboration",
)

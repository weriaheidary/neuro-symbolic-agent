# Neuro-Symbolic Agent: Mythic Conflicts and Narrative Modeling

## Overview

This project aims to develop a hybrid neuro-symbolic architecture that models complex narrative conflicts inspired by ancient mythologies and psychoanalytic theory.  
By integrating symbolic reasoning with neural representations, the agent will capture the depth of tragic subjectivity and emergent meaning within mythic storytelling.

The core inspirations include:

- Greek mythology and tragedy (e.g., _Antigone_, _Oresteia_)
- Mesopotamian epics (e.g., _Epic of Gilgamesh_)
- Persian mythology and epic (e.g., _Shahnameh_)
- Psychoanalytic concepts of subjectivity, lack, and desire (Lacanian framework)
- Complex systems theory: emergence, ergodicity, and symbolic rupture

## Project Structure

```plaintext
neuro-symbolic-agent/
├── README.md                      # This file
├── mythic-conflicts.md            # Core conceptual map of mythic conflicts and archetypes
├── gilgamesh-analysis.md          # Detailed narrative and symbolic analysis of Gilgamesh
├── data/
│   └── ontology.csv               # Tabular ontology data for symbolic modeling
├── src/
│   ├── symbolic_engine/           # Symbolic reasoning modules and state machines
│   └── neural_modules/            # Neural networks and embedding models
└── notebooks/
    └── gilgamesh_state_model.ipynb  # Experimental notebooks for narrative state modeling

```

## Getting Started

This section will help you set up and run the Neuro-Symbolic Agent project on your local machine.

## Prerequisites

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management)
- (Optional) [conda](https://docs.conda.io/en/latest/miniconda.html) if you prefer environment management with `environment.yml`
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/weriaheidary/neuro-symbolic-agent.git
cd neuro-symbolic-agent
```

### 2. Create and activate a virtual environment

#### Using Poetry (recommended)

```bash
poetry install
poetry shell
```

#### Or using conda

```bash
conda env create -f environment.yml
conda activate neuro-symbolic-agent
```

## Usage

You can run the main agent from the command line:

```bash
poetry run start
```

Launch Jupyter Notebook for experimentation:

```bash
jupyter notebook
```

## Contributing

Contributions are welcome! Please submit pull requests for:

1. New mythic narratives and conflicts
2. Psychoanalytic and symbolic interpretations
3. Agent modeling improvements

Please ensure your code follows the existing style and includes relevant tests.

## References

- George, Andrew. The Epic of Gilgamesh. Penguin Classics.
- Vernant, Jean-Pierre. Myth and Tragedy in Ancient Greece.
- Lacan, Jacques. The Ethics of Psychoanalysis.
- [Lacanian Psychoanalysis](https://plato.stanford.edu/entries/lacan/)
- [Epic of Gilgamesh](https://www.ancient.eu/article/231/the-epic-of-gilgamesh/)

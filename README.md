# py-time-series: Probabilistic, Statistical, and Time Series Analysis Learning

This repository serves as a dedicated learning and development space for Python-based data analysis, with a strong focus on:

- **Probabilistic and Statistical Methods:** Exploring core concepts, theoretical foundations, and practical implementations.
- **Time Series Analysis (TSA):** Techniques for modeling, analyzing, and forecasting time-dependent data across various domains.
- **Machine Learning Applications:** Implementing and understanding machine learning algorithms for diverse datasets.

It contains code examples, learning modules, and practical implementations inspired by academic texts, research, and real-world data across various fields. The aim is to build a robust collection of tools and insights for general data science and analytical studies.

## Contents & Structure

- `data/`: Contains raw and processed datasets used across various analyses and learning modules.
  - `data/raw/jj_data.json`: An example dataset for Johnson & Johnson quarterly earnings, often used in time series analysis studies.
- `src/`: Contains standalone Python scripts for common functions, utilities, and specific analysis tasks.
- `notebooks/`: Houses Jupyter Notebooks that walk through different topics, concepts, and case studies.
  - `notebooks/shumway_stoffer_fig1.1_p3.ipynb`: An initial example notebook demonstrating time series data loading, processing, and visualization for J&J quarterly earnings.
- `models/`: (Optional) Directory for saved machine learning models or model-related code.
- `docs/`: (Optional) For project documentation, reports, or research notes.
- `tests/`: Contains unit and integration tests to ensure code correctness and reliability.
- `.vscode/`: VS Code specific settings for consistent development environment setup.
- `mypy.ini`: MyPy configuration for strict static type checking.

## Getting Started

1.  Clone this repository:
    `git clone https://github.com/your-username/py-time-series.git`
2.  Navigate to the project directory:
    `cd py-time-series`
3.  Ensure your Python virtual environment is active (e.g., `source venvs/py-time-series/bin/activate`).
4.  Install required dependencies (e.g., `pip install -r requirements.txt` - _you might need to create this file based on your project's dependencies_).
5.  Explore the notebooks in the `notebooks/` directory or run scripts from `src/`.

## Resources

- **"Time Series Analysis and Its Applications: With R Examples"** by Robert H. Shumway and David S. Stoffer.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

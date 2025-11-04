# MLPerf Inference Dashboard

A comprehensive performance analysis dashboard for MLPerf Inference benchmark results. 

##  Features

### Multi-Version Support
- Compare MLPerf v5.0, v5.1 submissions


### Benchmark Comparisons
- Interactive bar charts for performance comparison across systems
- Support for multiple models: DeepSeek-R1, Llama 3.1 8B, Llama 2 70B, and more
- Filter by organizations, accelerators, scenarios (Offline/Server)

### Normalized Result Analysis
- Per-GPU and per-8-GPU-node normalization options
- Performance benefit calculation vs. global baseline
- Baseline system information displayed for each chart
- Handles systems with varying accelerator counts

### Dataset Representation
- Lightweight CSV-based dataset summaries
- Token length distribution histograms with statistics
- Visual representation of input/output token patterns
- Median and max value annotations

### Offline vs Server Comparison
- Performance degradation analysis between scenarios
- Side-by-side metric comparison
- Detailed per-system breakdown

### Cross-Version Analysis
- Track system performance evolution across MLPerf versions
- Automatic identification of multi-version systems

##  Directory Structure

```
mlperf-dashboard/
├── app.py                          # Main application entry point
├── mlperf_datacenter.py            # MLPerf dashboard module
├── dashboard_styles.py             # CSS styling
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project metadata
├── Makefile                        # Development commands
├── mlperf-data/                    # MLPerf data files
│   ├── mlperf-5.1.csv              # MLPerf v5.1 submission data
│   ├── mlperf-5.0.csv              # MLPerf v5.0 submission data
│   ├── summaries/                  # Dataset summaries (version controlled)
│   │   ├── README.md
│   │   ├── deepseek-r1.csv
│   │   ├── llama3-1-8b-datacenter.csv
│   │   └── llama2-70b-99.csv
│   └── original/                   # Original datasets (NOT version controlled)
│       ├── README.md
│       └── generate_dataset_summaries.py
└── tests/                          # Test suite
    ├── conftest.py
    ├── test_mlperf_datacenter.py
    └── README.md
```

##  Quick Start

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Harshith-umesh/mlperf-dashboard.git
   cd mlperf-dashboard
   ```

2. **Set up Python environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the dashboard**:
   ```bash
   streamlit run app.py
   ```

4. **Access**: Open http://localhost:8501 in your browser

### Development Environment Setup

For a complete development environment with linting, formatting, and code quality tools:

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

**Available development commands:**

- `make format` - Auto-format code (Black, Ruff)
- `make lint` - Run linting checks
- `make type-check` - Run static type checking
- `make test` - Run tests with coverage
- `make ci-local` - Run all CI checks locally
- `make clean` - Clean temporary files

##  MLPerf Data Management

### MLPerf CSV Files

The dashboard includes MLPerf submission data:

- `mlperf-data/mlperf-5.1.csv` - v5.1 submissions
- `mlperf-data/mlperf-5.0.csv` - v5.0 submissions

These files are version controlled.

### Dataset Summaries

Lightweight CSV summaries (40-180 KB vs 1-20 MB originals):

- `mlperf-data/summaries/deepseek-r1.csv`
- `mlperf-data/summaries/llama3-1-8b-datacenter.csv`
- `mlperf-data/summaries/llama2-70b-99.csv`

### Managing Original Datasets

Original datasets are stored in `mlperf-data/original/` (NOT version controlled).

**To download datasets:**

Visit [MLCommons Inference Benchmark Data Download](https://inference.mlcommons-storage.org/index.html)

Example:
```bash
cd mlperf-data/original/
bash <(curl -s https://raw.githubusercontent.com/mlcommons/r2-downloader/refs/heads/main/mlc-r2-downloader.sh) -d ./ https://inference.mlcommons-storage.org/metadata/deepseek-r1-datasets-fp8-eval.uri
```

**To generate summaries:**

```bash
cd /path/to/mlperf-dashboard
python mlperf-data/original/generate_dataset_summaries.py
```

See `mlperf-data/original/README.md` for detailed instructions.

##  Testing

Run all tests:

```bash
pytest tests/
```

Run with coverage:

```bash
pytest tests/ --cov=. --cov-report=html
```

Quick test:

```bash
make test
```

##  Configuration

### Environment Variables

- `STREAMLIT_SERVER_HEADLESS=true` - Headless mode for production
- `STREAMLIT_SERVER_PORT=8501` - Server port
- `STREAMLIT_SERVER_ADDRESS=0.0.0.0` - Listen address

### Data Requirements

- CSV files must include columns for model, scenario, organization, accelerator, and metrics
- Dataset summaries require `input_length` and `output_length` columns

##  Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Set up development environment: `pip install -e ".[dev]"`
4. Install pre-commit hooks: `pre-commit install`
5. Make changes and test: `pytest tests/`
6. Run code quality checks: `make ci-local`
7. Submit a pull request

##  Key Metrics Analyzed

- **Performance**: Samples/s, Tokens/s, Queries/s
- **Normalization**: Per-GPU, Per-8-GPU-Node
- **Scenarios**: Offline (batch), Server (online)
- **Systems**: Multi-vendor, multi-accelerator comparison
- **Dataset Statistics**: Token length distributions

##  License

Apache-2.0 License

## 🔗 Resources

- [MLCommons Inference](https://mlcommons.org/benchmarks/inference/)
- [MLPerf Inference Results](https://mlcommons.org/benchmarks/inference-datacenter/)
- [Dataset Downloads](https://inference.mlcommons-storage.org/index.html)

---

**Note**: This dashboard displays MLPerf Inference benchmark results for analysis and comparison purposes.


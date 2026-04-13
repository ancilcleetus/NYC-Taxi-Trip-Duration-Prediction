# NYC Taxi Trip Duration Prediction: Step-by-Step Development Log

## Day 0 — Set Up Claude Code, Create Project Structure and Install libraries & dependencies

### Step 0: Install Node, Python 3.12

#### Download and install nvm:
* `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash`

#### in lieu of restarting the shell
* `\. "$HOME/.nvm/nvm.sh"`

#### Download and install Node.js:
* `nvm install 24`

#### Verify npm version:
* `npm -v`  # Should print "11.9.0"

#### Verify npx version:
* `npx -v`  # Should print "11.9.0"

#### Verify nvm version:
* `nvm -v`  # Should print "0.40.4"

#### Verify the Node.js version:
* `node -v`  # Should print "v24.14.0"

#### Verify the git version:
* `git --version`  # Should print "git version 2.25.1"

### Step 1: Install Claude Code
* `npm install -g @anthropic-ai/claude-code`
* `claude --version`

### Step 2: Get your Anthropic API key
1. Go to console.anthropic.com
2. Sign up or log in
3. Click API Keys in the left sidebar
4. Click Create Key
5. Copy the key

* `export ANTHROPIC_API_KEY="sk-ant-your-key-here"`
* Add `export ANTHROPIC_API_KEY="sk-ant-your-key-here"` to ~/.bashrc

### Step 3: Create Project parent directory (create empty repo in GitHub & clone locally), Create & activate virtual environment
* `cd ~/Work/GitHub/NYC-Taxi-Trip-Duration-Prediction
* `python3.12 -m venv .venv`
* `source .venv/bin/activate`
* `claude --bare`  # Start Claude Code with existing API key

### Step 4: Pick your dataset
* Checkout [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
* Download [Yellow Taxi Trip Records (PARQUET) Feb 2026](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-02.parquet)

### Step 5: Tell Claude Code to scaffold your project

#### Prompt:
```
Create the folder structure for a production ML project. I need:
- src/data/ for data loading and validation scripts
- src/features/ for feature engineering
- src/models/ for model training and prediction
- app/ for the FastAPI API and Streamlit dashboard
- tests/ for unit tests
- notebooks/ for EDA
- data/ folder (add to .gitignore)
- models/ folder (add to .gitignore)
- a requirements.txt with: pandas, scikit-learn, xgboost, lightgbm,
  fastapi, uvicorn, streamlit, mlflow, great-expectations, pytest, plotly
- a .gitignore that excludes data/, models/, .env, __pycache__,
  .ipynb_checkpoints
- a setup.py that makes src/ importable as a package
- empty __init__.py files in every Python package
```

#### Results:

##### 📁 Project Structure
```
NYC-Taxi-Trip-Duration-Prediction/
├── src/                        ← installable package root (via setup.py)
│   ├── __init__.py
│   ├── data/                   ← data loading & validation
│   │   └── __init__.py
│   ├── features/               ← feature engineering
│   │   └── __init__.py
│   ├── models/                 ← training & prediction
│   │   └── __init__.py
├── app/                        ← FastAPI + Streamlit
│   └── __init__.py
├── tests/                      ← pytest unit tests
│   └── __init__.py
├── notebooks/                  ← EDA notebooks
│   └── .gitkeep
├── data/                       ← raw/processed data (git-ignored)
│   └── .gitkeep
├── models/                     ← saved model artefacts (git-ignored)
│   └── .gitkeep
├── requirements.txt
├── setup.py
└── .gitignore
```

##### Key decisions
                                                                                                                                              
| Decision | Reason |
|:---------|:-------|
| src/ layout + setup.py | find_packages(where="src") makes all sub-packages importable after pip install -e ., preventing import path hacks |
| data/ & models/ git-ignored | Large binaries / raw files don't belong in version control |
| .gitkeep in ignored folders | Keeps the empty directories tracked so collaborators get the same structure on clone |
| mlruns/ & mlartifacts/ in .gitignore | MLflow writes here by default — always local, never committed |
| extras_require: dev in setup.py | Keeps pytest out of the production install (`pip install -e ".[dev]"` for dev) |

#### Install your dependencies

| Command                         | Installs deps? | Makes src/ importable? | Installs pytest? |
|---------------------------------|----------------|------------------------|------------------|
| pip install -r requirements.txt | ✅ Yes         | ❌ No                  | ✅ Yes           |
| pip install -e .                | ✅ Yes         | ✅ Yes                 | ❌ No            |
| pip install -e ".[dev]"         | ✅ Yes         | ✅ Yes                 | ✅ Yes           |

* `pip install -e ".[dev]"`

# AI AWS Architect ☁️

> Generate AWS architecture diagrams from plain-English application
> requirements using AI, Python, Streamlit, Pydantic, and Graphviz.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Tests](https://img.shields.io/badge/Tests-pytest-brightgreen.svg)](https://pytest.org/)

## Overview

AI AWS Architect is a learning and portfolio project that turns an
application idea into a structured AWS architecture and a visual
diagram. Describe your business requirement in plain English. The
application asks an AI model to propose an architecture, validates it
against the project's supported AWS service catalog, and renders a PNG
diagram using Graphviz and AWS service icons.

This project is for learning, prototyping, and architecture exploration.
Review generated architectures before using them in production.

## Features

-   Natural-language requirements instead of manually choosing every AWS
    service.
-   AI-generated architecture components and connections.
-   Validation against the supported AWS service catalog.
-   PNG architecture diagrams with AWS icons and connection labels.
-   Modular Python code and automated tests.
-   No AWS resources are created just by generating a diagram.

## How it works

1.  Enter an application requirement in Streamlit.
2.  The AI proposes AWS components and connections.
3.  Pydantic parses the response into structured models.
4.  The architecture validator checks the result.
5.  Graphviz renders the diagram.
6.  Streamlit displays the architecture and diagram.

## Project structure

``` text
aws-architect-ai/
├── app/
│   ├── config/settings.py
│   ├── knowledge/
│   │   ├── aws_services.py
│   │   └── aws_service_catalog.py
│   ├── models/architecture.py
│   ├── prompts/architecture_prompt.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── architecture_loader.py
│   │   ├── architecture_service.py
│   │   ├── architecture_validator.py
│   │   ├── cost_service.py
│   │   ├── diagram_service.py
│   │   └── icon_service.py
│   └── ui/streamlit_app.py
├── assets/aws-icons/
├── tests/
│   ├── fixtures/sample_architecture.json
│   └── test_*.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

The tree is illustrative. Keep it aligned with the files actually
present in your repository.

## Prerequisites

-   Git
-   Python version supported by `requirements.txt` (Python 3.10+ is a
    reasonable starting point)
-   Graphviz system application
-   An OpenAI API key for AI generation (API usage may incur charges)

### Install Graphviz

-   **Windows:** install from
    [graphviz.org/download](https://graphviz.org/download/), then reopen
    your terminal.
-   **macOS:** `brew install graphviz`
-   **Ubuntu/Debian:**
    `sudo apt-get update && sudo apt-get install graphviz`

Verify it is available:

``` bash
dot -V
```

## Quick start

### 1. Clone the repository

Replace `YOUR-GITHUB-USERNAME` with the GitHub account that owns this
repository.

``` bash
git clone https://github.com/YOUR-GITHUB-USERNAME/aws-architect-ai.git
cd aws-architect-ai
```

### 2. Create a virtual environment

**Windows PowerShell:**

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell activation is blocked, use Command Prompt:

``` bat
.venv\Scripts\activate.bat
```

**macOS/Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure your API key

Create a local `.env` file in the repository root. If `.env.example`
exists, copy it:

**Windows PowerShell:**

``` powershell
Copy-Item .env.example .env
```

**macOS/Linux:**

``` bash
cp .env.example .env
```

Add your own key to `.env`:

``` dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

Use the exact variable name read by `app/config/settings.py`. Ensure the
settings module loads `.env` if the project expects it.

**Never commit `.env` or expose your API key.** Each student should use
their own API key. OpenAI API usage is billed separately from a ChatGPT
subscription.

### 5. Check the AWS icons

The renderer expects icon files referenced by the service catalog.
Ensure required files are included in `assets/aws-icons/`. If they are
missing, download the corresponding official AWS Architecture Icons from
[AWS Architecture Center](https://aws.amazon.com/architecture/icons/)
and preserve the filenames expected by the application. Review AWS's
applicable icon usage terms.

### 6. Run the tests

From the repository root:

``` bash
python -m pytest -q
```

### 7. Start the app

``` bash
python -m streamlit run app/ui/streamlit_app.py
```

Open the local URL Streamlit prints, usually `http://localhost:8501`.

### 8. Generate an architecture

Try this requirement:

> Build a task management application where users can create tasks,
> update their status, store task information, and receive notifications
> when tasks are completed. Include secure access, monitoring, and a
> scalable backend.

Click **Generate Architecture** to see the proposed architecture and
diagram.

## Supported AWS services

The supported services and aliases are defined in
`app/knowledge/aws_service_catalog.py`. The catalog does not necessarily
include every AWS service.

To add a service: 1. Add its official name and useful aliases to the
catalog. 2. Add the required icon filename and asset if the current
implementation needs one. 3. Add or update tests for catalog lookup,
validation, and icon resolution. 4. Run `python -m pytest -q`.

If the AI returns an unknown service, check the catalog and the
service-name normalization logic.

## Troubleshooting

**`OPENAI_API_KEY is not configured`** - Check that `.env` exists at the
repository root. - Check the variable name against
`app/config/settings.py`. - Confirm `.env` is loaded by the settings
module. - Restart the app after changing configuration.

**Graphviz or `dot` not found** - Install Graphviz as a system
application. - Verify `dot -V` works and Graphviz is on your `PATH`.

**Unknown AWS service** - Check `app/knowledge/aws_service_catalog.py`
and the validator/icon resolution logic.

**AWS icon not found** - Confirm the icon exists in `assets/aws-icons/`
and the filename matches the catalog.

**Python import errors** Run commands from the repository root and use
`python -m`:

``` bash
python -m streamlit run app/ui/streamlit_app.py
python -m pytest -q
```

**API errors** Check that your API key is active, API access is enabled,
and usage/billing limits are configured. Avoid repeatedly retrying
requests that fail.

## Deploy with Streamlit Community Cloud

1.  Push the repository to GitHub.

2.  Confirm `requirements.txt` contains all required packages and icon
    assets are available.

3.  Go to [Streamlit Community Cloud](https://share.streamlit.io/) and
    sign in with GitHub.

4.  Select **Create app**, then choose your repository, branch (usually
    `main`), and entrypoint `app/ui/streamlit_app.py`.

5.  Open **Advanced settings** and configure the required secret, for
    example:

    ``` toml
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

6.  Choose a supported Python version and deploy.

7.  Test the deployed URL and review the app logs if startup fails.

**Deployment configuration warning:** Streamlit Community Cloud secrets
are commonly read through `st.secrets`, while this project's settings
module currently reads `OPENAI_API_KEY` from its configured environment.
Verify that `app/config/settings.py` supports the deployment secret
source before deploying. If necessary, update settings to read Streamlit
secrets as well as local environment variables, without hardcoding
credentials, and test the change locally.

A public app using your API key can create costs. Set usage limits,
monitor usage, and consider access controls before sharing it widely.

## Push your local project to GitHub

### 1. Check Git status and `.gitignore`

``` bash
git status
```

A typical `.gitignore` includes:

``` gitignore
# Secrets
.env
.env.*
!.env.example
.streamlit/secrets.toml

# Virtual environments
venv/
.venv/

# Python
__pycache__/
*.py[cod]
.pytest_cache/

# Editors and OS
.vscode/
.idea/
.DS_Store
Thumbs.db

# Generated output (adjust if you intentionally publish sample output)
output/
```

Do not exclude files required by the app, such as icons and test
fixtures. Make sure `.env` and any secret files are not staged.

### 2. Initialize Git if needed

``` bash
git init
git branch -M main
```

Skip `git init` if the project is already a Git repository.

### 3. Stage, inspect, and commit

``` bash
git add .
git status
git commit -m "Initial commit: AI AWS Architect"
```

Review the staged file list before committing. If a secret is staged,
unstage it and fix `.gitignore` before proceeding.

### 4. Create the GitHub repository

On GitHub, create a repository named `aws-architect-ai`. For an existing
local project, do not initialize the new remote repository with another
README, license, or `.gitignore`; add those locally instead.

### 5. Add the remote and push

``` bash
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/aws-architect-ai.git
git push -u origin main
```

Replace the URL with your own. If `origin` already exists, inspect it
with `git remote -v` instead of adding it again.

### 6. Verify on GitHub

Confirm the README renders, `app/`, `assets/`, and `tests/` are present,
and `requirements.txt` is included. Confirm `.env` and virtual
environments are absent. Test cloning the repository into a separate
folder if possible.

For future changes:

``` bash
git add .
git commit -m "Describe your change"
git push
```

## Make the repository look professional

-   Add a screenshot of the app and a sample generated diagram.
-   Add a `LICENSE` file after choosing a license.
-   Add a `CONTRIBUTING.md` if you want students to contribute.
-   Keep the service catalog and README updated.
-   Add GitHub Actions tests when ready.
-   Add the live demo URL and a short demo GIF after deployment.
-   Use GitHub Issues to track bugs and future improvements.

## Cost, security, and limitations

-   Generating a diagram does not deploy AWS infrastructure.
-   AI generation can incur API charges.
-   Never publish API keys or commit `.env`.
-   Generated architectures are drafts and may contain unsupported or
    incorrect service choices.
-   Review security, availability, data handling, cost, and service
    limits before production use.
-   Review licensing and usage terms for third-party icons/assets.

## Contributing

For changes, add or update tests and run:

``` bash
python -m pytest -q
```

## License

Choose a license before presenting the project as open source. If you
choose MIT, add a `LICENSE` file containing the complete MIT license
text and your copyright notice.

------------------------------------------------------------------------

Built for learners exploring AWS architecture, AI, Python, and
Streamlit.

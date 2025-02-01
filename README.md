# AI Agent Template

## Getting Started

### Prerequisites

Ensure you have **Git** installed on your local machine. If not, look up or ask ChatGPT how to install Git for your operating system.

### Clone the Repository

Run the following command in your terminal:

```sh
git clone https://github.com/RPD123-byte/ai_agent_template.git
```

### Open in an IDE

- Open **VSCode** or your preferred IDE.
- Open the folder that was cloned onto your computer.
- Open a terminal inside your IDE.

### Set Up a Virtual Environment

Create a virtual environment to isolate your packages:

```sh
python -m venv agent_env
```

Activate the virtual environment:

```sh
source agent_env/bin/activate  # For macOS/Linux
```

For Windows, use:

```sh
agent_env\Scripts\activate
```

### Install Dependencies

Run the following command to install all required packages:

```sh
pip install -r requirements.txt
```

Wait for the installation to complete.

### Configure API Keys

1. Navigate to the `config/` folder.
2. Rename the `config_sample.yml` file to `config.yml`.
3. Add your API keys inside `config.yml`:
   - **OpenAI API Key** (required) – You must generate an API key from the OpenAI website.
   - **Langsmith API Key** (optional but recommended) – This allows you to track the agent's operations in a UI.

### Run the Agent

Start the agent by running:

```sh
python -m app.app
```

You should see the agent start executing in the terminal.

---

## Tech Stack

The agent is built using:

- **LangGraph**: Defines the agent's execution flow using a graph-based architecture.
- **LangChain**: Provides LLM abstraction and framework.
- **LangSmith**: Logs and visualizes agent behavior.

---

## Codebase Overview

### 1. **Graph Folder**

Contains the entire workflow logic of the agent.

- The agent operates as a directed graph where nodes represent execution units (functions).
- Edges define transitions between nodes.
- Example of a simple edge:

  ```python
  graph.add_edge("industry_creator", "background_identifier")
  ```
  This means that after `industry_creator` runs, `background_identifier` will execute next.

- Conditional transitions:

  ```python
  graph.add_conditional_edges(
      "background_identifier",
      lambda state: "industry_creator" if not json.loads(state["checker_response"][-1].content)["data"] else "questions_generator"
  )
  ```
  This ensures that if `checker_response` contains data, execution moves to `questions_generator`, otherwise it loops back to `industry_creator`.

### 2. **Agents Folder**

- Houses the logic for the **nodes** in the execution graph.
- Each file corresponds to a node's execution function.

### 3. **App Folder**

- The **entry point** for running the agent.
- When you execute `python -m app.app`, it initializes and executes the graph workflow.

### 4. **Config Folder**

- Stores API keys and environment variables in `config.yml`.
- Keeping sensitive credentials here instead of hardcoding them in the source code prevents security risks.

### 5. **Models Folder**

- Contains model abstraction files.
- Example: `openai_models.py` defines functions to interact with OpenAI models.

  ```python
  def get_open_ai_json(temperature=0, model='gpt-3.5-turbo-1106'):
      client = Client()
      llm = ChatOpenAI(
          model=model,
          temperature=temperature,
          model_kwargs={"response_format": {"type": "json_object"}},
      )
      return llm
  ```
  This function initializes an OpenAI model with JSON output formatting.

### 6. **Prompts Folder**

- Stores system prompts used for node executions.
- Defines instructions given to LLMs to ensure optimal outputs.

### 7. **States Folder**

- Defines persistent variables accessible across different nodes.
- LangGraph allows nodes to read/write to this state, enabling inter-node communication.

### 8. **Tools Folder**

- Contains non-AI functions used across various nodes.
- Example: Helper functions for API calls, text processing, etc.

### 9. **Utils Folder**

- Houses miscellaneous utility functions used across multiple files.

---

## Experiment & Customize

- Modify nodes in the `agents/` folder to change execution behavior.
- Adjust state variables in `states/` to track new parameters.
- Create new prompt templates in `prompts/` to refine outputs.
- Track agent behavior using **LangSmith UI** if you’ve set up an API key.

---

## Need Help?

- If you encounter issues, ask ChatGPT for debugging help.
- Try modifying the agent and testing different configurations.
- Explore `LangGraph`, `LangChain`, and `LangSmith` documentation for advanced customization.

Enjoy building your AI agent! 🚀


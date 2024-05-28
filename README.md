# YouTubTron

YouTubTron is a Python application designed to fetch relevant YouTube videos using the CrewAI library and a local instance of the LLM (Large Language Model).

## Description

YouTubTron leverages the power of CrewAI and the local LLM to search for and recommend YouTube videos related to Python tutorials. It provides a seamless and efficient way to discover educational content on YouTube, making it an invaluable tool for Python learners and enthusiasts.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/IPcaser/YouTubTron.git
    ```

2. Navigate to the project directory:

    ```sh
    cd YouTubTron
    ```

3. Install the required dependencies:

    ```sh
    pip install crewai
    pip install langchain-openai
    ```

4. Set up the environment variable for the OPENAI_API_KEY:

    ```sh
    export OPENAI_API_KEY="NA"
    ```

## Usage

1. Run the Python script `Myagent.py`:

    ```sh
    python Myagent.py
    ```

2. The script will search for YouTube videos of Python tutorials and provide the links to the relevant videos.

## Features

- **Python Tutorial Videos:** Search for and fetch YouTube videos related to Python tutorials.
- **AI-driven Recommendations:** Utilize the power of CrewAI and the local LLM to recommend high-quality educational content.
- **User-friendly Interface:** Simple and intuitive interface for easy usage.

## Files Included

- `Myagent.py`: Python script for fetching relevant YouTube videos of Python tutorials.
- `README.md`: This README file providing instructions and information about the project.

## Contributing

Contributions to improve the functionality or add new features are welcome. Feel free to open a pull request with your changes.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

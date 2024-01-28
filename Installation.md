
# DarkPatternLLM Installation and Usage Guide

DarkPatternLLM is a project aimed at detecting and combating dark patterns on websites using advanced Language Models (LLMs). This guide provides step-by-step instructions on how to install and run the project.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

To install DarkPatternLLM, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Venkateeshh/DarkPatternLLM.git
   ```

2. Navigate to the project directory:
   ```bash
   cd DarkPatternLLM
   ```

3. Change directory to the "api" folder:
   ```bash
   cd api
   ```

4. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After completing the installation, follow these steps to run DarkPatternLLM:

1. Ensure you are still in the "api" folder:
   ```bash
   cd api
   ```

2. Run the Python script:
   ```bash
   python app.py
   ```

3. Open Google Chrome and go to [chrome://extensions/](chrome://extensions/).

4. Enable "Developer mode" at the top-right corner.

5. Click on "Load unpacked" and select the "app" folder in your DarkPatternLLM project directory.

6. The DarkPatternLLM extension icon should appear in your browser toolbar. Click on it to activate the extension.

7. Visit any website, and the extension will automatically analyze the page for dark patterns. If a dark pattern is detected, you will receive a notification, and the relevant elements will be highlighted on the page.

## Contributing

We welcome contributions! If you want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.


# ShellAI

ShellAI is a Unix shell assistant that combines a C++ shell with a Python-based language model to help users interact with the terminal using natural-language commands.

## Project Structure

```text
ShellAI/
├── main.cpp
├── assistant.py
├── merged_model_folder/
└── README.md
```

## Model Setup

The model is not included in this repository because of its size.

Before running ShellAI, download the required `merged_model_folder` from Hugging Face and place it in the **root directory of this project**.

After downloading, your project should look like:

```text
ShellAI/
├── main.cpp
├── assistant.py
├── merged_model_folder/
│   ├── config.json
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   └── ...
└── README.md
```

Make sure the folder is named exactly:

```text
merged_model_folder
```

## Requirements

* Linux/macOS
* C++ compiler with C++17 support
* Python 3
* Python packages required by `assistant.py`
* Hugging Face model files in `merged_model_folder`

Install the Python dependencies:

```bash
pip install transformers torch
```

## Build

From the project root:

```bash
g++ -std=c++17 main.cpp -o shellai
```

## Run

```bash
./shellai
```

You can then interact with the shell normally and use ShellAI's natural-language functionality.

Example:

```text
$ shellai what does ls do
```

## Model Path

`assistant.py` expects the model at:

```text
./merged_model_folder
```

Therefore, keep `merged_model_folder` in the project root.


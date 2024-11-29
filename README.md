:construction: alpha development :construction:

[:brazil: Versão Português Brasileiro](./README-pt.md)

# Asrbench-Cli

## Index

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Introduction
ASRBench CLI is a complementary tool to the [ASRBench](https://github.com/ASRBench/asrbench) framework, designed 
to simplify the execution of audio transcription system benchmarks directly from the command line.

With it, you can:

- Use the most popular transcription systems on the market.
- Add new customized transcription systems.
- Run benchmarks simply, using just one configuration file.

## Installation
To install ASRBench, all you need is [Python 3.12+](https://www.python.org/downloads/) and pip. Use the
command below to install the latest version:

```sh
pip install asrbench-cli
```

> [!NOTE]
> The list of project dependencies is available in the file [CONTRIBUTING.md]()

## Usage
The CLI requires a configuration file to work, in the same format as the framework. 
benchmark environment, defining datasets, transcribers and output parameters in a simple and declarative way. 
declarative. For more details on the structure of the configuration file, go to
[documentation]().

Below is an example of the configuration file structure:

```yaml
# data output configuration
output:
  type: "csv"
  dir: "./results"
  filename: "example_filename"

# datasets configuration
datasets:
  dataset1:
    audio_dir: "resources/common_voice_05/wav"
    reference_dir: "resources/common_voice_05/txt"

# transcription system configuration
transcribers:
  faster_whisper_medium_int8:
    asr: "faster_whisper"
    model: "medium"
    compute_type: "int8"
    device: "cpu"
    beam_size: 5
    language: "en"  
```

With the configuration file in hand, just run the command:

```sh
asrbench-cli run path/to/configfile.yml
```
The CLI will read the configuration file, set up the benchmark and run it automatically. All progress and steps 
will be displayed directly in the terminal, including the percentage of completion and a time estimate for the 
completion of each stage of the transcription process.

For a complete list of available commands and instructions for more advanced uses, see [documentation]().

## Contribution
If you want to contribute to ASRBench, see [CONTRIBUTING.md]() for information on: 

- Configuration of the development environment.
- Project structure and dependencies.
- Best practices.

## License
Distributed under the MIT license. See the [LICENSE](./LICENSE) file for more details.

[:arrow_up: Go to top](#index)
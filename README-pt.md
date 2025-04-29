:construction: desenvolvimento em fase alpha :construction:

[:us: American English Version](./README.md)

# Asrbench-Cli

## Índice

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução
O ASRBench CLI é uma ferramenta complementar ao framework [ASRBench](https://github.com/ASRBench/asrbench), projetada 
para simplificar a execução de benchmarks de sistemas de transcrição de áudio diretamente pela linha de comando.

Com ele, você pode:

- Utilizar os sistemas de transcrição mais populares do mercado.
- Adicionar novos sistemas de transcrição personalizados.
- Executar benchmarks de forma simples, usando apenas um arquivo de configuração.

## Instalação
Para instalar o ASRBench, você só precisa do [Python 3.12+](https://www.python.org/downloads/) e do pip. Use o
comando abaixo para instalar a versão mais recente:

```sh
pip install asrbench-cli
```

> [!NOTE]
> A lista de dependências do projeto está disponível no arquivo [CONTRIBUTING.md]()

## Uso
A CLI requer um arquivo de configuração para funcionar, no mesmo formato utilizado pelo framework, nele o usuario faz a 
configuração do ambiente de benchmark, definindo os datasets, transcritores e parâmetros de saída de forma simples e 
declarativa. Para mais detalhes sobre a estrutura do arquivo de configuração, acesse a
[documentação]().

Abaixo está um exemplo de estrutura do arquivo de configuração:

```yaml
# configuração da saída de dados
output:
  type: "csv"
  dir: "./results"
  filename: "example_filename"

# configuração dos datasets
datasets:
  dataset1:
    audio_dir: "resources/common_voice_05/wav"
    reference_dir: "resources/common_voice_05/txt"

# configuração dos sistema de transcrição
transcribers:
  faster_whisper_medium_int8:
    asr: "faster_whisper"
    model: "medium"
    compute_type: "int8"
    device: "cpu"
    beam_size: 5
    language: "pt"  
```

Com o arquivo de configuração em mãos, basta executar o comando:

```sh
asrbench-cli run path/to/configfile.yml
```
A CLI lerá o arquivo de configuração, montará o benchmark e o executará automaticamente. Todo o progresso e as etapas 
serão exibidos diretamente no terminal, incluindo a porcentagem de conclusão e uma estimativa de tempo para a 
finalização de cada etapa do processo de transcrição.

> [!TIP]
> Para uma lista completa de comandos disponíveis e instruções para usos mais avançados, consulte a [documentação]().

## Contribuição
Se você deseja contribuir para o ASRBench, consulte [CONTRIBUTING.md]() para informações sobre: 

- Configuração do ambiente de desenvolvimento.
- Estrutura e dependências do projeto.
- Práticas recomendadas.

## Licença
Distribuído sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.

[:arrow_up: Ir para o topo](#índice)

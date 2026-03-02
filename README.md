# jornada-python-hashtag

Este repositório contém um projeto Python inicializado com uma estrutura mínima.

## Estrutura

- `src/` - código fonte do pacote
- `tests/` - testes
- `pyproject.toml` - configuração do pacote
- `requirements.txt` - dependências

## Como iniciar

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
2. Ative-o:
   ```bash
   # Windows
   venv\\Scripts\\activate
   ```
3. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o aplicativo:
   ```bash
   python -m src.main
   ```

**Observação:** o script tenta usar `pyautogui`. Se não estiver instalado, ele apenas imprimirá uma mensagem.

## Executando testes

Com `pytest` instalado (listado em `requirements.txt`), execute:
```bash
pytest
```

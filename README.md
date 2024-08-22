# Rastreador de Preços do Bitcoin

Este projeto é um programa Python que rastreia o preço do Bitcoin e envia uma notificação por e-mail quando o preço cai abaixo de um valor especificado pelo usuário.

## Funcionalidades

- **Rastreamento de Preço**: Monitora o preço do Bitcoin em BRL usando a API CoinGecko.
- **Notificações por E-mail**: Envia um e-mail de alerta quando o preço do Bitcoin cai abaixo de um valor mínimo definido pelo usuário.
- **Verificação Regular**: O programa verifica o preço do Bitcoin em intervalos regulares (10 minutos, por padrão).

## Pré-requisitos

Antes de executar o programa, certifique-se de ter os seguintes pacotes Python instalados:

- `requests`
- `smtplib`
- `schedule`
- `email` (parte da biblioteca padrão do Python)

Você pode instalá-los usando o `pip`:

```bash
pip install requests schedule


Como Usar
Clonar o repositório:

git clone https://github.com/seu_usuario/rastreador-bitcoin.git
cd rastreador-bitcoin

Como Usar
Clonar o repositório:

from_email = 'seu_email@gmail.com'  # Seu e-mail aqui
from_password = 'sua_senha'         # Sua senha aqui

Nota: Se você estiver usando o Gmail, pode ser necessário gerar uma Senha de App e usá-la no lugar da senha principal.

Executar o Programa:

Execute o programa no terminal:
python rastreador_bitcoin.py

O programa pedirá para você inserir o valor mínimo para o Bitcoin e o e-mail para notificações.

Receber Notificações:

O programa monitorará o preço do Bitcoin em intervalos regulares. Se o preço cair abaixo do valor que você especificou, você receberá um e-mail de alerta.

Configurações
Intervalo de Verificação: O intervalo de verificação padrão é de 10 minutos. Você pode alterar isso na linha:
schedule.every(10).minutes.do(monitor_price, target_price, user_email)


Aqui está um exemplo de um arquivo README.md para o projeto que você criou:

markdown
Copy code
# Rastreador de Preços do Bitcoin

Este projeto é um programa Python que rastreia o preço do Bitcoin e envia uma notificação por e-mail quando o preço cai abaixo de um valor especificado pelo usuário.

## Funcionalidades

- **Rastreamento de Preço**: Monitora o preço do Bitcoin em BRL usando a API CoinGecko.
- **Notificações por E-mail**: Envia um e-mail de alerta quando o preço do Bitcoin cai abaixo de um valor mínimo definido pelo usuário.
- **Verificação Regular**: O programa verifica o preço do Bitcoin em intervalos regulares (10 minutos, por padrão).

## Pré-requisitos

Antes de executar o programa, certifique-se de ter os seguintes pacotes Python instalados:

- `requests`
- `smtplib`
- `schedule`
- `email` (parte da biblioteca padrão do Python)

Você pode instalá-los usando o `pip`:

```bash
pip install requests schedule
Como Usar
Clonar o repositório:

bash
Copy code
git clone https://github.com/seu_usuario/rastreador-bitcoin.git
cd rastreador-bitcoin
Configurar o E-mail para Envio:

No arquivo rastreador_bitcoin.py, substitua os campos from_email e from_password pelas suas credenciais de e-mail.

python
Copy code
from_email = 'seu_email@gmail.com'  # Seu e-mail aqui
from_password = 'sua_senha'         # Sua senha aqui
Nota: Se você estiver usando o Gmail, pode ser necessário gerar uma Senha de App e usá-la no lugar da senha principal.

Executar o Programa:

Execute o programa no terminal:

bash
Copy code
python rastreador_bitcoin.py
O programa pedirá para você inserir o valor mínimo para o Bitcoin e o e-mail para notificações.

Receber Notificações:

O programa monitorará o preço do Bitcoin em intervalos regulares. Se o preço cair abaixo do valor que você especificou, você receberá um e-mail de alerta.

Configurações
Intervalo de Verificação: O intervalo de verificação padrão é de 10 minutos. Você pode alterar isso na linha:

python
Copy code
schedule.every(10).minutes.do(monitor_price, target_price, user_email)
Para outros intervalos, substitua 10.minutes por hours, seconds, etc., conforme necessário.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto é licenciado sob a MIT License.

Contato
Se você tiver alguma dúvida, sinta-se à vontade para entrar em contato:

Nome: Kleber
E-mail: kleber@example.com


### Explicação das Seções:

1. **Título e Descrição**: Apresenta o projeto e sua funcionalidade principal.
2. **Funcionalidades**: Descreve as principais funcionalidades do programa.
3. **Pré-requisitos**: Lista as bibliotecas necessárias para executar o programa e como instalá-las.
4. **Como Usar**: Passo a passo para clonar, configurar e executar o programa.
5. **Configurações**: Instruções para alterar o intervalo de verificação.
6. **Contribuições e Licença**: Informação sobre contribuição e licença do projeto.
7. **Contato**: Seus dados para contato, caso alguém queira tirar dúvidas ou colaborar.

Com esse `README.md`, qualquer pessoa interessada em usar ou contribuir para o seu projeto terá as informações necessárias para começar.

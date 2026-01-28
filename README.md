# 🚀 Banco Digital - Zentora Bank

> Breve descrição de uma linha sobre o que o projeto faz.

### 📋 Sobre o Projeto
Este projeto foi desenvolvido para simulação de um vanco digital. Ele permite que usuários gerenciem suas finanças de uma interface de linha de comando. O sistema foi construpido pensando na resiliência e no tratamento de exceções, facilitando o suporte técnico e a manutenção do código.

### 🚀 Funcionalidades
- **Abertura de Conta: Cadastro de Usuários com validação de dados.
- **Depósitos e Saques: Atualização de saldo em tempo real com travas de segurança.
- **Extrato Detalhado: Histórico de transações formato para o usuário.
- **Sistema de Limites: Controle de valor máximo por saque e quantidade de saques diários.
- **Logs de Erro: Sistema preparado para identificar falhas de entrada de dados.

### 🛠 Tecnologias Utilizadas
- **Linguagem:** Python
- **POO Avançado:** Herança,Abstração,Polimorfismo e Encapsulamento
- **CLI:** Interação via terminal com entrada de dados do usuário
- **Modelagem de Dados:** Representação de entidades reais(Cliente, Conta, Transação).

### 🧾 Estrutura do Código
├── main.py            # Ponto de entrada da aplicação
├── modelos/           # Classes de Conta, Cliente e Transação
├── utilitarios/       # Funções de validação e formatação
└── README.md          # Documentação do projeto

### ⚙️ Como Executar
1. Certifique-se de ter o Python instalado:
   ```bash
   python --version

2. Clone o repositório:
   ```bash
   git clone https://github.com/teu-usuario/python-digital-bank.git

3. Navegue até a pasta e execute:
   ```bash
   python main.py

### ✔ Lógica de Negócio Aplicada
Para garantir a estabilidade do sistema (visão de Suporte), foram aplicadas as seguintes regras:

1. **Validação de Saldo: O Sistema impede saques que excedam o saldo disponível + limite.
2. **Input Sanitization: Tratamento de erros caso o usuário digite letras em campos numéricos
3. **Atomicidade Simulada. As operações de saldo só são confirmadas se todos os requisitos da transação forem atendidos.
  

  Lixux ou macOS é necessário usar "python3"

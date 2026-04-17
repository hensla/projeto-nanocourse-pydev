🧮 Menu Interativo — Elogio & Fatorial
Programa em Python com menu interativo que oferece duas funcionalidades: receber um elogio ou calcular o fatorial de um número inteiro.

📋 Descrição
O programa exibe um menu em loop, aguardando que o usuário escolha uma das opções disponíveis. A execução continua até que o usuário opte por sair. O cálculo do fatorial é feito manualmente com laço for, sem uso de bibliotecas externas.

🚀 Como executar
Pré-requisito: Python 3.x instalado.
bashpython main.py
Exemplo de uso
1 - Receber um elogio
2 - Calcular o fatorial de um número
3 - Sair
Informe o número da opção desejada e depois tecle ENTER: 1

Você é uma pessoa muito esperta

1 - Receber um elogio
2 - Calcular o fatorial de um número
3 - Sair
Informe o número da opção desejada e depois tecle ENTER: 2
Informe um número do qual deseja o fatorial: 5

O fatorial para o valor informado foi 120.

1 - Receber um elogio
2 - Calcular o fatorial de um número
3 - Sair
Informe o número da opção desejada e depois tecle ENTER: 3

Saindo do sistema...

🧠 Como funciona
OpçãoAção1Exibe uma mensagem de elogio ao usuário2Solicita um número e calcula seu fatorial usando laço for3Encerra o programaoutroExibe aviso de opção inválida e repete o menu
O laço while mantém o menu ativo até que a opção 3 seja escolhida. O fatorial é calculado multiplicando o número por todos os valores de 1 até n-1.

📁 Estrutura do projeto
├── main.py      # Código principal
└── README.md    # Este arquivo

🛠️ Tecnologias

Python 3
Estruturas utilizadas: while, for, if/elif/else, input(), f-strings


📄 Licença MIT
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

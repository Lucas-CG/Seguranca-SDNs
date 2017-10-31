# EEL840 - Tópicos Especiais em Sistemas de Comunicação

## Alunos
- Lucas de Carvalho Gomes (DRE 113080060)
- Vinícius Silva Campos (DRE 113023327)

## Título

Ataques a SDNs: uma análise exploratória de ataques baseada em suas vulnerabilidades

## Descrição

Esse projeto busca explorar algumas das falhas de segurança existentes na arquitetura das Redes Definidas por Software expostas em [1] e [2], por meio da execução de ataques. Pretende-se implementar as arquiteturas de rede necessárias e os ataques usando-se as ferramentas oferecidas pelo virtualizador de redes Mininet[5].

## Tarefas:

### Configurar MiniNet (até 2/11)
Envolve realizar o *download* da máquina virtual oferecida pelo Mininet, que já oferece um ambiente Linux com todas as ferramentas do virtualizador instaladas e realizar quaisquer ajustes necessários.

### Executar o Exemplo do OpenFlow (até 6/11)
Essa etapa serve para o grupo aprender a programar os controladores e criar uma arquitetura básica de rede, conhecimentos necessários para implementar os ataques. Ao final, serão gerados códigos e comandos que podem ser reutilizados para facilitar o desenvolvimento dos ataques.

### Ausência de TLS (até 22/11):
Pretendemos implementar um ataque de *man-in-the-middle*. Para isso, interceptaremos os pacotes e descobriremos o IP do controlador, podendo portanto, utilizar IP _spoofing_ para enviar mensagens para os comutadores.

#### Tarefas Associadas
* Verificar se é possível desabilitar o TLS no OpenFlow (até 6/11)
* Implementar a arquitetura da rede (até 13/11)
* Desenvolver o script do ataque (até 20/11)
* Coletar resultados (até 22/11)

### Ataque de Vazamento de Informação (regras) (até 22/11):
Esse ataque é baseado na implementação descrita em [3] e [4]. Em controladores que utilizam *agregação* para criar regras , é possível que um usuário verifique os tempos de resposta de um serviço oferecido na rede a outro usuário e infira se uma regra foi implementada.

#### Tarefas Associadas
* Implementar a arquitetura da rede (até 13/11)
* Implementar o método para inferir se existe regra (até 18/11)
* Coletar resultados (até 21/11)
* Escolher um ataque que se aproveite da regra aprendida (até 22/11)

### Ataque de Negação de Serviço (até 22/11):
Esse ataque também é baseado em [3] e [4]. Objetiva-se executar um ataque de negação de serviços (DoS) em um dispositivo do plano de dados, considerando que o controlador não utiliza agregação.

#### Tarefas Associadas
* Implementar a arquitetura da rede (até 13/11)
* Desenvolver o script do ataque (até 20/11)
* Coletar resultados (até 22/11)

### Preparar Apresentação e Relatório (até 24/11)

## Infraestrutura Necessária

Prevemos que apenas será necessário usar **1 computador** para a execução dos experimentos. Toda a rede será controlada pelo Mininet, que permite simular uma rede com vários dispositivos 

## Bibliografia:

[1] Sandra Scott-Hayward, Gemma O’Callaghan, Sakir Sezer - SDN Security: A
Survey - 2013 IEEE SDN for Future Networks and Services (SDN4FNS)

[2] Diego Kreutz et al., Software-Defined Networking: A Comprehensive Survey -Proceedings of the IEEE - Janeiro de 2015

[3] R. Kloeti, V. Kotronis, P. Smith, OpenFlow: A Security Analysis, em: 2013 21st IEEE International Conference on Network Protocols (ICNP), Abril de 2013.

[4] R. Kloeti, OpenFlow: A Security Analysis, Tese de Mestrado, Swiss Federal Institute of Technology Zurich (ETH), 2013. Disponível em: ftp://ftp.tik.ee.ethz.ch/pub/students/2012-HS/MA-2012-20.pdf.

[5] Mininet (Ferramenta de Virtualização de Redes): http://mininet.org/

[6] Seungwon Shin; Guofei Gu; “Attacking Software-Defined Networks: A First Feasibility Study”. 

# Unidade 2 - Turtlebot

A solução proposta apresenta um Script Python que envia a aceleração linear e angular do TurtleBot para que este realize um movimento para se locomover até um ponto pré-definido em coordenadas pelo programador. Para tal implementação, foi utilizada a feature Windows Subsystem for Linux, o Sistema Operacional Ubuntu e seu Framework Robot Operating System versão Humble e seu simulador Gazebo e o Turtlebot Burguer simulado. O script conta com a biblioteca RCLpy que nos permite trabalhar com os recursos do ROS 2, como publicação e subscrição de tópicos e com a implementação de uma fila nutella (deque) que permite que sejam colocadas (append) novas coordenadas para o robô seguir. Com isso, publico no tópico '/cmd_vel', que é ouvido pelo nosso burguer TurtleBot simulado e executado pelo mesmo, concomitantemente estamos recebendo os valores do tópico '/odom', que aparece no terminal para fins de analise da trajetória do robô. Assim, implementei a coordenada x=10.0 e y=10.0 na fila e com os cálculos exercidos no código de distância entre pontos e ângulo (atual e meta) para alcançar o objetivo, o robô é capaz de se locomover e parar quando houver concluído. Após realizar as devidas instalações, deve-se executar a simulação no terminal Ubuntu utilizando do ROS2. (Utilize - ros2 launch turtlebot3_gazebo empty_world.launch.py), caso não tenha o robô em tela, no canto superior esquerdo em Insert selecione o Turtlebot Burguer para criar um na simulação. Em seguida em outro terminal Ubuntu, deve-se navegar até a pasta onde se encontra o script python e executa-lo. (Utilize -  cd /mnt/<NOME_DISCO/Users/<USUÁRIO> - e depois - python3 controle.py). 
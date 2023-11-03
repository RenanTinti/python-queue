# python-queue
 
<b>Instruções:</b><br>
<ul>
 <li>Realizar o download do RabbitMQ: https://www.rabbitmq.com/download.html</li>
 <li>Executar o RabbitMQ para que o serviço de mensageria funcione</li>
 <li>Abrir três terminais, cada um para um arquivo</li>
 <li>Executar em ordem:</li>
 <ul>
  <li><i>producer.py</i></li>
  <li><i>consumer_orders.py</i></li>
  <li><i>consumer_errors.py</i></li>
 </ul>
 <li>Analisar os logs que estão sendo enviados pela producer e recebidos pelos consumers</li>
</ul>
<p>Foi programado uma pausa de 0.1s entre os envios para que seja possível verificar log por log</p>
<p>Para executar a aplicação, o usuário deve estar autenticado no RabbitMQ. Para isso, deve inserir suas credenciais no programa instalado do RabbitMQ</p>

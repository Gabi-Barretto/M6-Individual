# Unidade 7 - Publisher e Subscriber ROS + Supabase

Considerando a atividade proposta os dois scripts em Python utilizam a biblioteca ROS 2 (Robot Operating System) para comunicação. O primeiro script realiza a publicação de quadros de vídeo, enquanto o segundo assina esses quadros e os armazena no Supabase, um serviço de banco de dados e armazenamento em nuvem.

O primeiro script define uma classe chamada `ImagePublisher`, que é uma subclasse da classe `Node` do ROS:

```python
class ImagePublisher(Node):
  def __init__(self):
    ...
```

Nesta classe, o construtor inicializa um objeto `publisher_` que publica mensagens do tipo `Image` no tópico 'video_frames':

```python
self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
```

Ele também cria um temporizador que dispara a função de retorno de chamada (`timer_callback`) a cada 0,1 segundos. Esta função lê um quadro do vídeo:

```python
self.timer = self.create_timer(timer_period, self.timer_callback)
...
def timer_callback(self):
  ret, frame = self.cap.read()
```

Se ainda existem quadros no vídeo para ler, o quadro é convertido em uma mensagem de imagem ROS usando a função `cv2_to_imgmsg` do `CvBridge` e publicado no tópico 'video_frames':

```python
self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
```

O segundo script define uma classe chamada `ImageSubscriber`, que também é uma subclasse da classe `Node` do ROS:

```python
class ImageSubscriber(Node):
  def __init__(self):
    ...
```

No construtor desta classe, é criado um objeto de assinatura que recebe mensagens de imagem do tópico 'video_frames':

```python
self.subscription = self.create_subscription(Image, 'video_frames', self.listener_callback, 10)
```

A função de retorno de chamada (`listener_callback`) é chamada sempre que uma mensagem é recebida neste tópico. Esta função converte a mensagem de imagem ROS de volta em uma imagem OpenCV:

```python
current_frame = self.br.imgmsg_to_cv2(data)
```

Em seguida, o quadro da imagem é convertido em um arquivo de bytes jpg:

```python
is_success, buffer = cv2.imencode(".jpg", current_frame)
byte_image = buffer.tobytes()
```

Finalmente, o arquivo de bytes é enviado para um bucket no Supabase:

```python
res = supabase.storage.from_(bucket_name).upload(f"frame_{self.frame_number}.jpg", byte_image)
```

O quadro da imagem também é exibido em uma janela OpenCV chamada "camera". Se a tecla 'q' for pressionada, a janela OpenCV será fechada:

```python
cv2.imshow("camera", current_frame)
if cv2.waitKey(25) & 0xFF == ord('q'):
  cv2.destroyAllWindows()
  return
```

Portanto, esses dois scripts em conjunto demonstram como transmitir vídeo de um arquivo em tempo real usando ROS 2, além de como armazenar cada quadro do vídeo em um serviço de banco de dados e armazenamento em nuvem, no caso, o Supabase.

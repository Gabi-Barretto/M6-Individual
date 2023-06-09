# Import the necessary libraries
import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

# Criando o cliente do supabase
from supabase import create_client, Client
import os
import time


# Dentro do Dashboard do Projeto no Supabase, selecionar Project Settings -> API -> API Settings (OK!)
url: str = "https://vkwoahlzgchzxhvbbsvs.supabase.co"

# Copiar a Project API Keys. IMPORTANTE: por hora, utilizar a service_role key.(OK!)
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrd29haGx6Z2NoenhodmJic3ZzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njc2Mzg1NywiZXhwIjoyMDAyMzM5ODU3fQ.DCY0-vlQetCrlPYOQQQdQw7-0A28Q3sCURpnPN2j3i8"

# Cria o cliente para conectar na API do supabase
supabase: Client = create_client(url, key)

# Nome do bucket utilizado (precisa criar em storage no Supabase)
bucket_name: str = "arquivos"


class ImageSubscriber(Node):
  """
  Create an ImageSubscriber class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('image_subscriber')
      
    # Create the subscriber. This subscriber will receive an Image
    # from the video_frames topic. The queue size is 10 messages.
    self.subscription = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback, 
      10)
    self.subscription # prevent unused variable warning
      
    # Used to convert between ROS and OpenCV images
    self.br = CvBridge()

    # Contador de frames
    self.frame_number = 0
   
  def listener_callback(self, data):
    """
    Callback function.
    """
    # Display the message on the console
    self.get_logger().info('Receiving frame')
 
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data)

    # Convertendo o ndarray para um arquivo de bytes jpg
    is_success, buffer = cv2.imencode(".jpg", current_frame)

    # O buffer agora contém a imagem codificada como jpg
    byte_image = buffer.tobytes()


    # Envia os arquivos do diretório para o bucket
    res = supabase.storage.from_(bucket_name).upload(f"frame_{self.frame_number}.jpg", byte_image)
    print(res)

    # Display image
    cv2.imshow("camera", current_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      return
    
    # Increment the frame number
    self.frame_number += 1
    
  
def main(args=None):
  
  # Initialize the rclpy library
  rclpy.init(args=args)
  
  # Create the node
  image_subscriber = ImageSubscriber()
  
  # Spin the node so the callback function is called.
  rclpy.spin(image_subscriber)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  image_subscriber.destroy_node()
  
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
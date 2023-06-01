import cv2
import os

def tirar_foto():
    # Inicializa a webcam
    cap = cv2.VideoCapture(0)

    # Verifica se a webcam foi aberta corretamente
    if not cap.isOpened():
        print("Não foi possível abrir a webcam.")
        return

    # Captura o quadro da webcam
    ret, frame = cap.read()

    # Verifica se o quadro foi capturado corretamente
    if not ret:
        print("Não foi possível capturar o quadro.")
        return

    # Exibe o quadro capturado em uma janela
    cv2.imshow("Foto", frame)

    # Aguarda até que uma tecla seja pressionada
    key = cv2.waitKey(0)

    # Verifica se a tecla pressionada foi a tecla 's' (salvar)
    if key == ord('s'):
        # Obtém o diretório atual do script
        diretorio_atual = os.getcwd()

        # Define o caminho completo para salvar a foto
        caminho_foto = os.path.join(diretorio_atual, "foto.jpg")

        # Salva a foto no diretório atual
        cv2.imwrite(caminho_foto, frame)
        print("Foto salva com sucesso.")

    # Fecha a janela
    cv2.destroyAllWindows()

    # Libera a webcam
    cap.release()

# Chama a função para tirar a foto
tirar_foto()

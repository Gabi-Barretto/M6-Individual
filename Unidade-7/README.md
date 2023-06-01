# Unidade 5 - Treinando Modelo para avaliação de rachaduras em paredes de concreto. (YoLov8)

A solução proposta apresenta um Jupyter Notebook, este contém o modelo treinado para detecção de rachaduras em paredes de concreto. Para tal, utilizei da linguagem python e seus frameworks Ultralytics versão 8.0.28, utilize < !pip install ultralytics==8.0.28 >, depois de importar as bibliotecas necessárias (YOLO) para execução do treino e avaliação do mesmo, instale o RoboFlow, utilize < !pip install roboflow > importe e inicie ele com sua API key pessoal, vincule o projeto a um workspace da RoboFlow e inicie o download do dataset. Por fim, basta treinar o modelo, exemplo < !yolo task=segment mode=train model=yolov8s-seg.pt data={dataset.location}/data.yaml epochs=10 imgsz=640>. Para fins de análise, são gerados arquivos como a matriz de confusão, exemplo para plot < Image(filename=f'{HOME}/runs/segment/train/confusion_matrix.png', width=600) >.

Link do Colab - https://colab.research.google.com/drive/197rlNcaTV-MsaLqo7NAWY2SRV9WEQ--P?usp=sharing

Link do Vídeo - https://drive.google.com/file/d/1F_GVidsdwPae777JQuUjHMn3I-N75BLl/view?usp=sharing

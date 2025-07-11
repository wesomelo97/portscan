import socket
import sys

def scan_port(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    try:
        client.connect((host, port))
        print(f"[+] Porta {port} aberta em {host}")
        try:
            client.send(b"Hello world!")
            resposta = client.recv(1024)
            print(f"    ↳ Resposta: {resposta.decode(errors='ignore')}")
        except Exception as e:
            print(f"    ↳ Erro ao enviar/receber dados: {e}")
    except (socket.timeout, ConnectionRefusedError):
        print(f"[-] Porta {port} fechada em {host}")
    except socket.gaierror:
        print("[!] Host inválido ou não resolvido.")
        sys.exit()
    finally:
        client.close()

def main():
    print("\n--- Yanix Portscan V1.0 ---\n")

    host = input("Digite o host/IP a ser escaneado: ").strip()

    portas_input = input("Digite as portas (ex: 80,443,21-25): ").replace(" ", "")
    portas = set()

    try:
        for part in portas_input.split(","):
            if "-" in part:
                inicio, fim = map(int, part.split("-"))
                portas.update(range(inicio, fim+1))
            else:
                portas.add(int(part))
    except ValueError:
        print("[!] Formato de porta inválido.")
        return

    print(f"\n[~] Iniciando scan em {host}...\n")
    for port in sorted(portas):
        scan_port(host, port)

if __name__ == "__main__":
    main()

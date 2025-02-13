import subprocess

# Exibe as redes Wi-Fi disponíveis
result = subprocess.run(["nmcli", "-t", "-f", "SSID,SIGNAL", "dev", "wifi"], capture_output=True, text=True)
print("Saída1:", result.stdout)
print("Erros1:", result.stderr)

# Conecta-se à rede Wi-Fi especificada com a senha fornecida
result2 = subprocess.run(["nmcli", "dev", "wifi", "connect", "2GEDILTON", "--ask"], capture_output=True, text=True)
print("Saída2:", result2.stdout)
print("Erros2:", result2.stderr)

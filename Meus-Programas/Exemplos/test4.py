import platform

print(platform.platform())    # Exibe informações sobre o sistema operacional
print(platform.system())    # Exibe o nome do sistema operacional
platform_info = platform.uname()  # Exibe informações detalhadas do sistema
print(platform_info)  # Exibe as informações detalhadas do sistema

print(platform.machine)

import errno
import os

def handle_file_error(error):
    error_mapping = {
        errno.ENOENT: "Arquivo não encontrado",
        errno.EACCES: "Sem permissão de acesso",
        errno.EEXIST: "Arquivo já existe",
        errno.ENOSPC: "Espaço em disco insuficiente",
        errno.EMFILE: "Muitos arquivos abertos (limite do processo)",
        errno.ENFILE: "Muitos arquivos abertos (limite do sistema)",
        errno.EINVAL: "Argumento inválido",
        errno.EISDIR: "É um diretório, não um arquivo",
        errno.ENOTDIR: "Não é um diretório",
        errno.ENOMEM: "Memória insuficiente",
        errno.EBUSY: "Recurso ocupado",
        errno.EROFS: "Sistema de arquivos somente leitura",
        errno.ENODEV: "Dispositivo não encontrado",
        errno.EIO: "Erro de entrada/saída",
        errno.EPIPE: "Pipe quebrado",
        errno.EAGAIN: "Recurso temporariamente indisponível",
        errno.ENAMETOOLONG: "Nome do arquivo muito longo",
        errno.EFAULT: "Endereço inválido"
    }
    
    return error_mapping.get(error, f"Erro desconhecido: {error}")

# Exemplo de uso
try:
    with open('/arquivo_inexistente', 'r') as f:
        content = f.read()
except IOError as e:
    print(f"Erro {e.errno}: {handle_file_error(e.errno)}")
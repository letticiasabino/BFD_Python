"""Imaginar que temos uma aplicação que a pessoa pode coloca um video (mp4 ou AVI); Terei que ter uma aplicação que só lê .vmk. Terei que adaptar."""

class LeitorDeMP4:
    def ler_dados_mp4(self, video_path1: str) -> str:
        print(f"Adapter MP4: Processando arquivo em '{video_path1}'...")
        dados = f"Vídeo passando..."
        return dados
    
class LeitorDeVMK:
    def ler_dados_vmk(self, video_path2: str) -> str:
        print(f"Adapter VMK: Processando arquivo em '{video_path2}'...")
        dados = f"Vídeo passando..."
        return dados

class LeitorDeAVI:
    def ler_dados_avi(self, video_path3: str) -> str:
        print(f"Adapter AVI: Processando arquivo em '{video_path3}'...")
        dados = f"Vídeo passando..."
        return dados


class LeitorDeVideoTarget:
    def extrair_video(self, caminho_video: str) -> str:
        raise NotImplementedError
    
class LeitorDeVideoAdapter(LeitorDeVideoTarget):
    def __init__(self, tipo_arquivo: str):
        self.adapter = None
        tipo = tipo_arquivo.lower()

        if tipo == 'vmk':
            self.adapter = LeitorDeVMK
        else:
            raise ValueError(f"Tipo de arquivo não suportado")
    
    def extrair_video(self, caminho_video: str) -> str:
        
        if isinstance(self.adapter, LeitorDeVMK):
            return self.adapter.ler_dados_vmk(caminho_video)
        
        elif isinstance(self.adapter, LeitorDeVMK):
            return self.adapter.obter_conteudo_vmk(caminho_video)
        else:
            return "Erro: Adapte não configurado corretamente."
        

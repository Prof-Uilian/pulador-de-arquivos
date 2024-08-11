import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Copiar Arquivos")
        self.root.geometry("400x200")

        self.pasta_origem = ""
        self.pasta_destino = ""

        self.botao_origem = tk.Button(root, text="Selecionar Pasta de Origem", command=self.selecionar_pasta_origem)
        self.botao_origem.pack(pady=10)

        self.botao_destino = tk.Button(root, text="Selecionar Pasta de Destino", command=self.selecionar_pasta_destino)
        self.botao_destino.pack(pady=10)

        self.botao_copiar = tk.Button(root, text="Copiar Arquivos", command=self.copiar_arquivos)
        self.botao_copiar.pack(pady=10)

    def selecionar_pasta_origem(self):
        self.pasta_origem = filedialog.askdirectory(title="Selecione a Pasta de Origem")
        if self.pasta_origem:
            messagebox.showinfo("Pasta de Origem", f"Pasta de Origem selecionada: {self.pasta_origem}")

    def selecionar_pasta_destino(self):
        self.pasta_destino = filedialog.askdirectory(title="Selecione a Pasta de Destino")
        if self.pasta_destino:
            messagebox.showinfo("Pasta de Destino", f"Pasta de Destino selecionada: {self.pasta_destino}")

    def copiar_arquivos(self):
        if not self.pasta_origem or not self.pasta_destino:
            messagebox.showerror("Erro", "Por favor, selecione ambas as pastas de origem e destino.")
            return

        try:
            arquivos = os.listdir(self.pasta_origem)
            print(f'Arquivos encontrados na pasta de origem: {arquivos}')  # Adiciona print para depuração
            arquivos_foto = [f for f in arquivos if f.startswith('photo (') and f.endswith(').jpg')]
            print(f'Arquivos filtrados: {arquivos_foto}')  # Adiciona print para depuração
            if not arquivos_foto:
                messagebox.showerror("Erro", "Nenhum arquivo encontrado no formato esperado 'photo (XXX)'")
                return

            arquivos_foto.sort(key=lambda x: int(x.split('(')[-1].split(')')[0]))

            os.makedirs(self.pasta_destino, exist_ok=True)

            for i in range(0, len(arquivos_foto), 2):
                arquivo_origem = os.path.join(self.pasta_origem, arquivos_foto[i])
                arquivo_destino = os.path.join(self.pasta_destino, arquivos_foto[i])
                shutil.copy2(arquivo_origem, arquivo_destino)

            messagebox.showinfo("Sucesso", "Arquivos copiados com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicativo(root)
    root.mainloop()

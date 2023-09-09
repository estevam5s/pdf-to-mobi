import os
import subprocess

class PDFConverter:
    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = output_folder

    def convert_to_mobi(self):
        try:
            input_filename = os.path.basename(self.input_file)
            output_mobi = os.path.join(self.output_folder, os.path.splitext(input_filename)[0] + ".mobi")
            subprocess.run(["ebook-convert", self.input_file, output_mobi, "--output-profile", "kindle"], check=True)
            print(f"Conversão concluída: {self.input_file} para {output_mobi}")
        except subprocess.CalledProcessError as e:
            print(f"Erro na conversão: {e}")
        except Exception as e:
            print(f"Erro desconhecido: {str(e)}")

def main():
    print("=== Conversão de PDF para MOBI ===")
    input_pdf = input("Digite o caminho completo do arquivo PDF: ")
    
    # Defina a pasta de saída
    mobi_folder = "converted_mobi"  # Pasta para armazenar os arquivos MOBI

    # Certifique-se de que a pasta de saída exista ou crie-a
    if not os.path.exists(mobi_folder):
        os.makedirs(mobi_folder)

    pdf_converter = PDFConverter(input_pdf, mobi_folder)
    pdf_converter.convert_to_mobi()

if __name__ == "__main__":
    main()

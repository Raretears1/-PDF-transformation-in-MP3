from art import tprint
from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='glory_to_ua.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'Original file: {Path(file_path).name}')
        print("Processing.....")

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('/n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!'

    # return 'File exist!'
    else:
        return 'File not exist'


def main():
    tprint('PDF>>TO>>NP3', font='bulbhead')
    file_path = input('\n Enter a files path: ')
    language = 'en'
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
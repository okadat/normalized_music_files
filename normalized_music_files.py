import os
import unicodedata

def normalize_filename(filename):
    # 全角英数字・記号を半角に変換
    normalized = unicodedata.normalize('NFKC', filename)
    # スラッシュをハイフンに置換
    normalized = normalized.replace('/', '-')
    return normalized

def rename_music_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        full_path = os.path.join(directory_path, filename)

        if os.path.isfile(full_path):
            # 音楽ファイルだけ対象（拡張子で判断）
            if filename.lower().endswith(('.mp3', '.flac', '.m4a', '.wav', '.aac', '.ogg')):
                new_filename = normalize_filename(filename)
                new_full_path = os.path.join(directory_path, new_filename)

                # 名前が変わっている場合のみリネーム
                if new_filename != filename:
                    print(f'Renaming: {filename} → {new_filename}')
                    os.rename(full_path, new_full_path)

# ここに対象のディレクトリパスを入力（例: "/Users/yourname/Music"）
target_directory = "/Users/yourname/Music"

rename_music_files_in_directory(target_directory)

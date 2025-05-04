# normalized_music_files
- Please read the description and Terms of Use, Disclaimer, Cautions and Warnings.
- 説明と利用規約・免責事項・注意点・警告を読んでご利用ください。

# 音楽ファイルに全角の文字で英語数字記号が入力されていて，使用するのに重複があったりと困ったので，ファイル名を正規化するためのpythonのソースです。
- 音楽ファイルのファイル名に使用されいている英語数字記号が，日本語と同じ全角文字から半角文字に変換するソースコード
- ただし，”/”は”-”に変換する。
# This is a python source to normalize file names, because I had trouble with English numeral symbols entered in full-width characters in music files, and there were duplicates to use.
- Source code to convert English numeric symbols used in file names of music files from full-width characters to half-width characters, the same as Japanese. 
- However, “/” is converted to “-”.
  
##音楽ファイルに全角の文字で英語数字記号が入力されていて，使用するのに重複があったりとつかがってが悪かったので正規化するためのpythonのソースです。
##The source code is a python source code to normalize English numeral symbols in music files that have been input in full-width characters.

##対象機種はmacです。
- 指定されたディレクトリ内の音楽ファイルのファイル名に含まれる全角の英数字や記号を半角に変換し、さらにファイル名に含まれるスラッシュ（/）をハイフン（-）に置換するPythonスクリプトです。
## Target machine is a mac.
- This is a python script that converts full-width alphanumeric characters and symbols in the file names of music files in the specified directory to half-width characters, and replaces slashes (/) with hyphens (-) in the file names.

##ソースの内容は下記です。
- unicodedata.normalize('NFKC', text) により、全角の英数字・記号を半角に変換します。
- ファイル名に含まれるスラッシュ（/）は、ファイルシステム上でディレクトリの区切りとして使用されるため、ファイル名に含めることはできません。そのため、スラッシュ（/）をハイフン（-）に置換しています。
- ファイル名が変更されるときだけ os.rename() を実行します。
##The source contents are as follows.
-converts full-width alphanumeric characters and symbols to half-width by unicodedata.normalize(‘NFKC’, text).
-Slashes (/) in file names are used as directory separators on the file system and cannot be included in file names. Therefore, slashes are replaced with hyphens (-).
-Os.rename() is executed only when the file is renamed.

##注意点
このスクリプトは、指定されたディレクトリ内の音楽ファイルのファイル名を変更します。実行する前に、必ずバックアップを取ってください。
ファイル名の変更により、他のアプリケーションやシステムで問題が発生する可能性がありますので、注意して使用してください。
ご利用は自己責任でお願いします。
## Notes 
This script renames music files in the specified directory. Be sure to back up the files before executing it.
Use with caution, as file renaming may cause problems with other applications or systems.
Use at your own risk.

# 利用規約・免責事項・注意点・警告
# Terms of Use, Disclaimer, Cautions, and Warnings

# 1. 利用規約
- 本スクリプト（以下「本ソフトウェア」）は、個人利用を目的として無償で提供されます。
- 本ソフトウェアの著作権は作者に帰属し、無断での再配布、商用利用、改変後の再配布は禁止されています。
- 本ソフトウェアの使用により発生したいかなる損害についても、作者は一切の責任を負いません。
- 本ソフトウェアの利用をもって、上記の利用規約に同意したものとみなされます。
# 1. Terms of Use 
- This script (“Software”) is provided free of charge for personal use.
- The copyright of this software belongs to the author, and redistribution without permission, commercial use, or redistribution after modification is prohibited.
- The author assumes no responsibility for any damage caused by the use of this software.
- By using this software, you agree to the above terms of use. 2.

# 2. 免責事項
- 本ソフトウェアは、全角英数字・記号を半角に変換し、ファイル名に含まれるスラッシュ（/）をハイフン（-）に置換する機能を提供しますが、その動作の正確性や適用結果について保証するものではありません。
- 本ソフトウェアの使用により発生したデータの損失、システムの不具合、その他の問題について、作者は一切の責任を負いません。
# 2. Disclaimer 
- This software provides functions to convert full-width alphanumeric characters and symbols to half-width characters and to replace slashes (/) in file names with hyphens (-), but the author does not guarantee the accuracy of its operation or application results.
- The author assumes no responsibility for any loss of data, system malfunction, or other problems that may result from the use of this software. 3.

# 3. 注意点
- 本ソフトウェアを実行する前に、対象となるディレクトリおよびファイルのバックアップを必ず取得してください。
- ファイル名の変更により、他のアプリケーションやシステムで問題が発生する可能性がありますので、注意して使用してください。
- 本ソフトウェアは、指定されたディレクトリ内の音楽ファイル（.mp3, .flac, .m4a, .wav, .aac, .ogg）のみを対象としています。
# 3. Precautions 
- Before running this software, be sure to back up the target directories and files.
- Use this software with caution, as file renaming may cause problems with other applications or systems.
- This software only works with music files (.mp3, .flac, .m4a, .wav, .aac, .ogg) in the specified directory.

# 4. 警告
- 本ソフトウェアは、ファイル名の変更を行うため、誤った使用により重要なファイルがアクセス不能になる可能性があります。
- スクリプトの内容を十分に理解し、自己の責任において使用してください。
- 本ソフトウェアの使用により発生したいかなる損害についても、作者は一切の責任を負いません。
# 4. WARNING 
- This software renames files, so misuse may cause important files to become inaccessible.
- Please fully understand the contents of the script and use it at your own risk.
- The author assumes no responsibility for any damage caused by the use of this software.

4. 警告
本ソフトウェアは、ファイル名の変更を行うため、誤った使用により重要なファイルがアクセス不能になる可能性があります。
スクリプトの内容を十分に理解し、自己の責任において使用してください。
本ソフトウェアの使用により発生したいかなる損害についても、作者は一切の責任を負いません。

import os
import pytube

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print('''\033[1;33m
πbem vindo ao lado alternativoπ

ββββ βββββ ββββββ   βββ   ββ ββββββββββ ββββββ  ββββββ    ββββββ
βββββββ βββββββ  βββββββ   ββββββββββ βββββ   β ββββ  ββββββ    β
βββ    ββββββββ ββββ βββ  ββββββββββ   ββββββ   ββββ  ββββ ββββ
βββ    βββ βββββββ β  βββ βββββββββββ   ββββ  β βββ   βββ  β   βββ
ββββ   ββββββββ β  β   ββββ  βββββββββββ ββββββββ ββββββββββββββββ
β ββ   β  βββββ β  β   β ββ  ββ   βββ  β ββ ββ ββ ββββββ β βββ β β
β  β      βββ β        β ββ   β β β β  β  β β  β  β β ββ β ββ  β β
β      β   ββ            ββ   β β β β  β    β   β β β β  β  β  β
       β                  β   β     β       β  β    β β        β
                         β        β
                         @bydeathlxncer


\033[1;36m(\033[1;32m1\033[1;36m) \033[1;32mbaixar video do Youtubeπ¬
\033[1;36m(\033[1;32m2\033[1;36m) \033[1;32mmeu canalπΊ
\033[1;36m(\033[1;32m3\033[1;36m) \033[1;32mvazar do scriptβ
''')

	r = input("\033[1;33m-\033[1;36m-\033[1;32m>\033[1;34m ")

	if r == '1':
		os.system('cls' if os.name == 'nt' else 'clear')
		url = input("\033[1;32mcoloque o link do video para baixarπΎ:\033[1;34m ")
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f"""\033[1;95mbaixando garai paraekkkkk
                
[                    ] 0%
[=====               ] 25%
[==========          ] 50%
[===============     ] 75%
[====================] 100%""")
		yt = pytube.YouTube(url)
		video =  yt.streams.first()
		video.download()
               
               

                
		print(f"\033[1;32mvideo \033[;1m{yt.title} \033[1;mfoi baixadoπ para mover o vΓ­deo para sua memoria interna use o comando (mv (nome do vΓ­deo com o .mp4 no final) /sdcard/Download)")

                
		pt = input("""

\033[1;31m(1) \033[1;32mvazar do scriptβ
\033[1;31m(2) \033[1;32mvoltar para o  menuπ»

\033[1;33m-\033[1;36m-\033[1;32m>\033[1;34m """)

		if pt == '1':
			exit()
		if pt == '2':
			main()
		else:
			print("\n\033[1;31mopΓ§Γ£o invalida chefeπ³πkkkkj\n")
			exit()

	if r == '3':
		os.system('cls' if os.name == 'nt' else 'clear')
		print('''\033[1;107m\033[1;30m



              __             _    _
._ _ _  ___  /. |  ___  _ _ <_> _| | ___  ___  ___
| ' ' || . \/_  .||___|| | || |/ . |/ ._>/ . \<_-<
|_|_|_||  _/  |_|      |__/ |_|\___|\___.\___//__/
       |_|          @bydeathlxncer


fiz essa merda apenas para testes entΓ£o nΓ£o enche vadiaππ
@bydeathlxncer
\n''')

	if r == '2':
		os.system("am start -a android.intent.action.VIEW https://youtube.com/channel/UCnDHlOBQY-EfJsLr6oAxTjQ")
		os.system('cls' if os.name == 'nt' else 'clear')
		

main()


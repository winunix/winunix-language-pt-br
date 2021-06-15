import os

# Launchers
def setPropertyPtBr(file, prop, value):
	cmd = r"cat %s.desktop | grep '^%s\[pt_BR\]=' | wc -l" % (file,prop)
	hasProp = int(os.popen(cmd).read().rstrip()) != 0
	if hasProp:
		os.system(r"sed -i '/^%s\[pt_BR\]=/c\%s\[pt_BR\]=%s' %s.desktop" % (prop, prop, value, file))
	else:
		os.system(r"echo '%s[pt_BR]=%s' >> %s.desktop" % (prop, value, file))

def setProperties(file, name, generic, comment):
	setPropertyPtBr(file, "Name", name)
	setPropertyPtBr(file, "GenericName", generic)
	setPropertyPtBr(file, "Comment", comment)

launchers = [
	["lxqt-leave", "Abandonar", "Abandonar sessão", "Exibe dialogo abandonar"],
	["lxqt-config", "Centro de Configuração", "Configurações", "Configurar módulos do LXQt"],
	["lxqt-config-file-associations", "Associação de arquivos", "Definições de associação de arquivos", "Configurar associação de arquivos para os tipos conhecidos"],
	["lxqt-config-brightness","Brilho","Configurações de brilho","Configurações de brilho"],
	["lxqt-config-locale","Idiomas","Definições de idioma","Definições de idioma para o LXQt"],
	["lxqt-config-input","Teclado e mouse","Ajustes de teclado e mouse","Configuração do mouse, teclado e outros dispositivos de entrada"],
	["software-properties-drivers-lxqt","Drivers Adicionais","Drivers Adicionais","Configurações de drivers proprietários"],
	["nm-connection-editor","Configuração avançada de rede","Conexões de rede","Gerenciamento de conexões de rede"],
	["upg-apply","Aplicar atualização completa","Faz a atualização completa do sistema","Busca e aplica atualizações"],
	["fcitx-configtool","Métodos de entrada Fcitx","Configuração de métodos de entrada","Altera configurações do Fcitx"],
	["im-config","Método de entrada","Configuração de métodos de entrada","Configura método de entrada do teclado"],
	["system-config-printer","Impressoras","Impressoras","Configurações das impressoras"],
	["xscreensaver-properties","Proteção de tela","Preferências do protetor de tela","Muda propriedades de proteção de tela"],
	["software-properties-lxqt","Fontes de softwares","Fontes de softwares","Configura as fontes para instalação de softwares e atualização"],
	["software-properties-qt","Fontes de softwares","Fontes de softwares","Configura as fontes para instalação de softwares e atualização"],
	["org.kde.bluedevilsendfile","Envio de arquivo por Bluetooth","Envio de arquivo do BlueDevil","Envio de arquivo do BlueDevil"],
	["org.kde.bluedevilwizard","Assistende de dispositivos Bluetooth","Assistente BlueDevil","Assistente BlueDevil"],
	["fcitx","Teclado virtual do Fcitx","Inicia teclado virtual","Inicia método de entrada"],
	["htop","Gerenciador de tarefas Htop","Visualizador de processos","Mostra os processos do sistema"],
	["usb-creator-kde","Criar disco de inicialização","Criador de discos de inicialização","Cria disco de inicialização usando image"],
	["qps","Gerenciador de tarefas Qps","Gestor de processos em Qt","Aplicação em Qt para mostrar e gerir os processos em execução"],
	["pavucontrol-qt","Controle de volume PulseAudio","Controle de volume","Ajustar o nível do volume"],
	["lximage-qt","Visualizador de imagens","LXImage-Qt","O visualizador de imagens do LXQt"],
	["screengrab","Captura de tela","Captura de tela ScreenGrab","Captura de tela ScreenGrab"],
	["org.kde.skanlite","Digitalizador Skanlite","Aplicativo para digitalização de imagens","Digitaliza e salva imagens"],
	["org.kde.ark","Compressor de arquivos","Compressor de arquivos Ark","Manipulação de arquivos compactados"],
	["trojita","Cliente de e-mail","Cliente de e-mail IMAP","Cliente de e-mail IMAP"],
	["2048-qt","2048-Qt","2048-Qt","Jogo 2048 implementado em Qt"],
	["compton-conf","Efeitos de janelas","Configuração do Compton","Configurar os efeitos de janelas"],
	["compton","Habilitar Compton","X compositor","Um compositor para X11"],	
	["info","TeXInfo","Visualizador para TexInfo","Visualizador para documentos TexInfo"],
	["qlipper","Área de transferência","Área de transferência Qlipper","Área de transferência Qlipper"],	
	["vim","Editor Vim","Editor de texto por terminal","Edite arquivos de texto"],
	["software-properties-gtk","Fontes de softwares GNOME","Fontes de softwares e atualização","Configura as fontes para instalação de softwares e atualização"],
	["software-properties-drivers","Drivers Adicionais GNOME","Drivers proprietários","Configurações de drivers proprietários"],
	["org.gnome.FileRoller","Compressor de arquivos GNOME","Gerenciador de arquivos compactados","Um gerenciador de arquivos compactados para o GNOME"],
	["gucharmap","Mapa de Caracteres","Mapa de caracteres do GNOME","Insira caracteres especiais em documentos"],
	["org.gnome.DiskUtility","Utilitário de Discos","Discos","Exibe, modifica e configura discos e mídias"],
	["org.gnome.FontViewer","Visualizador de fontes","Visualizador de fontes do GNOME","Visualizador de fontes do GNOME"],
	["galculator","Calculadora GNOME","Galculator","Uma calculadora científica baseada no GTK+"],
	["org.kde.kcalc","Calculadora KDE","KCalc","Calculadora Cientifica"],
	["xpad","Notas adesivas","Xpad","Xpad"],
	["org.gnome.Evince","Visualizador de documentos","Evince","Visualizador de documentos"],
	["pdfarranger","Manipulador de PDF","PDF Arranger","Rearranja e modifica arquivos PDF"],
	["org.gnome.eog","Visualizador de imagens GNOME","Eye of GNOME","Visualizador de imagens do GNOME"],
	["audacious","Reprodutor de música","Audacious","Player baseado no XMMS"],
	["blueman-manager","Gerenciador de bluetooth","Blueman Manager","Gerenciador de bluetooth do GTK+"],
	["system-config-samba","Compartilhamentos do samba","compartilhamentos SMB/CIFS","Criar, modificar e apagar compartilhamentos do samba"]
]

for launcher in launchers:
	setProperties(*launcher)

# Directories
direc="/usr/share/desktop-directories/lxqt-settings.directory"
cmd = r"cat %s | grep '^Name\[pt_BR\]=' | wc -l" % direc
hasProp = int(os.popen(cmd).read().rstrip()) != 0
if hasProp:
	os.system(r"sed -i '/^Name\[pt_BR\]=/c\Name\[pt_BR\]=Definições do LXQt' %s" % direc)
else:
	os.system(r"echo 'Name[pt_BR]=Definições do LXQt' >> %s" % direc)

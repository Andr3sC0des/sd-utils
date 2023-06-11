def clone(webui_version):
    return f'git clone -b {webui_version} https://github.com/Andr3sC0des/stable-diffusion-webui'

def name():
    return 'stable-diffusion-webui'

def controlNet():
    return 'git clone https://github.com/Mikubill/sd-webui-controlnet /content/stable-diffusion-webui/extensions/sd-webui-controlnet'

# -*- mode: python -*-

block_cipher = None


a = Analysis(['sshot.py'],
             pathex=['C:\\Users\\ray\\Desktop\\git_projects\\ope\\client_tools\\sshot'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='sshot',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='logo_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='sshot')

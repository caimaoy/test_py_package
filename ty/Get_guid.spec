# -*- mode: python -*-
a = Analysis(['Get_guid.py'],
             pathex=['D:\\caimaoy\\python\\ty'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Get_guid.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )

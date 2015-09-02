# -*- mode: python -*-
a = Analysis(['test_watchdog.py'],
             pathex=['D:\\caimaoy\\python\\watchdog'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='test_watchdog.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )

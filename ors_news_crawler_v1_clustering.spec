# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [ ("./ors_news_crawler.xlsx", '.')

              ]
a = Analysis(
    ['ors_news_crawler_v1_clustering.py'],
    pathex=['C:\\Python\\workspaces\\ors_news'],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ors_news_crawler_v1_clustering',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    console=True,
    uac_admin=True,
    icon='./ors.ico')
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ors_news_crawler_v1_clustering',
)

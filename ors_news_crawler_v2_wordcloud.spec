# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ors_news_crawler_v2_wordcloud.py'],
    pathex=['C:\\Python\\workspaces\\ors_news'],
    binaries=[],
    datas=[   ("C:\\Python\\workspaces\\ors_news\\venv\\Lib\\site-packages\\konlpy\\"               , "./konlpy")
            , ("C:\\Python\\workspaces\\ors_news\\venv\\Lib\\site-packages\\konlpy\\java\\"         , "./konlpy/java")
            , ("C:\\Python\\workspaces\\ors_news\\venv\\Lib\\site-packages\\konlpy\\data\\tagset\\*", "./konlpy/data/tagset")
            , ("C:\\Python\\workspaces\\ors_news\\ors_news_crawler.xlsx"                            , ".")
            , ("C:\\Python\\workspaces\\ors_news\\resource"                                         , "./resource")
          ],
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
    name='ors_news_crawler_v2_wordcloud',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ors_news_crawler_v2_wordcloud',
)

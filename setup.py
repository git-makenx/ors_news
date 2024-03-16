from cx_Freeze import setup, Executable

buildOptions = {
    "packages": [
                    'konlpy'
                  , 'sklearn'
                  , 'numpy'
                  , 'os'
                  , 'bs4'
                  , 'datetime'
                  , 'requests'
                  , 'requests'
                  , 'pandas'
                  , 're'
                  , 'openpyxl'
                  , 'time'
                  , 'os'
                  , 'sys'
    ],
    "excludes": []
}

exe = [Executable('ors_news_crawler_v1_clustering.py')]

setup(
    name='ors_news_crawler_v1_clustering',
    version='1.0',
    author='bnkrisk',
    description = "I'M IML!",
    options=dict(build_exe=buildOptions),
    executables=exe
)
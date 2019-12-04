# -*- mode: python -*-
a = Analysis(['scripts/totalopenstation-gui.py'],
             pathex=['.'],
             hiddenimports=[
                 'csv',
                 'decimal',
                 'numbers',
                 'totalopenstation.formats',
                 'totalopenstation.formats.carlson_rw5',
                 'totalopenstation.formats.leica_gsi',
                 'totalopenstation.formats.leica_tcr_705',
                 'totalopenstation.formats.leica_tcr_1205',
                 'totalopenstation.formats.nikon_raw_v200',
                 'totalopenstation.formats.polar',
                 'totalopenstation.formats.sokkia_sdr33',
                 'totalopenstation.formats.topcon_gts',
                 'totalopenstation.formats.trimble_are',
                 'totalopenstation.formats.zeiss_r5',
                 'totalopenstation.formats.zeiss_rec_500',
                 'totalopenstation.models',
                 'totalopenstation.models.custom',
                 'totalopenstation.models.leica_tcr_705',
                 'totalopenstation.models.leica_tcr_1205',
                 'totalopenstation.models.nikon_npl_350',
                 'totalopenstation.models.trimble',
                 'totalopenstation.models.zeiss_elta_r55',
                 'totalopenstation.output',
                 'totalopenstation.output.tops_csv',
                 'totalopenstation.output.tops_dat',
                 'totalopenstation.output.tops_dxf',
                 'totalopenstation.output.tops_geojson',
                 'totalopenstation.output.tops_sql',
                 'totalopenstation.output.tops_txt',],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='totalopenstation.exe',
          icon='docs/_static/tops.ico',
          debug=False,
          strip=None,
          upx=False,
          console=True)

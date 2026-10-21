import os, glob
from PIL import Image, ImageDraw
res='android/app/src/main/res'
full=Image.open('assets/icon-only.png').convert('RGBA')
fg=Image.open('assets/notebook-cutout.png').convert('RGBA')
for f in glob.glob(res+'/mipmap-*/ic_launcher*.webp'): os.remove(f)
D={'mdpi':(48,108),'hdpi':(72,162),'xhdpi':(96,216),'xxhdpi':(144,324),'xxxhdpi':(192,432)}
for d,(l,f) in D.items():
    p=res+'/mipmap-'+d
    os.makedirs(p,exist_ok=True)
    ic=full.resize((l,l),Image.LANCZOS)
    ic.save(p+'/ic_launcher.png')
    m=Image.new('L',(l,l),0); ImageDraw.Draw(m).ellipse((0,0,l-1,l-1),fill=255)
    r=Image.new('RGBA',(l,l),(0,0,0,0)); r.paste(ic,(0,0),m); r.save(p+'/ic_launcher_round.png')
    h=int(f*0.56); w=int(fg.width*h/fg.height)
    c=Image.new('RGBA',(f,f),(0,0,0,0))
    c.alpha_composite(fg.resize((w,h),Image.LANCZOS),((f-w)//2,(f-h)//2))
    c.save(p+'/ic_launcher_foreground.png')
os.makedirs(res+'/values',exist_ok=True)
open(res+'/values/ic_launcher_background.xml','w').write('<?xml version="1.0" encoding="utf-8"?><resources><color name="ic_launcher_background">#F6ECD6</color></resources>')
print('icons done')

"""Install a finished poster and regenerate the Workshop preview."""
from pathlib import Path
import argparse
import shutil
from datetime import datetime
from PIL import Image

project = Path(__file__).resolve().parents[1]
mod = project / 'Contents/mods/batman_ArtelManufactoryFR/42.21'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('image', type=Path, help='Finished poster with French translation ribbon')
args = parser.parse_args()
image = Image.open(args.image).convert('RGB')
backup = project / 'source' / ('art-backup-' + datetime.now().strftime('%Y%m%d-%H%M%S'))
backup.mkdir(parents=True, exist_ok=False)
for old in (mod / 'poster.png', project / 'preview.png'):
    if old.is_file():
        shutil.copy2(old, backup / old.name)
image.save(mod / 'poster.png')
# Preserve the source poster's composition when fitting the square preview.
preview = Image.new('RGB', (512, 512), image.getpixel((0, 0)))
thumb = image.copy()
thumb.thumbnail((512, 512), Image.Resampling.LANCZOS)
preview.paste(thumb, ((512-thumb.width)//2, (512-thumb.height)//2))
preview.save(project / 'preview.png')
print(f'Poster and preview installed. Previous assets: {backup}')

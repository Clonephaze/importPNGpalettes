# 🎨 Import PNG Palette

---

### 🧩 Description
**Import PNG Palette** is a lightweight Blender add-on that lets you import color palettes directly from PNG images — perfect for palette collections from [Lospec](https://lospec.com/palette-list).

Other community addons provide the option to import palettes in other formats, but not PNG, so this addon is meant to fill that gap and hopefully help artists!

---

### ✨ Features
- 🖼️ **Import any PNG image** as a color palette.
- 🎨 Works perfectly with **Lospec PNG palette formats** (horizontal, vertical, and grid).
- 🧠 **Merge similar colors** automatically, with adjustable tolerance.
- ⚙️ Limit the number of imported colors to keep palettes clean.
- 🪶 Skip transparent pixels and blank regions.
- 💡 Fully compatible with Blender **4.x+**.

---

### 🚀 Installation
1. Go to the [Releases](https://github.com/Ruuubickk/importPNGpalettes/releases) page and click on  `import_png_palette.zip` to download it.
2. In Blender, go to **Edit → Preferences → Add-ons → Install from disk...** 

<img width="811" height="281" alt="blender_jrF5iIgLr0" src="https://github.com/user-attachments/assets/9562011e-c14b-459f-9452-fb652ed19d8d" />
 
3. Select the `import_png_palette.zip` file.  
4. Enable **Import PNG Palette** in the add-ons list if not already done automatically.

---

### 🧭 Usage
1. Go to **File → Import → Import PNG as Palette**.  
2. Choose your `.png` palette file (e.g., downloaded from Lospec).  
3. Set your preferences:
   - **Max Colors** — limits the number of colors imported.
   - **Merge Similar Colors** — removes near-identical colors.
   - **Color Similarity Tolerance** — adjusts sensitivity.
   - **Ignore Transparent Pixels** — skips transparent areas.
4. Click **Import PNG as Palette**.  
5. Your new palette will appear in **Properties → Tool Settings → Palette**, named after your image file.

---

### 🧪 Example
You can test it using palettes from [Lospec’s Palette List](https://lospec.com/palette-list).  
All three Lospec PNG export types — *horizontal*, *vertical*, and *grid* — are supported, as well as 1x, 8x and 32x resolution!

---

### ⚠️ Limitations
- Very large or photographic PNGs may be slow to process.  
- If the color limit is reached, additional colors are skipped.  
- Duplicate palette names will overwrite existing palettes unless renamed manually.

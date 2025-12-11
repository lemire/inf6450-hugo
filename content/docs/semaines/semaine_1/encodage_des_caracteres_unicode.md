---
title: "Encodage des caractères Unicode"
weight: 70
---
<header style="margin-bottom: 16px;">
 <h1 style="margin: 0 0 8px 0; font-size: 22px; font-weight: 700; color:#0b1220;">
  Visualiseur d’octets UTF-8 / UTF-16
 </h1>
 <p>
  Le XML est généralement stocké dans un fichier texte avec un encodage Unicode (soit UTF-16, soit UTF-8). Il peut être intéressant de voir comment le texte est converti en données binaires sur votre disque. Saisissez du texte. Voyez les octets en UTF-8 et UTF-16. Pour distinguer les encodages, il arrive que les systèmes ajoutent quelques octets au début du contenu (appelé BOM pour Byte-Order-Mask). Le format UTF-16 comporte deux variantes : LE (little endian) et BE (big endian).
 </p>
</header>
<section style="display:block; margin-bottom: 12px;">
 <label for="input" style="display:block; font-weight:600; font-size: 13px; margin-bottom:6px;">
  Texte
 </label>
 <textarea id="input" placeholder="Tapez ici…" spellcheck="false" style="display:block; width:100%; max-width: 980px; height: 160px; padding: 12px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace; font-size: 13px; line-height: 1.4; resize: vertical; background:#ffffff; color:#0f172a;"></textarea>
</section>
<section style="display:flex; flex-wrap: wrap; gap: 16px; align-items: center; margin: 10px 0 18px 0;">
 <div style="display:flex; align-items:center; gap:10px;">
  <span style="font-weight:600; font-size:13px;">
   UTF-16
  </span>
  <label style="display:inline-flex; align-items:center; gap:6px; font-size:13px; color:#334155;">
   <input checked="" name="endian" style="margin:0;" type="radio" value="le"/>
   LE
  </label>
  <label style="display:inline-flex; align-items:center; gap:6px; font-size:13px; color:#334155;">
   <input name="endian" style="margin:0;" type="radio" value="be"/>
   BE
  </label>
 </div>
 <label style="display:inline-flex; align-items:center; gap:8px; font-size:13px; color:#334155;">
  <input id="bom" style="margin:0;" type="checkbox"/>
  Inclure BOM
 </label>
 <div style="margin-left:auto; font-size:12px; color:#64748b;">
  Les valeurs sont affichées en hexadécimal (octets).
 </div>
</section>
<section style="display:grid; grid-template-columns: 1fr; gap: 16px; max-width: 980px;">
 <div style="border:1px solid #e2e8f0; border-radius:10px; padding:12px; background:#f8fafc;">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
   <strong style="font-size:14px; color:#0b1220;">
    UTF-8
   </strong>
   <span id="len8" style="font-size:12px; color:#334155;">
    0 octet
   </span>
  </div>
  <pre id="hex8" style="margin:0; white-space:pre-wrap; word-break:break-word; font-size:12px; line-height:1.45; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace; color:#0f172a;">—</pre>
 </div>
 <div style="border:1px solid #e2e8f0; border-radius:10px; padding:12px; background:#f8fafc;">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
   <strong style="font-size:14px; color:#0b1220;">
    UTF-16
    <span id="endiantag" style="font-weight:600; color:#0b1220;">
     LE
    </span>
    <span id="bomtag" style="font-weight:400; color:#64748b;">
     , sans BOM
    </span>
   </strong>
   <span id="len16" style="font-size:12px; color:#334155;">
    0 octet
   </span>
  </div>
  <pre id="hex16" style="margin:0; white-space:pre-wrap; word-break:break-word; font-size:12px; line-height:1.45; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace; color:#0f172a;">—</pre>
 </div>
</section>
<footer style="margin-top: 18px; font-size:12px; color:#64748b;">
 Conseils: les émojis et caractères hors BMP utilisent des paires de substituts en UTF‑16. Le comptage d’octets inclut le BOM si coché.
</footer>
<script>
 (function() {
        const $ = (id) => document.getElementById(id);
        const input = $('input');
        const len8 = $('len8');
        const hex8 = $('hex8');
        const len16 = $('len16');
        const hex16 = $('hex16');
        const bom = $('bom');
        const endiantag = $('endiantag');
        const bomtag = $('bomtag');
        const endianRadios = Array.from(document.querySelectorAll('input[name="endian"]'));
        function pluralize(n) { return n > 1 ? 'octets' : 'octet'; }
        function toHex(bytes) {
          if (!bytes || bytes.length === 0) return '—';
          const parts = [];
          for (let i = 0; i < bytes.length; i++) {
            parts.push(bytes[i].toString(16).padStart(2, '0').toUpperCase());
          }
          // Group by 16 bytes per line for readability
          const lines = [];
          for (let i = 0; i < parts.length; i += 16) {
            lines.push(parts.slice(i, i + 16).join(' '));
          }
          return lines.join('\n');
        }
        function utf16Encode(str, littleEndian = true, includeBOM = false) {
          const codeUnits = [];
          for (const ch of str) {
            const cp = ch.codePointAt(0);
            if (cp <= 0xFFFF) {
              codeUnits.push(cp);
            } else {
              const uPrime = cp - 0x10000;
              const high = 0xD800 + (uPrime >> 10);
              const low = 0xDC00 + (uPrime & 0x3FF);
              codeUnits.push(high, low);
            }
          }
          const extra = includeBOM ? 2 : 0;
          const bytes = new Uint8Array(codeUnits.length * 2 + extra);
          let offset = 0;
          if (includeBOM) {
            if (littleEndian) { bytes[offset++] = 0xFF; bytes[offset++] = 0xFE; }
            else { bytes[offset++] = 0xFE; bytes[offset++] = 0xFF; }
          }
          for (let i = 0; i < codeUnits.length; i++) {
            const cu = codeUnits[i] & 0xFFFF;
            if (littleEndian) {
              bytes[offset++] = cu & 0xFF;
              bytes[offset++] = (cu >> 8) & 0xFF;
            } else {
              bytes[offset++] = (cu >> 8) & 0xFF;
              bytes[offset++] = cu & 0xFF;
            }
          }
          return bytes;
        }
        function update() {
          const text = input.value || '';
          const littleEndian = endianRadios.find(r => r.checked)?.value !== 'be';
          const includeBOM = bom.checked;
          // UTF-8
          const utf8 = new TextEncoder().encode(text);
          len8.textContent = utf8.length + ' ' + pluralize(utf8.length);
          hex8.textContent = toHex(utf8);
          // UTF-16
          const utf16 = utf16Encode(text, littleEndian, includeBOM);
          len16.textContent = utf16.length + ' ' + pluralize(utf16.length);
          hex16.textContent = toHex(utf16);
          endiantag.textContent = littleEndian ? 'LE' : 'BE';
          bomtag.textContent = includeBOM ? ', avec BOM' : ', sans BOM';
        }
        input.addEventListener('input', update);
        bom.addEventListener('change', update);
        endianRadios.forEach(r => r.addEventListener('change', update));
        // Init
        update();
      })();
</script>
<p>
 Pour en savoir plus...
</p>
<ul>
 <li>
  <a href="https://fr.wikipedia.org/wiki/UTF-8">
   UTF-8
  </a>
  (wikipédia);
 </li>
 <li>
  <a href="https://fr.wikipedia.org/wiki/UTF-16">
   UTF-16
  </a>
  (wikipédia);
 </li>
</ul>

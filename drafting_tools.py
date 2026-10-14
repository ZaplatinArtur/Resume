"""Flat, top-view drafting instruments, independently placed on the table."""

_TICKS = ''.join(f'<path d="M{16 + i * 12} 5v{20 if i % 5 == 0 else 10}"/>' for i in range(50))
_NUMBERS = ''.join(f'<text x="{13 + i * 12}" y="44">{i}</text>' for i in range(0, 50, 10))
TOOLS = f'''<div class="drafting-tools" aria-hidden="true">
  <svg class="desk-ruler" viewBox="0 0 620 60" fill="none" focusable="false"><g stroke="currentColor" stroke-width="1"><rect x="5" y="5" width="610" height="50" rx="2" fill="var(--paper)"/>{_TICKS}<circle cx="599" cy="39" r="5"/><path d="M16 50h565" opacity=".25"/></g><g fill="currentColor">{_NUMBERS}</g></svg>
  <svg class="desk-set-square" viewBox="0 0 190 225" fill="none" focusable="false"><g stroke="currentColor" stroke-width="1.2"><path d="M15 209V15l160 194H15Zm24-49V83l64 77H39Z" fill="var(--paper)" fill-opacity=".85"/><path d="M15 31h10m-10 12h6m-6 12h6m-6 12h10m-10 12h6m-6 12h6m-6 12h10m-10 12h6m-6 12h6m-6 12h10m-10 12h6m-6 12h6m-6 12h10m-10 12h6m-6 12h6M30 209v-10m12 10v-6m12 6v-6m12 6v-10m12 10v-6m12 6v-6m12 6v-10m12 10v-6m12 6v-6m12 6v-10"/></g><text x="75" y="197" fill="currentColor">45° / 1:1</text></svg>
  <svg class="desk-pencil" viewBox="0 0 340 30" fill="none" focusable="false"><g stroke="currentColor" stroke-width="1"><path d="M28 8h297v14H28L6 15Z" fill="var(--paper)"/><path d="M28 8v14m8-14v14m-8-7h287m0-7v14"/><path d="M6 15h8" stroke-width="2"/></g><text x="232" y="19" fill="currentColor">HB / 02</text></svg>
  <svg class="desk-compass" viewBox="0 0 160 220" fill="none" focusable="false"><g stroke="currentColor" stroke-width="1.3"><path d="M76 36V10h8v26" fill="var(--paper)"/><circle cx="80" cy="47" r="12" fill="var(--paper)"/><circle cx="80" cy="47" r="4"/><path d="M74 58 23 192l6 3L80 72l51 123 6-3L86 58" fill="var(--paper)"/><path d="m23 192-6 17m114-14 8 14M55 110h53m-53-4v12m53-12v12m-30-12v12m4-12v12"/><path d="M20 185a91 91 0 0 1 120 0" stroke-dasharray="2 6" opacity=".35"/></g></svg>
</div>'''
